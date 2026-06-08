# THE LEDGER — Per-Scene Shot Boards

Companion to `STYLE_GUIDE.md` and `research/script/FULL_SCRIPT.md`. One section per
script scene (19 total). Each section gives:

- Beat clock (start–end, duration)
- Frame-by-frame keyframes with second-resolution timing
- Camera move (Ken Burns push / pull / static / cut)
- Hyperframe gesture (one of the six from STYLE_GUIDE §5)
- Layer order (z-index intent: BG → photo → typography → verdict)
- Hero text plates (the on-screen "captions") with size and color
- Asset list for the scene
- Engagement role (which dip / payoff / anchor it serves; cross-reference
  `ENGAGEMENT_MAP.md`)

Composition framework: 16:9 1920×1080. Each scene is its own
`compositions/scene-NN-<slug>.html` with hardcoded GSAP positions referenced from
`index.html` via `data-start` / `data-duration` (matching how the 5-min preview's
scenes 1–4 are structured). The visual timing inside a composition is *scene-relative
seconds* — never narration-phoneme-aligned (per LEARNINGS line 13).

> **Notation.** `KF @t.tt` = keyframe at scene-relative t.tt seconds (NOT absolute
> document time). All durations are in seconds.

---

## SCENE 1 — 0:00–0:45 (45 s) — THE CARTOON

*Composition file:* `compositions/scene-01-cartoon.html`
*Engagement role:* sensory hook + name-drop reinforcement at the 0:45 dip.

