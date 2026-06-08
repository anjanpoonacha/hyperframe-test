# THE LEDGER — Visual Style Guide

Companion to `research/script/FULL_SCRIPT.md` (24-min long-form). All tokens here are
*production-binding* — animators on the assembly task (`t_e781bf96`) implement against
this document without re-asking design questions. Anything not specified here defers to
`mark-hanna/DESIGN.md` (the project DESIGN spec) and `mark-hanna/LEARNINGS.md`
(production quirks).

---

## 1. Mood and reference

Gilded-Age investigative documentary. Newsprint meets political thriller. The visuals
*indict*; they do not entertain. Reference triangulation:

- HBO documentary cold opens (Sumner / Gibney pacing) — long held shots, restrained
  motion, typography that arrives like evidence.
- New York Review of Books page geometry — left-aligned headlines, ragged-right body,
  hanging numerals.
- Old US Treasury Department typesetting — engraved serifs, period ornament, no neon.

What this is NOT: explainer-video kinetic typography, Vox-style data-pop, History
Channel sepia-and-zoom B-roll. The 5-minute preview already proved the tone — extend it,
do not modernise it.

---

## 2. Palette (locked tokens)

From `DESIGN.md` (do not introduce new colors):

| Token              | Hex       | Role                                                         |
|--------------------|-----------|--------------------------------------------------------------|
| Ink Black          | `#0E0B08` | Primary background; deep base plate                          |
| Newsprint Cream    | `#E8DEC8` | Body text on dark; archival paper plates                     |
| Hanna Amber        | `#C87533` | Money, the dollar-sign motif, accents, hairline borders      |
| Blood Oxide        | `#C03A2C` | Indictments, deaths, "20×", count-down stamps                |
| Patina Green       | `#2F4A3A` | Rare second accent — old money, copper oxide (use ≤2 scenes) |
| Faded Bone         | `#9A8E76` | Captions, attributions, dates, secondary metadata            |

Rules:
- **Backgrounds** are Ink Black or a textured Newsprint Cream plate. No gradients with
  more than two stops; no animated background hue shifts.
- **Money** (every dollar amount, every donor line, every "raised / spent / mailed"
  label) is Hanna Amber.
- **Death / collapse / negative-record beats** (the bullet, McKinley's "I am a beggar",
  "20×", "the candidate was now a debt", "the ledger won") are Blood Oxide.
- **Attributions, dates, source citations, scene chapter numbers** are Faded Bone.
- **Patina Green** appears only at:
  - SCENE 7 (`THE CHOKEPOINT`) — the Lake Erie ore-boat line on the chokepoint map.
  - SCENE 19 (`THE INHERITANCE`) — the connector lines back to the 1896 row.
  Used as memory color for "the underlying machine survives".
- **No bright saturated tertiaries.** No cyan, no magenta, no neon green. If you reach
  for a fifth color, instead lower or raise opacity on Hanna Amber / Newsprint Cream.

---

## 3. Typography (locked stack)

From DESIGN.md, with scene-scale decisions added:

| Family                     | Use                                         | Sizes                                 |
|----------------------------|---------------------------------------------|---------------------------------------|
| Playfair Display 700/900   | Display / headlines / indictment numbers    | 84–184 px hero · 56–84 px section     |
| Source Serif 4 400/600     | Quotes / longer narration text / pull-quote | 36–72 px emphasis · 28–32 px body     |
| IBM Plex Mono 500          | Numbers, dates, vote totals, attributions   | 18–32 px metadata · 56–84 px ledger   |

Roman number rules (every scene):
- `font-variant-numeric: tabular-nums` ALWAYS on dollar amounts, ballot tallies,
  electoral counts, mail counts, dates.
- Hero numbers (`$3,500,000`, `200,000,000`, `271`) are Playfair 900 in Newsprint Cream
  or Hanna Amber. The donor-list math is IBM Plex Mono.
