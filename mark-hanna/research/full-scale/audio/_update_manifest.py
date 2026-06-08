#!/usr/bin/env python3
"""Update VO_MANIFEST.json with rendered durations + paths."""
import json, subprocess
from pathlib import Path

ROOT = Path("/Users/I548399/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna")
mpath = ROOT / "research/full-scale/audio/VO_MANIFEST.json"
manifest = json.loads(mpath.read_text())

for m in manifest:
    n = m["scene"]
    rel = f"assets/scenes/scene-{n:02d}.wav"
    abs_path = ROOT / rel
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=nw=1:nk=1", str(abs_path)
    ]).decode().strip()
    dur = float(out)
    m["rendered"] = {
        "wav_path": rel,
        "duration_seconds": round(dur, 3),
        "voice": "kokoro bm_george",
        "post_processing": "atempo=1.18, loudnorm I=-16:TP=-1.5:LRA=11",
        "sample_rate": 48000,
        "channels": 1,
    }

mpath.write_text(json.dumps(manifest, indent=2))
print(f"updated {mpath}")
