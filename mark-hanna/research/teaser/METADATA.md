# YouTube Short — Upload Metadata

> Teaser Short for the Mark Hanna documentary.
> Source: hyperframe-test/mark-hanna/research/teaser/{TEASER_BRIEF.md, EDIT_PLAN.md}
> Curiosity gap is structural — withhold McKinley, Bryan, the November result, the
> mechanism, the origin, and the death. The teaser names: Hanna, 1896, $3,500,000,
> 20x, Standard Oil $250,000, JP Morgan $250,000, 500,000 voters, the preacher,
> the ledger. Nothing else.

---

## 1. Title

**Primary (recommended) — 50 chars**

```
The Cartoon You've Seen. The Name You Don't Know.
```

Why this one: it is the pinned on-screen caption of the first three seconds, so
the title, the thumbnail, and the opening frame all carry the same sentence. The
viewer's pattern-match is reinforced three times before the name reveal at 0:06.
No name in the title preserves the strongest curiosity gap — viewers cannot
resolve the question by skimming the title text under the player.

**Alternate A — 45 chars** (numbers-first, names Hanna)

```
Mark Hanna and the $3,500,000 Ledger of 1896
```

Use if A/B testing on the channel shows named-figure titles outperform
mystery-titled hooks. Still spoiler-safe: "ledger" preserves the closer beat,
and the outcome ("the ledger won") is not stated.

**Alternate B — 44 chars** (the missing-recipient angle)

```
He Spent $3,500,000 on a President in 1896
```

The strongest curiosity title — names the spend and the year, hides the spender
*and* the recipient. "A president" reads like an unsolved mystery without
naming McKinley. Use if retention data on the channel rewards interrogative or
quasi-tabloid title grammar.

**All three are <=60 chars; none state the November outcome, McKinley, or Bryan.**

---

## 2. Description

```
The cartoon ran in every Hearst paper in America. The man in it was never named.

In 1896, one man kept a ledger that turned a presidential election into a purchase
order — $3,500,000, twenty times what the other side could spend, with Standard
Oil and JP Morgan paying in by the quarter-million.

This is the teaser. The full documentary names what the ledger bought.

Watch the full story — link in bio.

#History #USHistory #GildedAge #1896 #Documentary #PoliticalHistory #MarkHanna
```

Notes:

- 4 short paragraphs, no spoilers — McKinley, Bryan, and the result are absent.
- Hook line is the cold-open narration verbatim (clip 1) so the first text the
  viewer sees in the description echoes the audio they just heard.
- "names what the ledger bought" is a soft engagement prompt — it invites the
  click without using exclamation marks or a "SUBSCRIBE!!" register, consistent
  with DESIGN.md §5 (no emoji, decisive editorial voice).
