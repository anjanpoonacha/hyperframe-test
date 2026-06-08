#!/usr/bin/env bash
# Build the music bed AND the v2 master (VO + music) for the 24-min Mark Hanna
# documentary. Reuses build_master.sh's amix-with-adelay pattern.
#
# Inputs:
#   assets/narration.fullscale.wav       (voice-only master, 1440 s mono 48k)
#   assets/music/cue-A.wav               (Liberty Bell March, period-PD)
#   assets/music/cue-B.wav               (Nearer My God to Thee, period-PD)
#   assets/music/cue-C.wav               (Cue A reharmonized, transformed)
#   assets/music/cue-D.wav               (Bryan counter-current, synthesised)
#
# Outputs:
#   assets/music/music_bed.fullscale.wav (music-only bed, 1440 s mono 48k)
#   assets/narration.fullscale.v2.wav    (VO + music final master, 1440 s)
#
# The mix targets the 4 lift sync points specified in the task body (must land
# within ±0.1s of these absolute times):
#   1. 105.0s–108.5s  — Cue A dropout for "$3,500,000" dry count-up,
#                       Cue A re-entry (single transformed note) at 108.5s
#   2. 969.5s         — Cue A title-card register full statement (mechanism)
#   3. 1224.0s        — HARD silence (the "lift into silence" moment)
#   4. 1410.0s        — Cue C onset (coda entry)
#
# Mix rules (from MUSIC_PLAN.md + research/music/PLAN.md §3.4):
#   - VO target: -16 LUFS short-term (already set by build_master.sh).
#   - Music bed under VO: ~-27 to -28 LUFS (we duck per-segment via volume gain).
#   - The four +3dB lifts: at sync-point moments only.
#   - Master: -14 LUFS integrated, peaks <= -1.5 dBTP (loudnorm at the end).

set -euo pipefail

PROJ="/Users/I548399/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna"
cd "$PROJ"

ASSETS=assets
MUSIC=$ASSETS/music
DUR=1440

VO=$ASSETS/narration.fullscale.wav
BED=$MUSIC/music_bed.fullscale.wav
MASTER=$ASSETS/narration.fullscale.v2.wav

[[ -f $VO ]] || { echo "missing VO: $VO" >&2; exit 1; }
for c in A B C D; do
  [[ -f $MUSIC/cue-${c}.wav ]] || { echo "missing cue-${c}" >&2; exit 1; }
done

#------------------------------------------------------------------------------
# Music bed segments table:
#   start    end      cue     gain_dB    src_offset    notes
# Each row becomes one ffmpeg input + adelay + volume node. Source offset lets
# us select a specific portion of the cue source.
#------------------------------------------------------------------------------
# Format: "start:end:cue:gain_dB:src_offset"
# Cue A is 176.05s, Cue B is 127.37s, Cue C is 45.07s, Cue D is 9.59s.
SEGMENTS=(
  # --- Scene 1+2 (0-210s): Cue A bed under cartoon + ledger.
  # Title-card statement at 0-6s, then duck under VO.
  "0.0:6.0:A:-3:0"            # title statement, near full
  "6.0:103.5:A:-15:6"         # ducked bed under VO ledger
  # 103.5-108.5: DROPOUT for $3,500,000 + 20× dry count-up. (No segment row.)
  "108.5:110.0:C:-9:0"        # SYNC POINT 1: re-entry single transformed-A note (Cue C 0-1.5s)
  "110.0:210.0:A:-17:50"      # bed continues, slightly back, exits before sting

  # --- Scenes 3-6 (210-510s): mostly dry (per MUSIC_PLAN scene 03/04/06/05).
  # Brief Cue A drone at scene 5 pull-quote (6:00-7:30 = 360-450s).
  "365.0:430.0:A:-21:90"      # low-string drone variant under typography plate

  # --- Scene 7 (510-600s): Cue B introduction.
  "510.0:595.0:B:-13:0"       # solo piano weight cue, breath-paced

  # --- Scene 8 (600-690s): silence (thesis pivot dry).

  # --- Scene 9 (690-840s): Cue A bed convention; Cue B at 13:00 loyalty refusal.
  "690.0:780.0:A:-15:30"      # convention floor bed
  "785.0:840.0:B:-13:30"      # Cue B at McKinley loyalty refusal

  # --- Scene 10 (840-960s): Cue B + sting before mechanism.
  "840.0:955.0:B:-13:0"       # Cue B carries the panic

  # --- Scene 11 (960-1065s): Cue A title-card register at full register.
  # SYNC POINT 2 (969.5s): Cue A title statement crescendos to full.
  "960.0:969.5:A:-9:0"        # ramp-in
  "969.5:1062.0:A:-3:9.5"     # FULL title-card register
  # exits at 1062 cleanly into scene 12.

  # --- Scene 12 (1065-1110s): silence + counter ticks.

  # --- Scene 13 (1110-1170s): Cue D ONLY appearance.
  "1140.0:1149.5:D:-6:0"      # Bryan rising 4-note motif

  # --- Scene 14 (1170-1215s): Cue A counter (snare-ostinato variant).
  "1170.0:1215.0:A:-13:30"    # ledger counter beats under VO

  # --- Scene 15 (1215-1245s): silence.
  # SYNC POINT 3 (1224.0s): HARD silence (no segment within 1215-1245).
  # Single low-piano transformed-A note 0.5s after the line lands.
  # The line "And when November came, the ledger won." plays at ~1224s in the VO,
  # so the note lands at 1224.5s.
  "1224.5:1227.0:C:-12:5"     # transformed-A note re-entry (low piano-ish)

  # --- Scene 16 (1245-1320s): Cue A bed; exits before pull quote.
  "1245.0:1295.0:A:-15:60"    # senatorial timeline bed

  # --- Scene 17 (1320-1380s): mostly silence; Cue B late entry on McKinley dies.
  "1355.0:1380.0:B:-15:60"    # quiet muted-cornet-substitute (Cue B late entry)

  # --- Scene 18 (1380-1410s): Cue B muted-cornet line.
  "1380.0:1410.0:B:-13:90"    # funeral march that doesn't quite arrive

  # --- Scene 19 (1410-1440s): SYNC POINT 4 — Cue C entry.
  "1410.0:1440.0:C:-7:0"      # Coda full statement, fades naturally
)

