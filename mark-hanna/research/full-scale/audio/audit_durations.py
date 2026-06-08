#!/usr/bin/env python3
"""Audit rendered scene wavs against script-window targets."""
import json, subprocess
from pathlib import Path

ROOT = Path("/Users/I548399/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna")
manifest = json.loads((ROOT / "research/full-scale/audio/VO_MANIFEST.json").read_text())

def parse_window(s):
    a, b = s.split("-")
    def to_sec(x):
        if ":" in x:
            m, s = x.split(":")
            return int(m) * 60 + int(s)
        return int(x)
    return to_sec(a), to_sec(b)

def ffprobe_duration(p):
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=nw=1:nk=1", str(p)
    ]).decode().strip()
    return float(out)

print(f"{'scene':<6} {'window':>11} {'target':>7} {'spoken':>7} {'silence':>7} {'sum':>6} {'fits':>6}")
print("-" * 70)
total_spoken = 0.0
total_silence = 0.0
total_target = 0.0
for m in manifest:
    n = m["scene"]
    wav = ROOT / f"assets/scenes/scene-{n:02d}.wav"
    dur = ffprobe_duration(wav)
    a, b = parse_window(m["window"])
    target = b - a
    silence = m["silence_seconds"]
    summ = dur + silence
    fits = "OK" if summ <= target * 1.10 else "OVER"
    print(f"{n:<6d} {m['window']:>11} {target:>6.1f}s {dur:>6.2f}s {silence:>6.1f}s {summ:>5.1f}s {fits:>6}")
    total_spoken += dur
    total_silence += silence
    total_target += target

print("-" * 70)
print(f"{'TOTAL':<6} {'':>11} {total_target:>6.1f}s {total_spoken:>6.2f}s {total_silence:>6.1f}s {total_spoken+total_silence:>5.1f}s")
print(f"\nNarration density: {(total_spoken+total_silence) / total_target * 100:.1f}% of total runtime")
print(f"Visual hold time: {total_target - (total_spoken + total_silence):.1f}s")
