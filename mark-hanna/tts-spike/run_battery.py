#!/usr/bin/env python
"""Run the punctuation spike test battery in one Kokoro session.

Outputs:
- clips/<id>.wav
- results.json   (per-test: text, duration, silences)
- summary.txt    (human-readable per-test report)
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

import kokoro_onnx
import soundfile as sf

ROOT = Path(__file__).parent
CLIPS = ROOT / "clips"
CLIPS.mkdir(exist_ok=True)

MODEL = "/Users/I548399/.cache/hyperframes/tts/models/kokoro-v1.0.onnx"
VOICES = "/Users/I548399/.cache/hyperframes/tts/voices/voices-v1.0.bin"

# ---- Test cases ---------------------------------------------------------
# Each case: (id, text, note). id is short kebab-case, used as filename.

TESTS = [
    # ---- 1. SENTENCE GAP CONTROL ----
    # control: identical two clauses with varying junction
    ("01-period",            "He took a cut. The crowd applauded.", "baseline period"),
    ("01-period-double-space","He took a cut.  The crowd applauded.", "period + double space"),
    ("01-question",          "He took a cut? The crowd applauded.", "question mark"),
    ("01-exclam",            "He took a cut! The crowd applauded.", "exclamation"),
    ("01-ellipsis",          "He took a cut... The crowd applauded.", "three-dot ellipsis"),
    ("01-ellipsis-unicode",  "He took a cut\u2026 The crowd applauded.", "unicode ellipsis"),
    ("01-emdash",            "He took a cut\u2014 The crowd applauded.", "em-dash + space"),
    ("01-emdash-spaced",     "He took a cut \u2014 The crowd applauded.", "spaced em-dash"),
    ("01-double-period",     "He took a cut.. The crowd applauded.", "double period"),
    ("01-period-newline",    "He took a cut.\nThe crowd applauded.", "period + \\n"),
    ("01-period-double-nl",  "He took a cut.\n\nThe crowd applauded.", "period + \\n\\n"),
    ("01-period-space-period","He took a cut. . The crowd applauded.", "'. .' trick"),
    ("01-semicolon",         "He took a cut; the crowd applauded.", "semicolon + lowercase"),
    ("01-comma-lower",       "He took a cut, the crowd applauded.", "comma + lowercase (merge)"),

    # ---- 2. MID-SENTENCE PAUSE CONTROL (identical context) ----
    ("02-comma",            "The room was hot, then it changed temperature.", "comma"),
    ("02-emdash",           "The room was hot \u2014 then it changed temperature.", "em-dash"),
    ("02-ellipsis",         "The room was hot... then it changed temperature.", "ellipsis"),
    ("02-semicolon",        "The room was hot; then it changed temperature.", "semicolon"),
    ("02-paren",            "The room was hot (then it changed temperature).", "parenthetical"),
    ("02-colon",            "The room was hot: then it changed temperature.", "colon"),

    # ---- 3. PARAGRAPH-LEVEL WHITESPACE ----
    ("03-single-space",  "Banks held the gold. Hanna held the banks. Politics held Hanna.", "single-space sentences"),
    ("03-double-space",  "Banks held the gold.  Hanna held the banks.  Politics held Hanna.", "double-space sentences"),
    ("03-newlines",      "Banks held the gold.\nHanna held the banks.\nPolitics held Hanna.", "\\n between sentences"),
    ("03-paragraphs",    "Banks held the gold.\n\nHanna held the banks.\n\nPolitics held Hanna.", "\\n\\n paragraphs"),
    ("03-indent",        "Banks held the gold.\n  Hanna held the banks.\n  Politics held Hanna.", "indented"),

    # ---- 4. NUMBER / YEAR READING RULES ----
    ("04-1896-bare",     "1896.", "bare year"),
    ("04-1896-in",       "In 1896, he won.", "'In 1896,'"),
    ("04-1896-the-year", "The year 1896.", "'The year 1896'"),
    ("04-1896-words",    "Eighteen ninety-six.", "spelled out"),
    ("04-1880-in",       "In 1880, he ran.", "1880 mid-sentence"),
    ("04-1867-bare",     "1867.", "1867 bare"),
    ("04-1837-of",       "Born in 1837.", "1837 mid-sentence"),
    ("04-25-cardinal",   "Twenty-five percent.", "25 spelled out"),
    ("04-25-digits",     "25 percent.", "25 digits"),
    ("04-100-mil",       "One hundred million dollars.", "100M words"),
    ("04-100mil-digits", "$100 million.", "$100M digits"),

    # ---- 5. PROPER-NOUN CONFUSION ----
    ("05-coal-iron",         "Daniel Rhodes. Coal, iron.", "original failure"),
    ("05-coal-and-iron",     "Daniel Rhodes. Coal and iron.", "fixed"),
    ("05-salt-pepper",       "John Smith. Salt, pepper.", "salt pepper"),
    ("05-salt-and-pepper",   "John Smith. Salt and pepper.", "salt and pepper"),
    ("05-wind-water",        "Marcus Hanna. Wind, water.", "wind water"),
    ("05-wind-and-water",    "Marcus Hanna. Wind and water.", "wind and water"),
    ("05-coal-iron-lower",   "He sold coal, iron, and steel.", "lowercase list (control)"),
    ("05-jp-morgan",         "J.P. Morgan financed the trusts.", "initials with periods"),
    ("05-jp-morgan-nodots",  "JP Morgan financed the trusts.", "initials no periods"),
    ("05-jp-morgan-spaced",  "J. P. Morgan financed the trusts.", "spaced initials"),

    # ---- 6. VOICE CONSISTENCY (same text, two calls) ----
    ("06-george-1",  "Hanna ran the campaign from a hotel room.", "first call"),
    ("06-george-2",  "Hanna ran the campaign from a hotel room.", "second call (same text)"),
    ("06-george-ctx",
        "It was eighteen ninety-six. Hanna ran the campaign from a hotel room.",
        "with leading context"),

    # ---- BONUS: original failure cases for reference ----
    ("07-banks-comma",     "Banks, assessed at a quarter.", "leading-word comma"),
    ("07-banks-no-comma",  "Banks assessed at a quarter.", "no comma"),
    ("07-brokers-period",  "Brokers like him. He took a cut.", "period split"),
    ("07-brokers-comma",   "Brokers like him, he took a cut.", "comma merge"),
]


def parse_silences(stderr: str):
    silences = []
    cur = None
    for line in stderr.splitlines():
        m = re.search(r"silence_start: ([\d.\-]+)", line)
        if m:
            cur = {"start": float(m.group(1))}
            continue
        m = re.search(r"silence_end: ([\d.\-]+) \| silence_duration: ([\d.\-]+)", line)
        if m and cur is not None:
            cur["end"] = float(m.group(1))
            cur["duration"] = float(m.group(2))
            silences.append(cur)
            cur = None
    return silences


def measure(wav_path: Path, noise_db=-40, min_dur=0.05):
    cmd = ["ffmpeg", "-hide_banner", "-i", str(wav_path),
           "-af", f"silencedetect=noise={noise_db}dB:d={min_dur}",
           "-f", "null", "-"]
    p = subprocess.run(cmd, capture_output=True, text=True)
    return parse_silences(p.stderr)


def main():
    voice = sys.argv[1] if len(sys.argv) > 1 else "bm_george"
    print(f"[load] Kokoro model + voices...", flush=True)
    t0 = time.time()
    model = kokoro_onnx.Kokoro(MODEL, VOICES)
    print(f"[load] {time.time()-t0:.1f}s", flush=True)

    results = []
    summary_lines = []

    for tid, text, note in TESTS:
        wav = CLIPS / f"{tid}.wav"
        try:
            t0 = time.time()
            samples, sr = model.create(text, voice=voice, speed=1.0)
            synth_t = time.time() - t0
            sf.write(wav, samples, sr)
            duration = round(len(samples) / sr, 3)
        except Exception as e:
            print(f"[FAIL {tid}] {e}", flush=True)
            results.append({"id": tid, "text": text, "note": note, "error": str(e)})
            continue

        sils = measure(wav)
        # leading silence (start at 0), trailing (end at duration)
        leading = next((s for s in sils if s["start"] < 0.05), None)
        trailing = next((s for s in sils if abs(s["end"] - duration) < 0.05), None)
        internal = [s for s in sils
                    if s is not leading and s is not trailing]

        rec = {
            "id": tid, "text": text, "note": note,
            "duration": duration, "synth_s": round(synth_t, 2),
            "leading_silence": leading,
            "trailing_silence": trailing,
            "internal_silences": internal,
        }
        results.append(rec)

        # summary line
        ils = ", ".join(f"{s['duration']:.2f}s@{s['start']:.2f}" for s in internal) or "-"
        ld = f"{leading['duration']:.2f}" if leading else "-"
        td = f"{trailing['duration']:.2f}" if trailing else "-"
        line = (f"[{tid}] dur={duration:.2f}s lead={ld} trail={td} "
                f"internal=[{ils}] :: {note}\n           text={text!r}")
        print(line, flush=True)
        summary_lines.append(line)

    (ROOT / "results.json").write_text(json.dumps(results, indent=2))
    (ROOT / "summary.txt").write_text("\n".join(summary_lines))
    print(f"\n[done] {len(results)} tests -> {ROOT/'results.json'}")


if __name__ == "__main__":
    main()
