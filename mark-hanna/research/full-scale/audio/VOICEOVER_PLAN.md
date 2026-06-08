# Voiceover Plan — full-scale Mark Hanna documentary

> Sibling task: t_be6c1904 (audio plan) for parent t_aa7698b0 (script).
> Source script: `mark-hanna/research/script/FULL_SCRIPT.md` (24:00, 19 scenes, 12 named characters).
> Voice constraints: `mark-hanna/LEARNINGS.md`, `mark-hanna/TTS_PUNCTUATION_REFERENCE.md`.

## 1. Voice direction (single-narrator policy)

- **Single narrator** for the entire 24-minute documentary. No character actors. No voice doubles.
  Quoted speech (Hanna's *"Don't any of you realize..."*, Bryan's *"Cross of Gold"*, McKinley's *"I am a beggar"*) is delivered by the same narrator with intonation cues; on-screen typography carries the attribution. This matches the 5-minute preview's voice rule and per-scene LEARNINGS evidence that switching voices forces a full anchor-based timing re-warp (see `LEARNINGS.md` line 13: bm_george is ~12% faster than am_michael — a swap mid-doc would torch every hardcoded GSAP timing in `compositions/scene-*.html`).
- **Engine: Voicebox George (Kokoro `bm_george`)**, post-processed at `atempo=1.18` and `loudnorm I=-16:TP=-1.5`.
  - George at default rate is ~117 wpm; post-atempo lands at ~155 wpm — the floor for sustained long-form retention.
  - Voicebox app's Kokoro path is identical model weights to `hyperframes tts -v bm_george`; we render via the bundled CLI for reproducibility (no MCP roundtrip per scene).
  - Loudnorm `I=-16:TP=-1.5` matches §3.4 of the music PLAN.md (voice short-term −16 LUFS, true peak −1.5 dBFS leaves 1.5 dB safety against intersample clipping).
- **Tone direction (per scene below).** A single narrator carrying 24 minutes risks tonal flatness. The narrator's emotional register is shaped by the **script** (silence beats, sentence length, vocabulary), not by re-recorded inflection — Kokoro doesn't take direction. Where a tonal shift is required (the bullet at 22:00, the funeral at 23:00, the indictment numbers at 16:00), the script has been engineered to produce it via cadence and word choice.
- **No re-recording with a human voice actor in this pass.** Budget is zero per the music PLAN. If a human voice is later commissioned, the entire VO pipeline below applies unchanged — only the rendering step changes.

## 2. Pre-flight script hygiene (already applied to FULL_SCRIPT.md)

These transformations are baked into the script source so that *zero splice fixes are needed downstream*. Per `LEARNINGS.md` line 29, splices stack badly — the cleanest run is the one that needs the fewest splices.

| Hard pattern | Fix in script | Source line |
|---|---|---|
| Years read as cardinals (`1896` → "one thousand…") | Spell every year as words: "eighteen ninety-six" | `LEARNINGS.md` 7 |
| Leading word + comma clip (`Banks,`) | Drop the comma: "Banks assessed at…" | `LEARNINGS.md` 8 |
| Comma-listed nouns blur into proper name (`Coal, iron.` → "Cole Iron") | Use connector: "Coal and iron." | `LEARNINGS.md` 9 |
| Initials with periods (`J.P.`) hesitate | Drop dots: "JP Morgan" | `LEARNINGS.md` 26 |
| Sentence-merge for natural prosody | "brokers like him, he took a cut." (comma-merge) | `LEARNINGS.md` 27 |
| Punctuation does NOT control pacing | Real silences must be `anullsrc` chunks between renders, not ellipses | `LEARNINGS.md` 25 |

The whisper transcriber will normalize spelled-out years back to digits and may mishear `Marcus Alonzo` as "Marcus Alonso" — that's a recognition artifact, not the audio. Fix at caption-generation time via `tmp/align_caps.py` per `LEARNINGS.md` line 30, *after* the per-scene wavs are concatenated.

## 3. Per-scene render plan (19 scenes)

The full per-scene chunking lives in `research/full-scale/audio/scenes/scene-NN-narration.{md,txt}` and `research/full-scale/audio/VO_MANIFEST.json`. Summary:

| Scene | Window | Title | Words | Silence beats |
|---|---|---|---|---|
| 01 | 0:00–0:45 | THE CARTOON | 41 | 4.6 s (incl. 4 s cold-open) |
| 02 | 0:45–3:30 | THE LEDGER | 126 | 2.6 s |
| 03 | 3:30–5:00 | NEW LISBON, OHIO. 1837. | 55 | 0.4 s |
| 04 | 5:00–6:00 | THE BOY AT THE NEXT DESK | 42 | 0.6 s |
| 05 | 6:00–7:30 | THE PRICE OF THINGS | 75 | 0.0 s |
| 06 | 7:30–8:30 | CHARLOTTE | 27 | 0.8 s |
| 07 | 8:30–10:00 | THE CHOKEPOINT | 111 | 0.4 s |
| 08 | 10:00–11:30 | THE THESIS | 74 | 2.4 s |
| 09 | 11:30–14:00 | CHICAGO, 1888 | 177 | 2.8 s |
| 10 | 14:00–16:00 | THE PANIC | 163 | 2.0 s |
| 11 | 16:00–17:45 | THE MECHANISM | 79 | 1.8 s |
| 12 | 17:45–18:30 | THE FRONT PORCH | 69 | 1.0 s |
| 13 | 18:30–19:30 | CROSS OF GOLD | 78 | 1.6 s |
| 14 | 19:30–20:15 | TWO HUNDRED MILLION | 44 | 0.0 s |
| 15 | 20:15–20:45 | NOVEMBER 3, 1896 | 7 | 1.5 s |
| 16 | 20:45–22:00 | SENATOR HANNA. AND THE COWBOY. | 173 | 3.2 s |
| 17 | 22:00–23:00 | BUFFALO | 72 | 3.5 s |
| 18 | 23:00–23:30 | TYPHOID | 43 | 0.4 s |
| 19 | 23:30–24:00 | THE INHERITANCE | 73 | 1.6 s |

Total: ~1,549 spoken words (~10:00 narration at 155 wpm) + ~31 s of intentional silence beats + visual-hold time ≈ 24:00 finished runtime. The mismatch between spoken-word count and runtime is the engagement-engineering choice from FULL_SCRIPT.md §4 (long held shots on emotional anchors, big-number theatre, silence as a beat).

## 4. Per-scene rendering procedure (reproducible)

Rationale (per `LEARNINGS.md` line 18): re-rendering a 24-minute single take to fix one mispronunciation costs 10–15 min of compute and breaks every downstream caption/timing. Per-scene rendering means a fix touches one 30 s–2 min file.

```bash
cd hyperframe-test/mark-hanna

# 1. Render each scene's narration text via bundled Kokoro CLI.
#    Output goes to assets/scenes/scene-NN-narration.wav.
mkdir -p assets/scenes
for f in research/full-scale/audio/scenes/scene-*-narration.txt; do
  scene=$(basename "$f" -narration.txt)
  bunx --bun hyperframes@latest tts "$f" \
    --voice bm_george \
    -o "assets/scenes/${scene}-raw.wav"
done

# 2. Apply atempo + loudnorm per-scene (single ffmpeg pass).
for raw in assets/scenes/scene-*-raw.wav; do
  out="${raw%-raw.wav}.wav"
  ffmpeg -y -i "$raw" \
    -af "atempo=1.18,loudnorm=I=-16:TP=-1.5:LRA=11" \
    -ar 48000 -ac 1 "$out" >/dev/null 2>&1
  rm "$raw"
done

# 3. Insert silence beats between chunks (where script has [BEAT — N s]).
#    Driven by VO_MANIFEST.json — see scripts/_concat_with_beats.py for the
#    chunk-aware concat. (For scenes whose silence is purely at scene boundaries,
#    the boundary silence is added to the assembly timeline, not the per-scene wav.)

# 4. Concat per-scene wavs → assets/narration-fullscale.wav for the assembly task.
ffmpeg -y -f concat -safe 0 -i research/full-scale/audio/_concat_list.txt \
  -c:a pcm_s16le -ar 48000 -ac 1 assets/narration-fullscale.wav

# 5. Re-transcribe the full track for caption alignment.
python3 scripts/make-captions.py
python3 tmp/align_caps.py    # source-text override per LEARNINGS line 30
python3 scripts/make-captions.py --skip-whisper
```

The audio assembly (step 4) is intentionally deferred to the assembly sibling (`t_e781bf96`) because scene boundary silence + music sting + SFX layering all happen in the same pass. This task ships per-scene VO wavs as the input to that assembly.

## 5. Splice-fix budget

Per `LEARNINGS.md` line 29: **stop after 2 splices on any single scene wav.** A third splice means re-render that scene from text (1–2 min, vs. the audible "br broker" / "Co Coal" stutter that compounds at splice 4+).

Pre-emptive design choices that should hold the splice count to zero:
- Every year is pre-spelled (line 7).
- No `Word, descriptor` openers (line 8).
- All comma-listed two-word nouns use connectors (line 9).
- All `J.P.` initials are written `JP` (line 26).
- All sentence-merge prosody is in source (line 27).

If a fix is needed anyway, the `tts-narration` skill's `splice_fix.py` and `rewarp_timings.py` cover the procedure.

## 6. Recording brief (if outsourced to a human)

If the user later commissions a human voice actor, the brief below is paste-ready:

```
PROJECT:        The Ledger — Mark Hanna documentary, ~24 min
NARRATOR:       Single voice, English (US), male, 30–55, baritone-leaning
REGISTER:       HBO investigative documentary. Cold-eyed, period-aware,
                never wry. Adam-Curtis-meets-Ken-Burns.
PACE:           ~155 wpm sustained. Slower on number-theatre lines
                (let "$3,500,000" land). Faster on scene-bridge sentences.
QUOTED LINES:   Read in slightly tightened diction (Hanna's quote at 21:30,
                Bryan's "Cross of Gold" at 19:00, McKinley's "I am a beggar"
                at 14:30) — about 5% slower than narration body, no
                impersonation. The on-screen attribution does the labelling.
TECH:           48 kHz / 24-bit WAV per scene. Pop filter. ≤ -42 dBFS room
                noise. Deliver each of the 19 scene wavs separately.
TARGETS:        Loudness will be normalized to I=-16 LUFS / TP=-1.5 dBTP
                in the mix. Send raw, do not gain-stage.
DELIVERABLES:   19 wavs named scene-01-narration.wav .. scene-19-narration.wav.
                One pickups session of any line the editor flags.
TIMING:         Editor needs the wavs to fit visual windows in
                FULL_SCRIPT.md §3 ±10%. The script's word counts assume
                155 wpm; deliver any reads that drift wider than ±15% as
                pickup candidates.
HARD WORDS:     "Marcus Alonzo Hanna" (uh-LON-zoh, not uh-LON-soh).
                "Czolgosz" (CHAWL-gosh) — pronounced once at 22:30.
                "M.A. Hanna" reads as "M-A Hanna", spelled-letter style.
```

## 7. Acceptance — what this plan delivers

- ✅ Voiceover plan: single-narrator policy, engine choice, tone direction per scene (encoded in script not narrator), per-scene render procedure, splice budget, recording brief for the outsourced fallback.
- ✅ Per-scene narration text files (`scene-NN-narration.txt`) ready for TTS, with all LEARNINGS-listed pre-flight transformations applied.
- ✅ Per-scene plan files (`scene-NN-narration.md`) showing chunked TTS + silence-beat schedule.
- ✅ VO_MANIFEST.json — machine-readable index for the assembly sibling task.
- ▶ Per-scene WAV stems — produced via §4 procedure (run before handoff to t_e781bf96).
