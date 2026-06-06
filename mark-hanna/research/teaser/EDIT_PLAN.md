# Edit Plan — Mark Hanna Teaser Short

> Concrete cut plan for a vertical 9:16 (1080×1920) YouTube Short.
> Consumes [TEASER_BRIEF.md](TEASER_BRIEF.md) + [clips.json](clips.json) + the project's [DESIGN.md](../../DESIGN.md) + [research/music/PLAN.md](../music/PLAN.md).
> Specific enough for an editor to cut from directly. Curiosity gap is preserved end-to-end.

**Target runtime:** 40.0 s (36.05 s of narration clips + 4 s end card). Comfortably inside Shorts' 60 s ceiling.
**Source render:** `renders/mark-hanna-ep01-preview.mp4` (1920×1080 — must be reframed to 1080×1920).
**Source audio:** `assets/narration.wav` — extract by timecode per `clips.json`. Do **not** re-render TTS; the locked narration is the canonical voice.

---

## 1. The hook (0:00–0:03)

The hook has to do three things in three seconds:

1. **Pattern-interrupt.** Open on a single arresting cartoon, not on a title card. The dollar-sign suit is the most recognizable visual in the source set.
2. **Pose the mystery.** A pinned caption frames the entire teaser: *the cartoon you've seen, but never knew the name of.*
3. **Make the eye work.** Visual density (3 cartoons crossfading inside 3 seconds) signals "this was a sustained press campaign," priming the viewer for the scale claim that follows.

### 1.1 Hook spec

| Layer | 0.0 → 1.0 s | 1.0 → 2.0 s | 2.0 → 3.0 s |
|---|---|---|---|
| **Visual** | `cartoon-dollar-mark-hanna.jpg` — push-in 1.0 → 1.04 on cigar/dollar-sign suit. Vertical reframe: crop to centered figure, fill top/bottom with Ink Black `#0E0B08` matte. | Crossfade (300 ms) to `cartoon-shylock-hanna.jpg` — slight zoom continues. | Crossfade (300 ms) to `cartoon-boss-of-bosses.jpg` — settles. |
| **Audio (VO)** | clip 1 narration starts: *"The cartoon ran in every Hearst paper in America."* (0.04 → 3.08 s of `narration.wav`) | (continues) | (lands) |
| **Pinned caption** | **"THE CARTOON YOU'VE SEEN."** — Playfair Display 900, 96 px, Newsprint Cream `#E8DEC8`, lower-third on ragged-right alignment. Letter-spacing 0.05em → −0.02em over 600 ms. | Hold caption. | Caption swaps line 2: **"THE NAME YOU DON'T KNOW."** — same type, Hanna Amber `#C87533` for the second line. |
| **Sound design** | Single low sustained drone (Ink Black — see §4). −24 LUFS short-term. | Drone continues, faint 78 rpm vinyl crackle layer at −36 LUFS. | Drone continues. |

**Why this beats opening on the name or the money:** the strongest curiosity gap is a face you recognize without a label. Leading with `$3,500,000` would be louder but resolves the "what is this about" question too early; the audience would settle into "campaign finance video." The cartoon montage forces them to ask *who is this guy* — and we hold that question for 6 more seconds before naming him.

### 1.2 Hook alternates (held in reserve)

- **Alt-A — Lead with money.** Open on clip 6's `$3,500,000` count-up (0.0–2.0 s) + `20×` Blood Oxide stamp; cut to cartoon at 2.0–3.0 s. Use only if A/B testing on the channel shows numbers-first hooks outperform mystery-first hooks for this register. Default cut does **not** use this.
- **Alt-B — Lead with the closer.** Cold-open with `davenport-hanna-1896.jpg` freeze + caption *"HE HAD A LEDGER."* for 1.5 s, hard-cut to standard montage. Spoils the closing line; not recommended.

---

## 2. Timeline / shot list

