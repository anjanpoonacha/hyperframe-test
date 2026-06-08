# REBUILD.md — Mark Hanna ep01: Phased Rebuild from the 4-min Preview

> Owner: this directory. Read this first; it's the spine.
>
> Created 2026-06-07 after the v2 24-min full-scale render was rejected.
> Root cause: (a) bad audio mix — music at VO level, no sidechain ducking;
> (b) generator-grade scenes (5.8× less expressive than the preview).
> Both v2 artifacts were deleted; v1 24-min and the 4:30 preview survive.
>
> **Voice is NOT the issue. bm_george at normal speed is locked from
> yesterday's preview work — it's the documentary voice. Do not confuse
> with the shorts pace work; this is long-form and stays at default speed.**

---

## 1. Source of truth — one place, no ambiguity

| Concern | Lives at |
|---|---|
| **Composition + renders** | `~/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna/` (this dir) |
| **Editorial inputs** (script, research, voiceover text, PD assets) | `~/SAPDevelop/github.com/personal/american-audacity/episodes/mark-hanna/` |
| **Abandoned stub — DO NOT EDIT** | `~/SAPDevelop/github.com/personal/american-audacity/video-projects/mark-hanna-e01/` |
| **Shorts (vertical 9:16)** | `~/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna-shorts/` (separate composition) |

If the script changes, edit `american-audacity/episodes/mark-hanna/script.md` and re-sync to
`assets/` here. **Composition HTML is authored only in this dir.**

---

## 2. The 4:30 preview is the fidelity ceiling — here's why it works

| Scene | Lines | Voice | What makes it land |
|---|---|---|---|
| 01 cold-open | 490 | bm_george | hand-tuned per-element GSAP, BEAT-MAP comments tied to whisper word boundaries, real Ken Burns push (1.00→1.04 over 12s, not 0.55→0.561) |
| 02 who-was | 594 | bm_george | bespoke 2-pane layouts, donor-list staggered write-ins matched per-line to specific narration words |
| 03 machine | 497 | bm_george | mechanism reveal beat with snare-cluster sync points (985/986/987s), real motion easing curves |
| 04 finding-mckinley | 594 | bm_george | Rockefeller diptych with hand-authored 1px Hanna Amber hairline draw, scale push 1.00→1.02 over 12s plus pull-out 1.04→1.00 over 25s |

**Average: 544 lines per scene, ~50–80 hand-written `tl.to()` calls.**

The 19 full-scale scenes that replaced this average **94 lines, generator-emitted**. That gap is
the entire problem.

---

## 3. Mistakes from v1 + v2 — never again

These are extracted from `LEARNINGS.md` and the v2 failure tonight. Numbered for direct rule citation.

### Audio / voice
- **M1.** **Voice is locked: `bm_george` at default speed (Kokoro).** This was finalized in
  yesterday's preview work — bm_george is the documentary voice for this project. Do not
  add `--speed`. The "12% faster than am_michael" bullet in `LEARNINGS.md` is a *timing-rewarp*
  warning (every hardcoded GSAP timing drifts on voice swap), NOT a complaint about pace.
  Long-form pace ≠ shorts pace; the shorts work used different voices for retention reasons,
  this project does not. Do not bring shorts voice debates into this plan.
- **M2.** **Voiceover text is phonetic prose. Spell everything. No symbols.**
  Don't fake pacing by fragmenting prose into one-word "sentences" — Kokoro
  ignores it (every terminator lands within a 22 ms band, spike-tested over
  87 clips). Pacing is engineered via ffmpeg silence between chunks (M15),
  not via fake periods. Rule: write `Coal and iron.` not `Coal. Iron.` —
  prose reads as prose for the human reviewer AND for the TTS.
  Spell everything else too: `eighteen ninety-six` not `1896`,
  `three and a half million dollars` not `$3,500,000`, `JP Morgan` not
  `J.P. Morgan`, `Marcus Alonzo Hanna` not `M.A. Hanna`, `and` not `&`,
  `percent` not `%`, `Doctor` not `Dr.`, `September fourteenth` not
  `Sept. 14`, `two-fifteen in the morning` not `2:15 a.m.`