- **Spell-out years on screen when they're prosody-critical** (matches script's spelled
  narration): the cold open's `1 8 9 6` letter-spaced 0.5em is correct because the eye
  reads the year as a unit, not as a sum. For ledger lines and timestamps inside body
  copy, plain `1896` is fine.

Letter-spacing on display text starts at `0.05em` and tightens to `-0.02em` on entry
(per DESIGN.md motion notes). No reverse — text never *loosens* on entry.

Asymmetry rule: do not center every plate. Left-align headlines on columns 1–8; let
numbers and metadata hang in columns 10–12. Centered text is reserved for the *single
moment* of resolution per scene (the verdict line, the hero number landing).

---

## 4. The 5-minute reference — visual rules learned

The preview at `mark-hanna/index.html` (scenes 1–4, 53.5/67/54/65 s) is the proven
vocabulary for this project. Do not reinvent it; *extend* it. Concrete carry-overs:

### 4.1 Compositional grammar

- **Chapter card.** Every scene opens with a Faded Bone Roman numeral chapter mark
  (`I`, `II`, `III`, …) plus a one-line chapter title in Source Serif 4 italic. Hold
  1.0–1.5 s before the scene proper begins. (Already used in scenes 2/3/4 of the
  preview as `s2-chapter`, `s3-chapter`, `s4-chapter`.)
- **Year strap.** Where a scene is anchored to a year, that year appears at top-left
  in IBM Plex Mono 32 px Faded Bone, prefixed `YEAR ` and letter-spaced 0.3em. Persist
  for the whole scene (anchored, never animated).
- **Newsprint header strip.** 22 px IBM Plex Mono Faded Bone uppercase strap with a
  Hanna Amber 1px hairline above and below — used for context (location, time period,
  source publication). Lives at top-margin (`top: 92px`) as in the cold open.
- **Hero number plate.** Centered, single number, Playfair 900, Hanna Amber or
  Newsprint Cream, with Faded Bone label above and Source Serif italic sub below.
  Always inside a faint cream-on-black panel (`rgba(232,222,200,0.02)` background, top
  border 2px Hanna Amber, bottom border 1px Faded Bone) — that panel IS the brand.
- **Dichotomy split.** Left/right grid with a Blood Oxide italic `vs.` glyph between.
  Used for Bryan ↔ Hanna in the cold open; reused at the Cross-of-Gold pivot
  (Scene 13) and the Roosevelt warning (Scene 16).
- **Ledger panel.** Black plate with IBM Plex Mono cream lines writing themselves in,
  one per line, `expo.out`, then the total stamping in Blood Oxide. Reused exactly as
  the cold open's number scoreboard but as a vertical balance sheet (Scene 11).
- **Verdict line.** A single closing line per scene, anchored 200 px from the bottom
  in Playfair 900 Hanna Amber or Blood Oxide, all caps. The phrase that the scene was
  built to deliver. No motion under it.

### 4.2 What worked — keep doing

- **Vignette + grain + sepia LUT** on every archival image: `filter: sepia(0.25)
  contrast(1.05) brightness(0.92) saturate(0.85)`. This is the period filter; *every*
  photo passes through it. No uncolor-graded JPEGs land on screen.
- **Hairline 1px Hanna Amber border on photographs.** Box-shadow `0 30px 80px
  rgba(0,0,0,0.65)` to anchor the image as an object on the cream-on-black plate.
- **Caption safe-zone is dead.** The 5-min preview removed the captions track in v5
  (per `mark-hanna-shorts/LEARNINGS.md`). For long-form, hero text on screen IS the
  caption — see §10.
- **Static for emotional anchors.** The held-image rule from DESIGN.md is real and
  measured: the loyalty refusal beat in scene-04 of the preview held a single portrait
  for 2.5 s with no motion and the audience's retention curve was *flatter*, not
  steeper, through it. Keep doing this for the three emotional anchors (Charlotte,
  the loyalty refusal, the bullet).

