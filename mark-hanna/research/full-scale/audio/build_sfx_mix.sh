#!/usr/bin/env bash
# Build the SFX layer for the Mark Hanna full-scale doc.
#
# Inputs:
#   - assets/sfx/<family>-NN.wav   procedural stems (run _synth_sfx.py)
#   - assets/sfx/_placements.json  validated event table (run _sfx_placements.py)
#   - assets/narration.fullscale.wav  voice-only master
#
# Outputs:
#   - assets/sfx/_mix.wav                SFX-only stem at master timing (1440s)
#   - assets/narration.fullscale.sfx.wav VO + SFX (no music; the music task
#                                          owns the .v2 master)
#
# We deliberately do NOT write narration.fullscale.v2.wav: the music task
# (sibling t_65915e49) owns that filename and will integrate the SFX stem
# into v2 when it ships. Coordination via MIX_MANIFEST.md.
set -euo pipefail

PROJ="/Users/I548399/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna"
cd "$PROJ"

VO="assets/narration.fullscale.wav"
OUT_SFX="assets/sfx/_mix.wav"
OUT_VO_SFX="assets/narration.fullscale.sfx.wav"
DUR=1440

# Generate the ffmpeg filter graph from _placements.json
python3 - <<'PY'
import json, math, sys
from pathlib import Path

PROJ = Path("/Users/I548399/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna")
plc = json.loads((PROJ / "assets/sfx/_placements.json").read_text())
events = plc["events"]

# Expand the clock tick bed into 30 individual stem fires at 1.0s spacing
expanded = []
for e in events:
    if e["family"] == "clock" and e.get("tick_bed_dur"):
        n = int(e["tick_bed_dur"] / e.get("tick_period", 1.0))
        t0 = e["t"]
        period = e.get("tick_period", 1.0)
        for k in range(n):
            ee = dict(e)
            ee["t"] = t0 + k * period
            ee.pop("tick_bed_dur", None)
            ee.pop("tick_period", None)
            ee["cue"] = f"{e['cue']} (tick {k+1}/{n})"
            expanded.append(ee)
    else:
        expanded.append(e)

print(f"# expanded events: {len(expanded)}", file=sys.stderr)

# Build ffmpeg command:
#   - input 0: silent base anullsrc, mono 48k, 1440s
#   - inputs 1..N: stems (one per fire)
#   - filter:  for each fire i: [i+1:a]volume={gain},adelay={off}|{off}[s_i]
#   - amix: [0:a][s_0][s_1]...[s_{N-1}] amix=inputs=N+1, hpf=80
inputs = ["-f", "lavfi", "-t", "1440", "-i",
          "anullsrc=channel_layout=mono:sample_rate=48000"]
filters = []
for i, e in enumerate(expanded):
    stem = f"assets/sfx/{e['file']}"
    inputs += ["-i", stem]
    off_ms = int(round(e["t"] * 1000))
    gain = 10 ** (e["gain_db"] / 20.0)
    filters.append(
        f"[{i+1}:a]volume={gain:.6f},adelay={off_ms}|{off_ms}[s{i}]"
    )

mix_in = "[0:a]" + "".join(f"[s{i}]" for i in range(len(expanded)))
filters.append(
    f"{mix_in}amix=inputs={len(expanded)+1}:"
    "duration=first:dropout_transition=0:normalize=0,"
    "highpass=f=80[mix]"
)

filter_str = ";".join(filters)

# Write ffmpeg args list to /tmp for the bash side to pick up
cmd_args = inputs + [
    "-filter_complex", filter_str,
    "-map", "[mix]",
    "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le",
    "-t", "1440",
]
(Path("/tmp/sfx_ffmpeg_args.txt")).write_text(
    "\n".join(cmd_args)
)
print(f"# wrote /tmp/sfx_ffmpeg_args.txt ({len(cmd_args)} args)", file=sys.stderr)
PY

# 1) build the SFX-only stem
# Read args via a python helper (macOS bash 3.2 has no mapfile)
ARGS_FILE=/tmp/sfx_ffmpeg_args.txt
# Use xargs -0-style with newline delimiter + python builder
python3 -c "
import json, subprocess, sys, pathlib
args = pathlib.Path('$ARGS_FILE').read_text().split('\n')
cmd = ['ffmpeg', '-y', '-hide_banner', '-loglevel', 'warning'] + args + ['$OUT_SFX']
sys.exit(subprocess.run(cmd).returncode)
"
echo "wrote $OUT_SFX"
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$OUT_SFX"

# 2) mix VO + SFX (no music)
ffmpeg -y -hide_banner -loglevel warning \
  -i "$VO" -i "$OUT_SFX" \
  -filter_complex "[0:a][1:a]amix=inputs=2:duration=first:dropout_transition=0:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11[out]" \
  -map "[out]" \
  -ar 48000 -ac 1 -c:a pcm_s16le \
  -t "$DUR" \
  "$OUT_VO_SFX"

echo "wrote $OUT_VO_SFX"
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$OUT_VO_SFX"