**Layers (z-index low → high):**
1. Ink Black BG (#0E0B08), film-grain layer at 8% opacity.
2. Cartoon image: `cartoon-dollar-mark-hanna.jpg` (Davenport).
3. Spotlight glow (radial Hanna Amber 18%, ellipse 600×500 px).
4. Newsprint header strap (top, 22 px IBM Plex Mono Faded Bone).
5. Hanna name plate (Playfair 184 px, MARK in cream, HANNA in Hanna Amber).

**Keyframes:**
- KF @0.00  — black plate; 4 s of silence (per script).
- KF @0.50  — newsprint strap fades in (`power3.out`, 0.6 s): "A CAMPAIGN
  MANAGER · CLEVELAND, OHIO · EIGHTEEN NINETY-SIX".
- KF @4.00  — cartoon enters from screen-down with `power3.out` (0.8 s),
  scale 1.02 → 1.00, opacity 0 → 1; spotlight glow ramps in 0 → 0.6.
- KF @4.50  — Ken Burns *push-in* begins, scale 1.00 → 1.04 over 24 s linear.
  Narration begins: "The cartoon ran in every Hearst paper in America."
- KF @18.00 — cross-fade to `cartoon-shylock-hanna.jpg` (1.5 s); push-in continues
  on the new image at 1.00 → 1.03.
- KF @28.00 — cross-fade to `cartoon-boss-of-bosses.jpg` (1.5 s).
- KF @38.00 — hard cut to Ink Black for 0.6 s (silence: BEAT 0.6 s).
- KF @38.60 — `hanna-portrait.jpg` enters at 30% screen height upper, fades in
  (0.6 s power3.out), held; vignette tightens (filter sepia 0.25 → 0.30 over 4 s).
- KF @39.20 — `MARK` plate enters from y+40 with letter-spacing 0.05 → −0.02 em
  over 0.7 s; `HANNA` follows at +0.4 s offset, identical motion.
- KF @42.00 — year strap `1 8 9 6` (32 px IBM Plex Mono Hanna Amber, letter-spacing
  0.5em) fades in below the name (0.6 s).
- KF @44.00 — held still (1.0 s).
- KF @45.00 — scene exits to Ink Black (`power2.in`, 0.5 s; carries 0.5 s into
  Scene 2's `data-start` for the cross-fade overlap).

**Hyperframe gesture:** *push-in* (5.1) chained across three Davenport cartoons,
landing in *hard cut to black + name plate* (5.3).

**Hero text plates:**
- Newsprint strap (Faded Bone, 22 px) — full duration after KF 0.50.
- `MARK HANNA` (Playfair 184 px, cream + amber) — held 6.4 s (KF 38.60 → 45.00).
- `1 8 9 6` (IBM Plex Mono 32 px Hanna Amber) — held 3.0 s.

**Assets:** `cartoon-dollar-mark-hanna.jpg`, `cartoon-shylock-hanna.jpg`,
`cartoon-boss-of-bosses.jpg`, `hanna-portrait.jpg`. All on disk.

---

## SCENE 2 — 0:45–3:30 (2:45) — THE LEDGER

*Composition file:* `compositions/scene-02-ledger.html`
*Engagement role:* Number-theatre payoff #1 at 2:30 ($3,500,000 + 20×).

**Layers:**
1. Ink Black BG + grain.
2. Newspaper plate: `newspaper-eveningstar-1896-01-11.jpg` rendered as the cream
   plate background for 0:00–0:35.
3. Year glyph `1896` (Playfair 280 px Blood Oxide).
4. Hero `$3,500,000` (Playfair 184 px Hanna Amber, count-up).
5. Donor list block (IBM Plex Mono ledger).
6. `20×` Blood Oxide stamp.
7. Verdict line `Hanna had a ledger.` (Playfair 96 px Hanna Amber).
8. Transition cue: `To understand how — we go back fifty-nine years.`

**Keyframes:**
- KF @0.00  — newspaper plate slides in from top with `power3.out` 0.8 s.
- KF @0.50  — Ken Burns *pull-out* on the newspaper (scale 1.06 → 1.00 over 12 s).
- KF @12.00 — hard cut Ink Black 0.4 s; year `1896` enters Blood Oxide 280 px,
  letter-spacing 0.05 → −0.02 em (0.7 s power3.out); held 1.2 s.
- KF @14.50 — year exits up (`power2.in` 0.5 s); count-up plate composes in.
- KF @15.50 — `$3,500,000` count-up runs 0 → 3,500,000 over 1.0 s `expo.out`,
  Hanna Amber, with horizontal hairline rule sliding in across cols 4–9 to
  underscore the freeze; held 2.0 s. Faded Bone label above: `RAISED · 1896`.
- KF @18.50 — `20 ×` Blood Oxide stamp lands with brief 1.05 → 1.00 scale snap
  (0.4 s `expo.out`), positioned cols 9–11. Faded Bone sub: `over Bryan's campaign`.
- KF @22.00 — donor ledger writes in. Ink Black plate, IBM Plex Mono Newsprint
  Cream lines, one every 0.7 s:
    `BANKS                — assessed at 1/4% of capital`
    `RAILROADS            — assessed by line-mile`
    `STANDARD OIL         — $250,000`
    `J P MORGAN           — $250,000`
- KF @28.00 — counter strip enters: `500,000 voters by train` (0.8 s expo.out)
  paired with `200,000,000 mail pieces` count-up beneath.
- KF @38.00 — dichotomy split arrives (left BRYAN, right HANNA, italic Blood Oxide
  `vs.` between):
    Left: "A 36-year-old preacher who could move a crowd to tears"
    Right: "A ledger"
  Held 6.0 s. (Re-uses the 5-min preview's `s1-dichotomy` block exactly.)
- KF @48.00 — verdict plate: `And when November came, the ledger won.` Playfair
  96 px Hanna Amber, anchor 200 px from bottom. Held 4.0 s.
- KF @120.00 — hard cut Ink Black 0.5 s; transition line: `To understand how — we
  go back fifty-nine years.` Source Serif italic 48 px Faded Bone, centered, held
  3.0 s.
- KF @165.00 → 165.50 — exit to next scene.

**Hyperframe gesture:** *pull-out* on newspaper → *number theatre count-up* ×3 →
*ledger plate write-in* (5.5) → *hard cut* into Scene 3.

**Hero text plates:**
- `1896` Blood Oxide 280 px, 1.2 s.
- `$3,500,000` Hanna Amber 184 px, 3.0 s + count-up.
- `20×` Blood Oxide stamp, 3.0 s.
- Donor ledger, 16 s.
- Dichotomy split, 6 s.
- `And when November came, the ledger won.` 4 s.
- `To understand how — we go back fifty-nine years.` 3 s.

**Assets:** `newspaper-eveningstar-1896-01-11.jpg`. Typography only otherwise.

---

## SCENE 3 — 3:30–5:00 (1:30) — NEW LISBON, OHIO. 1837.

*Composition file:* `compositions/scene-03-new-lisbon.html`
*Engagement role:* Act break (3:30 dip recovery — origin story).

**Layers:**
1. Ink Black BG + grain.
2. Chapter card: `IV` Roman in Faded Bone 96 px, italic title
   `THE COUNTRY GROCERY` Source Serif 4 italic 56 px (held 1.2 s).
3. Year strap `YEAR  1837` (top-left, IBM Plex Mono 32 px Faded Bone).
4. Photograph plate: `hanna-birthplace.jpg` 8-col block (cols 2–11).
5. Crossfade to `hanna-young.jpg` for the second half.
6. Caption strap: `NEW LISBON, OHIO. 1837.` (IBM Plex Mono 28 px, top, between
   hairlines).

**Keyframes:**
- KF @0.00  — chapter card. Held 1.2 s.
- KF @1.20  — chapter exits (power2.in 0.5 s); year strap fades in.
- KF @1.70  — `hanna-birthplace.jpg` enters with 0.8 s `power3.out` from y+40,
  Ken Burns *push-in* 1.00 → 1.04 over 28 s.
- KF @4.00  — caption strap arrives (between Hanna Amber hairlines, 22 px).
- KF @30.00 — crossfade to `hanna-young.jpg` (1.5 s); push-in continues 1.00 → 1.03
  on new image.
- KF @45.00 — pull-out on hanna-young 1.03 → 1.00 over 30 s.
- KF @75.00 — caption strap exits, scene exits to black.
- KF @78.00 — transition line in cream: `And when he was fifteen, the family
  moved to Cleveland.` Held 2.5 s.
- KF @90.00 — exit.

**Hyperframe gesture:** *chapter card* → *push-in* → *crossfade* → *pull-out*.

**Hero text plates:**
- Chapter card `IV — THE COUNTRY GROCERY`, 1.2 s.
- `NEW LISBON, OHIO. 1837.` between hairlines, 28 s.
- Transition line, 2.5 s.

**Assets:** `hanna-birthplace.jpg`, `hanna-young.jpg`. On disk.

---

## SCENE 4 — 5:00–6:00 (1:00) — THE BOY AT THE NEXT DESK

*Composition file:* `compositions/scene-04-rockefeller.html`
*Engagement role:* Sensory delivery at 5:00 (Rockefeller name reveal).

**Layers:**
1. Ink Black BG + grain.
2. Year strap `YEAR  1852` Faded Bone IBM Plex Mono.
3. Left half: `hanna-young.jpg` cols 1–6.
4. Right half: `rockefeller.jpg` cols 7–12 (entering from screen-right at 5 s).
5. 1px Hanna Amber hairline between the two faces.
6. Hero name plate `JOHN D. ROCKEFELLER` Playfair 132 px Newsprint Cream, hold.
7. Sub-line `90% of American oil refining capacity.` Faded Bone 28 px.

**Keyframes:**
- KF @0.00  — `hanna-young.jpg` enters cols 1–6 (0.8 s power3.out).
- KF @1.00  — Ken Burns push-in on Hanna's portrait (1.00 → 1.02 over 12 s).
- KF @8.00  — `rockefeller.jpg` enters from cols 7–12 (0.8 s power3.out from x+60).
- KF @9.00  — 1px Hanna Amber hairline draws between (left → right, 0.6 s).
- KF @14.00 — name plate `JOHN D. ROCKEFELLER` rises from y+40 (0.7 s power3.out),
  positioned across cols 1–12, top y=860; sub-line follows +0.3 s.
- KF @18.00 — held 4 s.
- KF @25.00 — pull-out on the diptych (scale 1.04 → 1.00 over 25 s).
- KF @55.00 — verdict line: `The two would orbit each other for the next forty
  years.` Playfair 84 px Hanna Amber, anchor 200 px bottom. Held 4 s.
- KF @60.00 — exit.

**Hyperframe gesture:** *diptych entry* → *push-in* → *hard cut* on the name plate.

**Hero text plates:**
- `JOHN D. ROCKEFELLER` 132 px, 11 s.
- Verdict line, 4 s.

**Assets:** `hanna-young.jpg`, `rockefeller.jpg`. On disk.

---

## SCENE 5 — 6:00–7:30 (1:30) — THE PRICE OF THINGS

*Composition file:* `compositions/scene-05-price.html`
*Engagement role:* Thesis-reinforce; quiet beat between Rockefeller intro and
Charlotte anchor.

**Layers:**
1. Ink Black BG + grain.
2. Year strap `YEAR  1853–1860`.
3. Photo plate: `cleveland-1870.jpg` (period-near, full 8-col block, cols 2–11).
4. Pull-quote (right margin, cols 9–12, Playfair italic 56 px Newsprint Cream):
   *"the real education was in the price of things."*

**Keyframes:**
- KF @0.00  — chapter card `V — THE COUNTER` Faded Bone, italic, 1.2 s.
- KF @1.20  — chapter exits.
- KF @1.70  — `cleveland-1870.jpg` enters (0.8 s power3.out).
- KF @2.50  — Ken Burns push-in 1.00 → 1.04 over the next 60 s.
- KF @8.00  — pull-quote enters from x+40 with `power3.out` 0.8 s and a Hanna
  Amber hairline above. Held throughout the rest of the scene.
- KF @55.00 — quote exits (power2.in 0.5 s).
- KF @60.00 — transition line: `Then the Civil War came. He served briefly. Came
  home.` Source Serif italic 36 px Newsprint Cream, centered. Held 4 s.
- KF @90.00 — exit.

**Hyperframe gesture:** *push-in* + *held pull-quote*.

**Hero text plates:**
- Chapter card, 1.2 s.
- Pull-quote, 47 s.
- Transition line, 4 s.

**Assets:** `cleveland-1870.jpg`. On disk.

---

## SCENE 6 — 7:30–8:30 (1:00) — CHARLOTTE

*Composition file:* `compositions/scene-06-charlotte.html`
*Engagement role:* Emotional anchor #1 (7:30 dip — the only love beat).

**Layers:**
1. Ink Black BG + grain (no vignette tightening — held perfectly still).
2. Single image OR (procurement-fail fallback) typographic plate:
   - **If procured:** Charlotte Hanna portrait, cols 4–9 (centered 6-col block),
     hairline 1px Hanna Amber, box-shadow as in §4.2.
   - **If not procured:** typography plate, Source Serif 4 italic 56 px Newsprint
     Cream, centered: *"Charlotte Augusta Rhodes — married Mark Hanna,
     September 27, 1864."*

**Keyframes:**
- KF @0.00  — chapter card `VI — CHARLOTTE` Faded Bone italic, 1.5 s. Slower than
  other chapter cards — this is the rest stop.
- KF @1.50  — chapter exits to black (power2.in 0.7 s — also slower).
- KF @2.20  — image (or typography plate) enters with a 1.2 s `power3.out`
  cross-fade. **No motion** for the next 8 s. Vignette static. Grain only.
- KF @10.20 — caption strap appears below: `CLEVELAND, OHIO · SEPTEMBER 27, 1864.`
  IBM Plex Mono 28 px Faded Bone, between Hanna Amber hairlines. Held to end.
- KF @55.00 — exit.

**Hyperframe gesture:** *held silence on a single plate* — deliberate absence of
Ken Burns. This is the only scene where motion is *banned*.

**Hero text plates:**
- Chapter card, 1.5 s.
- Caption strap, 45 s.

**Assets:** Charlotte portrait (TO PROCURE). Fallback typography plate.

---

## SCENE 7 — 8:30–10:00 (1:30) — THE CHOKEPOINT

*Composition file:* `compositions/scene-07-chokepoint.html`
*Engagement role:* Sensory recovery (act break + map gesture introduction).

**Layers:**
1. Ink Black BG + grain.
2. Daniel Rhodes portrait `rhodes-daniel.jpg` (cols 1–5, 5 s only).
3. **Chokepoint map** — motion graphic, no satellite imagery.
   - Lake Erie polygon at top (Newsprint Cream stroke 2px).
   - Pittsburgh mills polygon at bottom-right (Faded Bone stroke 1px).
   - Patina Green ore-boat trace lines drawing top-down across the lake.
   - Cleveland node: a Hanna Amber dollar-sign glyph at the geographic pivot.
4. Verdict line: `Cleveland was the chokepoint. And Hanna sat on it.`
   Playfair 96 px Hanna Amber, bottom anchor 200 px.

**Keyframes:**
- KF @0.00  — chapter card `VII — THE CHOKEPOINT` 1.2 s.
- KF @1.20  — Rhodes portrait enters cols 1–5 (0.8 s power3.out); paired with role
  tag `Daniel P. Rhodes — Cleveland coal-and-iron magnate. Father-in-law.` (Faded
  Bone 28 px).
- KF @6.00  — Rhodes exits.
- KF @8.00  — map composes in. Order:
    a. Lake Erie polygon strokes in 1.5 s (`power3.out`).
    b. Pittsburgh polygon strokes in at +0.5 s offset, 1.5 s.
    c. First ore-boat line traces Lake Erie → Cleveland in 2.0 s linear.
    d. Cleveland node: Hanna Amber dollar-sign glyph fades in 0.4 s, then a
       single Hanna Amber pulse (scale 1.00 → 1.06 → 1.00 over 0.6 s).
- KF @20.00 — second ore-boat line traces Cleveland → Pittsburgh.
- KF @28.00 — third ore-boat line; the Cleveland node pulses again.
- KF @55.00 — verdict line lands; map dims to 40% behind it.
- KF @70.00 — micro-acquisitions list strip writes in (4 lines, IBM Plex Mono):
    `i. The Cleveland Herald — Newspaper`
    `ii. An Opera House — Theater`
    `iii. Banking Interests — Finance`
    `iv. A Streetcar Line — Transit`
  (This re-uses the 5-min preview's `s3-acquisitions` element exactly; it already
  works.)
- KF @86.00 — second verdict: `When he walked into a room, the room changed
  temperature.` Playfair italic 72 px Newsprint Cream, anchor 200 px bottom. Held
  3.0 s.
- KF @90.00 — exit.

**Hyperframe gesture:** *map* (7.3) — first appearance of the gesture.

**Hero text plates:**
- Chapter card, 1.2 s.
- Rhodes role tag, 5 s.
- Map title (top): `CLEVELAND — THE CHOKEPOINT`, 60 s.
- Verdict line, 15 s.
- Acquisitions list, 16 s.
- Second verdict, 3 s.

**Assets:** `rhodes-daniel.jpg`. Map is custom motion graphic. On disk.

---

## SCENE 8 — 10:00–11:30 (1:30) — THE THESIS

*Composition file:* `compositions/scene-08-thesis.html`
*Engagement role:* Emotional hit at 10:00 (the line crossing — vignette tightens).

**Layers:**
1. Ink Black BG + grain.
2. `hanna-portrait.jpg` cols 4–9 (centered).
3. Vignette layer (radial Ink Black at 8% → 28% across the scene).
4. Pull-quote 1: `Money was the second most powerful thing in America.` Playfair
   84 px Newsprint Cream, on a black plate.
5. Pull-quote 2 (the answer): `The most powerful thing was who decided where the
   money went.` Playfair 84 px Blood Oxide.

**Keyframes:**
- KF @0.00  — chapter card `VIII — THE THESIS` 1.2 s.
- KF @1.20  — `hanna-portrait.jpg` enters with 1.0 s `power3.out`, no Ken Burns,
  vignette starts soft (8%).
- KF @2.50  — vignette begins tightening linearly (8% → 28% over 60 s).
- KF @25.00 — portrait fades to 0.4 opacity; pull-quote 1 enters from y+40
  (0.8 s power3.out), centered, held.
- KF @40.00 — black flash (1.0 s of pure Ink Black — silence beat).
- KF @41.00 — pull-quote 2 enters in Blood Oxide, identical motion. Held 4 s.
- KF @55.00 — verdict line: `That was politics. And no one had ever run it like a
  business. Not yet.` Playfair 72 px Hanna Amber, 200 px bottom anchor. Held 4 s.
- KF @90.00 — exit.

**Hyperframe gesture:** *push-in* (light, via vignette tightening) → *held silence
on typography*.

**Hero text plates:**
- Chapter card.
- Pull-quote 1 (cream), 14 s.
- Pull-quote 2 (Blood Oxide), 14 s.
- Verdict, 4 s.

**Assets:** `hanna-portrait.jpg`. On disk.

---

## SCENE 9 — 11:30–14:00 (2:30) — CHICAGO, 1888

*Composition file:* `compositions/scene-09-chicago-1888.html`
*Engagement role:* Emotional anchor #2 at 13:00 (McKinley's loyalty refusal).

**Layers:**
1. Ink Black BG + grain.
2. Convention photograph: `convention-1888.jpg` (cols 1–12, full bleed).
3. Sherman name plate (Playfair 96 px Newsprint Cream).
4. Vote tally crawl (left margin cols 1–2, IBM Plex Mono 28 px tabular-nums):
    `BALLOT 1   229  Sherman`
    `BALLOT 2   244  Sherman`
    `BALLOT 3   230  Sherman`
    `BALLOT 4   235  Sherman`
    `BALLOT 5   244  Sherman`
    `BALLOT 6   230  Sherman`
    `BALLOT 7   231  Sherman`
    `BALLOT 8   ---  Harrison nominated`
5. McKinley name plate at 13:00 — Playfair 132 px Newsprint Cream.
6. McKinley sub-line: `Congressman, 17th District, Ohio. 45 years old.`

**Keyframes:**
- KF @0.00  — chapter card `IX — CHICAGO, 1888` 1.2 s.
- KF @1.20  — `convention-1888.jpg` enters (0.8 s power3.out); Ken Burns *push-in*
  begins (1.00 → 1.04 over 30 s).
- KF @4.00  — newsprint strap top: `REPUBLICAN NATIONAL CONVENTION · CHICAGO ·
  JUNE 1888.`
- KF @10.00 — Sherman name plate enters cols 1–12, top y=200; held 4 s; exits to
  upper-right corner (translateX +600, translateY -120, 1.0 s `power2.in`) and
  shrinks to a tag-size 28 px IBM Plex Mono entry: `SHERMAN, JOHN — Ohio · Treas.`.
- KF @20.00 — convention image pulls out (1.04 → 1.00 over 60 s).
- KF @28.00 — vote tally crawl writes in (one ballot every 1.4 s, `power2.out`).
  Ballot 8 lands in Blood Oxide.
- KF @42.00 — Sherman tag dims to 30%; the floor of the convention image dims
  with it.
- KF @60.00 — hard cut to black 1.0 s (the pivot — the script's BEAT 0.8 s + a
  little extra for the visual).
- KF @61.00 — McKinley name plate enters Playfair 132 px Newsprint Cream
  (0.7 s power3.out, letter-spacing tighten). Sub-line at +0.4 s.
- KF @67.00 — `mckinley-1896.jpg` enters cols 4–9 below the name (0.8 s).
  Ken Burns push-in (1.00 → 1.02 over 35 s).
- KF @100.00 — pull-quote: `That kind of loyalty was rare in eighteen eighty-eight
  politics. It was almost extinct.` Source Serif italic 56 px Newsprint Cream,
  cols 1–12 centered. Held 4 s.
- KF @130.00 — verdict: `He had just found his president.` Playfair 96 px
  Hanna Amber, bottom anchor 200 px. Held 5 s.
- KF @150.00 — exit.

**Hyperframe gesture:** *pull-out* on the convention image → *vote-tally crawl*
(unique to this scene; not a reusable gesture) → *hard cut to black + name plate*
for McKinley → *push-in* on the McKinley portrait → *verdict line*.

**Hero text plates:**
- Chapter card, 1.2 s.
- Sherman plate, 4 s + tag-size persistence ~40 s.
- Vote tally, 14 s.
- McKinley name + role, 6 s.
- Loyalty pull-quote, 4 s.
- Verdict, 5 s.

**Assets:** `convention-1888.jpg`, `mckinley-1896.jpg`. On disk.

---

## SCENE 10 — 14:00–16:00 (2:00) — THE PANIC

*Composition file:* `compositions/scene-10-panic.html`
*Engagement role:* Tension before mechanism payoff (#2).

**Layers:**
1. Ink Black BG + grain.
2. Newspaper-front composite: `M'KINLEY FACING FINANCIAL RUIN — Liabilities,
   $130,000.` Cleveland Plain Dealer style, period typesetting, two columns.
3. McKinley note plate: black, Source Serif italic 72 px Newsprint Cream:
   *"I am a beggar."*
4. Ida McKinley typography plate (procurement-fail fallback): `Ida Saxton McKinley
   — chronically ill, often bedridden — kept off the campaign trail by her health.`
5. `mckinley-1896.jpg` paired with the Ida plate.
6. Verdict pair: `The candidate was now a debt.` (Playfair 84 px Blood Oxide) and
   below it `And Hanna held the paper.` (Playfair 84 px Hanna Amber).

**Keyframes:**
- KF @0.00  — chapter card `X — THE PANIC. 1893.` 1.2 s.
- KF @1.20  — newspaper-front composite enters from y-60 (0.8 s power3.out);
  Ken Burns *push-in* on the headline 1.00 → 1.05 over 25 s.
- KF @4.00  — sub-headline `1,5000 BUSINESSES UNDER. 640 BANKS FAIL.` (Faded Bone
  IBM Plex Mono 28 px) animates in below.
- KF @28.00 — hard cut to black 0.8 s (the BEAT 0.6 s).
- KF @28.80 — McKinley note plate: black background, italic quote enters
  centered with letter-spacing tighten 0.05 → −0.02 (0.7 s power3.out). Held 8 s.
- KF @37.00 — Ida McKinley plate slides in from screen-right (cols 7–12) paired
  with `mckinley-1896.jpg` cols 1–6 (1.0 s `power3.out`). Held 12 s.
- KF @50.00 — Ida + McKinley exit; Hanna's quiet rescue ledger writes in:
    `WALKER NOTES — absorbed by Cleveland/NY syndicate, March 1893`
    `MCKINLEY signed: nothing`
    `MCKINLEY owed:  nothing`
  IBM Plex Mono Newsprint Cream, one line every 1.0 s.
- KF @75.00 — verdict pair lands (cross-fade in over 1.0 s). Held 5 s.
- KF @120.00 — exit.

**Hyperframe gesture:** *push-in* (newspaper) → *held silence on a typography
plate* (the "I am a beggar" plate) → *ledger plate* (small, the rescue) → *verdict
pair*.

**Hero text plates:**
- Chapter card, 1.2 s.
- Newspaper composite, 25 s.
- McKinley note italic, 8 s.
- Ida plate, 12 s.
- Rescue ledger, 4 lines × 1 s.
- Verdict pair, 5 s.

**Assets:** `mckinley-1896.jpg`. Newspaper composite is custom typographic plate.

---

## SCENE 11 — 16:00–17:45 (1:45) — THE MECHANISM

*Composition file:* `compositions/scene-11-mechanism.html`
*Engagement role:* Number-theatre payoff #2 (the math is on screen).

**Layers:**
1. Ink Black BG + grain.
2. Cream plate fills cols 2–11 (centered).
3. Hero ledger lines (IBM Plex Mono Newsprint Cream on the cream plate, rendered
   as Ink Black text *for legibility on cream*).
4. Total stamp in Blood Oxide.

**Keyframes:**
- KF @0.00  — chapter card `XI — THE MECHANISM` 1.2 s.
- KF @1.20  — cream plate slides up from screen-bottom (1.0 s `power3.out`).
- KF @2.50  — first ledger line writes in (0.4 s power2.out, +0.4 s stagger
  between subsequent lines):

    ```
    BANKS                — 1/4 % of paid-in capital
    RAILROADS            — assessed by line-mile
    STANDARD OIL         — $250,000
    J P MORGAN           — $250,000
    NEW YORK LIFE        — $50,000
    EQUITABLE            — $50,000
    METROPOLITAN LIFE    — $50,000
    ─────────────────────
    ```
- KF @8.00  — underline rule draws across (1.2 s expo.out).
- KF @9.50  — total line writes in: `TOTAL, 1896           — $3,500,000`. The
  dollar amount stamps in Blood Oxide (scale 1.05 → 1.00 over 0.4 s expo.out).
- KF @20.00 — Bryan comparison line writes in below the total in Faded Bone
  IBM Plex Mono: `BRYAN, 1896           — $300,000 (estimated)`.
- KF @23.00 — comparison hairline draws between total and Bryan (Hanna Amber,
  1.0 s).
- KF @27.00 — verdict: `Twenty times what William Jennings Bryan would raise.`
  Playfair 84 px Blood Oxide, anchor 200 px bottom. Held 4 s. (The antagonist's
  name lands here for the first time on screen — emphasized.)
- KF @100.00 — cream plate exits (slides down off-screen 1.0 s `power2.in`).
- KF @105.00 — exit.

**Hyperframe gesture:** *ledger plate write-in* (5.5 — single use of this
gesture in the entire 24 minutes; this is the canonical mechanism reveal).

**Hero text plates:**
- Chapter card, 1.2 s.
- Ledger plate, 25 s of write-in + holds.
- Bryan comparison, 5 s.
- Verdict, 4 s.

**Assets:** Typography only.

---

## SCENE 12 — 17:45–18:30 (45 s) — THE FRONT PORCH

*Composition file:* `compositions/scene-12-front-porch.html`
*Engagement role:* Scale theatre ahead of the Cross-of-Gold contrast.

**Layers:**
1. Ink Black BG + grain.
2. McKinley front-porch photograph (TO PROCURE — fallback: held wide static plate
   of Canton, Ohio with Faded Bone caption).
3. Visitor counter strip (cols 9–12, IBM Plex Mono Hanna Amber):
    Stop-motion stamps that increment on screen.
4. `+12,400 → +74,000 → +218,000 → +501,200` count.

**Keyframes:**
- KF @0.00  — chapter card `XII — THE FRONT PORCH` 1.2 s.
- KF @1.20  — porch photograph (or fallback plate) enters (0.8 s `power3.out`).
- KF @4.00  — counter starts at `+0` and stamps to `+12,400` (0.4 s).
- KF @12.00 — counter stamps `+74,000`.
- KF @22.00 — counter stamps `+218,000`.
- KF @32.00 — counter stamps `+501,200` in Blood Oxide; horizontal hairline
  underscore draws.
- KF @38.00 — verdict: `Half a million voters. By train. To Canton.` Playfair
  72 px Hanna Amber, anchor 200 px bottom. Held 4 s.
- KF @45.00 — exit.

**Hyperframe gesture:** *number theatre count-up* (5.4) — but stop-motion stamping
rather than smooth count-up, because the irregular increments are the joke
(scale arrives in jumps, not a smooth curve).

**Hero text plates:**
- Chapter card.
- Counter strip, 30 s.
- Verdict, 4 s.

**Assets:** McKinley front-porch photograph (TO PROCURE) — fallback typography.

---

## SCENE 13 — 18:30–19:30 (1:00) — CROSS OF GOLD

*Composition file:* `compositions/scene-13-cross-of-gold.html`
*Engagement role:* Emotional contrast — the ledger pivot rhyme.

**Layers:**
1. Ink Black BG + grain.
2. Held quote plate (no portrait first 8 s): Source Serif 4 italic 84 px
   Newsprint Cream, cols 1–12 centered:
   *"You shall not press down upon the brow of labor this crown of thorns. You
   shall not crucify mankind upon a cross of gold."*
3. Bryan portrait (TO PROCURE) cols 4–9, entering at +30 s.

**Keyframes:**
- KF @0.00  — chapter card `XIII — CROSS OF GOLD` 1.2 s.
- KF @1.20  — quote plate composes in line by line. Top stanza enters from y+40
  (0.8 s power3.out); bottom stanza follows +0.6 s.
- KF @4.00  — first held silence: 1.5 s with no motion, just grain.
- KF @5.50  — Bryan attribution arrives below the quote in Faded Bone 28 px IBM
  Plex Mono: `WILLIAM JENNINGS BRYAN · DEMOCRATIC NATIONAL CONVENTION · CHICAGO ·
  JULY 9, 1896.`
- KF @20.00 — second held silence: 1.5 s.
- KF @30.00 — quote dims to 30%; Bryan portrait (or Bryan typographic plate
  fallback) cross-fades in cols 4–9 (1.0 s).
- KF @40.00 — Ken Burns push-in on Bryan 1.00 → 1.03 over 18 s.
- KF @55.00 — verdict: `Hanna read the speech in Cleveland that night, and went,
  the next morning, to the bank.` Source Serif italic 36 px Newsprint Cream,
  centered, anchor 200 px. Held 5 s.
- KF @60.00 — exit.

**Hyperframe gesture:** *held silence on a typography plate* (5.6) → *push-in*
on the antagonist's portrait.

**Hero text plates:**
- Chapter card.
- Cross-of-Gold quote, 26 s.
- Bryan attribution, 26 s.
- Verdict, 5 s.

**Assets:** Bryan portrait (TO PROCURE — fallback: typographic plate with the
attribution alone).

---

## SCENE 14 — 19:30–20:15 (45 s) — TWO HUNDRED MILLION

*Composition file:* `compositions/scene-14-two-hundred-million.html`
*Engagement role:* Number-theatre payoff #3 (the mail count) + asymmetric warfare.

**Layers:**
1. Ink Black BG + grain.
2. **Three-pane composition**:
   - Top-left: `200,000,000` count-up Playfair 184 px Hanna Amber.
   - Top-right: animated rail-line tracing 18,000 miles of Bryan's tour across a
     simplified continental US outline (Patina Green stroke 2px). Counter:
     `18,000 mi.` Faded Bone IBM Plex Mono.
   - Bottom: pamphlet stack rising — typographic stack of language tags
     (`German · Polish · Yiddish · Italian · Spanish · Norwegian · Swedish ·
     Czech · Hungarian · Lithuanian · Slovak · Greek · Welsh · French`).

**Keyframes:**
- KF @0.00  — chapter card `XIV — ASYMMETRY` 1.2 s.
- KF @1.20  — top-left counter starts at `0`. Counter runs 0 → 200,000,000 over
  4.0 s `expo.out`. Horizontal hairline lands at the freeze. Caption: `PIECES OF
  CAMPAIGN MAIL.` (Faded Bone IBM Plex Mono 22 px under the number).
- KF @9.00  — top-right map composes; rail-line traces in (3.0 s linear), counter
  ticks `+1,000 mi → +18,000 mi`.
- KF @18.00 — bottom pamphlet stack rises one tag every 0.4 s, `power2.out`,
  total of 14 language tags.
- KF @38.00 — verdict: `Hanna mailed a country.` Playfair 96 px Hanna Amber,
  anchor 200 px bottom. Held 4 s.
- KF @45.00 — exit.

**Hyperframe gesture:** *number theatre count-up* (5.4) + *map* (7.3 — second of
two map appearances; deliberate echo of Scene 7's Cleveland chokepoint to draw
the line: same gesture, different scale).

**Hero text plates:**
- Chapter card.
- `200,000,000` and label, full scene.
- Rail-line counter, 25 s.
- Pamphlet stack, 17 s.
- Verdict, 4 s.

**Assets:** Typography + custom motion graphic.

---

## SCENE 15 — 20:15–20:45 (30 s) — NOVEMBER 3, 1896

*Composition file:* `compositions/scene-15-election-night.html`
*Engagement role:* Resolution (number-theatre payoff #3 final landing).

**Layers:**
1. Ink Black BG + grain.
2. Single result plate, IBM Plex Mono Newsprint Cream:
    ```
    McKINLEY   271 electoral votes
    BRYAN      176 electoral votes
    ```
3. Verdict line (re-use of script's third payoff): `And when November came, the
   ledger won.` Playfair 96 px Hanna Amber.

**Keyframes:**
- KF @0.00  — black plate. Hold 1.5 s of silence (per script BEAT).
- KF @1.50  — result plate composes: McKinley line first (0.6 s power3.out),
  Bryan line +0.5 s. tabular-nums vital here.
- KF @5.50  — held 4 s in silence.
- KF @9.50  — verdict line lands centered, mid-screen, scale 1.05 → 1.00
  (`expo.out` 0.4 s), Hanna Amber. Held 4 s.
- KF @14.00 — popular-vote sub-line writes in below in Faded Bone 28 px IBM Plex
  Mono: `7,108,480 — 6,511,495 · 51% McKinley.` Held to end.
- KF @25.00 — exit (1.0 s `power2.in` to black; longer than usual for the
  resolution beat).
- KF @30.00 — full exit.

**Hyperframe gesture:** *held silence on a typography plate* (5.6) — the third
appearance and the strongest one, since the silence after the result plate is the
most dramatic in the document.

**Hero text plates:**
- Result plate, 24 s.
- Verdict, 15 s.
- Popular vote sub, 11 s.

**Assets:** Typography only.

---

## SCENE 16 — 20:45–22:00 (1:15) — SENATOR HANNA. AND THE COWBOY.

*Composition file:* `compositions/scene-16-cowboy.html`
*Engagement role:* Pre-climax patience window + dramatic-irony pull-quote.

**Layers:**
1. Ink Black BG + grain.
2. Timeline strip — cols 1–12, three rows, IBM Plex Mono Newsprint Cream:
    ```
    1897 — Hanna takes the Senate seat, Ohio.
    1899 — Vice-President Hobart dies in office.
    1900 — Roosevelt forced onto McKinley's re-election ticket.
    ```
3. Held Hanna pull-quote (Playfair italic 84 px Hanna Amber):
   *"Don't any of you realize there's only one life between this madman and the
   Presidency?"*
4. Roosevelt name reveal (Playfair 132 px Newsprint Cream).

**Keyframes:**
- KF @0.00  — chapter card `XVI — THE COWBOY` 1.2 s.
- KF @1.20  — timeline strip writes in row by row (1.0 s per row, `power2.out`);
  each row's year stamps in Hanna Amber.
- KF @14.00 — timeline dims to 30%; the third row (1900) brightens back to
  100% and animates a small Hanna Amber underline.
- KF @28.00 — pull-quote composes. Hard cut to black 0.8 s. Then italic quote
  enters from y+40 (0.8 s power3.out). Held 2.5 s of silence (the script's BEAT
  0.8 s + a longer beat for dramatic irony).
- KF @55.00 — pull-quote exits (0.7 s `power2.in`).
- KF @58.00 — Roosevelt name plate enters: `THEODORE ROOSEVELT` Playfair 132 px
  Newsprint Cream (no portrait — script intentionally withholds), Faded Bone
  sub-line: `Governor of New York. War hero. Reformer. The madman.` Held 6 s.
- KF @70.00 — verdict: `They did not listen.` Playfair 96 px Blood Oxide,
  anchor 200 px bottom. Held 5 s.
- KF @75.00 — exit.

**Hyperframe gesture:** *held silence on a typography plate* (5.6 — the
dramatic-irony version).

**Hero text plates:**
- Chapter card.
- Timeline strip, 14 s.
- Pull-quote, 25 s.
- Roosevelt name, 6 s.
- Verdict, 5 s.

**Assets:** Typography only. (Roosevelt portrait deliberately withheld until
Scene 17.)

---

## SCENE 17 — 22:00–23:00 (1:00) — BUFFALO

*Composition file:* `compositions/scene-17-buffalo.html`
*Engagement role:* Climax shock — held silence + name flash.

**Layers:**
1. Ink Black BG + grain.
2. Typography plate: `BUFFALO. SEPTEMBER 6, 1901.` Playfair 132 px Newsprint
   Cream, centered.
3. Newspaper-front composite: `PRESIDENT SHOT AT EXPOSITION.` Period
   Cleveland Plain Dealer / Buffalo Courier headline, two-column typesetting.
4. Czolgosz name flash (Faded Bone 32 px IBM Plex Mono): `Leon Czolgosz,
   anarchist, of Cleveland.` — held 1.0 s, then off.
5. Time-of-death plate: `2:15 a.m. · September 14, 1901.` IBM Plex Mono
   Newsprint Cream.

**Keyframes:**
- KF @0.00  — full black, 1.5 s of silence (per script BEAT 1.5 s).
- KF @1.50  — typography plate: `BUFFALO. SEPTEMBER 6, 1901.` enters with
  letter-spacing tighten (0.7 s power3.out). Held 4 s.
- KF @7.00  — plate exits (0.5 s); newspaper front composite enters (0.8 s
  `power3.out`); Ken Burns *push-in* 1.00 → 1.04 over 20 s.
- KF @18.00 — Czolgosz name flash bottom-right cols 9–12 in Faded Bone 32 px
  IBM Plex Mono. Held 1.0 s. Exits to black with 0.4 s `power2.in`.
- KF @22.00 — held silence: 1.2 s (the BEAT after "two shots").
- KF @28.00 — newspaper exits (0.6 s); time-of-death plate enters: `2:15 a.m.
  · SEPTEMBER 14, 1901.` IBM Plex Mono Newsprint Cream cols 1–12 centered.
  Held 5 s.
- KF @45.00 — Roosevelt sworn-in line writes in: `THEODORE ROOSEVELT — sworn in,
  borrowed library, Delaware Avenue, Buffalo. September 14, 1901.` Faded Bone
  IBM Plex Mono 28 px. Held 6 s.
- KF @55.00 — verdict: `Mark Hanna's project ends — eight years before Mark
  Hanna does.` Playfair 84 px Blood Oxide, anchor 200 px bottom. Held 5 s.
- KF @60.00 — exit.

**Hyperframe gesture:** *held silence on a typography plate* (5.6) → *push-in*
(5.1) on a newspaper → *hard cut + name flash* → *held silence* → *verdict*.

**Hero text plates:**
- `BUFFALO. SEPTEMBER 6, 1901.` 4 s.
- Newspaper front, 11 s.
- Czolgosz name, 1.0 s — deliberately the shortest hero plate in the document.
- Time-of-death plate, 5 s.
- Roosevelt sworn-in, 6 s.
- Verdict, 5 s.

**Assets:** All typography + custom newspaper plate. (Pan-American Expo Temple
of Music image is not required for the climax; if procured, it lives as a
secondary inset under the time-of-death plate at low contrast.)

---

## SCENE 18 — 23:00–23:30 (30 s) — TYPHOID

*Composition file:* `compositions/scene-18-typhoid.html`
*Engagement role:* Quiet obituary beat before the closing thesis.

**Layers:**
1. Ink Black BG + grain.
2. Typographic obituary plate (cols 2–11, cream plate, period typesetting):
    Headline (Playfair 124 px): **M. A. HANNA DEAD**
    Dateline (IBM Plex Mono 24 px Faded Bone): `WASHINGTON, FEB. 15.`
    Two columns of period body text (Source Serif 4 18 px Ink Black on cream).
3. End-of-life sub-strap: `MARK HANNA · 1837–1904. AGE SIXTY-SIX.` Faded Bone.

**Keyframes:**
- KF @0.00  — chapter card `XVIII — TYPHOID. WASHINGTON, 1904.` 1.2 s.
- KF @1.20  — cream plate slides in from screen-bottom (1.0 s `power3.out`).
- KF @2.50  — headline writes in (0.7 s); dateline +0.4 s; body columns
  cross-fade (1.5 s) — body is dim, decorative, not legible at full scale. The
  *image* of the obituary, not its readable text, is the beat.
- KF @18.00 — sub-strap arrives below the plate in Hanna Amber 32 px IBM
  Plex Mono. Held to end.
- KF @28.00 — exit (0.7 s `power2.in`, slower than usual — quiet ending).
- KF @30.00 — full exit.

**Hyperframe gesture:** *held silence on a typography plate* (5.6 — the
obituary version, fourth and final use of the gesture; this is the closing of
the silence motif from Scene 6 / Scene 13 / Scene 16).

**Hero text plates:**
- Chapter card.
- `M. A. HANNA DEAD` headline, 26 s.
- Sub-strap, 10 s.

**Assets:** Typography only. (Hanna funeral procession — TO PROCURE — would
sit as an under-plate inset at 30% opacity if procured. Fallback is fine.)

---

## SCENE 19 — 23:30–24:00 (30 s) — THE INHERITANCE

*Composition file:* `compositions/scene-19-inheritance.html`
*Engagement role:* Thesis-close — the template traced forward.

**Layers:**
1. Ink Black BG + grain.
2. Vertical timeline (cols 4–9, centered), IBM Plex Mono. Each row arrives
   stamped:
    ```
    1896 — $ 3,500,000   ●  Hanna · McKinley
    1900 — $ 3,000,000   ●
    1928 — $ 6,300,000   ●
    1972 — $ 138,000,000 ●
    2008 — $ 1,300,000,000 ●
    2024 — $ 2,700,000,000 ●
    ```
   Years and amounts in Hanna Amber; row dots in Patina Green.
3. Connector lines drawing from each row back to the 1896 row in Patina
   Green 1px stroke.
4. Final cartoon image returns: `cartoon-dollar-mark-hanna.jpg` cols 1–4 at
   30% opacity, slow held.
5. Verdict / closing trio:
   - `His name was Mark Hanna.` Playfair 96 px Newsprint Cream.
   - 2.0 s held silence on the cartoon.
   - `The cartoon ran in every Hearst paper in America.` Playfair 84 px
     Hanna Amber.

**Keyframes:**
- KF @0.00  — chapter card `XIX — THE INHERITANCE` 1.2 s.
- KF @1.20  — vertical timeline composes top-down. Each row writes in 0.5 s
  (power2.out), +0.5 s stagger; the dollar amount stamps with a 0.4 s `expo.out`.
  Total compose time ~6.0 s.
- KF @8.00  — connector lines draw from rows 2–6 back to row 1 (1.5 s
  expo.out, Patina Green). Each connector line arrives at +0.3 s offset.
- KF @14.00 — Ken Burns *pull-out* on the entire timeline (scale 1.04 → 1.00
  over 8 s) so the audience sees the full structural rhyme.
- KF @20.00 — `His name was Mark Hanna.` lands centered, 2.0 s.
- KF @22.50 — cartoon image cross-fades in cols 1–4 at 30% opacity; held 2.0 s
  in silence.
- KF @25.00 — `The cartoon ran in every Hearst paper in America.` lands
  centered (Playfair 84 px Hanna Amber), held 4 s.
- KF @30.00 → end card cross-fade (0.5 s) into END CARD.

**Hyperframe gesture:** *pull-out* (5.2 — third and final pull-out) over the
timeline + *held silence* + *verdict pair*. The pull-out direction echoes Scene
1's push-in: we end where we began but with the camera pulling back to reveal
the system Hanna built.

**Hero text plates:**
- Chapter card.
- Vertical timeline, 22 s.
- `His name was Mark Hanna.` 4 s.
- Cartoon held, 2 s.
- Closing line, 4 s.

**Assets:** `cartoon-dollar-mark-hanna.jpg`. Typography otherwise.

---

## END CARD — 23:55–24:00 (5 s)

*Composition file:* embedded in `scene-19-inheritance.html` final 5 s, OR a
dedicated `compositions/end-card.html` (assembly-time decision).

**Layout:**
- Black plate.
- `THE LEDGER` Playfair 124 px Newsprint Cream, centered.
- Hanna Amber 1px hairline below.
- `Mark Hanna · 1837–1904` IBM Plex Mono 32 px Faded Bone, centered.
- Bottom-right (cols 11–12): `@AmericanAudacity · Episode 02.` IBM Plex Mono
  18 px Faded Bone.

**Keyframes:**
- KF @0.00  — title block enters from y+40 (1.0 s `power3.out`).
- KF @1.50  — held 3.5 s in silence on black with grain only.
- KF @5.00  — full document end. Hard cut to absolute black.

**Hero text plates:** title + dates.
**Assets:** typography only.

---

## Layer-order summary (cross-scene)

For the assembly composition (`index.html`), the per-scene compositions are
stacked in `data-track-index` order with `.scene-layer.clip` overlap of 0.5 s
between scenes (matches the 5-min preview's pattern). Each scene's internal
GSAP timeline starts at 0 and runs to the scene's `data-duration` (per
LEARNINGS line 13). Scene-relative — never narration-aligned — so a per-scene
re-render of audio does not require re-warping visual GSAP.

Total visual duration: 1,440 s (= 24:00). Cumulative scene durations:
45 + 165 + 90 + 60 + 90 + 60 + 90 + 90 + 150 + 120 + 105 + 45 + 60 + 45 + 30 +
75 + 60 + 30 + 30 + 5 = 1,445 s with overlaps absorbed = 1,440 s net.

---

## Asset summary (delegate to `t_e781bf96` for procurement)

**On-disk, ready to use (13):**
`cartoon-dollar-mark-hanna.jpg`, `cartoon-shylock-hanna.jpg`,
`cartoon-boss-of-bosses.jpg`, `hanna-portrait.jpg`, `hanna-young.jpg`,
`hanna-birthplace.jpg`, `cleveland-1870.jpg`, `rhodes-daniel.jpg`,
`rockefeller.jpg`, `convention-1888.jpg`, `mckinley-1896.jpg`,
`newspaper-eveningstar-1896-01-11.jpg`, `davenport-hanna-1896.jpg`.

**To procure (7), with typographic fallbacks already designed:**
1. Charlotte Hanna portrait — Scene 6.
2. Ida Saxton McKinley portrait — Scene 10.
3. McKinley front-porch crowd photograph — Scene 12.
4. McKinley-Roosevelt 1900 inauguration — Scene 16 (optional).
5. William Jennings Bryan portrait c. 1896 — Scene 13.
6. Pan-American Exposition Temple of Music — Scene 17 (optional).
7. Hanna funeral procession — Scene 18 (optional).

Items 4, 6, 7 are *optional* — the typographic fallbacks for these scenes are
designed to stand alone and not feel like fallbacks. Items 1, 2, 3, 5 are *core*
— the scene loses something if no portrait/photo lands.

---

## Acceptance check

A reviewer reading this document can answer:

- **For each of 19 scenes, what is on screen at every second?** Yes (KF
  blocks).
- **What asset does each scene need?** Listed per-scene + summary §asset.
- **Which hyperframe gesture does each scene use?** Listed per-scene; tied
  back to STYLE_GUIDE §5's six-gesture vocabulary.
- **How does each scene fit the engagement plan?** "Engagement role" line per
  scene; full mapping in `ENGAGEMENT_MAP.md`.
- **What can the animator hand off to GSAP?** Each scene's KFs are explicit
  scene-relative seconds; eases match STYLE_GUIDE §9; GSAP can implement the
  KF list as `tl.to(...)` calls without re-asking design questions.