- **M3.** **Numbers need landing room. Spelled-out is half the job; the other half is silence.**
  In v1 some numbers were "blurted out" — Kokoro ran the digit-words straight into the next
  sentence so the meaning under-delivered. A number is an emotional payload, not a fact in
  passing. Rule:
  - Spell the year: `eighteen ninety-six` not `1896` (Kokoro reads "one thousand eight hundred…")
  - Spell the dollar: `three and a half million dollars` not `$3,500,000`
  - **Land it with a beat.** Big numbers get ≥0.4 s silence AFTER them (in the manifest,
    not as fake punctuation). The on-screen typography arrives during that silence — eye
    reads `$3,500,000` while the ear breathes. That's the dual-channel landing.
  - **Round in the voiceover, precise on screen.** Voice says "just under two and a half
    million," screen shows `2,429,300`. The voice carries emotional weight; the screen
    carries credibility. Never make Kokoro read commas.
  - **One number per breath.** Don't list four dollar amounts in one sentence — split into
    chunks with 0.3-0.6 s pauses so the audience can catch each one.
- **M4.** `J.P.` initials clip; `JP` flows. (Spike: 1.98s vs 1.83s.) Strip periods inside initials.
- **M5.** Splices accumulate stutter at boundaries. After 4+ splices stacked over the same
  base wav, you hear "br broker" / "Co coal" stutters because whisper word boundaries are
  ~70 ms loose. Fix: splice for 1–2 localized issues, full re-render past that.
- **M6.** **The v2 mix had VO + music at the same level.** Music must duck under VO.
  Sidechain compression on the music bus, keyed off the VO, ~6 dB duck floor minimum.
  See `research/full-scale/audio/MUSIC_PLAN.md` §3 for cue levels — they were spec'd correctly,
  the mix step did not implement them. Don't ship a mix without `ffmpeg silencedetect` proof
  that VO peaks 6+ dB above music during spoken windows.

### Composition
- **M7.** Generator-grade scenes ≠ hand-tuned scenes. The 5.8× line-count gap is real expressiveness
  loss. **Rule going forward: every scene gets ≥400 lines of hand-authored layout + GSAP, with a
  BEAT-MAP comment block matching whisper word boundaries.** No more bulk-emit from a Python dict.
- **M8.** Scene 4/9/10 hand-tunes proved the pattern works (Rockefeller diptych, Sherman corner-pin
  shrink, McKinley front-porch counter). Use those as the template, not the generator.
- **M9.** When a CSS rule sets `transform: translate(-50%,-50%) scale(N)` and GSAP later animates
  `scale`, GSAP overwrites the entire transform — discarding centering. Fix: drop the CSS transform
  and prepend `gsap.set(el, { xPercent: -50, yPercent: -50, scale: N })` before any tweens.
- **M10.** Caption safe-zone is **y < 880**. `compositions/captions.html` puts cues at `bottom:32px`
  with 36px / 1.25 line-height + 14px padding. Two-line caption occupies y≈930–1055. Anything below
  y≈880 collides on 2-line wraps. Test against worst-case 2-line cue, not single-line samples.
- **M11.** Voice swap drifts every hardcoded GSAP timing. Use **scene-relative timing**
  (every `tl.to(... , N)` is relative to scene start, not absolute). Then a per-scene VO re-render
  doesn't require re-warping any visual GSAP — `build_master.sh` rebuilds the master VO and visuals
  stay locked.

### HyperFrames Studio
- **M12.** **HyperFrames Studio writes back when you scrub/click.** It silently injects
  `data-hf-studio-*` attributes + inline `style="translate:..."` overrides. This caused
  cartoon-flying-bottom-left and captions-at-top-of-frame on prior runs. **Treat the Studio UI
  as read-write.** After any preview session, grep `'data-hf-studio'` and remove those overrides.

### Captions
- **M13.** **Captions track stays in.** Yesterday's preview ships `compositions/captions.html`
  wired in (cues at `bottom:32px`, 36px / 1.25 line-height, ≤5 words per cue, breaks on `.!?`).
  The earlier "drop captions for long-form" idea was wrong for this project — verified against
  `preview/index.html` line 130. The rule is M10 (safe-zone y<880), not "no captions". When
  audio changes: re-run `bun run captions:make` then `bun run captions:align` to
  source-text-override (per LEARNINGS line 30). Drift target ≤100 ms.