#------------------------------------------------------------------------------
# Build music bed via amix + adelay. Slot 0 = base silence; slots 1..N = cues.
#------------------------------------------------------------------------------
INPUTS=()
INPUTS+=("-f" "lavfi" "-t" "$DUR" "-i" "anullsrc=channel_layout=mono:sample_rate=48000")

FILTER=""
N=${#SEGMENTS[@]}
for i in $(seq 0 $((N-1))); do
  IFS=":" read -r start end cue gain off <<< "${SEGMENTS[$i]}"
  src="$MUSIC/cue-${cue}.wav"
  INPUTS+=("-ss" "$off" "-i" "$src")

  off_ms=$(awk -v s="$start" 'BEGIN{printf "%d", s*1000}')
  seg_dur=$(awk -v s="$start" -v e="$end" 'BEGIN{printf "%.4f", e-s}')
  fade_in=0.25
  fade_out=0.40
  fade_out_st=$(awk -v d="$seg_dur" -v fo="$fade_out" 'BEGIN{printf "%.4f", d-fo}')

  # Convert dB gain to linear factor for `volume` filter.
  gain_lin=$(awk -v g="$gain" 'BEGIN{printf "%.6f", 10^(g/20)}')

  # Each input slot is i+1 (slot 0 = base silence).
  FILTER+="[$((i+1)):a]atrim=duration=${seg_dur},asetpts=N/SR/TB,"
  FILTER+="afade=t=in:st=0:d=${fade_in},afade=t=out:st=${fade_out_st}:d=${fade_out},"
  FILTER+="volume=${gain_lin},adelay=${off_ms}|${off_ms}[s${i}];"
done

# amix all the segments + base silence. Use longest so we keep 1440s.
MIX_IN="[0:a]"
for i in $(seq 0 $((N-1))); do MIX_IN+="[s${i}]"; done
FILTER+="${MIX_IN}amix=inputs=$((N+1)):duration=longest:dropout_transition=0:normalize=0,"
FILTER+="atrim=duration=${DUR},asetpts=N/SR/TB[bed]"

echo "[1/2] building music bed ($BED)..."
ffmpeg -y -hide_banner -loglevel error \
  "${INPUTS[@]}" \
  -filter_complex "$FILTER" \
  -map "[bed]" \
  -ar 48000 -ac 1 -c:a pcm_s16le \
  -t "$DUR" \
  "$BED"

#------------------------------------------------------------------------------
# Final master: VO + bed → loudnorm to -14 LUFS integrated, TP -1.5 dB.
#------------------------------------------------------------------------------
echo "[2/2] mixing VO + bed → $MASTER ..."
ffmpeg -y -hide_banner -loglevel error \
  -i "$VO" \
  -i "$BED" \
  -filter_complex "[0:a]volume=1.0[v];[1:a]volume=1.0[m];[v][m]amix=inputs=2:duration=longest:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11[out]" \
  -map "[out]" \
  -ar 48000 -ac 1 -c:a pcm_s16le \
  -t "$DUR" \
  "$MASTER"

echo "duration check:"
for f in "$BED" "$MASTER"; do
  d=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$f")
  echo "  $f : ${d}s"
done

echo "wrote $BED and $MASTER"
