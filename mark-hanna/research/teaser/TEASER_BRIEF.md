# Teaser Compilation Brief — Mark Hanna Shorts

**Target:** YouTube Shorts, vertical 1080x1920, ~35–45s
**Source:** owned production at `hyperframe-test/mark-hanna/` (270s preview, narration.wav + transcript.json + caption-groups.json + archival image set)
**Audience handoff:** the long documentary (or ep01) — Short hooks, full doc resolves.

---

## Theme statement

**"The cartoon you've seen, but never knew the name of."**

The hook leans on the Davenport / Hearst political cartoons of the 1890s — a fat man in a dollar-sign suit, smoking a cigar — that millions of Americans saw weekly without ever being told who he actually was. The teaser names him (Mark Hanna), then hammers a rapid-fire ledger of *uncomfortable numbers* from the 1896 election (3.5 million dollars, 20× the opposition, Standard Oil + JP Morgan paying in, half a million voters bussed in, 200 million pieces of mail) — and stops on the dry line "**Hanna had a ledger.**" before the audience learns *what the ledger did*, *who he made president*, *why*, or *how he died*. The curiosity gap is structural: the teaser shows scale (money, mechanics, scope) while withholding outcome (the ledger won), motive (kingmaking McKinley, the Rockefeller orbit, the Cleveland coal-iron empire that financed it), and consequence (his obituary, his successors, what he invented for American politics). A viewer leaves knowing *something gigantic happened in 1896* and *one man ran it like a balance sheet* — and not what that means.

## What's withheld (and why)

- **The election outcome** — "And when November came, the ledger won." — punchline of the cold open. Cut.
- **William McKinley** — never named in the teaser. The full doc makes him the second main character; here, he's the missing piece.
- **William Jennings Bryan** — referenced obliquely as "a thirty-six year old preacher." Naming him would let viewers Google the result in 4 seconds.
- **Hanna's origin story** — Cleveland, the Rhodes marriage, coal-and-iron, Rockefeller as a college classmate. All of it is the *answer* to "how did one man have that kind of money to spend on politics." Removed entirely.
- **The mechanism** — the assessment system (banks at 0.25% of capital), the 1888 convention scene where he "found his president." Showing the mechanism collapses the mystery.
- **His death and legacy** — the larger doc closes on Hanna's 1904 death and what he invented for the next century of American politics. Not in the teaser.

What the teaser *gives away*: his name, the year, the totals, two corporate donor names. These are enough to feel the weight without resolving the story.

## Source licensing

All footage and audio are user-owned (the documentary preview at `hyperframe-test/mark-hanna/`). All archival photographs in `assets/` are pre-1929 and public-domain in the United States by age (Hanna died 1904; the cartoons are 1896–1900 Hearst political cartoons). Narration is the user's own TTS render. No third-party clips required.

---

## Candidate clip list (10 clips, ~37s)

Timecodes are from the 270-second preview narration (`assets/narration.wav`). Each clip pairs a narration beat with a visual cue from `assets/`.