### Voice fidelity to the locked preview
- **M17.** **The 4-min preview's `narration.txt` is the locked voice anchor.** Every line in
  the long-form script is read against it. Specific rules derived from the preview:
  - **Em-dash budget: ≤1 per paragraph, ≤3 per scene.** Preview has zero em-dashes in 97 lines.
    When you reach for an em-dash, you're probably reaching for a [BEAT] marker — use that.
  - **No subject-verb em-dash splits.** Banned: "Money — was the second most powerful thing"
    or "Under the handkerchief — is a revolver." Preview voice never breaks subject from verb
    with a dash.
  - **No em-dash before a date or number anchor.** Banned: "— in nineteen oh four". Use the
    Date Anchor transition: "In nineteen oh four, Hanna…"
  - **Past tense throughout the body.** Preview is uniformly past tense across 97 lines.
    Historic-present at climaxes is a TV-trailer reflex and breaks voice. Direct primary-source
    quotes use whatever tense the source used.
  - **Witness voice, not teacher voice.** Banned: "He is, at last, what he set out to be: a
    senator who…" or "Mark Hanna — who has watched men more carefully than any other man — sees
    what is coming." Preview voice reports the act, not the actor's qualifications.
  - **No alliterative title-card prose.** Banned: "before the kingmaker could make a king" /
    "makers and breakers" / "the silver-tongue had broken thirty-six years of political quiet."
    Use the date / name / sensory anchor.
  - **Rhetorical questions are zero, except primary-source quotes flagged with `<!-- noqa:
    STYLE: direct historical quote -->` and a citation.**
  - **Test:** if a passage in the script does not sound like it could be cut into the preview
    audio without a seam, rewrite it.

### Production architecture
- **M14.** **Voiceover ≠ on-screen typography.** Two layers, two jobs.
  *Voiceover (TTS input)*: phonetic prose, rounded numbers ("three and a half million dollars").
  *On-screen typography (composition HTML)*: precise number with commas/symbols (`$3,500,000`).
  They land together — voice carries emotion, screen carries credibility. Same source-of-truth
  number; different rendering per channel. Never put the precise number in the voiceover, never
  hide the precise number from the screen.
- **M15.** **Chunked audio with a manifest.** No more 1440-second master built atomically.
  Architecture:
  ```
  assets/narration/
    manifest.json              ← single source of truth for pacing + chunk order
    chunks/
      001-cartoon.wav          ← one paragraph per wav (re-renderable in ~5 s)
      002-name-was.wav
      …
    narration.fullscale.wav    ← derived: ffmpeg-concat per manifest, ~3 s rebuild
  ```
  `manifest.json` is `[{"chunk":"001-cartoon.wav"},{"silence":0.6},{"chunk":"002-name-was.wav"},…]`
  — pauses are data, not embedded in audio. To change a pause: edit number, run
  `bun run audio:concat` (~3 s). To fix a sentence: re-render that one chunk
  (~5 s), re-concat. To A/B a beat: swap a chunk filename in manifest.

  **Chunked vs single-call: research-validated equivalence.** Kokoro is chunk-level,
  not sentence-level — up to ~510 phonemes (~30–50 s of speech) per forward pass with
  full self-attention WITHIN that chunk, but **no state across chunks**. Whether you pass
  the entire 5,500-word script in one call or 19 separate scene calls, KPipeline
  internally chunks at phoneme boundaries anyway. External chunking ≡ internal chunking
  perceptually; we just get explicit per-scene wavs + JSON-editable pauses as the bonus.
  Source: perplexity research pass 2026-06-07 against StyleTTS2 paper, hexgrad/Kokoro
  model card, KPipeline source, Kokoro-FastAPI smart-chunker docs.

  Scenes longer than ~45 s will split internally (the renderer does this at sentence
  boundaries within the scene). We cannot control that, but it doesn't matter — the
  split happens at natural pauses, prosody breaks are normal there.

  This unifies the existing `research/full-scale/audio/scenes/scene-NN-narration.md`
  chunk pattern (which was right) with one root-level manifest (instead of 19 disconnected
  scene plans). The "Voicebox George + atempo 1.18" line in those existing files is stale
  and contradicts M1 — drop it during consolidation.

