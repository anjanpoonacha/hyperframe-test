# Mark Hanna — Project Rules

> The agent's contract for this project. Numbered, declarative, terse.
> If you violate one of these, the user will catch it and we lose trust.
> Long-form historical lessons live in `LEARNINGS.archive.md`.

## V — Voice (bm_george Kokoro, default speed)

- V1 Spell every year out: `eighteen ninety-six`, never `1896`.
- V2 No commas after a single-word opener: `Banks paid` not `Banks, paid`.
- V3 Replace staccato lists with connectors: `Coal and iron` not `Coal, iron`.
- V4 No initials with periods: `JP Morgan` not `J.P. Morgan`, `M A Hanna` not `M.A. Hanna`.
- V5 Voice is locked. No `--speed` flag, no voice swap mid-rebuild.
- V6 Long-form: split narration per scene (re-render = 1-2 min, not 10-15).
- V7 Punctuation does NOT control pacing. Pacing comes from manifest silences.

## S — Screen typography (the dual-channel rule)

- S1 Voice spells, screen uses numerals: `1896`, `59`, `$3,500,000`.
- S2 Audit before sign-off: grep for `Eighteen|Nineteen|Twenty|...|hundred|thousand|million` in composition HTML.
- S3 Names per source: `Hanna` not `Hannah`, `Alonzo` not `Alonso`. Whisper transcribes wrong; trust source.

## C — Captions are inviolable

- C1 Caption strip lives at y=950–1050. Nothing else may live there.
- C2 No visual element may cross y=880 at any point during any tween.
- C3 Full-bleed images use `height: 880px`. Never `height: 100%`.
- C4 Any time `narration.wav` changes, run `python3 scripts/make-captions.py`.
- C5 Verify caption sync three ways: regenerator drift, audit_drift.py, live snapshot. Don't trust the first alone.
- C6 Caption strip already has text-shadow + box-shadow halo. That's a safety net, not a license to cross C2.

## P — Phases never co-exist

- P1 Predecessor element fully exits (opacity 0 + visibility hidden) BEFORE successor lands.
- P2 Cross-fade is not a substitute. A 0.6s cross-fade has both at >50% opacity for ~0.3s — that frame is a bug.
- P3 Anchor successor reveal to the audio word that names it.
- P4 Pattern:
  ```js
  tl.to("#prev", { opacity: 0, duration: 0.7 }, exitStart);
  tl.set("#prev", { visibility: "hidden" }, exitStart + 0.9);
  tl.fromTo("#next", {...}, {...}, exitStart + 1.0);
  ```

## T — Centering: GSAP owns the transform (the M9 rule)

- T1 No CSS `transform: translateX(-50%)` on any element that will be `scale`-tweened.
- T2 Centering goes inside the GSAP tween: `xPercent: -50` in BOTH the from-state and to-state.
- T3 Subsequent tweens on the same element (ken-burns, exits) must also include `xPercent: -50`.
- T4 Corner-pop between adjacent frames = T1–T3 violated.

## H — Color hierarchy (4 locked roles)

| Role | Color | Used for |
|---|---|---|
| Identity | Cream `#E8DEC8` | Names, body text, primary captions |
| Atmosphere | Champagne `#D4B679` | Connector text, italic asides, date anchors |
| Structure | Orange `#C87533` | Borders, eyebrow stamps, accent emphasis |
| Climax | Blood red `#C03A2C` | Punch slams only |

- H1 Each text element picks ONE role. Two elements sharing a role = one is wrong.
- H2 WCAG-passing contrast (4.5:1) is necessary, not sufficient. Same color family = flat hierarchy.
- H3 When iterating on a color, log every version tried in a CSS comment.

## L — Layout: space distribution

- L1 No empty band >200px above first element, below last (excl. caption strip), or beside hero.
- L2 Hero element occupies 40–65% of canvas height.
- L3 Top margin to first element ≤ 150px (unless airy is intentional and defended).
- L4 All elements fully inside 1920×1080 at hold AND during every tween.
- L5 Ken-burns peak scale stays inside canvas. Cap source dims, don't allow overflow.

## A — Audio pipeline

- A1 Splices accumulate stutter. After 4+ splices on the same base, full re-render is cleaner.
- A2 Audio change = caption regen. Period.
- A3 Verify VO collisions against the actual master wav (`silencedetect`), NOT the preview transcript.
- A4 Renders predate fixes unless re-rendered. Don't visually verify against an old MP4.

## R — Runtime contract (CHANNEL.md §3)

- R1 Before any TTS pass, run `script-to-vo.ts --dry-run` and count words in extracted scene .txt only.
- R2 Channel target: 30–40 min. Sweet spot 35 min ≈ 5,500–5,800 spoken words at 172 wpm.
- R3 If gap > 20%, expand the script first. Do NOT render to find out.

## G — Sign-off discipline

- G1 Never `git commit` until the user types approval ("approved", "go", "ship it", "commit it").
- G2 Lint clean + vision clean is necessary, not sufficient. The user's eye is final.
- G3 If commit happened ahead of approval: acknowledge the rule break, offer `git reset --soft HEAD~1`, wait for the user's call.
- G4 When user reports a fault on a beat the agent declared clean, the failure is in the QA. Patch this file or `hyperframes-frame-qa` skill to encode the missed check.

---

## Process loop (per scene)

1. Load `hyperframes-frame-qa` skill.
2. Author the scene HTML against V/S/C/P/T/H/L rules.
3. `npx hyperframes lint && npx hyperframes inspect` — must be 0 errors.
4. `npx hyperframes snapshot . --at <every phase boundary + every audio anchor>`.
5. Vision Verifier pass on the snapshots.
6. Vision Challenger pass — push back on every "pass", especially T (centered), H (contrast), P (phase).
7. Post findings table to user. STOP.
8. User says "approved" / "fix N" / "redo".
9. Only on explicit approval: `git commit`.

## When a new mistake class appears

1. Identify it precisely (not "captions broken" — `image height:100% bled to y=1080 behind caption strip`).
2. Add a numbered sub-rule under the matching letter section above.
3. Don't create new top-level letter categories without explicit user confirmation.
4. Long-form historical context goes in `LEARNINGS.archive.md`, not here.

---

See `LEARNINGS.archive.md` for the full historical record (TTS quirks, splice case studies, scene-4/9/10 hand-tune notes, SFX layer, runtime audit narrative).