All narration timecodes are **into `assets/narration.wav`**. Cut order is chronological with the source — preserves the original pacing curve. Total VO runtime is 36.05 s (sum of clip durations); the timeline below adds a 4 s end card → **40.0 s total**.

| Beat | T-in | T-out | Dur | Source VO range | Visual | Reframe (1080×1920) | On-screen text |
|---|---:|---:|---:|---:|---|---|---|
| 1 — Hook | 0.00 | 3.04 | 3.04 | 0.04 → 3.08 | Cartoon montage (see §1.1) | Centered crop on figure; Ink Black mattes top/bottom | Pinned 2-line caption (see §1.1) |
| 2 — Sustain | 3.04 | 6.24 | 3.20 | 8.36 → 11.56 | Crossfade `cartoon-shylock-hanna.jpg` → `cartoon-boss-of-bosses.jpg` (1.5 s each, 200 ms x-fade) | Same — vertical center crop | Lower-third caption: **"The caption changed every week."** then swap to **"The man did not."** Source Serif 4 56 px, Newsprint Cream |
| 3 — Name reveal | 6.24 | 7.99 | 1.75 | 11.56 → 13.31 | Hard cut to `hanna-portrait.jpg` on Ink Black | Portrait centered, top/bottom mattes; portrait fills middle 9-column band | Display: **"MARK HANNA"** Playfair Display 900, 144 px, Newsprint Cream. Letter-spacing 0.05em → −0.02em over 600 ms. Below: meta line *"1896"* in IBM Plex Mono 32 px, Faded Bone `#9A8E76`. |
| 4 — Year drop | 7.99 | 11.88 | 3.89 | 13.31 → 17.20 | Big numerals: **"1896"** filling frame | Numerals stack-vertical, 480 px tall; vignette closes through beat | Hold **"1896"** numerals — Blood Oxide `#C03A2C`, IBM Plex Mono 480 px, tabular-nums. expo.out entrance over 800 ms. |
| 5 — The claim | 11.88 | 15.96 | 4.08 | 17.20 → 21.28 | `newspaper-eveningstar-1896-01-11.jpg` | Vertical Ken Burns: pan **down a column** (not horizontal), 1.0 → 1.04 | Two-line lower-third building word-by-word with VO: **"A PRESIDENTIAL ELECTION / TURNED INTO A PURCHASE ORDER."** Source Serif 4 64 px, Newsprint Cream, ragged-right. |
| 6 — Numbers | 15.96 | 20.36 | 4.40 | 21.28 → 25.68 | Number graphic | Centered, vertical stack | Top: **"$3,500,000"** Hanna Amber `#C87533`, IBM Plex Mono 220 px, tabular-nums, count-up over 800 ms (0 → 3,500,000). On the word *"twenty"*: **"20×"** Blood Oxide stamp slams in (180 px, scale 1.2 → 1.0, 120 ms, drop shadow 0.2 opacity). Sub-caption: *"vs his opponent"* IBM Plex Mono 36 px, Faded Bone. |
| 7 — Donors | 20.36 | 26.22 | 5.86 | 30.82 → 36.68 | Stacked ledger lines on Ink Black | Vertical stack: lines fill columns 2-11, 320 px line-height | Lines type in left-aligned, IBM Plex Mono 64 px, Hanna Amber for org names, Blood Oxide for amounts: `STANDARD OIL ............ $250,000` then below `JP MORGAN ............ $250,000`. Hairline 1 px Hanna Amber rule between. **Total line stays blank** — no recipient. |
| 8 — One man | 26.22 | 30.14 | 3.92 | 36.68 → 40.60 | `convention-1888.jpg` push-in 1.0 → 1.06 | Crop to crowd density; the candidate figure is **deliberately not centered** — leave edge of frame, viewer can't fix on him | Lower-third: **"500,000 VOTERS / TRANSPORTED BY TRAIN."** Source Serif 4 60 px, Newsprint Cream. Sub-caption in Faded Bone: *"to shake one man's hand."* — *"one man"* in italics, no portrait shown. |
| 9 — The opposition | 30.14 | 34.68 | 4.54 | 44.36 → 48.90 | Newsprint paper texture only — **no portrait** | Full-bleed paper texture, faint film grain | Italic Source Serif 4 72 px, Faded Bone: *"a thirty-six year old preacher / who could move a crowd to tears."* Floating attribution in Plex Mono 24 px lower-right: *"— the opposition."* **No name shown.** |
| 10 — Closer | 34.68 | 36.05 | 1.37 | 48.90 → 50.27 | `davenport-hanna-1896.jpg` freeze | Centered crop on cartoon figure; vignette closes hard at end | Display lower-third: **"HANNA HAD A LEDGER."** Playfair Display 900, 88 px, Newsprint Cream. Vignette closes through final 600 ms; cut to black. |
| 11 — End card | 36.05 | 40.00 | 3.95 | (silent) | Static end card on Ink Black | — | See §5. |

