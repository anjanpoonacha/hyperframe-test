#!/usr/bin/env bash
# Cue D — Bryan Counter-current. Single rising 4-note phrase, never resolves.
# Per MUSIC_PLAN §5 the brief said "no period-PD analog; Suno Pro generation
# allowed". Without Suno access in this run, we synthesize a sparse
# cornet-like motif with ffmpeg sine + harmonic stack + short ADSR envelope.
# 4 notes: A3 (220 Hz) → C4 (261.63) → E4 (329.63) → F4 (349.23). Rises by
# minor 3rd, then major 3rd, then minor 2nd: an unresolved leading tone.
#
# Cornet-ish timbre: fundamental + 2nd + 3rd harmonic with descending amps,
# shaped by triangular envelope. Slight tape-like hiss for period grain.
set -euo pipefail
PROJ="/Users/I548399/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna"
cd "$PROJ"
OUT=assets/music
TMP=/tmp/mh-cue-d-build
rm -rf "$TMP" && mkdir -p "$TMP"

# Per-note duration (seconds) and envelope shape.
NOTE_DUR=1.6
NOTE_GAP=0.4

build_note() {
  # $1 = freq (Hz), $2 = output file
  local f=$1 ; local o=$2
  local f2=$(awk -v x=$f 'BEGIN{print x*2}')
  local f3=$(awk -v x=$f 'BEGIN{print x*3}')
  ffmpeg -y -hide_banner -loglevel error \
    -f lavfi -t $NOTE_DUR -i "sine=frequency=${f}:sample_rate=48000" \
    -f lavfi -t $NOTE_DUR -i "sine=frequency=${f2}:sample_rate=48000" \
    -f lavfi -t $NOTE_DUR -i "sine=frequency=${f3}:sample_rate=48000" \
    -filter_complex "[0:a]volume=0.65[a0];[1:a]volume=0.30[a1];[2:a]volume=0.10[a2];[a0][a1][a2]amix=inputs=3:duration=first,afade=t=in:st=0:d=0.18,afade=t=out:st=$(awk -v x=$NOTE_DUR 'BEGIN{print x-0.45}'):d=0.45,lowpass=f=2200,highpass=f=180" \
    -ar 48000 -ac 1 -c:a pcm_s16le "$o"
}

build_note 220.00  "$TMP/n1.wav"   # A3
build_note 261.63  "$TMP/n2.wav"   # C4
build_note 329.63  "$TMP/n3.wav"   # E4
build_note 349.23  "$TMP/n4.wav"   # F4 (unresolved leading tone over E)

# silence between notes
ffmpeg -y -hide_banner -loglevel error -f lavfi -t $NOTE_GAP -i "anullsrc=channel_layout=mono:sample_rate=48000" \
  -ar 48000 -ac 1 -c:a pcm_s16le "$TMP/gap.wav"

# concat: gap, n1, gap, n2, gap, n3, gap, n4, longtail
ffmpeg -y -hide_banner -loglevel error -f lavfi -t 1.5 -i "anullsrc=channel_layout=mono:sample_rate=48000" \
  -ar 48000 -ac 1 -c:a pcm_s16le "$TMP/tail.wav"

cat > "$TMP/list.txt" <<EOL
file '$TMP/gap.wav'
file '$TMP/n1.wav'
file '$TMP/gap.wav'
file '$TMP/n2.wav'
file '$TMP/gap.wav'
file '$TMP/n3.wav'
file '$TMP/gap.wav'
file '$TMP/n4.wav'
file '$TMP/tail.wav'
EOL

ffmpeg -y -hide_banner -loglevel error -f concat -safe 0 -i "$TMP/list.txt" -c copy "$TMP/raw.wav"

# Apply period grain: very mild echo (room) + LP shelf to push to "1890s recording"
ffmpeg -y -hide_banner -loglevel error -i "$TMP/raw.wav" \
  -af "aecho=0.5:0.4:90:0.20,lowpass=f=2400,highpass=f=200,loudnorm=I=-22:TP=-2:LRA=8" \
  -ar 48000 -ac 1 -c:a pcm_s16le "$OUT/cue-D.wav"

ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$OUT/cue-D.wav" | xargs -I{} echo "cue-D.wav = {}s"
