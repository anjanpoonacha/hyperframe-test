#!/usr/bin/env python
"""Measure silence regions with ffmpeg silencedetect.

usage: python measure.py <file.wav> [--noise -40] [--min 0.05]
"""
import re
import subprocess
import sys
import json
from pathlib import Path


def measure(path: str, noise_db: float = -40, min_dur: float = 0.05):
    cmd = [
        "ffmpeg", "-hide_banner", "-i", path,
        "-af", f"silencedetect=noise={noise_db}dB:d={min_dur}",
        "-f", "null", "-",
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)
    err = p.stderr
    # parse silence_start/end/duration
    silences = []
    cur = None
    for line in err.splitlines():
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
    # total duration
    dur_cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=nw=1:nk=1", path,
    ]
    dp = subprocess.run(dur_cmd, capture_output=True, text=True)
    duration = float(dp.stdout.strip()) if dp.stdout.strip() else None
    return {"path": path, "duration": duration, "noise_db": noise_db,
            "min_dur": min_dur, "silences": silences}


if __name__ == "__main__":
    args = sys.argv[1:]
    path = args[0]
    noise = -40
    mind = 0.05
    if "--noise" in args:
        noise = float(args[args.index("--noise") + 1])
    if "--min" in args:
        mind = float(args[args.index("--min") + 1])
    print(json.dumps(measure(path, noise, mind), indent=2))