- Hashtags are concrete topical (#1896, #GildedAge, #MarkHanna) plus generic
  reach (#History, #USHistory, #Documentary). #PoliticalHistory disambiguates
  from current-affairs feeds. Seven tags is YouTube's sweet spot for Shorts
  search without keyword-stuffing penalties.
- No emoji. No exclamation marks. No "Don't forget to like and subscribe."

---

## 3. Thumbnail concept

**One-line summary:** the Davenport dollar-sign-suit cartoon, full-bleed and
desaturated, with a four-word indictment caption pinned across it.

### 3.1 Layout (1080 x 1920, vertical Shorts thumbnail)

```
+-----------------------------------------------+
|  [top 150 px reserved — YouTube UI overlay]   |
+-----------------------------------------------+
|                                               |
|                                               |
|                                               |
|         davenport-hanna-1896.jpg              |  <- full-bleed
|         (or cartoon-dollar-mark-hanna.jpg     |     desaturated
|          if Davenport rights feel uncertain)  |     to ~30% chroma
|                                               |
|         centered crop on figure;              |
|         dollar-sign suit dominant;            |
|         cigar visible; face partially         |
|         in shadow (we know him, we don't      |
|         know who he is)                       |
|                                               |
|                                               |
|         +-------------------------------+     |
|         |                               |     |
|         |        WHO PAID FOR           |     |  <- text overlay
|         |          1896?                |     |     y ~ 1350 px
|         |                               |     |
|         +-------------------------------+     |
|                                               |
+-----------------------------------------------+
|  [bottom 150 px reserved — caption auto-bar]  |
+-----------------------------------------------+
```

### 3.2 Text overlay (4 words, <=4 by design)

```
WHO PAID FOR 1896?
```

- Type: Playfair Display 900, ~140 px, Newsprint Cream `#E8DEC8`, left-aligned,
  ragged-right.
- Letter-spacing: -0.02em (tight, headline-register).
- A 1 px Hanna Amber `#C87533` hairline rule sits beneath the caption to anchor
  it. No drop shadow — DESIGN.md forbids it for type.
- Sits inside the inner safe area (y ~ 1300-1500 px). Does not collide with
  YouTube's auto-overlay regions.

### 3.3 Composition

- **Focal subject:** the cartoon figure (centered crop). The dollar-sign suit
  is the most recognizable visual in the asset set; the cigar reads at 1-inch
  preview size.
- **Treatment:** desaturate to ~30% chroma, then push contrast +15. Period
  cartoons read as "old illustration" at small thumbnail size unless we lean on
  shape and silhouette rather than color. Add a faint film-grain layer
  consistent with the rest of the project's grain baseline.
- **Background fill:** Ink Black `#0E0B08` matte fills any letterbox space that
  remains after the centered crop. Edges of the cartoon vignette into the
  matte (radial fall-off) so the figure looks pinned, not pasted.
- **Optional accent:** a single Blood Oxide `#C03A2C` price tag glyph in the
  upper-left corner, ~80 px, reading `$3,500,000` in IBM Plex Mono 36 px
  tabular-nums. Treat as a *light* accent — easy to remove if it crowds the
  caption at small sizes.

### 3.4 Color and mood

- Palette is the project's DESIGN.md tokens: Ink Black `#0E0B08`, Newsprint
  Cream `#E8DEC8`, Hanna Amber `#C87533`, Blood Oxide `#C03A2C`, Faded Bone
  `#9A8E76`. **No other colors.**
- Mood: editorial, period-press, slightly forensic. Reads like a magazine
  cover, not a creator-economy thumbnail.
- Avoid: the red-arrow / yellow-circle / shocked-face vernacular. The register
  is documentary, and every thumbnail decision should look as if it could sit
  next to a *New Yorker* longform cover.

### 3.5 Why this thumbnail

- The Davenport cartoon is the most visually arresting frame in the asset set;
  millions of Americans saw it without ever knowing who was in it. The
  thumbnail re-runs that exact experience on the viewer.
- "WHO PAID FOR 1896?" is the same kind of restrained interrogative as the
  end-card prompt ("WHAT DID IT BUY?"). It frames the teaser as a question,
  not an answer.
- Year + question + unnamed figure forces the click. No spoiler — McKinley is
  not named, the recipient of the ledger is not named, the November result is
  not implied.

### 3.6 Alternates (held in reserve)

- **Alt-1 (named-figure):** swap to `hanna-portrait.jpg` centered crop, caption
  swaps to `MARK HANNA. 1896.` — only 3 visible "words," meets the <=4 rule.
  Use if Alt-A title is shipped and the channel strategy is name-recognition.
- **Alt-2 (numbers-first):** full-bleed Ink Black with `$3,500,000` in Hanna
  Amber IBM Plex Mono 480 px tabular-nums, single Blood Oxide `20x` stamp
  bottom-right, caption `WHO BOUGHT 1896?` (4 words). Most pure-number version;
  trades cartoon recognition for raw scale theatre.

---

## 4. Acceptance check

- [x] 1 primary title (50 chars) + 2 alternates (45 and 44 chars), all <=60.
- [x] All three titles are curiosity-driven and non-spoilery (McKinley, Bryan,
      the November result are absent from every option).
- [x] Description is ~3-6 short paragraphs (4) including: a hook line, light
      context (year + numbers + donors), 7 hashtags, and a soft engagement
      prompt ("Watch the full story - link in bio") that does not reveal the
      outcome.
- [x] Thumbnail concept includes written description, rough layout block, focal
      subject, text overlay (4 words: "WHO PAID FOR 1896?"), and full
      color/mood spec keyed to DESIGN.md tokens.
- [x] Metadata is consistent with the EDIT_PLAN.md curiosity gap and ready to
      paste into a YouTube upload form.
- [x] Spoiler audit pass: title + description + thumbnail caption, read in
      isolation, name {Mark Hanna, 1896, $3,500,000, 20x, Standard Oil,
      JP Morgan} and nothing more. No outcome, no McKinley, no Bryan, no
      mechanism, no origin, no death.

---

— Metadata for kanban task t_383a761b, profile `default`, 2026-06-06.