- **M15a. Loudness normalization: whole-stem only, two-pass, linear=true.** Research-
  validated: Kokoro is deterministic + non-sampling, so output loudness is consistent
  call-to-call for the same voice. Per-chunk loudnorm is **not just unnecessary — it
  actively harms the result** by boosting quieter chunks more than louder ones, creating
  audible micro-jumps at boundaries. Standard practice (EBU R128, ITU-R BS.1770,
  Google Assistant guidelines): single two-pass loudnorm on the concatenated master with
  `linear=true` so a single constant gain applies across the whole file, preserving
  natural dynamics between scenes.

  Recipe for our `-15 LUFS / -1.5 dBTP / LRA 18` target:
  ```bash
  # Pass 1 — measure
  ffmpeg -i narration.fullscale.raw.wav \
    -af "loudnorm=I=-15:TP=-1.5:LRA=18:print_format=json" \
    -f null - 2> loudnorm_log.json
  # Pass 2 — apply single linear gain using measured values from pass 1
  ffmpeg -i narration.fullscale.raw.wav \
    -af "loudnorm=I=-15:TP=-1.5:LRA=18:measured_I=...:measured_TP=...:measured_LRA=...:measured_thresh=...:offset=...:linear=true" \
    -ar 48000 -c:a pcm_s16le narration.fullscale.wav
  ```
  `linear=true` is the critical flag — without it, loudnorm applies time-varying gain
  (compression). With it, single constant gain across the file = natural dynamics
  preserved.
- **M16.** **Runtime budget is 24–35 minutes.** Don't pad to hit a target. Don't compress
  to hit a target. **Don't invent a target either.** v1's 1440 s was a constraint that pushed
  scene 17 (Buffalo) to 60 s when it needed 95 s. Removing the constraint per user direction.
  When v2 expansion of scenes 17/18 grew the script ~65 s past v1's spot, the right
  answer is "the script grew to N seconds; we'll measure once rendered" — NOT "target 25:00."
  Specifying a tighter intermediate target ("~25:00") inside this 24–35 window violates the
  rule. Caught and corrected in this session 2026-06-07.

---

## 4. Phased rebuild — collaborative preview loop

> **The user does not trust the v2 process. So the user will be in the preview every
> 2–3 minutes / per scene. There is no async sign-off; we review live, together,
> in the browser.**

### The loop

```
PER CHUNK (one scene, OR ~2–3 min of timeline if a scene is shorter):

  1. PROPOSE  — I read script + matching preview scene + SHOT_BOARD; I write a
                short SCENE_<NN>_PLAN.md (beats, GSAP gestures, asset list,
                ~400 line target). I post it to chat.

  2. AUTHOR   — I hand-author compositions/scene-NN-<slug>.html at preview
                fidelity (no -fs suffix; replacing the generator output, not
                adding to it). BEAT-MAP comment block at top tying every
                keyframe to a whisper word boundary. Captions for this scene
                regenerated (M13).

  3. PREVIEW  — I tell user: "ready, run `npm run dev` and open the URL".
                User runs the command (Hermes can't keep `npm run dev` alive
                across turns reliably; user owns the long-lived process).

  4. WALKTHROUGH — Both review, together:
                  - User scrubs the scene live in the browser.
                  - I capture `npx hyperframes snapshot --at <times>` and
                    read every PNG myself with vision_analyze.
                  - I post my findings (collisions, overflows, timing drift,
                    Studio drag-write residue) to chat.
                  - User adds their findings (anything I miss).

  5. DECIDE   — User says: ✅ approved, 🔁 fix N specific things, or ❌ redo.
                On ✅: commit `feat(scene-NN): <title>`, advance to next chunk.
                On 🔁: I patch the named issues only; back to step 4 (no full
                re-author).
                On ❌: back to step 1 with notes.

NO `npm run render` until ALL 19 scenes signed off + audio mix signed off.
NO BIG-BANG ASSEMBLY at the end either — every scene was already preview-tested.
```

### Chunk sizing

