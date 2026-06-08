#!/usr/bin/env bash
# Build master narration.fullscale.wav for the 24-min cut.
# Each scene's per-scene VO wav is placed at its window_start (in seconds), with
# the leading-silence beat from the chunk plan applied as additional offset.
# Output: 1440 s mono 48 kHz pcm_s16le, loudnorm-stable.
set -euo pipefail

PROJ="/Users/I548399/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna"
cd "$PROJ"

OUT="assets/narration.fullscale.wav"
DUR=1440  # 24 min

# Window starts (s) and leading-silence beats from VO chunk plans.
# scene_idx:window_start:leading_silence
ROWS=(
  "01:0:4.0"
  "02:45:1.0"
  "03:210:0.0"
  "04:300:0.0"
  "05:360:0.0"
  "06:450:0.4"
  "07:510:0.0"
  "08:600:0.0"
  "09:690:0.0"
  "10:840:0.0"
  "11:960:0.0"
  "12:1065:0.0"
  "13:1110:0.4"
  "14:1170:0.0"
  "15:1215:1.5"
  "16:1245:0.0"
  "17:1320:1.5"
  "18:1380:0.0"
  "19:1410:0.0"
)

# Build a base silent track + amix all the scenes onto it via -filter_complex.
INPUTS=()
INPUTS+=("-f" "lavfi" "-t" "$DUR" "-i" "anullsrc=channel_layout=mono:sample_rate=48000")

FILTER=""
N=${#ROWS[@]}
for i in $(seq 0 $((N-1))); do
  IFS=":" read -r idx start lead <<< "${ROWS[$i]}"
  wav="assets/scenes/scene-${idx}.wav"
  INPUTS+=("-i" "$wav")
  off_ms=$(awk -v s="$start" -v l="$lead" 'BEGIN{printf "%d", (s+l)*1000}')
  # input slot is i+1 (slot 0 is the silent base)
  FILTER+="[$((i+1)):a]adelay=${off_ms}|${off_ms}[a${i}];"
done

# amix all delayed inputs + base
MIX_IN="[0:a]"
for i in $(seq 0 $((N-1))); do MIX_IN+="[a${i}]"; done
FILTER+="${MIX_IN}amix=inputs=$((N+1)):duration=first:dropout_transition=0,loudnorm=I=-16:TP=-1.5:LRA=11[out]"

mkdir -p assets
ffmpeg -y "${INPUTS[@]}" \
  -filter_complex "$FILTER" \
  -map "[out]" \
  -ar 48000 -ac 1 -c:a pcm_s16le \
  -t "$DUR" \
  "$OUT"

ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$OUT"
echo "wrote $OUT"
