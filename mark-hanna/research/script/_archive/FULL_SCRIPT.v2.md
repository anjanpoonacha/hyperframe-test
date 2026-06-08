# THE LEDGER — full-scale hyperframe video script (v2.1)

> **v2.1 changelog (2026-06-07, post-MACI two-agent review pass):**
> Two independent reviewers (delegated tasks) read the locked preview narration + STYLE.md + v2 in parallel and converged on TWEAK-AND-SHIP. Seven surgical edits applied this pass:
> 1. **Scene 8 (Thesis)** — removed 4 em-dashes; restored preview-voice commas + "where the money went" (was "where it went"). Beats now in [BEAT] markers, not dashes.
> 2. **Scene 10 (Panic)** — replaced "before the kingmaker could make a king" alliteration with date anchor: "In February eighteen ninety-three, McKinley nearly went bankrupt." Smoothed "Knew, only later — who had paid" → "He knew, only later, who had paid."
> 3. **Scene 12 (Front Porch)** — split 38-word `because…and because…` compound into 3 preview-style fragments.
> 4. **Scene 13 (Cross of Gold)** — trimmed editorial "silver-tongue / political quiet" → "one speech, two thousand words long, had broken thirty-six years of party silence."
> 5. **Scene 16 (Senator/Cowboy)** — rewrote "He is, at last, what he set out to be: a senator who…" into witness voice. Rewrote "Mark Hanna — who has watched men more carefully…" as declaratives. Added `<!-- noqa: STYLE -->` on Hanna's documented "madman" rhetorical question (Croly biography source).
> 6. **Scene 17 (Buffalo)** — converted to past tense throughout (preview is uniformly past tense across 97 lines; v2 had drifted to historic-present at the climax). Removed subject-verb em-dashes ("A young man — steps forward" → "A young man stepped forward"). Softened "goes through the stomach" → "struck the stomach" for the CTV/female-44 demo.
> 7. **Scene 18 (Typhoid)** — converted to past tense. Replaced em-dash-before-date ("— in nineteen oh four") with Date Anchor transition.
>
> **v2 base changelog (preserved):**
> - **Scene 8 (Thesis)** — kept duration but broke the long center sentence into 3 chunks with beats so the philosophical pivot lands instead of blurting.
> - **Scene 10 (Panic) — FACTUAL FIX.** v1 had McKinley writing *"I am a beggar."* That phrase has no primary-source citation; the documented historical record (Beckley, Ohio History 69, 1960) is the OPPOSITE — McKinley refused to be a beggar and Hanna raised the $130k *without his knowledge*. v2 corrects the inversion.
> - **Scene 17 (Buffalo)** — expanded from 60 s → 95 s. Added held silence after "two shots." Added the documented detail that the first round caught a coat button. Czolgosz "of Cleveland" tag removed (he was born in Detroit).
> - **Scene 18 (Hanna's death)** — expanded from 30 s → 50 s. Added Lafayette Square location, "sixty-six years old" landed with a beat, and the documented "*That damn cowboy is President of the United States*" pull-quote on screen.
> - **Runtime** — v1's 24:00 spec dropped. Per CHANNEL.md §3 (data-backed): runtime sweet spot 35 min, range 22–55 min. v2.1 measured once rendered.
> - **Voice** — `bm_george` at default speed (Kokoro). Locked from yesterday's preview (CHANNEL.md's older AndrewNeural reference superseded by user direction).

**Working title:** *The Ledger — How Mark Hanna Bought the American Presidency (and Invented the Rest)*
**Channel:** @AmericanAudacity (long-form, 22–55 min)
**Runtime budget:** 24–35 min (per M16, REBUILD.md). No fixed target. v2 expansion of scenes 17 + 18 grew the script ~65 s past v1's ~24:00 spot — actual runtime determined by the rendered TTS, not a target.
**Voice:** Kokoro `bm_george` at default speed (no `--speed` flag, no atempo post-processing). M1.
**Aspect:** 1920×1080, 16:9 (long-form base composition; not the 9:16 shorts grid)
**Reference baseline:** the 5-minute preview at `hyperframe-test/mark-hanna/` ends at the 1888 McKinley handshake. This script *opens* with that same hook (deliberately — the preview is the trailer for this), then expands forward and outward to cover the 1896 mechanics, the assassination, the Roosevelt accident, and Hanna's death. Every line of the preview's 97-line narration is reused verbatim or near-verbatim inside this document, embedded in its proper context — so the existing `narration.wav` clips can be re-used as splice-grade source where it makes sense.

---

## 1. Logline

> In 1896 a Cleveland coal-and-iron broker raised three and a half million dollars, ran a presidential campaign like a balance sheet, and put the man he wanted in the White House. Eight years later he was dead — and every American election since has been run on his template.

Single-sentence sell: *the man you've seen in a thousand political cartoons and never been told the name of, and the system he built that outlived him by a hundred and twenty years.*

---

## 2. Character bios (12 — each carries narrative weight)

Every character below has a structural job. No filler.

### Principal (3)

**1. Marcus Alonzo "Mark" Hanna (1837–1904).** Protagonist. The operator who decides money should choose the president. Story arc: grocer's son → coal-and-iron broker → kingmaker → senator → corpse. *Function:* protagonist; the agent of the thesis.

**2. William McKinley (1843–1901).** The candidate. A Civil-War major from Canton, Ohio, with a wife so chronically ill he refused to leave Canton to campaign. Hanna's chosen vessel — chosen *because* he was decent, *because* he was loyal, *because* he was visibly someone you'd want to vote for. Story arc: dark-horse refusal at the 1888 convention → near-bankruptcy in the 1893 Panic → front-porch presidency → Buffalo. *Function:* the product Hanna sells; the human face of the ledger.

**3. William Jennings Bryan (1860–1925).** The antagonist. A 36-year-old Nebraska congressman who walks into the 1896 Democratic convention unknown and walks out the nominee on the strength of one speech. The "Cross of Gold" populist; a preacher who could move a crowd to tears. *Function:* the world Hanna had to outspend; the case for what almost happened.

