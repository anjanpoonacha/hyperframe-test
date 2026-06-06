# PERSPECTIVE-TECHNICAL — hyperframes integration, ducking, sting placement, loudness chain

> Position paper for the 3-eyes audition. **Technical** seat. Sibling papers: PERSPECTIVE-MUSIC (cue selection / Cue C call), PERSPECTIVE-LICENSE (PD pre-flight + Content ID kit). User reads all three and picks.
>
> Scope: how to wire the music plan from `PLAN.md §3.3 / §3.4` into the existing hyperframes composition without breaking the 11-rule render contract, what to pre-render offline, and the exact ffmpeg one-liners the editor will run at audition time.

---

## TL;DR

- **Ducking option chosen: Option 1 — pre-render ducked stems offline.** Hyperframes has no sidechain, no audio-graph automation, no envelope nodes. The 11-rule contract forbids `.play()/.pause()` and any imperative audio control. Static-volume per-segment <audio> (option 2) is theoretically possible but produces audible step-discontinuities at every duck transition, cannot do the −12 → −8 dB title-card transition smoothly, and turns the index.html into ~25 audio elements when one stem per cue is enough. Pre-rendered stems are the only option that actually delivers what §3.4 specifies (variable duck depth, breath swells, smooth ramps) given the framework.
- **Marker plan is implementable as-is in hyperframes** with one caveat: Cue C end-card duration is squeezed (narration ends at 237.38 s, stage ends at 238.36 s). To give Cue C a 5–7 s statement, the editor must extend `#stage data-duration` (and the captions overlay duration) to ~243 s. Flagged in §A.4 below.
- **5 ffmpeg one-liners** delivered: (1) sidechain duck against narration.wav, (2) loudnorm per cue, (3) loudnorm final master, (4) silencedetect for unscored-runtime measurement, (5) integrated-loudness verification.
- **Status: READY** to ship — once the editor has audition stems from the Music seat and license clearance from the License seat, the wiring + mix recipe in this paper takes the audition to final cut without additional research.

---

## A. Music-track wiring inside hyperframes

### A.1 Render contract reminder (the rules this section honours)

Per the workspace `LEARNINGS.md` and the 11-rule render contract carried in CLAUDE.md (workspace root):