**Audio assembly note for the editor:** narration timecodes are not contiguous — there are intentional jumps (clip 6 → clip 7 skips 25.68→30.82, clip 8 → clip 9 skips 40.60→44.36). At each jump, butt-cut the VO (no crossfade) and let the music + visual carry the transition. The skipped passages contain mechanism / origin material that's deliberately withheld (see §6).

### 2.1 Cumulative timing check

```
3.04 + 3.20 + 1.75 + 3.89 + 4.08 + 4.40 + 5.86 + 3.92 + 4.54 + 1.37 = 36.05 s VO
+ 3.95 s end card
= 40.00 s total → inside Shorts 60s ceiling, above the 30s floor. ✓
```

---

## 3. Caption / on-screen text plan (consolidated)

Every caption follows DESIGN.md tokens. Consolidated for the editor:

| Beat | Style class | Spec |
|---|---|---|
| 1, 2 (pinned hook + sustain) | `display.hook` | Playfair Display 900, 96 px display + 56 px sustain, Newsprint Cream `#E8DEC8`. Pinned across the cartoon montage. Second line of pinned caption swaps to Hanna Amber `#C87533` at 2.0 s. |
| 3 (name) | `display.name` | Playfair Display 900, 144 px, Newsprint Cream. Letter-spacing 0.05em → −0.02em over 600 ms. Sub-meta in IBM Plex Mono 32 px Faded Bone `#9A8E76`. |
| 4 (year) | `display.indictment` | IBM Plex Mono 480 px, Blood Oxide `#C03A2C`, tabular-nums. expo.out entrance 800 ms. |
| 5 (claim) | `body.editorial` | Source Serif 4 64 px, Newsprint Cream, ragged-right, two-line, types in word-by-word with VO. |
| 6 (money) | `display.money` | Hanna Amber `#C87533`, IBM Plex Mono 220 px, tabular-nums, count-up 800 ms. **20× stamp** in Blood Oxide 180 px on the word "twenty." |
| 7 (donors) | `body.ledger` | IBM Plex Mono 64 px. Org names Hanna Amber, amounts Blood Oxide, dot leaders Faded Bone. Hairline 1 px Hanna Amber rule between. |
| 8 (voters) | `body.editorial` | Source Serif 4 60 px Newsprint Cream + Faded Bone sub-caption with italics on "one man." |
| 9 (opposition) | `body.editorial.muted` | Italic Source Serif 4 72 px, Faded Bone. Plex Mono 24 px attribution. |
| 10 (closer) | `display.closer` | Playfair Display 900, 88 px, Newsprint Cream. |
| 11 (end card) | `display.endcard` | See §5. |

**Universal rules from DESIGN.md (not negotiable):**
- All numbers tabular-nums. Comma-separated, fully spelled out. **"$3,500,000"** never **"$3.5M"**.
- No center-aligned everything. Headlines left-aligned; numbers hang right.
- No emoji, no rounded corners, no bouncy eases. Decisive entrances (`power3.out`), hard exits (`power2.in`).
- Vignette + faint film grain are constant — film stock baseline, not effects.