### Supporting (5)

**4. John D. Rockefeller (1839–1937).** Hanna's college classmate at Western Reserve in 1852. Quiet, awkward, will grow up to control 90% of American oil refining. Donates $250,000 to the 1896 effort. *Function:* the corporate America Hanna packages and sells; the line connecting the school bench to the campaign chest.

**5. Daniel P. Rhodes (1814–1875).** Hanna's father-in-law. Cleveland coal-and-iron magnate. The man who hands Hanna a place inside the industrial order. *Function:* the door; without Rhodes, no chokepoint, no leverage, no campaign.

**6. Charlotte Augusta Rhodes Hanna (1840–1924).** Wife. Daughter of Rhodes. The single human relationship in Hanna's life that the cameras can't reduce to a transaction — and the entry credential that lets Cleveland's ruling families accept him. *Function:* one emotional anchor; the proof Hanna had a private life worth defending.

**7. John Sherman (1823–1900).** Ohio senator, Treasury veteran. Hanna's *first* candidate — the establishment choice Hanna champions at the 1888 Republican convention, and loses with. *Function:* the failure that teaches Hanna what kind of man wins; the dry run for McKinley.

**8. Theodore Roosevelt (1858–1919).** The wildcard. New York governor, war hero, reformer; the man Hanna loathes. Forced onto the 1900 ticket as VP because the New York machine wants him out of state, and the vice-presidency in 1900 looks like a coffin. Hanna says: *"Don't any of you realize there's only one life between this madman and the Presidency?"* They don't listen. *Function:* the unintended consequence; the man whose accidental presidency ends Hanna's project before Hanna himself dies.

### Pivotal cameo (3)

**9. Ida Saxton McKinley (1847–1907).** McKinley's wife. Epileptic, often bedridden; the reason McKinley campaigns from his front porch in Canton instead of touring. Her seizures are hidden from the public; McKinley quietly drapes a handkerchief over her face when one comes during a state dinner. *Function:* the human cost the campaign engineering protects; she explains *why* the front-porch campaign was personal as well as strategic.

**10. Garret A. Hobart (1844–1899).** McKinley's first VP. Dies in office in November 1899. The vacancy he leaves is the seat Roosevelt is shoved into. *Function:* the small absence that becomes the largest accident in the story.

**11. Leon Czolgosz (1873–1901).** Anarchist; the bullet at the Pan-American Exposition in Buffalo, September 6, 1901. Never named more than once. *Function:* the random event the ledger could not budget for.

### Collective (1)

**12. The American Voter — circa 1896.** Not a character we name, but a presence we draw: 13.9 million ballots cast, 51% for McKinley, 47% for Bryan; 200 million pieces of campaign mail received per voter on average ~14 pieces; half a million transported by railroad to shake McKinley's hand on the front porch. *Function:* the mass Hanna learned to model as a line item; the "we" the system was built to manage.

---

## 3. Beat sheet — engagement-aware (24 minutes)

Engagement-dip placement is informed by long-form retention data: drop points cluster at ~0:45 (hook test), ~3:30 (first act-break), ~5–6 minutes (curiosity exhaustion if the story stops paying), ~10–11 (mid-doc fatigue), ~15–16 (third-act lull), ~20 (pre-climax patience), and ~22 (just-before-end check-out). Each dip gets a *delivery moment*: a number, a twist, an emotional hit, or a sensory beat the eye and ear can't ignore.

| Time | Beat | Type | Delivery |
|---|---|---|---|
| 0:00 | Cold open: the cartoon | sensory hook | Slow push-in on Davenport "dollar-suit" cartoon; no narration for 4 seconds. |
| 0:08 | "The cartoon ran in every Hearst paper in America." | establishing line | — |
| 0:45 | **HOOK REINFORCE.** "His name was Mark Hanna." | name drop | Hard cut. Portrait. Playfair Display 160 px. |
| 1:00 | The 1896 claim | thesis | "He did something no one had ever done at that scale." |
| 2:30 | **PAYOFF #1.** "$3,500,000 raised. 20× the opposition." | number theatre | Blood Oxide count-up + 20× stamp. |
| 3:30 | **ACT BREAK.** "To understand how — we go back fifty-nine years." | structural | Ken Burns wipe to New Lisbon. |
| 4:00 | New Lisbon, Ohio. 1837. The grocery. | origin | Sepia archival. |
| 5:00 | **SENSORY DELIVERY.** Western Reserve, 1852. Rockefeller classmate intro. | twist | The boy at the next desk. Half the camera is on Rockefeller. |
| 6:00 | "The real education was in the price of things." | thesis-reinforce | Hanna leaves school. |
| 7:30 | **EMOTIONAL ANCHOR.** Charlotte Rhodes. The wedding. | human beat | One image, held long. The only love beat in the film. |
| 8:30 | Daniel Rhodes hands him coal-and-iron. | inheritance | — |
| 9:00 | **ACT BREAK.** Cleveland, 1880. Chokepoint visualization. | sensory | Map: Lake Erie ore boats, Pittsburgh mills, the broker in the middle. |
| 10:00 | **EMOTIONAL HIT.** "When he walked into a room, the room changed temperature." | character | Single sustained shot of Hanna's portrait, vignette tightens. |
| 10:30 | "Money was the second most powerful thing in America." | thesis pivot | Reveal: "The most powerful thing was who decided where the money went." |
| 11:30 | 1888 Republican Convention. Chicago. | scene | Wide on convention floor. |
| 12:30 | Sherman peaks at 229 votes, then bleeds out. | mechanism | Vote tally crawl. |
| 13:00 | **EMOTIONAL ANCHOR #2.** McKinley refuses the dark-horse pitch. | character | "That kind of loyalty was almost extinct." |
| 14:00 | "He had just found his president." | turn | Hanna walks across the floor. |
| 14:30 | The 1893 Panic. McKinley nearly bankrupts on a co-signed bond. | crisis | Newspaper headline. |
| 15:30 | Hanna engineers the rescue. Quietly. | mechanism | Ledger entries. |
| 16:00 | **PAYOFF #2 — THE MECHANISM.** Assessment system explained. | reveal | Banks: ¼% of capital. Railroads: shaken down personally. The math is on screen. |
| 17:00 | Standard Oil — $250,000. JP Morgan — $250,000. | ledger | IBM Plex Mono lines, Hanna Amber. |
| 17:45 | The Canton front-porch campaign. | scene | Half a million people delivered to McKinley's lawn. |
| 18:30 | **TENSION.** Bryan's tour. 18,000 miles by rail. | antagonist | Map traces the route, populist surge ticker. |
| 19:00 | **EMOTIONAL CONTRAST.** "Cross of Gold." | speech | Held quote, ink-on-cream text plate. |
| 19:30 | Hanna's counter: 200,000,000 pieces of mail. | scale | Counter from 0 → 200,000,000 over 4 s. |
| 20:00 | November 3, 1896. Election night. | quiet beat | Ticker tape. Quiet. |
| 20:15 | **PAYOFF #3.** "The ledger won." | resolution | Cut. Black. Title. |
| 20:45 | Hanna takes the Senate seat. Ohio, 1897. | epilogue setup | — |
| 21:15 | Hobart dies in office, November 1899. | small absence | Single line. |
| 21:30 | Roosevelt forced onto the 1900 ticket. | pivot | Hanna's voice (attributed quote): *"Don't any of you realize there's only one life between this madman and the Presidency?"* |
| 22:00 | **SHOCK.** Buffalo, September 6, 1901. The bullet. | climax | Newspaper plate, Pan-American Exposition. |
| 22:45 | "And like that — Mark Hanna's project ended." | reframe | Roosevelt sworn in; the cartoon Hanna and Roosevelt cartoons stop appearing. |
| 23:15 | February 15, 1904. Hanna dies of typhoid in Washington. | obituary | Funeral image. |
| 23:30 | **CLOSING IMAGE.** What he invented. | thesis-close | The 1896 mechanics, traced forward: 1900, 1904, 1928, 1972, 2008, 2024. The same template. |
| 23:55 | Title card: *"The Ledger — Mark Hanna, 1837–1904."* | end | Black. Cut. |

