#!/usr/bin/env bash
# usage: ./run_test.sh "<text>" <out_basename>
# Generates speech with bm_george, then measures silence regions with ffmpeg silencedetect.
set -e
TEXT="$1"
OUT="$2"
echo "$TEXT" > "${OUT}.txt"
npx --yes hyperframes@latest tts "${OUT}.txt" --voice bm_george --output "${OUT}.wav" 2>&1 | grep -E "Generated|error" || true
DUR=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "${OUT}.wav")
echo "DURATION: ${DUR}s"
echo "SILENCE (>50ms, -40dB):"
ffmpeg -hide_banner -i "${OUT}.wav" -af "silencedetect=noise=-40dB:d=0.05" -f null - 2>&1 | grep -E "silence_(start|duration)" | sed 's/^/  /'
echo "---"