**Vertical-format caption safe area:** keep all text inside the inner 1080×1620 box (top 150 px and bottom 150 px reserved for YouTube UI overlay, top-pinned channel handle, bottom captions auto-bar). Lower-thirds sit at y ≈ 1300 px.

---

## 4. Music direction

This teaser is the canonical short-form case from [research/music/PLAN.md](../music/PLAN.md). Compress the full doc's score system into 40 seconds, but obey the same five high-confidence rules: silence is structural, motif reuse beats variety, score function not timecode, voice is sovereign, restraint reads as honesty.

### 4.1 Cue map

| T-window | Cue | Texture | Level vs voice |
|---|---|---|---|
| 0:00 → 0:03 | **Drone-floor only** (no melody) | Single sustained low drone (sub + faint vinyl crackle layer). No rhythm yet. | bed at −27 LUFS short-term, −12 LU below voice |
| 0:03 → 0:06 | **Cue A enters** ("Mechanism") | Sparse parlor piano ostinato + soft military snare brushed pulse. **No melodic peak.** | bed at −28 LUFS, ducked under VO |
| 0:06 → 0:08 | Cue A holds; brief lift on name reveal | Same texture, +2 dB swell on the reveal beat | bed at −26 LUFS for the swell |
| 0:08 → 0:12 | Cue A continues under "1896" numerals | Slight fattening — add low-string drone under the parlor piano | bed at −27 LUFS |
| 0:12 → 0:20 | Cue A continues through claim + numbers | Hold texture, no dynamic change | bed at −28 LUFS |
| 0:20 → 0:26 | Cue A thins under donors ledger | Drop snare; piano only, single-line | bed at −29 LUFS |
| 0:26 → 0:30 | **Cue B enters** ("Weight") under "one man" beat | Single-line minor cornet melody enters quietly under Cue A piano; Cue A piano fades behind it | bed at −28 LUFS |
| 0:30 → 0:33 | Cue B alone over opposition tease | Cornet single-line, no accompaniment | bed at −28 LUFS |
| **0:33 → 0:34.5** | **FULL DROP — silence** (1.5 s) | Music out completely. Room tone + faint vinyl floor only. | — |
| **0:34.5 → 0:36** | "Hanna had a ledger." plays **DRY** | No music; closer line is the silent reveal. | — |
| 0:36 → 0:40 | **Cue C** ("Coda") under end card | Single low piano note → 3-note descending fragment of Cue A's contour, reharmonized minor. Slow. | up to −20 LUFS (no VO present); fade to silence at 0:39.5 |

**Total unscored runtime:** 0:00–0:03 (drone-floor counts as scored), 0:33–0:36 = 4.5 s of full-silence, plus 0:36.5–0:40 fade-out tail. Within the spirit of the music plan's 40–60% unscored target — for a 40 s teaser that target relaxes; the silent reveal at 0:33 is the load-bearing beat.

### 4.2 Sourcing (in audition order)

Per [research/music/PLAN.md §3.1](../music/PLAN.md), period public-domain first, AI second, named CC-BY third. **No generic royalty-free libraries.**

1. **Library of Congress National Jukebox** — search *"1896 march"*, *"1898 parlor piano"*, *"Sousa Liberty Bell 1893"*. Pull recording (not just score) PD status. Likely role: **Cue A "Mechanism" base material.**
2. **IMSLP (recordings tab only)** — Sousa marches in PD recordings, period band arrangements. Likely role: **Cue A variation.**
3. **Musopen** — minor-mode parlor piano, muted cornet. Likely role: **Cue B "Weight" material.**
4. **Internet Archive (78rpm Project)** — *"1890s band"*, *"early cornet"*, *"parlor piano roll"*. Period grain texture.
5. **Suno Pro (logged)** — fallback for Cue B if no PD muted-cornet single-line found. Prompt: *"1890s muted cornet single line, no accompaniment, slow, mournful, instrumental, no vocals, no drums, public-domain feel."* **Log mandatory** in `assets/MUSIC_LICENSES.md` (prompt + model + generation date + paid-tier TOS screenshot).
6. **Drone-floor (0:00–0:03)** — synthesise ourselves: 50 Hz sine + low-pass-filtered pink noise + faint 78 rpm vinyl crackle layer (`Internet Archive 78rpm Project` for PD crackle bed). −24 LUFS short-term. **Not** music; counts as sound design.

