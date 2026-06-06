#!/usr/bin/env python3
"""
make-captions.py — Regenerate caption cues from the current narration.wav.

Pipeline:
  1. Run whisper-cli word-level alignment on assets/narration.wav, producing
     assets/transcript.json (a flat list of {text, start, end} word entries).
  2. Group those words into caption cues using the project's established style:
       - hard maximum 5 words per group
       - force a break after any word whose token ends with sentence-terminal
         punctuation (".", "!", "?")
       - cue.start = first word.start, cue.end = last word.end
       - text = " ".join(word.text) (trailing-period commas etc preserved)
  3. Write assets/caption-groups.json (the canonical cue list).
  4. Patch the inline groups[] array AND the .cap-group <div>s inside
     compositions/captions.html so the live composition stays in sync.

Idempotent: re-running with no audio change produces no diff. Run this any
time assets/narration.wav is touched (splice fix, full re-render, voice swap).

Usage:
    python3 scripts/make-captions.py                   # regenerate everything
    python3 scripts/make-captions.py --skip-whisper    # reuse existing transcript.json
    python3 scripts/make-captions.py --dry-run         # show what would change

Drift target: ≤100 ms over the full track. The whisper-driven alignment
typically gets us to ≤50 ms; the diagnosis pre-fix saw up to 1880 ms because
the cues had been generated against a stale audio snapshot.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

# Repo layout: this script lives in scripts/ at the project root.
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
COMPOSITIONS = ROOT / "compositions"
NARRATION = ASSETS / "narration.wav"
TRANSCRIPT = ASSETS / "transcript.json"
CAPTION_GROUPS = ASSETS / "caption-groups.json"
CAPTIONS_HTML = COMPOSITIONS / "captions.html"

# Whisper config — small.en is enough for word-level timing on clean TTS.
WHISPER_MODEL = Path.home() / ".cache/hyperframes/whisper/models/ggml-small.en.bin"
WHISPER_BIN = "whisper-cli"

MAX_WORDS_PER_GROUP = 5
TERMINAL_PUNCT = (".", "!", "?")


# ──────────────────────────────────────────────────────────────────────────
# Whisper word-level alignment
# ──────────────────────────────────────────────────────────────────────────


def run_whisper(audio: Path, model: Path) -> list[dict[str, Any]]:
    """Run whisper-cli with word-level output and return a flat word list.

    Uses -ml 1 -sow to force one word per "segment" with start/end timing,
    and -ojf for JSON-full output that includes word timestamps.
    """
    if not shutil.which(WHISPER_BIN):
        raise RuntimeError(f"{WHISPER_BIN} not on PATH")
    if not model.exists():
        raise RuntimeError(f"whisper model missing: {model}")
    if not audio.exists():
        raise RuntimeError(f"audio missing: {audio}")

    out_prefix = audio.with_suffix("")  # strip .wav -> assets/narration
    cmd = [
        WHISPER_BIN,
        "-m", str(model),
        "-f", str(audio),
        "-ml", "1",
        "-sow",
        "-ojf",
        "-of", str(out_prefix),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    json_path = out_prefix.with_suffix(".wav.json")
    if not json_path.exists():
        # whisper-cli with -ojf writes <of>.json (no .wav) on some versions
        json_path = Path(str(out_prefix) + ".json")
    raw = json.loads(json_path.read_text())
    # raw is {"transcription": [{offsets, text, ...}, ...]} from whisper-cli -ojf
    # Each segment with -ml 1 -sow is a single word.
    words: list[dict[str, Any]] = []
    for seg in raw.get("transcription", []):
        text = seg.get("text", "").strip()
        if not text:
            continue
        offs = seg.get("offsets", {})
        start_ms = offs.get("from", 0)
        end_ms = offs.get("to", start_ms)
        words.append({
            "text": text,
            "start": round(start_ms / 1000, 2),
            "end": round(end_ms / 1000, 2),
        })
    # Tidy up whisper's intermediate file
    try:
        json_path.unlink()
    except OSError:
        pass
    return words


# ──────────────────────────────────────────────────────────────────────────
# Word → caption-group folding
# ──────────────────────────────────────────────────────────────────────────


def group_words(words: list[dict[str, Any]],
                max_words: int = MAX_WORDS_PER_GROUP,
                terminal_punct: tuple[str, ...] = TERMINAL_PUNCT) -> list[dict[str, Any]]:
    """Fold a flat word list into caption groups.

    Rules:
      - hard cap of `max_words` words per group
      - force break after any word whose stripped text ends in `terminal_punct`
      - group.start = first word.start
      - group.end   = last  word.end
      - group.text  = " ".join(word.text)
    """
    groups: list[dict[str, Any]] = []
    cur: list[dict[str, Any]] = []

    def flush() -> None:
        if not cur:
            return
        groups.append({
            "text": " ".join(w["text"] for w in cur),
            "start": cur[0]["start"],
            "end": cur[-1]["end"],
        })
        cur.clear()

    for w in words:
        cur.append(w)
        token = w["text"].rstrip()
        ends_terminal = token.endswith(terminal_punct)
        if ends_terminal or len(cur) >= max_words:
            flush()
    flush()
    return groups


# ──────────────────────────────────────────────────────────────────────────
# captions.html surgery
# ──────────────────────────────────────────────────────────────────────────

# Inline `const groups = [{"id":"cap-0", ...}, ...];` line inside captions.html
GROUPS_LINE_RE = re.compile(r"(\s*const groups = )(\[.*?\]);", re.DOTALL)
# `<div class="cap-group" id="cap-N">TEXT</div>`
CAP_DIV_RE = re.compile(r'(<div class="cap-group" id="cap-)(\d+)(">)([^<]*)(</div>)')


def patch_captions_html(html: str, groups: list[dict[str, Any]]) -> str:
    """Replace the inline groups[] array AND the static .cap-group divs.

    The HTML carries TWO copies of the cue list:
      (a) `<div class="cap-group" id="cap-N">TEXT</div>` — what gets rendered
      (b) `const groups = [...]` — what GSAP animates against
    Both must reflect the same N cues for visual + timing alignment.
    """
    # 1. Inline groups[] — JS array of {id,start,end} only (no text)
    js_groups = json.dumps(
        [{"id": f"cap-{i}", "start": g["start"], "end": g["end"]} for i, g in enumerate(groups)],
        separators=(",", ":"),
    )
    new_html, n = GROUPS_LINE_RE.subn(rf"\g<1>{js_groups};", html, count=1)
    if n != 1:
        raise RuntimeError("could not locate `const groups = [...]` in captions.html")

    # 2. <div class="cap-group" id="cap-N">TEXT</div> — rebuild the block.
    # Find all existing cap-group divs and rebuild from the new groups list.
    # Strategy: rewrite anywhere between the first and last cap-group div.
    matches = list(CAP_DIV_RE.finditer(new_html))
    if not matches:
        raise RuntimeError("could not locate any <div class='cap-group'> in captions.html")
    first_start = matches[0].start()
    last_end = matches[-1].end()

    # Preserve original indentation by sniffing the leading whitespace before
    # the first match.
    line_start = new_html.rfind("\n", 0, first_start) + 1
    indent = new_html[line_start:first_start]

    rebuilt_lines = [
        f'{indent}<div class="cap-group" id="cap-{i}">{g["text"]}</div>'
        for i, g in enumerate(groups)
    ]
    rebuilt_block = "\n".join(rebuilt_lines)
    new_html = new_html[:first_start] + rebuilt_block + new_html[last_end:]
    return new_html


# ──────────────────────────────────────────────────────────────────────────
# Drift verification
# ──────────────────────────────────────────────────────────────────────────


def verify_alignment(groups: list[dict[str, Any]], words: list[dict[str, Any]],
                     tolerance_ms: int = 100) -> tuple[int, list[tuple[int, int]]]:
    """Each group.start must equal its first word.start (no drift).

    Returns (max_abs_skew_ms, [(group_idx, skew_ms) for any over tolerance]).
    """
    wi = 0
    bad: list[tuple[int, int]] = []
    max_skew = 0
    for gi, g in enumerate(groups):
        first_tok = g["text"].split()[0]
        # Walk forward to find a matching word
        target = re.sub(r"[^a-z0-9]", "", first_tok.lower())
        match = None
        for j in range(wi, min(len(words), wi + 8)):
            wnorm = re.sub(r"[^a-z0-9]", "", words[j]["text"].lower())
            if wnorm == target:
                match = j
                break
        if match is None:
            continue
        skew_ms = round((g["start"] - words[match]["start"]) * 1000)
        max_skew = max(max_skew, abs(skew_ms))
        if abs(skew_ms) > tolerance_ms:
            bad.append((gi, skew_ms))
        # Skip forward by group word-count
        wi = match + len(g["text"].split())
    return max_skew, bad


# ──────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--skip-whisper", action="store_true",
                    help="reuse existing assets/transcript.json (skip the whisper pass)")
    ap.add_argument("--dry-run", action="store_true",
                    help="don't write files, just report what would change")
    ap.add_argument("--audio", type=Path, default=NARRATION,
                    help="path to narration audio (default: assets/narration.wav)")
    ap.add_argument("--tolerance-ms", type=int, default=100,
                    help="max acceptable per-cue drift in ms (default: 100)")
    args = ap.parse_args()

    # 1. words = whisper(narration.wav) OR load existing transcript.json
    if args.skip_whisper:
        if not TRANSCRIPT.exists():
            print(f"--skip-whisper but {TRANSCRIPT} missing", file=sys.stderr)
            return 2
        words = json.loads(TRANSCRIPT.read_text())
        print(f"reusing {TRANSCRIPT} ({len(words)} words)")
    else:
        print(f"running whisper-cli on {args.audio}...")
        words = run_whisper(args.audio, WHISPER_MODEL)
        print(f"whisper produced {len(words)} words; last word ends at {words[-1]['end']:.2f}s")
        if not args.dry_run:
            TRANSCRIPT.write_text(json.dumps(words, indent=2))
            print(f"wrote {TRANSCRIPT}")

    # 2. groups = fold(words)
    groups = group_words(words)
    print(f"folded into {len(groups)} caption groups (max_words={MAX_WORDS_PER_GROUP})")

    # 3. verify drift before writing — a regenerated cue file should sit at 0ms
    max_skew, bad = verify_alignment(groups, words, args.tolerance_ms)
    print(f"max per-cue drift: {max_skew} ms (tolerance {args.tolerance_ms} ms)")
    if bad:
        print(f"WARNING: {len(bad)} groups drift over tolerance:", bad[:5], file=sys.stderr)

    # 4. write caption-groups.json
    if args.dry_run:
        print("--dry-run: would write caption-groups.json + patch captions.html")
        return 0

    CAPTION_GROUPS.write_text(json.dumps(groups, indent=2) + "\n")
    print(f"wrote {CAPTION_GROUPS}")

    # 5. patch captions.html (both the divs and the inline groups[] array)
    html = CAPTIONS_HTML.read_text()
    new_html = patch_captions_html(html, groups)
    if new_html != html:
        CAPTIONS_HTML.write_text(new_html)
        print(f"patched {CAPTIONS_HTML}")
    else:
        print(f"{CAPTIONS_HTML} unchanged")

    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