| # | Source range | Narration beat | Visual cue | Hint without spoiler |
|---|---|---|---|---|
| 1 | 0.04 – 3.08 (3.04s) | "The cartoon ran in every Hearst paper in America." | `cartoon-dollar-mark-hanna.jpg` — slow push-in on dollar-sign suit | Establishes the visual icon; the *man* is unnamed. |
| 2 | 8.36 – 11.56 (3.20s) | "The caption changed every week. The man did not." | Crossfade `cartoon-shylock-hanna.jpg` → `cartoon-boss-of-bosses.jpg` | Tells viewers there was a campaign of cartoons — but not why. |
| 3 | 11.56 – 13.31 (1.75s) | "His name was Mark Hanna." | Hard cut to `hanna-portrait.jpg` (Ink-Black background, name in Playfair Display) | Name reveal — feels like an indictment, gives no context. |
| 4 | 13.31 – 17.20 (3.89s) | "And in eighteen ninety-six, he did something no one had ever done at that scale." | "**1896**" Blood Oxide numerals filling frame (motion graphic from existing DESIGN.md tokens) | Year drop + scale claim, no description of *what*. |
| 5 | 17.20 – 21.28 (4.08s) | "He turned the American presidential election into a corporate purchase order." | `newspaper-eveningstar-1896-01-11.jpg` slow Ken Burns pan | Names the genre of crime; not who paid, won, or lost. |
| 6 | 21.28 – 25.68 (4.40s) | "Three and a half million dollars raised. Twenty times what his opponent spent." | "**$3,500,000**" Hanna Amber count-up + "**20×**" Blood Oxide stamp | Pure number theatre. Opponent unnamed. |
| 7 | 30.82 – 36.68 (5.86s) | "Standard Oil, two hundred and fifty thousand dollars. JP Morgan, two hundred and fifty thousand dollars." | Stacked ledger lines: "STANDARD OIL — $250,000" / "JP MORGAN — $250,000" in IBM Plex Mono | Names the donors, hides the recipient and the use of funds. |
| 8 | 36.68 – 40.60 (3.92s) | "Half a million voters, transported by train, to shake one man's hand." | `convention-1888.jpg` Ken Burns push-in | The "one man" is *deliberately not shown* — it's not Hanna. |
| 9 | 44.36 – 48.90 (4.54s) | "The opposition had a thirty-six year old preacher who could move a crowd to tears." | Newsprint paper texture only, no portrait | Bryan unnamed; viewers can't Google forward to the result. |
| 10 | 48.90 – 50.27 (1.37s) — **HARD STOP** | "Hanna had a ledger." | `davenport-hanna-1896.jpg` (Davenport cartoon) freeze-frame, vignette closes | Closes on the *instrument*, not the *outcome*. |

**Total cut length:** ~36.0s before pacing trims. Adding a 2–3s closing title card ("WATCH THE FULL STORY") brings the runtime to ~38–40s — comfortably inside Shorts' 60s ceiling.

### Optional alternates (held in reserve, not in the cut)

- **25.68 – 28.44** "Banks assessed at a quarter of a percent of capital." — too mechanism-revealing for a teaser; saved for the long doc.
- **40.60 – 44.36** "Two hundred million pieces of campaign literature, printed and mailed." — strong number, swap in if clip 9 feels weak.
- **52.36 – 55.48** "He wasn't born with money. He was born in a grocery." — origin-story; explicitly withheld per theme.

---

## Asset locations (already on disk, no fetch needed)

```
hyperframe-test/mark-hanna/
├── assets/
│   ├── narration.wav                          # full 270s render — extract via ffmpeg -ss/-t
│   ├── caption-groups.json                    # word-group timings for caption overlays
│   ├── cartoon-dollar-mark-hanna.jpg          # clip 1 visual
│   ├── cartoon-shylock-hanna.jpg              # clip 2a
│   ├── cartoon-boss-of-bosses.jpg             # clip 2b
│   ├── hanna-portrait.jpg                     # clip 3
│   ├── newspaper-eveningstar-1896-01-11.jpg   # clip 5
│   ├── convention-1888.jpg                    # clip 8
│   └── davenport-hanna-1896.jpg               # clip 10 closer
└── renders/
    └── mark-hanna-ep01-preview.mp4            # source render — clip extraction by timecode
```

## How to extract (handoff for the editor / next kanban task)

```bash
# Example: extract clip 1 audio (0.04 – 3.08s)
cd hyperframe-test/mark-hanna
ffmpeg -ss 0.04 -to 3.08 -i assets/narration.wav -c copy /tmp/teaser_clip01_audio.wav

# Example: extract clip 10 with audio + still image (still-frame Ken Burns)
ffmpeg -loop 1 -t 1.37 -i assets/davenport-hanna-1896.jpg \
       -ss 48.90 -to 50.27 -i assets/narration.wav \
       -c:v libx264 -c:a aac -shortest /tmp/teaser_clip10.mp4
```

The next kanban task (`t_36b986c7` — edit plan) should consume this brief and produce the ordered timeline + on-screen text plan + music direction.