### 4.3 Mix targets (verbatim from music plan §3.4)

- **Master integrated:** −14 LUFS.
- **Voice short-term:** −16 LUFS.
- **Music bed when VO present:** −27 to −28 LUFS short-term (~12 LU below voice).
- **Music in pure-VO-absent moments (end card):** ducks back to −20 LUFS.
- **Duck depth:** −8 dB for sparse cues (default for this teaser); −12 dB if a denser arrangement is auditioned.
- **Manual breath swell:** +2–4 dB in the inter-sentence gap on the name reveal (0:07.5) and on the donors line break (0:23). Flat ducking elsewhere.
- **EQ pocket:** −3 dB carve at 1–4 kHz on the music bus to clear consonants.
- **Voice EQ:** HPF ~80 Hz, modest 2–4 kHz presence boost.
- **Cuts at musical phrase boundaries**; crossfades near zero crossings before transients.

### 4.4 The silent reveal (the one rule that cannot move)

The 1.5 s music-drop at 0:33 → 0:34.5 followed by the dry "Hanna had a ledger." at 0:34.5 → 0:36 is the load-bearing beat of the whole teaser. It's the single point where every reviewer in the music plan converged: *score from silence outward; the most important sentence in each section plays dry.*

If only one music recommendation survives editorial pressure, **it's this one.** Do not let a "I want to hear something here" instinct fill the silence with a pad swell. The silence is the cue.

---

## 5. End card / closing prompt (0:36 → 0:40)

A static frame on Ink Black `#0E0B08`. No moving graphics. Cue C plays under it.

**Layout (top to bottom on 1080×1920):**

```
                    [y ≈ 600 px]
        He had a ledger.                      ← Source Serif 4 italic 72 px
                                                Newsprint Cream #E8DEC8
                                                left-aligned with 96 px margin

                    [y ≈ 800 px]
        WHAT DID IT BUY?                      ← Playfair Display 900, 120 px
                                                Hanna Amber #C87533
                                                left-aligned, ragged-right

                    [y ≈ 1100 px]
        ──────────────────────────             ← 1 px Faded Bone hairline rule

                    [y ≈ 1200 px]
        WATCH THE FULL STORY                  ← IBM Plex Mono 36 px
                                                Faded Bone #9A8E76
                                                tracking 0.18em

                    [y ≈ 1280 px]
        ▶ link in bio                         ← IBM Plex Mono 28 px
                                                Faded Bone
```

**Why this nudges engagement without spoiling:**
- Calls back to the closer line ("He had a ledger") so the viewer hears the question they're already asking.
- "WHAT DID IT BUY?" reframes the entire teaser as setup — McKinley's name is never spoken, the election outcome never stated. The viewer can't resolve the question by Googling "Mark Hanna 1896" without committing to actually reading the answer.
- "WATCH THE FULL STORY" + "link in bio" is conventional Shorts CTA grammar. Don't overthink it. No emoji, no exclamation marks (DESIGN.md §5).
- No subscribe-button graphic. The doc's register is editorial, not creator-economy.

**Closing prompt alternates** (pick during locked-cut review):

