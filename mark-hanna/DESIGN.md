# DESIGN.md — Mark Hanna Documentary

## Style Prompt

Gilded Age investigative documentary. Dark editorial. Newsprint meets political thriller. Heavy serif typography over textured cream and ink-black. Numbers and dates land like indictments. Period archival photography rendered with a desaturated, slightly sepia-shifted palette — never modernized, never colorized. The visuals carry the weight; the text does not shout.

Reference mood: HBO documentary cold opens × New York Review of Books layouts × old Treasury Department typography.

## Colors

- **Ink Black** — `#0E0B08` — primary background, deep base
- **Newsprint Cream** — `#E8DEC8` — primary text, light surfaces, archival paper
- **Hanna Amber** — `#C87533` — accents, money, power, the dollar-sign motif
- **Blood Oxide** — `#C03A2C` — emphasis on indictments, deaths, key numbers
- **Patina Green** — `#2F4A3A` — secondary accent (rare; old money, copper oxide)
- **Faded Bone** — `#9A8E76` — captions, secondary text, dates

Color roles:
- Backgrounds: Ink Black or deep textured cream
- Body text on dark: Newsprint Cream
- Body text on light: Ink Black
- Money / amounts / indictments: Hanna Amber
- Death dates / "20x" / "purchased": Blood Oxide
- Citations, dates, attributions: Faded Bone

## Typography

- **Display / Headlines** — `"Playfair Display", "Times New Roman", serif` — weights 700/900. Used for scene titles, indictment numbers, the Hanna name. Tight letter-spacing on large sizes (`-0.02em`).
- **Body / Narration emphasis** — `"Source Serif 4", "Georgia", serif` — weight 400/600. Quotes, longer text, captions.
- **Numbers / Metadata** — `"IBM Plex Mono", "Courier New", monospace` — weight 500. Dates, dollar amounts, vote totals, attributions. ALWAYS `font-variant-numeric: tabular-nums`.

Display text: 84-160px. Section titles: 56-84px. Body emphasis: 36-48px. Captions: 44-52px. Metadata/dates: 18-24px.

## Motion Character

- **Decisive, not bouncy.** Eases: `power3.out` for entrances, `power2.in` for exits, `expo.out` for indictment numbers landing.
- **Slow reveals.** Big numbers count up over 0.8-1.2s. Headlines fade-and-rise over 0.6-0.8s. Letter spacing tightens slightly on entrance (start at `0.05em`, end at `-0.02em`) for typographic drama.
- **No bounces, no elastic.** This is documentary, not advertising.
- **Ken Burns** on archival images: 8-15 second slow drift + 3-6% scale change. Direction matches narrative momentum (zoom-in for accusation, zoom-out for context).
- **Vignette + grain** are constant — film stock baseline, not effects.

## What NOT to Do

1. **No bright saturated colors.** No pure cyan, no pure red, no neon, no Material Design palette. Everything goes through the period filter.
2. **No bouncy / elastic eases.** Nothing should feel "fun." The energy is grim and precise.
3. **No emoji, no flat-design icons, no rounded corners on cards.** Sharp edges, hairline borders, period-appropriate ornamentation only.
4. **No colorized historical photos.** Sepia-and-cream tone treatment only. Original B&W is preferred over fake color.
5. **No center-aligned everything.** Real editorial layout uses asymmetry — left-aligned headlines, ragged right body, hanging numerals in margins.
6. **No "$3.5M" — write `$3,500,000`.** Big numbers SHOULD feel uncomfortable. Comma-separated, fully spelled out.

## Composition Grid

12-column grid on 1920×1080. Outer margin 96px. Gutter 32px. Headlines occupy columns 1-8 typically. Numbers and metadata hang in columns 10-12. Photographs fill bleed-edge or sit in 8-column blocks with hairline `1px solid #C87533` borders.
