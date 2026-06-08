#!/usr/bin/env bash
# Render per-scene Kokoro bm_george VO stems for the full-scale Mark Hanna doc.
# Uses mise's python (which has kokoro-onnx installed) to call the bundled
# hyperframes synth-v2.py directly, then ffmpeg-postprocesses each scene.
set -euo pipefail

PROJ="/Users/I548399/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna"
PYTHON="/Users/I548399/.local/share/mise/installs/python/latest/bin/python3"
SYNTH="/Users/I548399/.cache/hyperframes/tts/synth-v2.py"
MODEL="/Users/I548399/.cache/hyperframes/tts/models/kokoro-v1.0.onnx"
VOICES="/Users/I548399/.cache/hyperframes/tts/voices/voices-v1.0.bin"

cd "$PROJ"
mkdir -p assets/scenes

for f in research/full-scale/audio/scenes/scene-*-narration.txt; do
  scene=$(basename "$f" -narration.txt)
  raw="assets/scenes/${scene}-raw.wav"
  out="assets/scenes/${scene}.wav"

  if [[ -f "$out" ]]; then
    echo "[skip] $out exists"
    continue
  fi

  text=$(cat "$f")
  echo "[synth] $scene ($(echo "$text" | wc -w | tr -d ' ') words)"
  "$PYTHON" "$SYNTH" "$MODEL" "$VOICES" "$text" bm_george 1.0 "$raw" en-us >/dev/null

  echo "[postprocess] $scene -> atempo 1.18 + loudnorm I=-16:TP=-1.5"
  ffmpeg -y -i "$raw" \
    -af "atempo=1.18,loudnorm=I=-16:TP=-1.5:LRA=11" \
    -ar 48000 -ac 1 "$out" >/dev/null 2>&1
  rm -f "$raw"

  dur=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$out")
  printf "[done] %s -> %s (%.2fs)\n" "$scene" "$out" "$dur"
done

echo
echo "all 19 scenes rendered"
ls -la assets/scenes/scene-*.wav | awk '{print $NF, $5}' | column -t