- **Alt-A** (if the channel's CTA convention is questions): "WHO DID HE MAKE PRESIDENT?" — slightly more pointed; risks viewers Googling forward to McKinley.
- **Alt-B** (more restrained): "1896 / THE LEDGER WON." — ditches the question entirely; lets the audience decide whether to chase it. This is the most documentary-register option.

**Recommendation:** ship the default ("WHAT DID IT BUY?") for the first upload. If retention drops sharply at 0:34, try Alt-A. If retention is fine but click-through to the long doc is weak, try Alt-B.

---

## 6. What's withheld (and why)

Audited beat-by-beat against the teaser brief. Every withheld item is structural, not accidental.

| Withheld | Where it could leak | Mitigation |
|---|---|---|
| **Election outcome** ("the ledger won") | Could be implied by the donors clip (people assume corporate money wins). | Closer line stops at *"Hanna had a ledger."* — no verb, no resolution. |
| **William McKinley** (the candidate Hanna manufactured) | Clip 8's "one man" is McKinley. | Visual deliberately doesn't center the candidate figure in `convention-1888.jpg`; caption italicizes "one man" but never names him. |
| **William Jennings Bryan** | Clip 9 references him as "thirty-six year old preacher." | No portrait shown; floating attribution reads *"— the opposition"*; viewer cannot search forward to the November result with the information given. |
| **Hanna's Cleveland origin / Rhodes marriage / coal-iron empire** | Would answer "how did one man have that money to spend." | Origin clips (52.36 → 55.48 *"He wasn't born with money. He was born in a grocery."*) are held in reserve — not in this cut. |
| **Rockefeller as college classmate** | Would explain Standard Oil's $250,000. | Mechanism passages (banks at 0.25% of capital, 1888 convention) are skipped in the VO cut (clip 6→7 jump). |
| **Hanna's death and legacy** | Would close the story. | No 1904, no obituary, no successor mention. Teaser stops on the ledger. |

**Spoiler audit pass:** read the complete on-screen-text + caption stream in isolation (no audio, no visuals). Result: viewer learns *Mark Hanna, 1896, $3,500,000, 20×, Standard Oil $250,000, JP Morgan $250,000, 500,000 voters, a thirty-six year old preacher, ledger.* No outcome, no candidate, no mechanism, no origin, no death. **Pass.**

---

## 7. Editor handoff notes

### 7.1 Vertical reframing (1920×1080 → 1080×1920)

The source render is 16:9. Every clip needs an active reframe to 9:16. **Do not** just letterbox or center-crop blindly:

- **Archival photos** (`hanna-portrait.jpg`, `cartoon-*.jpg`, `davenport-hanna-1896.jpg`) — crop to centered subject (figure, face). Allow ~30% black bleed top and bottom for caption space (lower-third) and YouTube UI safe area (upper top ~150 px reserved for channel-handle overlay).
- **Newspaper** (`newspaper-eveningstar-1896-01-11.jpg`) — pivot Ken Burns from horizontal pan to vertical drift down a single column of text. Pick a column with visible Hanna-era headlines if possible; the texture is what matters, not legibility.
- **Convention** (`convention-1888.jpg`) — crop to crowd density, **deliberately off-center the candidate figure** (top-left or top-right third). The "one man" caption sits lower-third over the crowd.
- **Number / ledger graphics** (clips 4, 6, 7) — recompose vertically. "1896" stacks (4-8-9-6 in column form, two digits per line); ledger lines stack natively. Hanna Amber/Blood Oxide tokens unchanged.

### 7.2 Audio extraction recipes

```bash
# Working directory:
cd hyperframe-test/mark-hanna

# Concat the 10 narration ranges into a single teaser_vo.wav with butt-cuts at jumps.
# Generate the input list:
cat > /tmp/teaser_concat.txt <<'EOF'
file 'assets/narration.wav'
inpoint 0.04
outpoint 3.08
file 'assets/narration.wav'
inpoint 8.36
outpoint 11.56
file 'assets/narration.wav'
inpoint 11.56
outpoint 13.31
file 'assets/narration.wav'
inpoint 13.31
outpoint 17.20
file 'assets/narration.wav'
inpoint 17.20
outpoint 21.28
file 'assets/narration.wav'
inpoint 21.28
outpoint 25.68
file 'assets/narration.wav'
inpoint 30.82
outpoint 36.68
file 'assets/narration.wav'
inpoint 36.68
outpoint 40.60
file 'assets/narration.wav'
inpoint 44.36
outpoint 48.90
file 'assets/narration.wav'
inpoint 48.90
outpoint 50.27
EOF

# ffmpeg concat-demuxer build:
ffmpeg -f concat -safe 0 -i /tmp/teaser_concat.txt -c copy /tmp/teaser_vo.wav

# Verify total duration ≈ 36.05 s:
ffprobe -v error -show_entries format=duration -of csv=p=0 /tmp/teaser_vo.wav
```

### 7.3 Render target

- **Container:** MP4
- **Video:** H.264, yuv420p, CRF 18, preset slow, 1080×1920 @ 30 fps (or 60 fps if source allows)
- **Audio:** AAC-LC, 192 kbps, 48 kHz stereo
- **Color:** BT.709
- **Output path convention:** `renders/teaser-shorts-v01.mp4` (then `-v02`, etc. for revisions). Do **not** overwrite previous renders.

### 7.4 Caption-timing safety (project-specific gotcha)

This project has had caption/audio drift before (see prior task `t_90813864` — caption-groups built on early narration.wav got drifted by later splices, accumulating up to 1.52 s by 0:50 of source narration). For the teaser:

- **Do not reuse `assets/caption-groups.json` directly.** That timing applies to the long doc's full narration timeline, not the spliced teaser.
- **Re-time captions against `/tmp/teaser_vo.wav`** (the freshly-concatenated teaser narration). Word-level alignment should regenerate from scratch — the simplest path is a single Whisper-large-v3 pass over `teaser_vo.wav` and use those timestamps.
- **Validate** every caption appears on screen during its corresponding word ±100 ms. Drift this short of a teaser is unforgiving.

### 7.5 Acceptance checklist (for the next task — `t_2e612a41`)

- [ ] Final MP4 is 1080×1920, 30+ fps, H.264 + AAC, ≤60 s, ≥30 s.
- [ ] Hook (0:00–0:03) is the cartoon montage + pinned 2-line caption — NOT a title card.
- [ ] All 10 narration clips concatenate cleanly with butt-cuts at the timecode jumps.
- [ ] Captions/on-screen text follow DESIGN.md tokens (Playfair Display + Source Serif 4 + IBM Plex Mono; Ink Black / Newsprint Cream / Hanna Amber / Blood Oxide / Faded Bone palette only).
- [ ] Music bed sits ~12 LU below voice during VO; goes fully silent 0:33 → 0:34.5; "Hanna had a ledger." plays dry.
- [ ] End card at 0:36–0:40 calls back to the closer ("He had a ledger. WHAT DID IT BUY?") with "WATCH THE FULL STORY" CTA — no McKinley, no Bryan, no November result.
- [ ] Spoiler audit (§6) passes: text-only stream names {Mark Hanna, 1896, $3,500,000, 20×, Standard Oil $250,000, JP Morgan $250,000, 500,000 voters, thirty-six year old preacher, ledger} and nothing else.
- [ ] Music cues are sourced per [research/music/PLAN.md §3.1](../music/PLAN.md) (period-PD or AI-generated logged in `assets/MUSIC_LICENSES.md`); **no Epidemic Sound, Artlist, Soundstripe, Musicbed.**
- [ ] Master integrated −14 LUFS; voice short-term −16 LUFS; bed −27 to −28 LUFS short-term during VO.
- [ ] Output saved to `renders/teaser-shorts-v01.mp4` (or higher version), pushed to git, **NOT uploaded to YouTube** (that's explicitly out of scope per the root task).

---

— Edit plan by `default` profile, kanban task `t_36b986c7`, 2026-06-06.
