#!/usr/bin/env bash
# Build the 4 cue stems for the Mark Hanna full-scale documentary.
# Inputs: research/full-scale/audio/music-sources/{cueA-source-liberty-bell.flac, cueB-source-nearer-my-god.mp3}
# Outputs: assets/music/cue-{A,B,C,D}.wav  (mono 48kHz pcm_s16le)
set -euo pipefail

PROJ="/Users/I548399/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna"
cd "$PROJ"
SRC=research/full-scale/audio/music-sources
OUT=assets/music
mkdir -p "$OUT"

# --- Cue A: Liberty Bell March (Sousa, 1893 composition; 1895 recording by Baldwin's
#     Cadet Band of Boston, IA item ne-liberty). Period-strict 1890-1898, public-domain
#     composition (US comp ≤1928), public-domain sound-recording (≤1922 per 17 USC §1401).
#     IA license tag is CC-BY-NC-SA which is a non-issue here because the recording is
#     federally PD. Convert to 48kHz mono, normalise loudness lightly.
ffmpeg -y -hide_banner -loglevel error -i "$SRC/cueA-source-liberty-bell.flac" \
  -af "aresample=48000,pan=mono|c0=0.5*c0+0.5*c1,loudnorm=I=-23:TP=-2:LRA=11" \
  -ar 48000 -ac 1 -c:a pcm_s16le \
  "$OUT/cue-A.wav"

# --- Cue B: Nearer My God to Thee (1902 cylinder, IA 78_nearer-my-god-to-thee_gbia0307065a).
#     Hymn arrangement; single-line-feeling melody. Recording ≤1922 → PD by
#     17 USC §1401. Slow, mournful, "weight" cue per PLAN §3.2.
ffmpeg -y -hide_banner -loglevel error -i "$SRC/cueB-source-nearer-my-god.mp3" \
  -af "aresample=48000,pan=mono|c0=c0,loudnorm=I=-26:TP=-2:LRA=11" \
  -ar 48000 -ac 1 -c:a pcm_s16le \
  "$OUT/cue-B.wav"

# --- Cue C: Coda — Motif-A contour reharmonized in B's register (per PLAN.md §3.2).
#     We synthesise this from Cue A by: time-stretch 1.5× (slower), down a perfect 5th
#     (semitones=-7), low-pass to 2kHz to push it into "memory" register, lightly reverb.
#     This is the "thinned reharmonization" variant from MUSIC_PLAN.md §6 open
#     editorial decision — full-volume variant lives only in the mix, not the stem.
#     Take 30s from a strong melodic phrase (Liberty Bell trio enters around 1:00).
#     Pitch-shift via asetrate trick: scale rate down 7 semitones (factor 2^(-7/12)),
#     then resample back to 48k. To slow without pitch-shift we'd need atempo; but
#     we WANT the pitch lower (B's register), so asetrate alone gives both effects.
SR_FACTOR=$(awk 'BEGIN{printf "%.6f", 48000 * (2^(-7/12))}')
ffmpeg -y -hide_banner -loglevel error -ss 60 -t 30 -i "$SRC/cueA-source-liberty-bell.flac" \
  -af "aresample=48000,pan=mono|c0=0.5*c0+0.5*c1,asetrate=${SR_FACTOR},aresample=48000,lowpass=f=1800,aecho=0.6:0.3:120:0.25,loudnorm=I=-23:TP=-2:LRA=9" \
  -ar 48000 -ac 1 -c:a pcm_s16le \
  "$OUT/cue-C.wav"

echo "Cue A/B/C built. ffprobe:"
for c in A B C; do
  ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$OUT/cue-${c}.wav" | xargs -I{} echo "  cue-${c}.wav = {}s"
done