### 4.3 What hurt — do not repeat

- **Captions duplicating hero text.** Banned. No `compositions/captions.html`
  equivalent for the long form. (See §10.)
- **Sub-second text appearances.** Every text element must occupy the screen for
  ≥ 1.0 s; ideally ≥ 1.5 s for hero typography. The shorts-video audit at
  `mark-hanna-shorts/` found 12 sub-1.0s timing violations; the long form must clear
  this on review.
- **Bottom-of-frame element collisions.** Anchor scene-bottom UI no lower than y≈880.
  At 16:9 1920×1080, that means anything below row 880 risks a multi-line title
  collision; the verdict-line lift trick from `mark-hanna/LEARNINGS.md` line 24 is the
  standard fix.
- **Bouncy / elastic eases.** Banned. `power3.out` for entrances, `power2.in` for
  exits, `expo.out` for indictment numbers. No `back.out`, no `elastic`, no
  `bounce.out` anywhere.

---

## 5. Hyperframe transition vocabulary

The library here is small and re-used heavily — the document's *visual rhyme* depends
on the same gesture meaning the same thing every time it appears. Six gestures total:

### 5.1 Push-in (Ken Burns accusatory)

8–15 second slow drift on an archival image, scale change 3–6%, direction *toward* the
subject. Means: "look at this person; we are about to indict them." Used at:
- SCENE 1 (cold open on the dollar-suit cartoon)
- SCENE 8 (held portrait of Hanna while the thesis lands)
- SCENE 17 (newspaper-front of the assassination)

### 5.2 Pull-out (Ken Burns context)

8–15 s slow drift, 3–6% scale change, direction *away* from the subject. Means: "this
is the world the subject lives inside; widen your frame." Used at:
- SCENE 7 (the Cleveland chokepoint map widens to show Lake Erie + Pittsburgh)
- SCENE 9 (the convention floor pulls back to reveal the vote-tally crawl)
- SCENE 19 (the 1896 row pulls out to reveal 1900, 1928, 1972, 2008, 2024)

### 5.3 Hard cut to black + name plate

Scene transitions through 0.5–0.8 s of Ink Black, then a single typographic plate
(name, year, or quote) in Newsprint Cream. Means: "the previous beat is over; the
next thing is a *fact*." Used between every scene and most beat changes inside scenes.
The cold-open's reveal of `MARK HANNA` is the canonical example.

### 5.4 Number theatre count-up

A counter element runs from 0 to the target number across 0.8–1.2 s with `expo.out`,
tabular-nums monospace tracking, accompanied by a single rising horizontal Hanna Amber
hairline that lands exactly at the moment the counter freezes. Means: "the number is
the indictment; absorb its scale." Used at the 3 number-theatre payoffs (2:30, 19:30,
plus the 200,000,000 mail-counter at 19:30).

### 5.5 Ledger plate write-in

A blank Newsprint Cream plate fills the screen. IBM Plex Mono lines write themselves
in one at a time, top-to-bottom, with a 0.4-second `power2.out` per line. The total
underline draws across left-to-right at the bottom (1.2 s `expo.out`); the total value
stamps in Blood Oxide. Means: "this is the math; nothing is hidden." Used once: the
mechanism reveal at SCENE 11. (Re-using this gesture elsewhere weakens it.)

### 5.6 Held silence on a typography plate

