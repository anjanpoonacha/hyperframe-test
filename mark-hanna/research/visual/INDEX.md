# Visual design package — `t_df363173`

Three deliverables for the full-scale hyperframe video (24-min, 19 scenes, 1,440 s).
Sibling `t_e781bf96` (assembly) reads these to start producing frames without
re-asking design questions.

## Files

- **`STYLE_GUIDE.md`** — Visual language. Palette tokens (DESIGN.md-locked), typography
  stack with scene-scale sizes, six-gesture hyperframe transition vocabulary, character
  treatments for all 12 named figures, three recurring environment motifs (newspaper
  plate / ledger / map), motion character + forbidden eases, caption strategy (no
  separate track — hero text IS the caption, per `mark-hanna-shorts/LEARNINGS.md` v5),
  asset procurement targets with typographic fallbacks, production constraints tied
  to LEARNINGS line numbers.
- **`SHOT_BOARDS.md`** — Per-scene shot board for all 19 script scenes plus the end
  card. Each scene gives composition file, layer order with z-index intent,
  scene-relative-second keyframes (KFs explicit so animator implements directly as
  `tl.to(...)` GSAP positions), the hyperframe gesture in use, hero text plates with
  size+color+hold time, asset list, engagement role.
- **`ENGAGEMENT_MAP.md`** — Audit table mapping the script's 31 engagement beats to
  the visual delivery moment that reinforces them. Coverage check for the 7
  retention dip windows + 3 number-theatre payoffs + 3 emotional anchors + climax +
  close. Gesture-frequency distribution (over-use risk audit). Music lift sync
  points (4 moments where audio and video must conform to the same frame). Silence
  beat visual contract (5 moments). QA audit list for assembly sign-off (6 items).

## Key constraints lifted directly to the assembly worker

- 16:9 1920×1080 base composition; per-scene `compositions/scene-NN-<slug>.html` files
  with hardcoded GSAP positions, scene-relative seconds (NEVER narration-phoneme-
  aligned — per `mark-hanna/LEARNINGS.md` line 13).
- Caption strategy: NO separate captions track. Do not regenerate one. Hero text on
  screen IS the caption (per `mark-hanna-shorts/LEARNINGS.md` v5).
- 13 images on disk, 7 to procure (4 core + 3 optional with designed typographic
  fallbacks). Procurement order and source list in STYLE_GUIDE §11.
- 6-gesture vocabulary (push-in, pull-out, hard cut + name plate, count-up, ledger
  plate, held silence) — single canonical mechanism reveal at SCENE 11 must NOT be
  reused.
- Music lifts (+3 dB) at 2:30 / 16:00 / 20:15 / 23:30 must land on the visual KF
  freeze, not 0.5 s off. Sync order: render narration → place music + mark lifts →
  tune visual GSAP to the lifts.
- Verdict line bottom-anchor 200 px from bottom (no captions track means the y≈880
  collision constraint from LEARNINGS line 24 is dead, but the anchor stays there
  to give the verdict typographic weight).