- Audio is **sibling-to-stage**, not nested in scene composition layers. The narration <audio> at index.html:138 already follows this. Music gets the same treatment.
- **No `.play()`, no `.pause()`**, no imperative playback control anywhere. The hyperframes runtime owns the timeline; we describe placement via `data-start` / `data-duration`.
- Every `<audio>` requires `data-start`, `data-duration`, `data-track-index`. Track indices are arbitrary numeric layers; convention here: narration is 100, music tracks live above.
- **No animation of `width`/`height`/`top`/`left` on media** — n/a for audio elements but called out for completeness.
- The `volume` HTML attribute is **not** in the standard <audio> element spec, but the `volume` *property* is settable. The hyperframes renderer reads a `data-volume` attribute (project convention; if it does not, the editor pre-bakes loudness into the stem — which is what we're doing anyway in option 1, so this is a non-issue here).

### A.2 Cue marker → data-start translation

Resolved against `assets/transcript.json` (719 word-level timestamps, narration ends at 237.38 s; ffprobe says wav file is 237.31 s). Helper: `research/music/_find_marker_times.py` (re-runnable).

| Beat | Line | Word-level start (s) | Stem |
|---|---|---|---|
| L9 titlecard | "And in eighteen ninety-six" | 13.31 | A1 |
| L13 mechanism | "Three and a half million dollars" | 21.28 | A1 (continuing) |
| L21 weight (Cue B in) | "The opposition had a thirty-six" | **44.36** | B1 |
| L23 [dry] | "Hanna had a ledger" | 48.90 | (silence) |
| L25 indictment (still dry) | "And when November came" | 50.27 | (silence) |
| L27 scene-2 mechanism | "He wasn't born with money" | 52.36 | A2a |
| L41 mechanism | "Hanna lasted one year" | 84.48 | A2a (continuing) |
| L45 weight (Cue B in) | "Then the Civil War came" | 104.34 | B2 |
| L51 mechanism (Cue A re-enter) | "Hanna walked into that business" | 116.32 | A2a (continuing — Cue B fades 0.5 s before) |
| L63 weight (Cue B brief) | "And he was bored" | 150.92 | B3 |
| L65 mechanism | "Because Hanna had figured out" | 154.84 | A2b |
| L67 [dry] | "The most powerful thing" | 165.84 | (silence) |
| L69 indictment | "That was politics" | 168.96 | (silence) |
| L71 scene-3 mechanism | "The year was eighteen eighty-eight" | **172.96** | A3a |
| L77 mechanism | "Hanna worked the convention floor" | 186.80 | A3a (continuing) |
| L79 weight (Cue B handoff) | "Sherman peaked on the first ballot" | 194.90 | B4 |
| **L81 [SILENT-REVEAL]** | "Hanna lost" | **204.34** | drop 1.5 s before = 202.84 |
| L83 mechanism re-entry (single low piano note) | "But he saw something" | 205.40 | A3b (transformed motif sting) |
| L91 [dry] | "That kind of loyalty was rare" | 223.80 | (silence) |
| L93 weight (scene-4 Cue B) | "His name was William McKinley" | 229.00 | B5 |
| L95 weight | "Hanna walked across the floor" | 231.12 | B5 (continuing) |
| L97 [dry] final | "He didn't know it yet" | 233.96 | (silence) |
| coda (Cue C) | end card | 235.6 → stage end | C1 |

These are word-level **transcript** times against `assets/narration.wav`. They are word-onset accurate, not phrase-onset, so add a 100–200 ms head-room when picking the actual cue-out point (you want music to settle before the dry word lands, not be cut off by it).

### A.3 The exact <audio> blocks for `index.html`

Paste these as siblings to `<audio id="narration">` (line 138 in current index.html). DO NOT modify scene divs or the GSAP timeline. **Do not** edit index.html now — these are paste-at-audition-time blocks.

```html
<!-- ================================================================== -->
<!-- MUSIC TRACK (sibling to #narration; pre-rendered ducked stems)      -->
<!-- ================================================================== -->

<!-- Cue A1 — section 1 mechanism (title-card peak baked in 0-7s of stem) -->
<audio id="cue-a1" data-start="13.31" data-duration="34.10" data-track-index="101"
       src="assets/music/cue-a1-section1-titlecard.wav"></audio>

<!-- Cue B1 — opposition / preacher (Cue A1 already faded by 47.4) -->
<audio id="cue-b1" data-start="44.36" data-duration="4.04" data-track-index="102"
       src="assets/music/cue-b1-opposition.wav"></audio>

<!-- Cue A2a — section 2 mechanism through to L63 weight handoff -->
<audio id="cue-a2a" data-start="52.36" data-duration="97.20" data-track-index="101"
       src="assets/music/cue-a2a-section2-mechanism.wav"></audio>

<!-- Cue B2 — Civil War / marriage / father-in-law's coal-and-iron -->
<audio id="cue-b2" data-start="104.34" data-duration="11.00" data-track-index="102"
       src="assets/music/cue-b2-civil-war.wav"></audio>

<!-- Cue B3 — "And he was bored" -->
<audio id="cue-b3" data-start="150.92" data-duration="3.50" data-track-index="102"
       src="assets/music/cue-b3-bored.wav"></audio>

<!-- Cue A2b — final mechanism beat before L67 dry -->
<audio id="cue-a2b" data-start="154.84" data-duration="9.50" data-track-index="101"
       src="assets/music/cue-a2b-section2-tail.wav"></audio>

<!-- Cue A3a — scene 3 mechanism to before L79 weight -->
<audio id="cue-a3a" data-start="172.96" data-duration="21.00" data-track-index="101"
       src="assets/music/cue-a3a-section3-mechanism.wav"></audio>

<!-- Cue B4 — Sherman bleed-out, exit 1.5s before L81 silent-reveal -->
<audio id="cue-b4" data-start="194.90" data-duration="7.94" data-track-index="102"
       src="assets/music/cue-b4-sherman.wav"></audio>

<!-- ===== SILENT-REVEAL drop window 202.84 → 205.40 (no music elements) ==== -->

<!-- Cue A3b — single low piano note re-entry (transformed motif) -->
<audio id="cue-a3b" data-start="205.40" data-duration="17.40" data-track-index="101"
       src="assets/music/cue-a3b-piano-reentry.wav"></audio>

<!-- Cue B5 — scene 4 weight under name reveal + walk -->
<audio id="cue-b5" data-start="229.00" data-duration="3.96" data-track-index="102"
       src="assets/music/cue-b5-mckinley.wav"></audio>

<!-- Cue C — coda over end card -->
<audio id="cue-c" data-start="235.60" data-duration="2.76" data-track-index="103"
       src="assets/music/cue-c-coda.wav"></audio>
<!-- NOTE: with current stage data-duration=238.36 the coda only has 2.76s.
     If the audition picks a longer Cue C statement (5-7s), the editor must:
       1. Extend #stage data-duration on index.html:116
       2. Extend #captions data-duration on index.html:130
       3. Bump scene-04's final fade-out target on index.html:162
     A 243.0s stage gives 7.4s for Cue C. Flagged in §A.4. -->

<!-- ================================================================== -->
<!-- STING TRACK — single motif family, ~1.5s each, same src              -->
<!-- ================================================================== -->

<!-- Sting 1 @ scene 1 → 2 cut -->
<audio id="sting-1" data-start="53.01" data-duration="1.50" data-track-index="110"
       src="assets/music/sting-motif.wav"></audio>

<!-- Sting 2 @ scene 2 → 3 cut -->
<audio id="sting-2" data-start="119.46" data-duration="1.50" data-track-index="110"
       src="assets/music/sting-motif.wav"></audio>

<!-- Sting 3 @ scene 3 → 4 cut -->
<audio id="sting-3" data-start="173.12" data-duration="1.50" data-track-index="110"
       src="assets/music/sting-motif.wav"></audio>

<!-- Sting 4 (re-entry note) @ silent-reveal exit, same family.
     The task brief asked for "4 sting elements"; the narration-annotated
     marker file only specifies 3 scene-cut stings + 1 transformed-motif
     re-entry on a single low piano note (post-L81). That re-entry is
     functionally a sting, so we expose it here as sting-4 (separate src
     because timbre is "single low piano note", not the snare/cornet sting).
     If the editor prefers to consider this part of cue-a3b instead, delete
     this block — cue-a3b already starts at 205.40. -->
<audio id="sting-4" data-start="205.40" data-duration="1.50" data-track-index="110"
       src="assets/music/sting-piano-note.wav"></audio>
```

**Track-index layering rationale:**
- 100 = narration (existing, do not change)
- 101 = Cue A bed (mechanism)
- 102 = Cue B float (weight)
- 103 = Cue C coda (separate so end-card mix can have its own loudness target)
- 110 = sting family (separate so stings sit on top of any tail of A/B without bus collision)

The hyperframes renderer is layer-agnostic for audio (no ducking by track), so these indices are organizational only — the duck is **baked into each stem** offline.

### A.4 Stage-duration squeeze (flagged blocker, easy fix)

Current `#stage data-duration="238.36"` and narration ends at 237.38 s. That leaves 0.98 s after the last word of L97 for Cue C. PLAN §3.3 says **"Cue C at full volume over a static end card. Fade to silence."** A 0.98 s window cannot land a "full volume statement + fade" with any musical credibility.

**Resolution path** (editor decides at audition):
- Audition Cue C at 3 lengths: 2.76 s (current stage), 5.0 s (243.36 s stage), 7.4 s (245.76 s stage).
- The 5–7 s variants require extending three numbers: stage `data-duration`, captions overlay `data-duration`, and the scene-04 final fade target on `tl.to("#scene-04", { opacity: 0, duration: 1.0 ... }, 236.78)` (currently anchored to old end). Mechanical edit; no GSAP timing warp needed because no narration was added.

Not a blocker for the marker plan itself — just a parameter the editor sets when Cue C is picked.

---

## B. Ducking implementation — Option 1 (pre-rendered stems), recommended

### B.1 Why option 1 wins

| Requirement from PLAN §3.4 | Option 1 (offline stems) | Option 2 (per-segment <audio> with discrete volume) |
|---|---|---|
| −8 dB baseline duck, sparse cues | clean, ramped | step at every <audio> boundary |
| −12 dB title-card statement only | smooth ramp inside one stem | requires splitting Cue A1 into ≥3 <audio> sub-segments with hard boundaries |
| Manual breath swells +2–4 dB in inter-sentence gaps | natural sidechain release does this for free | would need 1 <audio> element per inter-sentence gap (~30+ extra elements per cue) |
| EQ pocket −3 to −4 dB at 1–4 kHz on music bus | applied once during stem render | impossible without per-segment filter chain (no audio-graph in hyperframes) |
| Voice HPF + presence boost | applied to narration once during final master | impossible against the existing narration.wav without a re-bake |
| **Silent-reveal drop at L81 must be clean** | gap is between two <audio> elements with full fade in stem; sample-accurate silence | gap is between two <audio> elements; same outcome here — but option 2 still doesn't help |
| 11-rule render contract (no `.play()/.pause()`) | satisfied (framework owns playback) | satisfied (framework owns playback) |
| index.html readability | 12 audio elements | ~25–35 elements, dense `data-volume` clutter |

The **silent-reveal beat (L81)** is the load-bearing case for picking the right option. In both options the silence is achieved by simply not having any music element scheduled in the 202.84–205.40 window. Option 1 is cleaner because stem A3a already has its trailing fade ramped to silence inside the file at the right phrase boundary, and stem A3b begins on the single low piano note attack — no boundary-step artifact. Option 2 would step from `volume=0.4` to `volume=0` at a hard <audio> end, which is fine for the silence onset but cannot do the *re-entry* on a single transformed-motif piano note without yet another sub-segment.

Option 1 is unambiguously the right call for this composition.

### B.2 The exact ffmpeg sidechain duck command (one example cue)

The narration is the ducker key; the music cue is the ducked source.

```bash
# Pre-render Cue A2a (scene-2 mechanism, 52.36s entry, 97.2s duration).
# Inputs: source music (cue-a2a-source.wav) + narration.wav (key).
# Output: ducked stem aligned to the narration timeline.
#
# Filter chain explained:
#   atrim+asetpts                  — slice narration to the cue window so the
#                                    sidechain key is exactly the VO under this cue
#   sidechaincompress              — duck source by ~8 dB when key signal exceeds
#                                    threshold (-26 dB ~= speech presence)
#   highpass=f=80,lowshelf,equalizer — voice EQ pocket on the MUSIC (carve 1-4 kHz)
#   loudnorm                       — land at -27 LUFS short-term integrated for the
#                                    music bed under VO (PLAN §3.4 number)

ffmpeg -y \
  -i assets/music/_source/cue-a2a-source.wav \
  -i assets/narration.wav \
  -filter_complex "
    [1:a]atrim=start=52.36:duration=97.20,asetpts=PTS-STARTPTS,
         volume=1.0[key];
    [0:a]highpass=f=40,
         equalizer=f=2500:width_type=o:width=2:g=-3.5,
         equalizer=f=1500:width_type=o:width=2:g=-3.0[mus];
    [mus][key]sidechaincompress=
         threshold=0.05:ratio=4:attack=15:release=250:makeup=1:
         level_sc=1[ducked];
    [ducked]loudnorm=I=-27:TP=-2.0:LRA=7:print_format=summary[out]
  " \
  -map "[out]" -ar 48000 -ac 2 -c:a pcm_s16le \
  assets/music/cue-a2a-section2-mechanism.wav
```

Knobs the editor will tune:
- `threshold=0.05` (≈ −26 dBFS) → raise to 0.08 if the duck triggers on noise floor or quiet syllables; lower to 0.03 if VO sneaks through.
- `ratio=4` → 4:1 gives ~−8 dB of duck for typical voice peaks. Bump to `ratio=6` for the **title-card** Cue A1 stem (the −12 dB depth).
- `attack=15` ms / `release=250` ms → fast enough to catch sentence onsets; release long enough that breath swells lift naturally between sentences (this *is* the §3.4 "+2–4 dB breath swell" effect — it falls out of the sidechain release curve for free).
- The `equalizer` chain pre-carves the music bus pocket at 1–4 kHz so the duck doesn't have to do all the work.

Apply this template per cue with the right `atrim start/duration` for the cue's narration window. **Cue A1 only**: change `ratio=4` → `ratio=6` (title-card −12 dB depth). All other cues keep `ratio=4` for the −8 dB baseline.

### B.3 The silent-reveal stem boundary

The stem boundary handling that makes the L81 drop clean:

- `cue-a3a` source pre-ends with a ~0.6 s fade-to-zero crossing at a phrase boundary inside the source — pre-rendered with `afade=t=out:st=20.0:d=0.6` appended to the filter chain, then re-loudnormed. The stem is sample-accurate silence at its trailing edge.
- The next 2.56 s in the timeline have **no audio element scheduled** — that is the silent-reveal window. The narration plays L81 ("Hanna lost.") at 204.34–205.40 s in this window, dry.
- `cue-a3b` source begins with a single low piano note attack at sample 0; pre-render with `afade=t=in:st=0:d=0.05` (5 ms) to avoid click. Per §3.3 this is the "transformed motif Cue A" re-entry.

There is no sidechain duck on the silent-reveal flank because there is no music to duck. The mechanism is structural: the gap exists in the timeline because no <audio> covers it.

---

## C. Loudness + EQ chain — concrete pre-render pipeline

PLAN §3.4 numbers (non-negotiable):
- Master integrated **−14 LUFS**
- Voice short-term **−16 LUFS**
- Music bed under VO **−27 to −28 LUFS** short-term
- Music bed in pure-B-roll **−20 LUFS** short-term
- EQ pocket **−3 to −4 dB at 1–4 kHz** on music bus
- Voice HPF **80–100 Hz** + 2–4 kHz presence

### C.1 Per-cue loudnorm pass (already inlined in §B.2)

Each music cue is normalized to **I=-27 LUFS, TP=-2.0, LRA=7** during the offline ducking render. That hits the under-VO target. For pure-B-roll cues (none in this cut, but if a future episode has them), use `I=-20`.

### C.2 Voice loudnorm + EQ pass (one-time on narration.wav)

```bash
# Pre-master narration: HPF, presence boost, voice loudnorm.
# Source: assets/narration.wav (current bm_george render).
# Output: assets/narration-mastered.wav (do NOT overwrite the source).
# This file becomes the new key for sidechain ducks AND the voice track in final master.

ffmpeg -y -i assets/narration.wav \
  -af "
    highpass=f=90,
    equalizer=f=3200:width_type=o:width=1.5:g=2.5,
    loudnorm=I=-16:TP=-1.5:LRA=8:print_format=summary
  " \
  -ar 48000 -ac 1 -c:a pcm_s16le \
  assets/narration-mastered.wav
```

Editor must regenerate captions afterwards if the loudnorm shifts the duration (it usually doesn't with single-pass loudnorm; if duration drifts >50 ms, run `python3 scripts/make-captions.py` per LEARNINGS.md).

**Important:** if the editor uses `narration-mastered.wav` instead of `narration.wav` as the sidechain key in §B.2 commands, the duck triggers more reliably (HPF + presence boost gives a cleaner key signal). Recommended.

### C.3 Final master pass (against rendered MP4)

After hyperframes renders the MP4 with all stems in place, one final loudnorm pass to land integrated at −14 LUFS:

```bash
# Two-pass loudnorm for accurate integrated target.
# Pass 1: measure
ffmpeg -i renders/mark-hanna-ep01.mp4 \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json" \
  -f null - 2>&1 | tee /tmp/loudnorm-pass1.json

# Pass 2: apply (paste measured values from pass 1 into the second command)
# Look in pass1 output for: input_i, input_tp, input_lra, input_thresh, target_offset
ffmpeg -y -i renders/mark-hanna-ep01.mp4 \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11:
       measured_I=<paste>:measured_TP=<paste>:measured_LRA=<paste>:
       measured_thresh=<paste>:offset=<paste>:linear=true:print_format=summary" \
  -c:v copy -c:a aac -b:a 320k \
  renders/mark-hanna-ep01-mastered.mp4
```

YouTube will normalize anything above ~−14 LUFS; landing at −14 means YouTube does nothing and the mix you delivered is the mix the viewer hears. Above −14 → YouTube turns you down (your dynamics survive but headroom is wasted). Below −14 → YouTube does NOT turn you up (everyone else sounds louder; you sound quiet by comparison).

### C.4 Verification (third command)

```bash
# Confirm the final master landed at -14 LUFS integrated.
# This is the dispositive measurement; vibes-checking is not a method.
ffmpeg -i renders/mark-hanna-ep01-mastered.mp4 \
  -af loudnorm=print_format=json -f null - 2>&1 \
  | grep -E '"input_i"|"input_tp"|"input_lra"'
```

Expect `input_i` within ±0.5 LU of −14.0. If outside that band, the pass-2 measured values were wrong (re-run pass 1 cleanly without other ffmpeg traffic).

---

## D. Unscored-runtime measurement (PLAN §5 row 6)

PLAN §5 demands: **40–60% of 238.36 s = 95.3–143.0 s of music-off** in the final mix. The check requires soloing the music bus.

### D.1 Build the music-only stem

Hyperframes renders a single MP4 with everything mixed. To solo the music bus for measurement, render the stems-only mix offline:

```bash
# Sum all music + sting stems to a single music-only WAV at the timeline positions
# from §A.3. amix can't easily do timed positioning, so use adelay per stem.
# This is the editor's reference music bus — measure unscored runtime against THIS file.

ffmpeg -y \
  -i assets/music/cue-a1-section1-titlecard.wav \
  -i assets/music/cue-b1-opposition.wav \
  -i assets/music/cue-a2a-section2-mechanism.wav \
  -i assets/music/cue-b2-civil-war.wav \
  -i assets/music/cue-b3-bored.wav \
  -i assets/music/cue-a2b-section2-tail.wav \
  -i assets/music/cue-a3a-section3-mechanism.wav \
  -i assets/music/cue-b4-sherman.wav \
  -i assets/music/cue-a3b-piano-reentry.wav \
  -i assets/music/cue-b5-mckinley.wav \
  -i assets/music/cue-c-coda.wav \
  -i assets/music/sting-motif.wav \
  -i assets/music/sting-motif.wav \
  -i assets/music/sting-motif.wav \
  -i assets/music/sting-piano-note.wav \
  -filter_complex "
    [0:a]adelay=13310|13310[a0];
    [1:a]adelay=44360|44360[a1];
    [2:a]adelay=52360|52360[a2];
    [3:a]adelay=104340|104340[a3];
    [4:a]adelay=150920|150920[a4];
    [5:a]adelay=154840|154840[a5];
    [6:a]adelay=172960|172960[a6];
    [7:a]adelay=194900|194900[a7];
    [8:a]adelay=205400|205400[a8];
    [9:a]adelay=229000|229000[a9];
    [10:a]adelay=235600|235600[a10];
    [11:a]adelay=53010|53010[s1];
    [12:a]adelay=119460|119460[s2];
    [13:a]adelay=173120|173120[s3];
    [14:a]adelay=205400|205400[s4];
    [a0][a1][a2][a3][a4][a5][a6][a7][a8][a9][a10][s1][s2][s3][s4]
      amix=inputs=15:duration=longest:dropout_transition=0[out]
  " \
  -map "[out]" -ar 48000 -ac 2 -c:a pcm_s16le \
  /tmp/music-bus-only.wav
```

### D.2 Measure unscored runtime (the actual one-liner)

```bash
# silencedetect at -60 dB threshold, 0.4s minimum silence (PLAN §5 spec).
# Sums silent durations and prints unscored-seconds + percent of 238.36s runtime.
# Pure ffmpeg + awk; no sox dependency.

ffmpeg -hide_banner -nostats -i /tmp/music-bus-only.wav \
  -af "silencedetect=noise=-60dB:duration=0.4" -f null - 2>&1 \
| awk '
  /silence_duration:/ { sum += $NF }
  END {
    total = 238.36
    pct = sum / total * 100
    printf "unscored runtime: %.2f s  (%.1f%% of %.2f s)\n", sum, pct, total
    printf "target: 95.3-143.0 s  (40-60%%)\n"
    if (sum < 95.3)      print "STATUS: under-scored (too much music; thin Cue A or shorten cue stems)"
    else if (sum > 143.0) print "STATUS: over-scored (too much silence; either correct or cues are mis-placed)"
    else                  print "STATUS: in-target band ✓"
  }'
```

This is the dispositive check. If the result is in-band, ship. If not, the editor adjusts cue durations (not the marker plan — the marker plan has been verified to land within band by the math in `narration-annotated.txt` lines 184–188).

### D.3 Sanity prediction from the marker plan

Per `narration-annotated.txt` ll. 184-188 the marker plan predicts ~95–110 s unscored: cold-open silence (~12 s) + 4 dry climax windows (~6 s each = ~24 s) + silent-reveal (~3 s) + dry indictment beats (~6 s + ~5 s) + intra-section pad-outs ≈ 95–110 s.

That lands at the **bottom edge** of the 40–60% band. The editor has headroom to *add* music if a cue feels cold, but no headroom to add silence without dropping out of band. Practical implication: if the music seat picks denser/longer stems than the duration table in §A.3 specifies, push back — there's no slack.

---

## E. Status

**READY** — the marker plan from `narration-annotated.txt` is implementable in hyperframes as written, using:
- 12 music <audio> elements + 4 sting elements (16 total), all sibling to `<audio id="narration">`.
- Pre-rendered ducked stems via the §B.2 ffmpeg sidechain command, parameterized per cue.
- Voice pre-master pass (§C.2), per-cue loudnorm during ducking (§B.2 inline), final-master loudnorm against rendered MP4 (§C.3), verification (§C.4).
- silencedetect-based unscored-runtime check (§D.2) as the dispositive gate before publishing.

**One parameter call** the editor must make at audition time:
- Cue C duration (2.76 s as-is vs 5.0 s vs 7.4 s) → if longer than 2.76 s, extend `#stage data-duration` + `#captions data-duration` + scene-04 fade target as listed in §A.4.

**No blockers** in the wiring or mix recipe. License/sourcing/Cue C-treatment are sibling-paper concerns (PERSPECTIVE-LICENSE / PERSPECTIVE-MUSIC); the technical plumbing is solved.

---

— default profile, technical seat, t_73dd00b5