**Total narration target:** ~3,650 words at ~155 wpm (post-atempo) = ~23:30 spoken; +25 s of cold-open and end-card silence = 24:00 total.

---

## 4. Pacing notes (engagement engineering)

- **Cadence rule of three.** No information beat runs longer than ~12 seconds without a visible-change event (Ken Burns push, white flash, number-on-number cut, or hard-cut to a new image). The 5-min preview hit retention because no static shot survived past ~3 s; the long form has to allow longer sustained shots for emotional anchors but must place a sub-shot inside any beat over ~8 s.
- **Number theatre placement.** Three big-number payoffs anchor the 24 minutes: $3,500,000 (2:30), the assessment system math (16:00), and 200,000,000 mail pieces (19:30). Each lands at a known dip point and serves as the answer to the curiosity gap built up in the preceding 90 seconds.
- **Emotional anchors.** Three human beats are the rest stops: Charlotte (7:30), McKinley's loyalty refusal (13:00), the bullet (22:00). These are intentionally *quieter* than the surrounding number theatre — long held shots, restrained narration. They give the audience permission to feel something so the ledger lines hit harder when they return.
- **Sensory touches at engagement valleys.** Map drawings (Cleveland chokepoint at 9:00, Bryan's rail tour at 18:30) are deployed precisely where attention threatens to slip. A new visual *grammar* arriving — a moving line, a counter, a stamped seal — buys 30 to 60 seconds of recovered attention without spending narration words.
- **Ken Burns direction matches narrative momentum.** Push-in for accusation ("He turned the American presidential election into a corporate purchase order"), pull-out for context ("Cleveland was the chokepoint, and Hanna sat on it"), static for the loyalty beat (McKinley at the microphone), slow-drift for the funeral. Per DESIGN.md.
- **Voice pacing.** Voicebox George at default rate is ~117 wpm; post-atempo 1.18 it lands at ~155 wpm, which is the floor for sustained long-form retention. Splice tolerance is ~2 fixes per minute before audible boundary stutter (per `mark-hanna/LEARNINGS.md` line 29) — the script is therefore written so that any *known* hard words for the voice (years, comma-list nouns, the "J.P." initials) are pre-spelled in the source so we don't *need* splice fixes downstream.
- **Punctuation does not control Kokoro pacing** (`LEARNINGS.md` line 25). Where the script needs a beat, the script breaks to a new line and the *composition* inserts an `anullsrc` silence between scene clips. The script marks these as `[BEAT — 0.6 s]`.
- **Caption strategy.** No separate captions track. The `mark-hanna-shorts` v5 lesson — captions duplicating the hero text caused all the user-reported overlap — applies twice as hard at long-form scale. Hero text on screen *is* the caption. Every line below that's a key spoken phrase appears on-screen at hero typography in its scene.
- **Music bed.** Mid-bass orchestral drone, no melody, sub-`-22 LUFS` so it sits under the narrator. Lifts at the act-break payoffs (2:30, 16:00, 20:15, 23:30) by ~3 dB; otherwise flat. Per DESIGN.md, no bouncy / elastic ease and no "movie-trailer brass."
- **Silence as a beat.** The cold open holds 4 seconds of silence before the first line. The bullet at 22:00 holds 1.5 seconds of silence before "Buffalo, September 6, 1901." Silence is the most powerful thing the long form has and the preview never had room for.

---

## 5. Full scene script

Format per scene: `## SCENE N — start–end (duration) — TITLE`, then *Setting* / *Characters* / *Visuals (hyperframe concept)* / *Intended emotion* / *Narration* (voice-ready, with `[BEAT]` markers). Narration that is verbatim from the 5-minute preview is marked **(verbatim from preview)** so existing splice-grade audio can be reused.

---

### SCENE 1 — 0:00–0:45 (45 s) — THE CARTOON

*Setting:* archival flat plane. Newsprint cream over ink black.
*Characters:* Mark Hanna (in absentia, as cartoon).
*Visuals:* slow push-in (15 s) on `cartoon-dollar-mark-hanna.jpg`. Crossfade to `cartoon-shylock-hanna.jpg` (5 s) and `cartoon-boss-of-bosses.jpg` (5 s). Hard cut to ink black. Then `hanna-portrait.jpg` arrives, name in Playfair Display 160 px.
*Intended emotion:* recognition, then unease. The cartoon is familiar; the name lands like an accusation.
*Narration:*

> [4 s silence — push-in]
> The cartoon ran in every Hearst paper in America. **(verbatim)**
>
> A fat man, in a suit covered in dollar signs, smoking a cigar the size of his forearm. **(verbatim)**
>
> The caption changed every week. The man did not. **(verbatim)**
>
> [BEAT — 0.6 s]
>
> His name was Mark Hanna. **(verbatim)**

---

### SCENE 2 — 0:45–3:30 (2:45) — THE LEDGER

*Setting:* the 1896 election as a balance sheet.
*Characters:* Hanna (off-camera, the implied accountant); the donors (Standard Oil, JP Morgan) as ledger lines; Bryan (un-named yet, "the opposition").
*Visuals:* `newspaper-eveningstar-1896-01-11.jpg` Ken Burns 12 s. Cut to "**1896**" in Blood Oxide #C03A2C, 280 px tall, fills frame for 1.2 s. Cut to "**$3,500,000**" Hanna Amber count-up 0 → 3,500,000 over 1.0 s with `expo.out`. Cut to stacked donor lines in IBM Plex Mono. Cut to "**20×**" Blood Oxide stamp.
*Intended emotion:* uncomfortable scale. Numbers as physical objects.
*Narration:*

> And in eighteen ninety-six, he did something no one had ever done at that scale. **(verbatim)**
>
> He turned the American presidential election into a corporate purchase order. **(verbatim)**
>
> [BEAT — 0.6 s]
>
> Three and a half million dollars raised. Twenty times what his opponent spent. **(verbatim)**
>
> Banks assessed at a quarter of a percent of capital. Railroads, shaken down personally. Standard Oil, two hundred and fifty thousand dollars. JP Morgan, two hundred and fifty thousand dollars. **(verbatim — keep "JP" without periods, per LEARNINGS line 26)**
>
> Half a million voters, transported by train, to shake one man's hand. **(verbatim)**
>
> Two hundred million pieces of campaign literature, printed and mailed. **(verbatim)**
>
> The opposition had a thirty-six year old preacher who could move a crowd to tears. **(verbatim)**
>
> Hanna had a ledger. **(verbatim)**
>
> [BEAT — 1.2 s]
>
> And when November came, the ledger won. **(verbatim)**
>
> [BEAT — 0.8 s]
>
> To understand how — we go back fifty-nine years.

---

### SCENE 3 — 3:30–5:00 (1:30) — NEW LISBON, OHIO. 1837.

*Setting:* a country grocery in eastern Ohio.
*Characters:* young Mark Hanna; his father, Doctor Leonard Hanna.
*Visuals:* `hanna-birthplace.jpg` slow Ken Burns 8 s. Crossfade to `hanna-young.jpg`. Caption-strap: "**NEW LISBON, OHIO. 1837.**" in IBM Plex Mono.
*Intended emotion:* small. Beginnings as small.
*Narration:*

> He wasn't born with money. He was born in a grocery. **(verbatim)**
>
> New Lisbon, Ohio. Eighteen thirty-seven. **(verbatim — spell years per LEARNINGS line 7)**
>
> [BEAT — 0.4 s]
>
> His father, Doctor Leonard Hanna, was a country physician who ran a wholesale grocery on the side. Flour, salt, dry goods to Ohio farmers. **(verbatim)**
>
> When Mark was fifteen, the family moved to Cleveland. He enrolled at Western Reserve College. **(verbatim)**

---

### SCENE 4 — 5:00–6:00 (1:00) — THE BOY AT THE NEXT DESK

*Setting:* Western Reserve College, 1852.
*Characters:* Hanna; John D. Rockefeller (introduced).
*Visuals:* `rockefeller.jpg` arriving in second half of frame; `hanna-young.jpg` retreats. The two faces side by side, hairline 1px Hanna Amber border between.
*Intended emotion:* recognition; the long shadow.
*Narration:*

> In his class, was a quiet, awkward boy who would grow up to control ninety percent of the oil refining capacity in the United States. **(verbatim)**
>
> [BEAT — 0.6 s]
>
> His name was John D. Rockefeller. **(verbatim)**
>
> The two would orbit each other for the next forty years. **(verbatim)**

---

### SCENE 5 — 6:00–7:30 (1:30) — THE PRICE OF THINGS

*Setting:* Cleveland, 1853–1860. The Hanna family store floor.
*Characters:* Hanna.
*Visuals:* `cleveland-1870.jpg` (period-near) Ken Burns. Inset: Hanna at the counter. Pull-quote on right margin in Playfair Italic 56 px: *"the real education was in the price of things."*
*Intended emotion:* education through the eye, not the book.
*Narration:*

> Hanna lasted one year at Western Reserve before he quit. Not because he was failing. Because he had already figured out something the professors couldn't teach. The real education, was in the price of things. **(verbatim)**
>
> He went back to the store. Worked the floor. Watched how men negotiated. Watched who paid on time and who didn't. Watched which suppliers had leverage, and which ones begged. **(verbatim)**
>
> Then the Civil War came. He served briefly. Came home. **(verbatim)**

---

### SCENE 6 — 7:30–8:30 (1:00) — CHARLOTTE

*Setting:* Cleveland, 1864. Wedding.
*Characters:* Hanna; Charlotte Rhodes; Daniel Rhodes (in margin).
*Visuals:* a single image, held long. If a wedding portrait isn't on disk, use `hanna-portrait.jpg` paired with a typography-only plate: **"Charlotte Augusta Rhodes — married Mark Hanna, September 27, 1864."** in Source Serif 4. *No motion for the first 8 seconds.*
*Intended emotion:* the only love beat. Quiet. Permission to feel.
*Narration:*

> [BEAT — 0.8 s — silence on a held image]
>
> And married a woman named Charlotte Rhodes. **(verbatim)**
>
> Her father was Daniel Rhodes. Coal and iron. One of the men quietly getting rich off everything Cleveland was becoming. **(verbatim — keep "Coal and iron" with the connector per LEARNINGS line 9)**

---

### SCENE 7 — 8:30–10:00 (1:30) — THE CHOKEPOINT

*Setting:* Cleveland, 1867–1880.
*Characters:* Hanna; Daniel Rhodes (passing handoff); the city.
*Visuals:* `rhodes-daniel.jpg` 5 s. Then a deliberate motion-graphic map: Lake Erie at top, Pittsburgh mills at bottom, ore-boat icons drawing a line down through Cleveland. Hanna Amber dollar-sign appears at the Cleveland node and pulses once.
*Intended emotion:* geometric inevitability. The position was the prize.
*Narration:*

> Hanna walked into that business, and never walked out. **(verbatim)**
>
> [BEAT — 0.4 s]
>
> By eighteen sixty-seven, Marcus Alonzo Hanna had built MA Hanna and Company. A coal and iron brokerage, sitting at the exact pivot point where Lake Erie ore boats unloaded for the Pittsburgh steel mills. **(verbatim — note "Marcus Alonzo" per LEARNINGS line 30: whisper transcribes as "Alonso", spoken is correct)**
>
> Cleveland was the chokepoint. And Hanna sat on it. **(verbatim)**
>
> Every ton of iron ore that crossed Lake Erie in the eighteen seventies, passed through brokers like him, he took a cut. **(verbatim — comma-merge per LEARNINGS line 27)**
>
> Then he bought the newspaper, the Cleveland Herald. Then a theater. Then banking interests. Then a streetcar line.
>
> By eighteen eighty, he controlled enough of Cleveland that when he walked into a room, the room changed temperature. **(verbatim)**

---

### SCENE 8 — 10:00–11:30 (1:30) — THE THESIS

*Setting:* Hanna's office. Cleveland, c. 1885.
*Characters:* Hanna alone.
*Visuals:* `hanna-portrait.jpg` held. Vignette tightens through the scene. Pull-quote arrives at 10:30 in Playfair 84 px: **"Money was the second most powerful thing in America."** Then a 1.0 s black. Then the answer in Blood Oxide: **"The most powerful thing was who decided where the money went."**
*Intended emotion:* a man crossing a line.
*Narration:*

> By eighteen eighty, Hanna was bored.
>
> [BEAT — 0.4 s]
>
> Not with money. He had money.
>
> Bored with the ceiling.
>
> [BEAT — 0.8 s]
>
> Because he had figured out something. Watching the men who supplied his coal. The politicians who regulated his railroads. The judges who settled his contracts.
>
> [BEAT — 0.6 s]
>
> Money was the second most powerful thing in America.
>
> [BEAT — 1.2 s — black plate with text only]
>
> The most powerful thing was who decided where the money went.
>
> [BEAT — 0.8 s]
>
> That was politics. And no one had ever run politics like a business.
>
> [BEAT — 0.4 s]
>
> Not yet.

---

### SCENE 9 — 11:30–14:00 (2:30) — CHICAGO, 1888

*Setting:* Republican National Convention, Chicago, June 1888.
*Characters:* Hanna; John Sherman; William McKinley (introduced).
*Visuals:* `convention-1888.jpg` Ken Burns push-in 30 s. Vote-tally crawl in IBM Plex Mono left margin showing Sherman's 229 → 244 → 230 → 235 → 244 → 230 → 231 → out. Cut to typography plate at 13:00: **"WILLIAM MCKINLEY"**, name in Playfair 132 px, role-tag in Faded Bone *"Congressman, 17th District, Ohio. 45 years old."* Then `mckinley-1896.jpg` (period-shifted earlier where possible) arrives.
*Intended emotion:* the lesson. Loyalty as a rare object.
*Narration:*

> The year was eighteen eighty-eight. The Republican National Convention. Chicago. **(verbatim)**
>
> Mark Hanna arrived not as a candidate, but as a kingmaker. **(verbatim)**
>
> His man was John Sherman. Ohio senator. Treasury veteran. The establishment choice. **(verbatim)**
>
> Hanna worked the convention floor for six days. Trading delegates. Promising postmasterships. Calling in markers from Ohio to Pennsylvania. **(verbatim)**
>
> Sherman peaked on the first ballot at two hundred and twenty-nine votes. Then he bled out. Ballot after ballot, until the nomination went to Benjamin Harrison on the eighth. **(verbatim)**
>
> [BEAT — 0.8 s]
>
> Hanna lost. **(verbatim)**
>
> But he saw something that week he would never forget. **(verbatim)**
>
> A forty-five year old congressman from Canton, Ohio had been chairing the resolutions committee. **(verbatim)**
>
> When delegates began breaking toward him as a dark-horse alternative, the congressman walked to the microphone, and refused. **(verbatim)**
>
> He told the convention he was bound to Sherman. And he sat down. **(verbatim)**
>
> [BEAT — 1.0 s]
>
> That kind of loyalty was rare in eighteen eighty-eight politics. It was almost extinct. **(verbatim)**
>
> [BEAT — 0.6 s]
>
> His name was William McKinley. **(verbatim)**
>
> Hanna walked across the floor, and introduced himself. **(verbatim)**
>
> [BEAT — 0.4 s]
>
> He didn't know it yet. But he had just found his president. **(verbatim — closing line of the 5-minute preview; the long form pivots here)**

---

### SCENE 10 — 14:00–16:00 (2:00) — THE PANIC

*Setting:* Youngstown, Ohio, February 1893; Cleveland, March 1893.
*Characters:* McKinley; Ida McKinley (introduced briefly); Hanna; Robert Walker (the friend whose business collapse takes McKinley's signature down with it — named once for fidelity).
*Visuals:* newspaper headline plate: **"M'KINLEY FACING FINANCIAL RUIN — Liabilities, $130,000."** Cleveland Plain Dealer style. Then a typography plate of the documented McKinley refusal: *"He would not be a beggar."* in Source Serif Italic 72 px on cream — **note: this is the historians' paraphrase from Beckley's 1960 Ohio History reconstruction, not a verbatim quote; treat as reported speech on screen.** Then `mckinley-1896.jpg` paired with a small-format Ida portrait or her name plate (no public-domain Ida portrait is in `assets/`; if procurement fails, hold a typography plate: **"Ida Saxton McKinley — chronically ill, often bedridden — kept off the campaign trail by her health."**).
*Intended emotion:* the candidate is mortal. The patron decides what mortality costs — without telling the candidate.
*Narration:*

> In February eighteen ninety-three, McKinley nearly went bankrupt.
>
> [BEAT — 0.6 s]
>
> The Panic.
>
> Banks collapse from New York to San Francisco. Six hundred and forty banks fail in a single year.
>
> [BEAT — 0.4 s]
>
> Fifteen thousand businesses go under.
>
> [BEAT — 0.6 s]
>
> One of those businesses belonged to a man named Robert Walker, in Youngstown, Ohio. Walker was a friend of McKinley's. McKinley had co-signed Walker's notes — out of loyalty.
>
> [BEAT — 0.4 s]
>
> The same loyalty Hanna had watched at the Chicago microphone — five years earlier.
>
> [BEAT — 0.6 s]
>
> When Walker collapsed, the notes came due against McKinley.
>
> [BEAT — 0.6 s]
>
> One hundred and thirty thousand dollars. **(spoken; on-screen "$130,000" Hanna Amber)**
>
> [BEAT — 0.8 s]
>
> The governor of Ohio could not pay. He told his friends he would not solicit help. He would not be a beggar.
>
> [BEAT — 0.6 s]
>
> So Mark Hanna did it for him. Without asking.
>
> [BEAT — 0.4 s]
>
> Inside three weeks, a syndicate of Cleveland and New York industrialists — Hanna at the center — quietly absorbed every note.
>
> McKinley signed nothing. Owed nothing.
>
> [BEAT — 0.4 s]
>
> He knew, only later, who had paid.
>
> [BEAT — 0.8 s]
>
> The candidate was now a debt. **(spoken; on-screen Playfair 84 px)**
>
> [BEAT — 0.4 s]
>
> And Hanna held the paper.

---

### SCENE 11 — 16:00–17:45 (1:45) — THE MECHANISM

*Setting:* the operation, 1895–1896.
*Characters:* Hanna at the center; the donor classes as ledger entries.
*Visuals:* this is the **mechanism reveal scene** — full hero typography. A blank cream plate fills the screen. Black IBM Plex Mono lines write themselves in, one at a time, with `expo.out`:

```
   BANKS                 — 1/4 % of paid-in capital
   RAILROADS             — assessed by line-mile
   STANDARD OIL          — $250,000
   J P MORGAN            — $250,000
   NEW YORK LIFE         — $50,000
   EQUITABLE             — $50,000
   METROPOLITAN LIFE     — $50,000
   ─────────────────────
   TOTAL, 1896           — $3,500,000
```

The total stamps in Blood Oxide.
*Intended emotion:* the math is on screen. Nothing is hidden any more.
*Narration:*

> Here is how the ledger worked.
>
> [BEAT — 0.6 s]
>
> Every national bank in America was assessed at a quarter of one percent of its paid-in capital. Not asked. Assessed.
>
> Every railroad, by line-mile.
>
> [BEAT — 0.4 s]
>
> Standard Oil — two hundred and fifty thousand dollars.
>
> JP Morgan — two hundred and fifty thousand dollars. **(keep "JP" un-dotted)**
>
> New York Life. Equitable. Metropolitan Life. The big three insurers, fifty thousand each, billed to policy holders.
>
> [BEAT — 0.8 s]
>
> Three and a half million dollars. **(spoken)**
>
> Twenty times what William Jennings Bryan would raise. **(spoken; the antagonist's name lands here for the first time)**

---

### SCENE 12 — 17:45–18:30 (45 s) — THE FRONT PORCH

*Setting:* Canton, Ohio, summer–fall 1896.
*Characters:* McKinley on a porch; the half-million who arrive by railroad; Ida (off-camera, indoors).
*Visuals:* a wide static shot of the McKinley house in Canton (use convention/period composition; the project will source a public-domain photograph in the production task if not already on disk). Stop-motion-style stamping of the visitor count on screen: **"+12,400"** ... **"+74,000"** ... **"+218,000"** ... **"+501,200"** by November 2.
*Intended emotion:* delivery as theater; scale as choreography.
*Narration:*

> Bryan tours.
>
> [BEAT — 0.4 s]
>
> McKinley does not.
>
> McKinley sits on his front porch in Canton, Ohio.
>
> His wife is too ill to be left alone.
>
> Hanna has decided that staying still is more presidential than running.
>
> Hanna brings the country to the porch.
>
> [BEAT — 0.6 s]
>
> Half a million voters. By train. To Canton. **(spoken; counter visible)**
>
> Each one shakes McKinley's hand. Each one goes home and tells a story.

---

### SCENE 13 — 18:30–19:30 (1:00) — CROSS OF GOLD

*Setting:* Chicago, July 9, 1896. The Democratic National Convention.
*Characters:* William Jennings Bryan.
*Visuals:* a held typography plate, no portrait in the first 8 seconds. The plate: ink black background, Playfair Italic 84 px in Newsprint Cream:

> *"You shall not press down upon the brow of labor this crown of thorns. You shall not crucify mankind upon a cross of gold."*

Then, at 19:00, a tight portrait of Bryan (sourcing tag for art dept) replaces the plate.
*Intended emotion:* contrast. The thing the ledger is buying *against*.
*Narration:*

> The opposition had a thirty-six year old preacher who could move a crowd to tears. **(verbatim — placed here for the second time in the doc, deliberately, as the ledger pivot rhyme)**
>
> [BEAT — 1.0 s]
>
> William Jennings Bryan walked into the Democratic convention an unknown congressman from Nebraska. He walked out, the nominee.
>
> On one speech.
>
> [BEAT — silence 1.5 s — typography plate alone]
>
> The crowd in Chicago carried him on their shoulders. The newspapers wrote that one speech, two thousand words long, had broken thirty-six years of party silence.
>
> [BEAT — 0.6 s]
>
> Hanna read the speech in Cleveland that night, and went, the next morning, to the bank.

---

### SCENE 14 — 19:30–20:15 (45 s) — TWO HUNDRED MILLION

*Setting:* the final ten weeks.
*Visuals:* a counter that runs from 0 to 200,000,000 across 4 seconds, with `expo.out`. Caption: **"PIECES OF CAMPAIGN MAIL."** In a second pane, an animated rail-line traces 18,000 miles of Bryan's tour; in a third, a pamphlet stack rises.
*Intended emotion:* asymmetric warfare made visible.
*Narration:*

> Two hundred million pieces of campaign literature, printed and mailed. **(verbatim — restated for visual landing)**
>
> One thousand four hundred speakers under contract. Pamphlets in German, in Polish, in Yiddish, in Italian.
>
> Bryan rode eighteen thousand miles by rail. Spoke to five million people in person.
>
> Hanna mailed a country.

---

### SCENE 15 — 20:15–20:45 (30 s) — NOVEMBER 3, 1896

*Setting:* election night.
*Visuals:* black plate. Then a single line, IBM Plex Mono, Newsprint Cream:

```
    McKINLEY   271 electoral votes
    BRYAN      176 electoral votes
```

Hold for 4 seconds in silence after the result.
*Intended emotion:* resolution as quiet.
*Narration:*

> [BEAT — 1.5 s of silence on the result plate]
>
> And when November came, the ledger won. **(verbatim — third payoff)**

---

### SCENE 16 — 20:45–22:00 (1:15) — SENATOR HANNA. AND THE COWBOY.

*Setting:* Washington, 1897–1900.
*Characters:* Hanna (now Senator from Ohio); McKinley; Hobart; Theodore Roosevelt.
*Visuals:* a typographic timeline strip:

```
  1897 — Hanna takes the Senate seat, Ohio.
  1899 — Vice-President Hobart dies in office.
  1900 — Roosevelt forced onto McKinley's re-election ticket.
```

Then a single Hanna pull-quote in Playfair 84 px Hanna Amber:

> *"Don't any of you realize there's only one life between this madman and the Presidency?"*

Held for 2.5 seconds.
*Intended emotion:* dramatic irony. We know what the room doesn't.
*Narration:*

> Hanna takes McKinley's old Senate seat in Ohio. He runs the senate the way he ran a brokerage.
>
> McKinley wins again in nineteen hundred. The same ledger. The same machinery.
>
> [BEAT — 0.4 s]
>
> The vice-president on the second ticket is Garret Hobart, of New Jersey. A reliable man. A quiet man.
>
> Hobart dies in office in November of eighteen ninety-nine.
>
> The seat is open.
>
> [BEAT — 0.6 s]
>
> The New York Republican machine has a problem. Their reformist governor is a war hero. He is a moralist. He keeps breaking their patronage rings. They want him out of New York.
>
> They suggest the vice-presidency. The vice-presidency in nineteen hundred is widely understood to be a coffin.
>
> [BEAT — 0.6 s]
>
> Mark Hanna sees what is coming. He tries to stop it.
>
> [BEAT — 0.8 s — held quote plate]
>
> *"Don't any of you realize there's only one life between this madman and the Presidency?"* <!-- noqa: STYLE: direct historical quote, attributed to Hanna at the 1900 GOP convention; Croly biography -->
>
> [BEAT — 0.8 s]
>
> They do not listen.
>
> The madman is Theodore Roosevelt.

---

### SCENE 17 — 22:00–23:35 (1:35) — BUFFALO

*Setting:* Pan-American Exposition, Buffalo, New York. September 6, 1901.
*Characters:* McKinley; Czolgosz (named once); Roosevelt (off-camera).
*Visuals:* held silence on a typography plate: **"BUFFALO. SEPTEMBER 6, 1901."** for 1.5 s. Then a newspaper-front composite: **"PRESIDENT SHOT AT EXPOSITION."** A flash of the assassin's name in Faded Bone 32 px — *"Leon Czolgosz, anarchist."* — for 1.0 s, then off. Held black after "two shots." McKinley dies at 2:15 a.m., September 14. The screen carries the time: **"TWO-FIFTEEN A.M. SEPTEMBER FOURTEENTH, NINETEEN HUNDRED AND ONE."**
*Intended emotion:* the random event the ledger could not budget. Held silence is the point.
*Narration:*

> [BEAT — 1.5 s silence on typography plate]
>
> Buffalo. September sixth, nineteen hundred and one.
>
> [BEAT — 0.6 s]
>
> William McKinley shook hands at the Pan-American Exposition.
>
> [BEAT — 0.4 s]
>
> A young man in line stepped forward. He had a handkerchief over his right hand.
>
> [BEAT — 0.6 s]
>
> Beneath the handkerchief was a revolver.
>
> [BEAT — 0.8 s]
>
> Two shots.
>
> [BEAT — 2.5 s — held black, no narration, no music]
>
> The first round caught a coat button. The second struck the stomach.
>
> [BEAT — 0.6 s]
>
> McKinley died eight days later. Two-fifteen in the morning. September fourteenth.
>
> [BEAT — 1.0 s]
>
> Theodore Roosevelt was sworn in that afternoon. In a borrowed library on Delaware Avenue.
>
> [BEAT — 1.2 s]
>
> Mark Hanna's project ended.
>
> [BEAT — 0.4 s]
>
> Eight years before Mark Hanna did.

---

### SCENE 18 — 23:35–24:25 (50 s) — TYPHOID

*Setting:* Washington, D.C., February 15, 1904. Hanna's home on Lafayette Square.
*Characters:* Hanna alone.
*Visuals:* a typographic obituary plate in newspaper layout: **"M. A. HANNA DEAD"** Playfair 124 px, dateline **"WASHINGTON, FEB. 15."**, two columns of period typesetting. After 6 s, crossfade to a Hanna pull-quote in Playfair 64 px Hanna Amber: *"That damn cowboy is President of the United States."* Held 3 s. Then back to the obituary, vignette tightening.
*Intended emotion:* a small ending for a large life. The man who modelled everything could not model Theodore Roosevelt.
*Narration:*

> In nineteen oh four, Mark Hanna ran against Roosevelt for the Republican nomination.
>
> [BEAT — 0.4 s]
>
> He had the donors. He had the senate.
>
> [BEAT — 0.6 s]
>
> He did not have the time.
>
> [BEAT — 1.0 s]
>
> Typhoid fever took him on February fifteenth, nineteen oh four. In his home on Lafayette Square. He was sixty-six years old.
>
> [BEAT — 1.2 s]
>
> The man who built the modern American campaign died before he could solve the one variable he never modelled.
>
> [BEAT — 0.4 s]
>
> The cowboy.
>
> [BEAT — 0.8 s]
>
> Roosevelt walked the nomination.

---

### SCENE 19 — 24:25–25:00 (35 s) — THE INHERITANCE

*Setting:* the present looking back.
*Characters:* none on screen.
*Visuals:* a vertical timeline, IBM Plex Mono. As each year arrives, the dollar figure for that election's spending ticks up on the right margin in Hanna Amber. Years used (rounded for screen): 1896 — 3.5 M. 1900 — 3.0 M. 1928 — 6.3 M. 1972 — 138 M. 2008 — 1.3 B. 2024 — 2.7 B (presidential cycle, all-source). Each line draws a dim line back to the 1896 row.
*Intended emotion:* the template. The thesis closing.
*Narration:*

> The man you've seen in a thousand cartoons — the dollar suit, the cigar — invented something that outlived him by a hundred and twenty years.
>
> The assessment system. The corporate mail. The candidate as product. The convention as choreography.
>
> [BEAT — 0.6 s]
>
> Every American presidential campaign since nineteen hundred has used a piece of his ledger. Most use the whole thing.
>
> [BEAT — 1.0 s]
>
> His name was Mark Hanna.
>
> [BEAT — silence — final cartoon image returns, dollar-suit, cigar, 2.0 s]
>
> The cartoon ran in every Hearst paper in America.

---

### END CARD — 23:55–24:00

Black plate. Playfair Display 96 px:

```
THE LEDGER
Mark Hanna · 1837–1904
```

Hanna Amber rule. IBM Plex Mono Faded Bone subscript: *@AmericanAudacity · Episode 02.*

---

## 6. Production handoffs

This script is the input for siblings `t_be6c1904` (audio plan) and `t_df363173` (visual style + shot boards). The key constraints they need are:

- **Voice:** Voicebox George + atempo 1.18, single narrator. No voice doubles, no character actors. All quoted speech is read by George with intonation cues; on-screen typography carries the attribution.
- **Pre-spelled hard words for the voice:** every year is spelled out in narration source (`eighteen ninety-six`, not `1896`); `J.P.` is `JP`; `Marcus Alonzo` (whisper will mishear, ignore); `Coal and iron.` not `Coal, iron.`; `brokers like him, he took a cut.` not `brokers like him. He took a cut.` — all per `mark-hanna/LEARNINGS.md`.
- **Splice budget:** plan ≤2 splice fixes per minute of finished render before re-rendering the whole scene. Long-form (24 min) means we plan per-scene narration files (one wav per scene 1–19) so re-render cost stays at ~1–2 min per affected scene. Per `LEARNINGS.md` line 18.
- **Hard images on disk now (re-usable):** `cartoon-dollar-mark-hanna.jpg`, `cartoon-shylock-hanna.jpg`, `cartoon-boss-of-bosses.jpg`, `hanna-portrait.jpg`, `hanna-young.jpg`, `hanna-birthplace.jpg`, `cleveland-1870.jpg`, `rhodes-daniel.jpg`, `rockefeller.jpg`, `convention-1888.jpg`, `mckinley-1896.jpg`, `newspaper-eveningstar-1896-01-11.jpg`, `davenport-hanna-1896.jpg`. (See `mark-hanna/assets/`.)
- **Images to procure (all pre-1929, public-domain in US):** Charlotte Hanna portrait (Western Reserve Historical Society), Ida McKinley portrait, McKinley front-porch crowd photograph, McKinley-Roosevelt 1900 inauguration, Bryan portrait c. 1896, Pan-American Exposition Temple of Music exterior, Hanna funeral procession.
- **Music:** mid-bass orchestral drone, no melody; lifts ~3 dB at 2:30, 16:00, 20:15, 23:30. No movie-trailer brass. Per DESIGN.md.
- **Captions:** no separate captions track. Hero text on screen *is* the caption. Per `mark-hanna-shorts/LEARNINGS.md` v5.
- **Composition:** 16:9 base, 1920×1080. Re-use the long-form composition framework from `mark-hanna/index.html`, not the 9:16 shorts grid.

---

## 7. Acceptance check

A reviewer reading this document can answer, in plain English, every question on the task acceptance bar:

- **Who is each character and why are they here?** §2 names 12 and gives each a one-line structural function.
- **Where do engagement beats land and why?** §3 timestamps 31 beats and tags the 7 dip-windows with the delivery type (number theatre / emotional anchor / sensory touch / silence).
- **What does each scene look like?** §5 gives setting, characters present, dialogue/voiceover, intended emotion, and the hyperframe visual concept for all 19 scenes.
- **How does pacing work?** §4 documents the cadence rule, the music plan, the silence beats, and the voice-engine constraints that the pacing has to live inside.
- **What does the next worker need?** §6 hands off images, voice quirks, splice budget, and procurement targets directly to the audio and visual sibling tasks.