- **One scene per chunk** is the default — the preview's 4 scenes average 60 s each,
  the full-scale's 19 scenes average 75 s. Both fit "every 2–3 min" comfortably.
- **Long scenes split mid-scene.** Any scene whose duration > 180 s gets reviewed
  at a midpoint too (e.g. scene 11 mechanism, scene 19 inheritance). I'll flag at
  AUTHOR step which scenes will be split.
- **Stub-grade scenes (5–8, 11–19)** may need 2 chunks: chunk A = layout + first
  half of GSAP; chunk B = second half + verdict beat. Decided per scene at PROPOSE.

### What I'll do during WALKTHROUGH (my half of the review)

I am NOT skipping QA just because the user is also looking. Per chunk I run:

1. `npx hyperframes snapshot --at <scene_start, scene_mid, scene_end, +any KF beat>`
2. `vision_analyze` each PNG: collisions, cropping, wrong-asset-for-narration,
   text overflow, caption safe-zone breach (anything below y≈880), Studio drag-write
   residue (translate / data-hf-studio-* anywhere it shouldn't be).
3. `bunx hyperframes lint .` — must pass with 0 errors. Existing 2 intentional warnings
   on index.html / captions.html are fine.
4. `grep -rn 'data-hf-studio' compositions/scene-NN-*.html` — must be empty (M12).
5. `python3 tests/audit_drift.py` if captions touched in this chunk — drift ≤100 ms (M13).
6. Quick `ffprobe` on any audio touched this chunk — duration sanity vs scene window.

I post the findings table BEFORE the user opens the browser, so they know what to
look for and what I already caught.

### Audio strategy

- **A0. Voice is already chosen — `bm_george` (Kokoro), default speed.** No spike, no
  comparison, no `--speed` flag. M1.
- **A1.** Render the full narration ONCE with `bm_george` → `assets/narration.fullscale.wav`.
  Whisper word-level transcript → `assets/transcript.json`. Run `tmp/align_caps.py` to
  source-text-override caption text (per LEARNINGS line 30). This is the timing spine
  for all 19 scene chunks.
- **A2.** Defer music + SFX mix until ALL 19 scenes are signed off. Then, in a separate
  chunk reviewed live by user, ducking-compressed mix with hard rules:
  - VO peaks ≥6 dB above music during spoken windows (proven via `silencedetect` + `volumedetect`)
  - SFX events ≤−12 dB relative to VO peak
  - Music cue lifts (4 of them, see RELEASE_NOTE §5) land within ±33 ms of visual KFs

### Phasing of the 19 scenes — proposed order

Walking the script chronologically, but starting with **the 4 scenes that already have preview
fidelity** so we re-validate the workflow on known-good ground before authoring new material:

| Phase | Scene | Status | Approach |
|---|---|---|---|
| **0** | Audio: render master VO with bm_george + caption regen + source-text override | not started | A1 above (no voice choice, M1) |
| **1** | scene-01 cold-open | preview exists (490 lines) | port preview + apply M1–M13 fixes; no new authoring |
| **2** | scene-02 who-was | preview exists (594 lines) | same — port, fix, sign off |
| **3** | scene-03 machine | preview exists (497 lines) | same |
| **4** | scene-04 finding-mckinley | preview exists (594 lines) | same |
| **5** | scene-05 price | generator stub (77 lines) | hand-author from SHOT_BOARDS |
| **6** | scene-06 charlotte | stub | hand-author |
| **7** | scene-07 chokepoint | stub | hand-author (custom map SVG) |
| **8** | scene-08 thesis | stub | hand-author |
| **9** | scene-09 chicago-1888 | half-tuned (181 lines) | finish hand-tune from existing |
| **10** | scene-10 panic | half-tuned (144 lines) | finish hand-tune |
| **11** | scene-11 mechanism | stub | hand-author with snare sync (985/986/987s) |
| **12** | scene-12 front-porch | stub | hand-author with stop-motion counter |
| **13** | scene-13 cross-of-gold | stub | hand-author |
| **14** | scene-14 two-hundred-million | stub | hand-author |
| **15** | scene-15 election-night | stub | hand-author |
| **16** | scene-16 cowboy | stub | hand-author |
| **17** | scene-17 buffalo | stub | hand-author |
| **18** | scene-18 typhoid | stub | hand-author |
| **19** | scene-19 inheritance | stub | hand-author |
| **20** | Audio mix (music + SFX, ducked) | deferred | A2 above |
| **21** | Final assemble + render + spot-frame audit | deferred | only after every phase signed off |

That's 22 sign-off gates total, not one big-bang.

---

## 5. What gets cleaned up before phase 1

The current state is messy. Before authoring scene 1, we should:

1. **Quarantine the generator output** — move `compositions/scene-*-fs.html` (19 files) to
   `compositions/_generated_v1_archive/`. The generator script + SCENES_INDEX.json stays in
   `research/full-scale/` for reference but is no longer wired into `index.html`.
2. **Quarantine the v1 24-min `index.html`** — `cp index.html index.html.v1_fullscale.bak`
   so we can read it for reference but the active `index.html` becomes a fresh 5-min preview-style
   spine that grows scene-by-scene as we sign off phases.
3. **Pin the preview as `preview/index.html`** (already done — `preview/index.html` exists).
4. **Update `PROJECT.md`** to point at this REBUILD.md as the active plan.

---

## 6. Sign-off contract — what "approved" means

Approval happens **live, in the same chat session, after the walkthrough**. For each chunk:

- [ ] User has run `npm run dev` and opened the preview URL in their browser
- [ ] User has scrubbed the chunk's time window
- [ ] I have posted my snapshot+vision findings table BEFORE asking for approval
- [ ] User confirms (✅) or names specific fixes (🔁) or rejects (❌)
- [ ] On ✅: scene committed to git with `feat(scene-NN): <title>`

Anything less = stay in the chunk. No advancing.

---

## 7. What I won't do without your explicit go-ahead

- Run `npm run render` (full MP4 render) at any point before phase 21.
- Touch `american-audacity/video-projects/mark-hanna-e01/` (the abandoned stub).
- Re-trigger the `t_6eab435b` kanban task or add new render tasks before the phasing is done.
- Change the voice or add a `--speed` flag (M1).
- Drop the captions track (M13).
- Author a generator-emitted scene (M7).
- Advance to the next chunk before user has opened the preview and signed off this one.

---

## 8. Next action — kickoff

If you approve the revised plan above, the immediate next step is **Chunk 0 — script v2 +
chunked TTS render** (no preview review needed for audio-only; verification is per-chunk
ffprobe + caption drift audit). Concretely:

```bash
cd ~/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna

# 1. Verify the 5 historical claims (perplexity + web_search) and rewrite scenes 8/17/18
#    only. Save as research/script/FULL_SCRIPT.v2.md. I post the diff for your review.

# 2. Generate voiceover text + manifest from FULL_SCRIPT.v2.md:
bun run scripts/script-to-vo.ts \
  research/script/FULL_SCRIPT.v2.md \
  --out assets/narration/        # writes manifest.json + chunks/*.txt

# 3. TTS each chunk via bm_george at default speed (M1):
bun run scripts/tts-chunks.ts assets/narration/    # 90 s of TTS, ~30 chunks

# 4. Concat per manifest:
bun run scripts/audio-concat.ts assets/narration/  # 3 s, produces narration.fullscale.wav

# 5. Captions (source-text override per LEARNINGS line 30):
bun run scripts/captions-make.ts
bun run scripts/captions-align.ts

# 6. Verify:
bun run scripts/audit-drift.ts                     # caption drift ≤100 ms
ffprobe -v error -show_entries format=duration -of default=nw=1 \
  assets/narration/narration.fullscale.wav
```

I'll run those, post duration + drift numbers + a per-chunk listing, and only after you ✅
those numbers do I move to **Chunk 1 — scene-01 cold-open** (port from preview, then you
fire up `bun run dev` and we walk through together).

Side note on tooling: scripts in step 2/3/5/6 don't all exist yet — I'll write them as
TypeScript+bun (per memory rule: bun first, python only for ML/whisper-ecosystem where
there's no bun-native option). The whisper alignment in step 5 is the one place python may
still appear, since whisperx/faster-whisper don't have bun-native ports. I'll surface that
explicitly when I get there.

Say "go" and I start Chunk 0 with the script verification + scene 8/17/18 rewrite.
