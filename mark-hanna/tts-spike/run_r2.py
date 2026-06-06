#!/usr/bin/env python
"""Round 2: targeted follow-up tests after seeing battery results.

Hypotheses to verify:
- All sentence-junction punctuation gives identical ~0.22-0.24s gap (the model normalizes)
- Whitespace collapsing: \\n, \\n\\n, double-space all read identical (CONFIRMED in round 1)
- Therefore: how do we ADD extra silence?
   - extra periods?  "...." vs "..."
   - filler words ("then,", "and,")
   - inserted dummy short utterance
- Where does the user's "missing gap" actually come from?
   - Test the exact 'brokers' line in CONTEXT of the original narration
"""
import json
import re
import subprocess
import time
from pathlib import Path

import kokoro_onnx
import soundfile as sf

ROOT = Path(__file__).parent
CLIPS = ROOT / "clips"
CLIPS.mkdir(exist_ok=True)

MODEL = "/Users/I548399/.cache/hyperframes/tts/models/kokoro-v1.0.onnx"
VOICES = "/Users/I548399/.cache/hyperframes/tts/voices/voices-v1.0.bin"

TESTS = [
    # ---- Adding silence: try various tricks ----
    ("r2-baseline",         "He took a cut. The crowd applauded.", "baseline"),
    ("r2-four-period",      "He took a cut.... The crowd applauded.", "4 periods"),
    ("r2-six-period",       "He took a cut...... The crowd applauded.", "6 periods"),
    ("r2-period-emdash",    "He took a cut.\u2014 The crowd applauded.", "period+emdash"),
    ("r2-emdash-period",    "He took a cut\u2014. The crowd applauded.", "emdash+period"),
    ("r2-spaced-emdash-spaced", "He took a cut . \u2014 . The crowd applauded.", "spaced . — ."),
    ("r2-comma-comma",      "He took a cut, , the crowd applauded.", "comma comma"),
    ("r2-then",             "He took a cut. Then the crowd applauded.", "+'Then'"),
    ("r2-and-then",         "He took a cut. And then, the crowd applauded.", "+'And then,'"),
    ("r2-explicit-pause",   "He took a cut. Pause. The crowd applauded.", "literal 'Pause.'"),
    ("r2-uh",               "He took a cut. Uh, the crowd applauded.", "filler 'Uh,'"),
    ("r2-period-newlines",  "He took a cut.\n\n\n\nThe crowd applauded.", "4 newlines"),
    ("r2-tabs-newlines",    "He took a cut.\n\t\nThe crowd applauded.", "tab between"),

    # ---- Year reading: more contexts ----
    ("r2-year-quoted",      'He said "1896".', "quoted year"),
    ("r2-year-paren",       "It happened (1896).", "year in parens"),
    ("r2-year-after-dash",  "It happened — 1896.", "year after em-dash"),
    ("r2-year-of-1896",     "Of 1896.", "'Of 1896'"),
    ("r2-year-back-in",     "Back in 1896, he won.", "Back in 1896,"),
    ("r2-eighteen96",       "Eighteen 96.", "mixed words/digits"),

    # ---- Comma in long lists ----
    ("r2-three-list",       "He sold coal, iron, and steel.", "lowercase 3-list (control)"),
    ("r2-three-cap-list",   "He owned Coal, Iron, and Steel.", "Cap 3-list with 'and'"),
    ("r2-cap-list-noand",   "He owned Coal, Iron, Steel.", "Cap 3-list no 'and'"),
    ("r2-fragment-cap",     "Coal. Iron.",  "two cap fragments period-split"),
    ("r2-fragment-comma",   "Coal, Iron.",  "two cap fragments comma"),

    # ---- 'brokers' line: in fuller context (mimicking narration) ----
    ("r2-brokers-context",
     "Hanna built the network. Brokers like him. He took a cut. Banks held the gold.",
     "brokers in 4-sentence context"),
    ("r2-brokers-merged",
     "Hanna built the network. Brokers like him, he took a cut. Banks held the gold.",
     "brokers merged via comma"),

    # ---- The Pittsburgh Steel Mills stretch (rushed at 2:10-2:30) ----
    ("r2-rushed-original",
     "Pittsburgh Steel Mills doubled in size. The workers earned a dollar a day. The room changed temperature.",
     "rushed stretch baseline"),
    ("r2-rushed-ellipsis",
     "Pittsburgh Steel Mills doubled in size... The workers earned a dollar a day... The room changed temperature.",
     "ellipses inserted"),
    ("r2-rushed-emdash",
     "Pittsburgh Steel Mills doubled in size — and the workers earned a dollar a day — and the room changed temperature.",
     "em-dashes connecting"),
    ("r2-rushed-paragraphs",
     "Pittsburgh Steel Mills doubled in size.\n\nThe workers earned a dollar a day.\n\nThe room changed temperature.",
     "paragraphs (control)"),
    ("r2-rushed-pauses",
     "Pittsburgh Steel Mills doubled in size. Pause. The workers earned a dollar a day. Pause. The room changed temperature.",
     "literal 'Pause.' inserts"),

    # ---- Dollar amounts ----
    ("r2-dollars-bare",   "$100,000.", "100k digits"),
    ("r2-dollars-words",  "One hundred thousand dollars.", "100k words"),
    ("r2-dollars-3.5m",   "$3.5 million.", "$3.5M digits"),
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
    print("[load]", flush=True); t0 = time.time()
    model = kokoro_onnx.Kokoro(MODEL, VOICES)
    print(f"[load] {time.time()-t0:.1f}s", flush=True)

    results = []
    summary_lines = []
    for tid, text, note in TESTS:
        wav = CLIPS / f"{tid}.wav"
        try:
            t0 = time.time()
            samples, sr = model.create(text, voice="bm_george", speed=1.0)
            sf.write(wav, samples, sr)
            duration = round(len(samples) / sr, 3)
        except Exception as e:
            print(f"[FAIL {tid}] {e}", flush=True)
            continue
        sils = measure(wav)
        leading = next((s for s in sils if s["start"] < 0.05), None)
        trailing = next((s for s in sils if abs(s["end"] - duration) < 0.05), None)
        internal = [s for s in sils if s is not leading and s is not trailing]
        rec = {"id": tid, "text": text, "note": note, "duration": duration,
               "internal_silences": internal, "leading": leading, "trailing": trailing}
        results.append(rec)
        ils = ", ".join(f"{s['duration']:.2f}s@{s['start']:.2f}" for s in internal) or "-"
        ld = f"{leading['duration']:.2f}" if leading else "-"
        td = f"{trailing['duration']:.2f}" if trailing else "-"
        line = f"[{tid}] dur={duration:.2f}s lead={ld} trail={td} internal=[{ils}] :: {note}\n           text={text!r}"
        print(line, flush=True)
        summary_lines.append(line)

    (ROOT / "results-r2.json").write_text(json.dumps(results, indent=2))
    (ROOT / "summary-r2.txt").write_text("\n".join(summary_lines))
    print(f"[done] {len(results)} tests")


if __name__ == "__main__":
    main()