Black plate, single italicised quote in Source Serif 4 84 px, no motion, no music
swell, held 1.5–2.5 s. Means: "the words alone carry the beat — let them." Used at:
- SCENE 13 (`Cross of Gold` quote held 1.5 s before Bryan's portrait arrives)
- SCENE 16 (`Don't any of you realize there's only one life…` held 2.5 s)
- SCENE 17 (`BUFFALO. SEPTEMBER 6, 1901.` held 1.5 s before the news front)

### 5.7 (Forbidden gestures)

For clarity — these are NOT in the vocabulary:
- Whip-pans, glitch transitions, RGB-split effects.
- Letterbox-bar reveals, faux-film-strip framing.
- 3D parallax / perspective tilt on archival photos.
- Any motion involving the page itself rotating, scaling above 110%, or skewing.

---

## 6. Character visual designs

The 12 characters from the script's §2 are all rendered through the period filter +
typography treatment. No actor-replacements, no AI-generated portraits.

| # | Character        | On-disk asset                          | Treatment                                                                                          |
|---|------------------|----------------------------------------|----------------------------------------------------------------------------------------------------|
| 1 | Mark Hanna       | `hanna-portrait.jpg`, `hanna-1877.png`, `hanna-young.jpg` | Sepia LUT; tight crop on eyes for thesis beats; full-frame for the cold open |
| 2 | William McKinley | `mckinley-1896.jpg`                    | Sepia LUT; paired with Faded Bone role-tag *"Congressman, 17th District, Ohio. 45 years old."*     |
| 3 | William J. Bryan | TO PROCURE — see §11                   | Tight portrait for the speech beat; held in dichotomy frame opposite Hanna                         |
| 4 | John D. Rockefeller | `rockefeller.jpg`                   | Half-frame paired with `hanna-young.jpg` at hairline-Amber 1px border between                      |
| 5 | Daniel Rhodes    | `rhodes-daniel.jpg`                    | Sepia LUT; passes once at scene 7 transition; not re-used                                          |
| 6 | Charlotte Hanna  | TO PROCURE — see §11                   | Single held image (8 s no motion); typographic fallback if procurement fails — see SHOT_BOARDS §6  |
| 7 | John Sherman     | NOT ON DISK — fallback typographic     | Vote-tally crawl carries the beat; no portrait needed unless procurement is cheap                  |
| 8 | Theodore Roosevelt | TO PROCURE — see §11                 | Off-camera until Scene 16's pull-quote; no portrait in cold open or thesis                         |
| 9 | Ida McKinley     | TO PROCURE — see §11                   | Typographic plate fallback for the Panic beat; portrait only if procured                           |
| 10| Garret Hobart    | NOT ON DISK — typographic only         | One line in the timeline strip at Scene 16; never a portrait                                       |
| 11| Leon Czolgosz    | NEVER A PORTRAIT                       | Name appears once in Faded Bone 32 px for 1.0 s; that is all                                       |
| 12| The American Voter (collective) | counter elements only         | The half-million count-up at Scene 12; the 13.9 million ballot tally at Scene 15                   |

Treatment rule: a character's *visual weight* tracks their structural function. Hanna,
McKinley, and Bryan get held portraits; supporting characters get half-frames or
typographic plates; the cameos get one line and no portrait at all (Czolgosz
deliberately under-rendered — the script's choice not to humanize the assassin
matters).

---

## 7. Environment motifs

Three recurring environment motifs carry the document; nothing else is a "place".

### 7.1 The newspaper plate

A textured Newsprint Cream rectangle, 1px Hanna Amber hairline border, columns of
period-style typesetting. Used for:
- The cold open Hearst-paper context strap (Scene 1)
- The 1896 newspaper page (Scene 2 — `newspaper-eveningstar-1896-01-11.jpg` rendered as
  the plate)
- The Panic headline (Scene 10 — `M'KINLEY FACING FINANCIAL RUIN`)
- The Bryan speech reception headlines (Scene 13)
- The assassination front page (Scene 17)
- The obituary plate (Scene 18 — `M. A. HANNA DEAD`, two-column period typesetting)

The plate is the *primary* environment of the documentary; we're inside the press as
much as we are inside the events.

### 7.2 The ledger / balance sheet

Cream plate, IBM Plex Mono lines, hairline rules, totals stamped in Blood Oxide. Used
for:
- The scoreboard in the cold open (Scene 1)
- The donor list at Scene 2 (Standard Oil / JP Morgan)
- The full mechanism reveal at Scene 11
- The escalating-spend timeline at Scene 19 (1896 → 2024 dollar figures)

The ledger is the *system* the documentary is about; every time the audience sees one,
they're seeing the thing Hanna invented at work.

### 7.3 The map

A motion-graphic line drawing, no satellite imagery, no modern cartography. Drawn in
Newsprint Cream with Patina Green for the ore-boat / rail trace and Hanna Amber for the
chokepoint node. Used twice only:
- Scene 7 — Lake Erie at top, Pittsburgh mills at bottom, Cleveland node pulsing in
  Hanna Amber.
- Scene 14 — Bryan's 18,000-mile rail tour traced across the continental US.

The map is the *geography* the system operates inside; using it more than twice
dilutes the gesture.

---

## 8. Composition grid

12 columns on 1920×1080. Outer margin 96 px. Gutter 32 px. Standard regions:

```
   ┌── 96 ───┬──────────────────────────────────────────────┬── 96 ──┐
   │         │  HEADLINE (cols 1–8)         METADATA (10–12)│        │
   │         │                                              │        │
   │         │  HERO TYPOGRAPHY (full-bleed cols 1–12)      │        │
   │         │                                              │        │
   │         │  PHOTOGRAPHIC PLATE (cols 2–11, 8-col block) │        │
   │         │                                              │        │
   │         │  CAPTION HANG (col 12, ragged-right)         │        │
   └─────────┴──────────────────────────────────────────────┴────────┘
```

Verdict line lives bottom-anchored at 200 px from bottom (NOT at 880 — the captions-
collision constraint from `LEARNINGS.md` line 24 is dead because long-form has no
captions track). All other "bottom-line" UI uses the 200 px anchor.

---

## 9. Motion character

Speeds and eases (from DESIGN.md, with scene-scale decisions):

| Element                         | Duration  | Ease            | Notes                                              |
|---------------------------------|-----------|-----------------|----------------------------------------------------|
| Big-number count-up             | 0.8–1.2 s | `expo.out`      | tabular-nums; horizontal hairline lands at freeze  |
| Headline fade-and-rise          | 0.6–0.8 s | `power3.out`    | letter-spacing tightens 0.05em → −0.02em           |
| Section/scene exit              | 0.5–0.8 s | `power2.in`     | always to Ink Black, never to a photo              |
| Ledger line write-in            | 0.4 s/line | `power2.out`   | stagger 0.4 s; total stamps with `expo.out`        |
| Ken Burns drift                 | 8–15 s    | linear          | scale 1.00 → 1.03 (push) or 1.06 → 1.00 (pull)     |
| Photograph entry                | 0.6 s     | `power3.out`    | scale 1.02 → 1.00, opacity 0 → 1                   |
| Quote held silence              | 1.5–2.5 s | (no motion)     | absolute stillness; vignette and grain only        |

No motion exceeds 1.2 s for an entrance or 0.8 s for an exit; nothing eases longer
than 1.5 s except Ken Burns and held silences. Music does the long-tail emotional
work; visuals are decisive.

---

## 10. Caption strategy (locked)

**No separate captions track.** The hero text on screen IS the caption.

Rationale (from `mark-hanna-shorts/LEARNINGS.md` v5):
> The captions track was a verbatim semantic duplicate of beat-body hero text rendering
> at the same instant — that is the entire bug, not a tuning parameter.

Implementation rule for each scene:
- Every key spoken phrase (the ones that earn a hero-text plate) appears on screen at
  the same moment it is spoken, in Playfair Display or Source Serif at hero scale
  (≥ 56 px), and stays on screen for ≥ 1.0 s after the spoken phrase ends.
- Phrases that do NOT earn a hero plate (linking sentences, transitional clauses) get
  no on-screen text. The narrator's voice carries them.
- **Do not** add a `compositions/captions.html` file or any cue-driven text track.
  The shorts project's drift-free regenerator (`tests/audit_drift.py`) is irrelevant
  here because there is no separate cue layer to align.

---

## 11. Asset procurement targets (animator delegates)

These are pre-1929, US-public-domain images the script names but that aren't yet on
disk. The assembly worker (`t_e781bf96`) is responsible for procuring or commissioning
typographic fallbacks where listed:

| Target                                                  | Source likely                                         | Fallback if procurement fails                  |
|---------------------------------------------------------|-------------------------------------------------------|------------------------------------------------|
| Charlotte Augusta Rhodes Hanna portrait                 | Western Reserve Historical Society (Cleveland)        | Typography plate, see SHOT_BOARDS §6            |
| Ida Saxton McKinley portrait                            | Library of Congress Prints & Photographs Division    | Typography plate with the role-tag, see §10    |
| McKinley front-porch crowd photograph (Canton 1896)     | Stark County Library / LOC                            | Stop-motion stamping of `+12,400 → +501,200` only |
| McKinley-Roosevelt 1900 inauguration                    | LOC Brady-Handy collection                            | Typographic plate of timeline strip             |
| William Jennings Bryan portrait c. 1896                 | LOC; Bain News Service                                | Held black plate with the Cross-of-Gold quote   |
| Pan-American Exposition Temple of Music exterior        | Pan-American Expo official photographs (LOC)          | Newspaper-front composite alone                |
| Hanna funeral procession                                | Cleveland Plain Dealer archive / WRHS                 | Two-column period obituary type alone           |

Procurement order (cheapest first): LOC P&P → WRHS → Cleveland Public Library digital
collections. All targets are pre-1929 and public-domain in the US; no licensing path
needed.

---

## 12. Known production constraints (binding)

From `mark-hanna/LEARNINGS.md` and the parent task handoffs — these constrain visual
choices:

- **No motion below y≈880 unless captions are confirmed absent** (they are absent for
  long-form, but verify on assembly). Verdict-line bottom-anchor at 200 px is the
  default.
- **Photographs must pass through the period LUT** (sepia 0.25 / contrast 1.05 /
  brightness 0.92 / saturation 0.85). No raw archival JPEG goes on screen.
- **Per-scene narration files**: each scene gets its own composition file
  (`compositions/scene-N-<slug>.html`) and its own narration WAV. Visual timing inside
  a composition is hardcoded GSAP positions; if voice timing shifts, the composition's
  `tl.to(...)` positions get warped per `LEARNINGS.md` line 13. Visuals must NOT
  depend on narration phoneme alignment — only on scene-relative seconds.
- **`hyperframes validate`** false-flags `?v=2` cache busters as 404 (LEARNINGS line
  14). Pre-existing; ignore the warnings, do not strip the cache busters.
- **Long-form is untested for caption regenerator**, but we do not use the regenerator
  (no captions track). LEARNINGS line 23 is moot here.
- **Splice budget ≤ 2 fixes per minute** of finished render (LEARNINGS line 29). If
  visual timing pushes a re-warp, prefer a full per-scene re-render to stacking
  splices.

---

## 13. Acceptance check

A reviewer reading this document can answer:

- **Palette and typography?** §2 + §3.
- **What carried over from the 5-min preview?** §4.
- **What hyperframe gestures exist and where do they go?** §5 lists six gestures with
  scene mappings.
- **How is each character shown?** §6 maps all 12 to assets and treatments.
- **What environments recur?** §7 lists three motifs (newspaper plate, ledger, map).
- **What's the page geometry?** §8 with the verdict-line anchor rule.
- **Motion speeds and forbidden eases?** §9.
- **Captions?** §10 (no captions track; hero text IS the caption).
- **What's missing on disk?** §11 with procurement targets and fallbacks.
- **Production gotchas?** §12 with explicit ties to LEARNINGS line numbers.

Per-scene shot boards live in `SHOT_BOARDS.md`; the engagement-beat ↔ visual mapping
lives in `ENGAGEMENT_MAP.md`.
