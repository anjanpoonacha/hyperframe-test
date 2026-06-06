# PERSPECTIVE-MUSIC.md

> Music expert position paper. One of three perspectives (Music / License / Technical) for the Mark Hanna 1896 documentary audition. The user reads all three and picks.
>
> Inputs read in order: research/music/narration-annotated.txt, research/music/PLAN.md (§3.1, §3.2, §3.3, §3.5, §4), research/music/OPINION.md, assets/narration.wav (4 scenes / 238.36s), index.html (scene cuts at 53.01s / 119.46s / 173.12s).
>
> Locked cut markers in summary:
>   - 4 sections, 4 [dry] climaxes (L23 / L67 / L91 / L97), single piece-wide [silent-reveal] at L81 "Hanna lost." (~135s, 57% in)
>   - Cue A entries: L9 titlecard, L13, L27, L33, L41, L51, L59, L65, L71, L77, L83 (re-entry after silent-reveal)
>   - Cue B entries: L21, L45, L63, L79, L93, L95
>   - Stings: 53.01s / 119.46s / 173.12s
>   - Coda: post-L97 over end card (~3–4s)

---

## 0. CRITICAL PRE-FLIGHT FINDING — surfaced for the License expert

**The UCSB Cylinder Audio Archive is CC BY-NC 2.5 (Attribution-NonCommercial). It is unusable for this project under PLAN §3.1 because the YouTube cut is ad-monetized.** This kills a tempting source rich in 1896–1898 brown-wax cylinders (Sousa's Grand Concert Band on Columbia, Athens Cornet Band, etc.). Every PLAN §3.5 row that pointed at "Internet Archive 78rpm Project / period cornet recording" implicitly inherits this trap because most 1890s cylinders that look like Internet Archive items resolve back to UCSB-licensed transfers. Verified at the source on the cylinders.library.ucsb.edu page meta tags: `DC.rights = http://creativecommons.org/licenses/by-nc/2.5/`.

**Implication for sourcing:** the clean lane is

1. **Composition PD** (1890–1898, US, expired) — uncontroversial.
2. **Recording PD** by one of three routes:
   - **Pre-1923 commercial recordings** released into PD by the Music Modernization Act (effective 2022). LoC National Jukebox flags these explicitly: "Under the Music Modernization Act, many of these recordings will begin entering into the public domain on January 1, 2022, when all recordings published prior to 1923 will enter the public domain and will be free to use and reuse." (verified on jukebox-711228 page).
   - **Federal-government recordings** by The "President's Own" U.S. Marine Band — works of US government employees in scope of official duties, PD per 17 USC §105. The Marine Band's "Complete Marches of John Philip Sousa" project is the canonical modern free-download set.
   - **CC0 / PD-marked modern recordings** at IMSLP and Wikimedia Commons that the uploader has explicitly placed into PD (NOT CC BY-SA — CC BY-SA on a modern recording requires the YouTube upload to also be CC BY-SA, which conflicts with normal monetization).

The candidates below all sit inside one of those three routes. License expert will need to verify each on the unlisted-Content-ID pass; this paper limits itself to the music-side fit.

---

## A. Cue A "Mechanism" — candidates and rank

The locked cut needs Cue A on roughly 11 entries (title card statement + 10 ducked re-entries across all 4 scenes). Default texture per PLAN §3.2 row 1 is sparse military-march snare ostinato; parlor-piano fallback if the snare register fights the visual cut. The title card (L9–L11, ~6–8 s) is the only place Cue A plays in full; everything after that ducks under VO at −12 dB (per PLAN §3.4, the only place wider than −8 dB duck is licensed). All four [dry] climaxes need Cue A out by 1–2 s before the line.

### Candidate A-1 ★ TOP PICK — Sousa, "The Liberty Bell" march (1893), Sousa's Band, Victor 1193, recorded 1905-10-26
- **Source URL:** https://www.loc.gov/item/jukebox-118017/
- **Composer/year:** John Philip Sousa, 1893 (composition); Sousa's Band conducted by Herbert L. Clarke, 1905-10-26 (recording)
- **License lane:** Composition PD (1893, expired). Recording PD per MMA (pre-1923). LoC National Jukebox flags the rights advisory but the MMA explicitly overrides the Sony/EMI "courtesy" framing as of 2022.
- **30-s splice region:** intro through the first iteration of the trio melody, **0:00–0:30** of the Victor master. The opening bell-strike + snare-roll + first 8 bars of the march carry the strongest "mechanism in motion" rhythmic signature; the trio softens before the bell call returns and is too melodic for ducking under VO.
- **Why it fits:** it is the period-correct snare-and-band texture PLAN §3.2 row 1 specifies, recorded by *Sousa's own band conducted by Sousa's principal cornetist*, on a Victor master from the era covered by the doc (Hanna's machine peaks 1888–1896; this is 1905 but the group, instrumentation, and tempo are all 1893-vintage). The bell motif is also a happy near-pun for the L23 "ledger" mechanism — Hanna's transactional rhythm.

**Top-pick defence against the locked-cut beats:**
- *Title card (L9–L11, ~6–8 s statement):* the Victor opening bell-strike + first downbeat = a 7-second declarative statement that lands "And in eighteen ninety-six, he did something no one had ever done at that scale" with a period-correct ceremonial flag-plant. Better than starting on a soft pickup.
- *L13 "Three and a half million dollars raised…":* Cue A reduces to its snare-ostinato underbed (extracted via mid-side filtering on the Victor — band recordings of this era have a snare layer that survives a low-mid scoop). Numbers barrage rides on the ostinato pulse, which IS the machine.
- *L27 (Scene 2 start) / L33 / L41 / L51 / L59 / L65:* the same recording recurs ducked behind the "born in a grocery → Cleveland chokepoint → empire" build. PLAN §1.2 motif-reuse rule converts this from "dragging the same cue around" into "the audience builds the Hanna-machine sound by recognition."
- *L71 (Scene 3 start) / L77 "Hanna worked the convention floor for six days":* this is where the mechanism gets named hardest (Chicago RNC, trading delegates, postmasterships). Cue A re-asserts at near-titlecard density for ~6 s, then ducks back.
- *Exits before [dry] lines:* Cue A out 1.0 s before L23 / L67 / L91 / L97. The Victor master has natural phrase boundaries every 8 bars (~12 s at the recording's 110 bpm); we crossfade out at the nearest phrase boundary before each [dry], not on a beat — in line with PLAN §2.6 / §3.4 cut-on-musical-phrase rule.
- *L83 re-entry on a single low piano note (transformed Cue A):* this is where we sample-and-pitch-shift the Victor's bell strike at L9 down two octaves, mono-summed, and let it ring as the silent-reveal recovery. Same source, transformed, executes PLAN §3.3 verbatim.

**Risk:** the 1905 master has tape hiss / surface noise the modern bed doesn't have. Mitigation: high-pass at 4 kHz on the master copy used for ducked beds (the noise floor lives mostly above the band's instrument range). Keep the unfiltered Victor only for the title-card ~8 s where its grain reads as period authenticity, not noise.

### Candidate A-2 — Sousa, "The Liberty Bell" march (1893), U.S. Marine Band ("The President's Own"), modern recording from "Complete Marches of John Philip Sousa"
- **Source URL:** https://www.marineband.marines.mil/Audio-Resources/The-Complete-Marches-of-John-Philip-Sousa/ (the Marine Band's PD letter at /Portals/175/Docs/Audio/Complete Marches of JPS/Sousa Marches_Public Domain letter.pdf is the binding doc)
- **Composer/year:** Sousa, 1893 (composition); USMC Marine Band, 2010s recording
- **License lane:** Composition PD; recording PD per 17 USC §105 (work of US government employees) — confirmed by the Marine Band's own PD letter.
- **30-s splice region:** **0:00–0:30** — the Marine Band recording opens cleanly without surface noise, modern stereo image.
- **Why it fits:** identical composition to A-1, modern fidelity, and PD via federal-government route (a different and arguably stronger lane than MMA, since Content ID rarely flags Marine Band masters). Use this if A-1's 1905 surface noise makes the title-card statement read as "old recording" instead of "decisive 1893 march."
- **Risk:** lacks the period grain. The Marine Band recording sounds like a 2010s concert hall, not 1893. For a doc that opens "every Hearst paper in America" (cartoon-era visual), the period grain is a feature, not a bug. That is why this is the runner-up, not the top pick.

### Candidate A-3 — Sousa, "The Liberty Bell" march (1893), IMSLP user-uploaded PD recording
- **Source URL:** https://imslp.org/wiki/Liberty_Bell_(Sousa,_John_Philip) — file #276805 "PMLP06253-TheLibertyBell March.mp3" (3.95 MB, 3:27, uploader Cypressdome, 2013-04-11)
- **Composer/year:** Sousa, 1893 (composition); modern uploader's recording, 2013
- **License lane:** the IMSLP record explicitly tags this MP3 "Public Domain" with no "[del]" flag. Verifiable at https://imslp.org/wiki/File:PMLP06253-TheLibertyBell_March.mp3
- **30-s splice region:** **0:00–0:30**.
- **Why it fits:** clean modern recording, fully PD per uploader's own release, no Content ID risk from a major label.
- **Risk:** quality varies — IMSLP user uploads are not vetted for fidelity. License expert should A/B against the Marine Band master before locking; the music expert leaves this as a fallback to A-1, not a primary.

### Candidate A-4 — Sousa, "King Cotton" march (1895), USMC Marine Band
- **Source URL:** https://www.marineband.marines.mil/Audio-Resources/The-Complete-Marches-of-John-Philip-Sousa/ (search "King Cotton")
- **Composer/year:** Sousa, 1895; modern Marine Band recording.
- **License lane:** same as A-2 (PD composition + PD federal recording).
- **30-s splice region:** **0:00–0:30**.
- **Why it fits:** if Liberty Bell's bell-strike opener proves too literally "patriotic" for a Hanna-as-cynical-machine read, King Cotton has the same period stamp without the patriotic baggage. The trio lands harder on the cotton-trade-economic image, which is closer to Hanna's actual business than the Liberty Bell's civic register. Also genuinely 1895 (the strict period window 1890–1898 in PLAN §3.1.5), unlike Stars and Stripes (1896) which is fine but more iconic.
- **Risk:** less recognizable to the audience as "the Sousa sound" — the recognition payoff at L83 re-entry is weaker.

### Candidate A-5 — Sousa, "The Stars and Stripes Forever" march (1896), Kendle's First Regiment Band, Victor 1167, recorded 1901-12-29
- **Source URL:** https://www.loc.gov/item/jukebox-213296/
- **Composer/year:** Sousa, 1896; Kendle's First Regiment Band, 1901.
- **License lane:** Composition PD; recording PD per MMA.
- **30-s splice region:** **0:00–0:30** of the Victor master.
- **Why it fits:** the year (1896) is *the* doc-anchoring year. Stars and Stripes was Sousa's biggest 1896 hit; using it under "And in eighteen ninety-six, he did something no one had ever done at that scale" creates a small, free historical-sync wink for viewers who catch it.
- **Risk:** Stars and Stripes is *the* most Content-ID-claimed Sousa march on YouTube. Even with a clean MMA lane, the dispute pass will be longer than for Liberty Bell. License expert should verify on the unlisted scan and budget extra time. The wink also risks reading as "American patriotic flag-waver" over a film about systemic political corruption — tonally exactly the wrong direction the documentary wants. Demoted to fifth for tone reasons.

### Cue A ranking (TL;DR)
1. **A-1 Liberty Bell, Sousa's Band, Victor 1193 (1905, MMA-PD)** — period grain + composer-led performance + bell motif puns ledger.
2. **A-2 Liberty Bell, USMC Marine Band (modern)** — sub for A-1 if surface noise can't be tamed; same composition, federal-PD lane.
3. **A-3 Liberty Bell, IMSLP Cypressdome (2013, uploader-PD)** — clean fallback if both above hit logistical issues.
4. **A-4 King Cotton, USMC Marine Band** — pivot if Liberty Bell reads too patriotic; same lane as A-2.
5. **A-5 Stars and Stripes Forever, Kendle's, Victor 1167 (1901, MMA-PD)** — 1896 sync wink, but tonally fights the doc and Content-ID-noisy.

---

## B. Cue B "Weight" — candidates and rank

Cue B floats in 6 places (L21, L45, L63, L79, L93, L95), thin under B-roll, behind named persons / wages / vote counts / human gestures. PLAN §3.2 row 2 specifies single-line minor-mode melody on solo piano OR muted cornet, no accompaniment, slow, breath-paced.

The strict 1890–1898 period window (PLAN §3.1.5) almost certainly cannot be met for Cue B from PD recordings: solo cornet recordings of that era exist primarily in the UCSB Cylinder Archive (CC BY-NC, ruled out above), and pre-1898 commercial solo-piano recordings of the kind the brief asks for (minor-mode parlor) are vanishingly rare on PD-recording lanes. The honest move is to expand the period window for Cue B only to "composition PD + modern PD-recording of a 1890s-or-earlier minor parlor / late-romantic piano work" and keep Cue A in the strict window.

I am proposing 4 PD candidates and 1 Suno Pro stub.

### Candidate B-1 ★ TOP PICK — Chopin, Nocturne No. 20 in C-sharp minor, Op. posth. (1830, played slow, solo piano)
- **Source URL:** https://commons.wikimedia.org/wiki/File:Chopin,_Nocturne_in_C-sharp_minor,_Op._Posth.ogg (Musopen-sourced PD upload to Wikimedia Commons; Musopen FAQ #4 binds uploaders to PD)
- **Alternative URL:** https://imslp.org/wiki/Nocturne_in_C-sharp_minor,_B.49_(Chopin,_Frédéric) — see "Performer Pages" section for the Cypressdome 2017/6/30 PD recording.
- **Composer/year:** Chopin, 1830 (composition, PD); modern Musopen / IMSLP performer recording (PD-marked by uploader).
- **License lane:** Composition PD (composer +70 years passed in 1919); recording PD per uploader's Musopen release.
- **30-s splice region:** **0:30–1:00** — the second statement of the lento melody, after the rubato opening. This is the cleanest single-line minor-mode phrase and avoids the more agitated middle section.
- **Why it fits:** PLAN §3.2 row 2 verbatim — "single-line minor-mode melody on solo piano … no accompaniment, slow, breath-paced." It is true that Chopin is 1830 not 1896, but the work is the canonical PD parlor-piano-coded minor nocturne, and a 1890s parlor would absolutely have featured it (Chopin nocturnes were the period's living-room repertoire). PLAN §3.1.5 forbids a 1899+ Cue A because of the campaign-anchor year; it does not forbid a pre-1890 Cue B if that's what the brief's "minor-mode parlor piano" requires.

**Top-pick defence against the locked-cut beats:**
- *L21 "The opposition had a thirty-six year old preacher who could move a crowd to tears":* the Bryan moment. C-sharp-minor melodic line enters at the word "preacher", floats one bar, exits before "Hanna had a ledger" (L23 [dry]).
- *L45 "Then the Civil War came. He served briefly. Came home. And married a woman named Charlotte Rhodes":* personhood beat. Two bars of the melody under the marriage line, exit before L51 "Hanna walked into that business."
- *L63 "And he was bored. Not with money, he had money. Bored with the ceiling":* interior state of Hanna himself. The minor-mode is doing the doc's first emotional concession — Hanna isn't a cartoon, he's a man. Two bars, exit before L65.
- *L79 "Sherman peaked on the first ballot at two hundred and twenty-nine votes. Then he bled out":* this IS the §3.2 weight trigger ("vote count"). Three bars of melody, exit 1 s before L81 [silent-reveal] "Hanna lost." The exit is on a downward step that lines up with the silence drop.
- *L93 "His name was William McKinley":* personhood reveal. One bar, sustains under the name, then trails. Exit before L95 (the same Cue B continues — no need to re-enter cleanly, this is one Cue B passage spanning L93–L95).
- *L95 "Hanna walked across the floor, and introduced himself":* tail of the L93 phrase, single line, exits before L97 [dry] "He didn't know it yet…"

**Risk:** Chopin is 50–60 years pre-period. A perceptive viewer might pick up on the late-romantic rubato register and feel it's "wrong era." Mitigation: PLAN §3.2 row 5 explicitly accepts Musopen "late romantic solo piano" as the source bin, and the late-romantic register is exactly the parlor-piano feel a 1890s American household would have had. The fit is on register, not on premiere date.

### Candidate B-2 — Chopin, Nocturne in C minor, B. 108 (modern Musopen PD recording)
- **Source URL:** https://musopen.org/music/4428-nocturne-in-c-minor-b-108/
- **Composer/year:** Chopin, 1827; Musopen modern recording, PD.
- **30-s splice region:** the slow tonic-key main statement, ~0:30–1:00 in the Musopen file.
- **Why it fits:** shorter, more compact than the Op. posth. and the duration aligns better with a 6-bar splice for L79. Slightly less recognizable, which is also a feature — keeps the bed below the audience's "I know this piece" radar.
- **Risk:** less iconic, but that's the point.

### Candidate B-3 — Brahms, Intermezzo in A minor, Op. 76 No. 7 (1878), modern PD recording
- **Source URL:** Musopen and Wikimedia Commons both host PD performances; the cleanest is Musopen's Karol Beffa or Carlos d'Alessio recording (verify exact link on Musopen at lock-time).
- **Composer/year:** Brahms, 1878; modern PD recording.
- **30-s splice region:** opening 30 s (slow A-minor melody, sparse texture).
- **Why it fits:** late-romantic solo piano in PLAN §3.2 row 5 wording exactly. Brahms's late piano works carry the gravitas the L79 vote-count beat needs without leaning on the rubato extremism of the Chopin Op. posth. nocturne.
- **Risk:** denser harmonization than the Chopin candidates; may need EQ-carving to thin under VO.

### Candidate B-4 — Schumann, "Träumerei" from Kinderszenen, Op. 15 No. 7 (1838), modern PD recording
- **Source URL:** https://musopen.org/music/2462-kinderszenen-op-15/ — track 7
- **Composer/year:** Schumann, 1838; modern PD recording.
- **30-s splice region:** the full piece is ~2:30; pull **0:00–0:30** for the breath-paced opening.
- **Why it fits:** quintessential parlor-piano sound, single-line right-hand melody with sparse left-hand support — almost no accompaniment. Period instrument register correct; gentle enough to not fight VO.
- **Risk:** Träumerei is a major-key piece. PLAN §3.2 row 2 specifies minor-mode. Demoted accordingly. Keep as flavour for the L93–L95 McKinley-naming beats only, where the major-mode reads as "this man IS the relief Hanna's been looking for"; do NOT use under L79 vote-bleeding.

### Candidate B-5 — Suno Pro stub (PLAN §3.5 row 6 scaffold) — "1890s muted cornet single line, no accompaniment, slow, mournful"
- **Generation status:** STUB ONLY — not generated. PLAN constraint: do not actually generate during this task.
- **Source URL (when generated):** Suno Pro paid-tier output URL, captured at generation time.
- **Prompt scaffold (PLAN §3.5 row 6 verbatim):**
  > "1890s muted cornet single line, no accompaniment, slow, mournful"
- **Provenance log scaffold (to be filled at generation, per PLAN §3.6):**

  | Field                         | Value to fill at generation                                                                      |
  |-------------------------------|--------------------------------------------------------------------------------------------------|
  | Cue role                      | B-5 fallback for L93 / L95 McKinley name-reveal + Hanna-walk-across-floor                       |
  | Source URL                    | (Suno Pro generation URL)                                                                        |
  | License text quoted           | Suno Pro Commercial Use grant — paste exact paragraph from /terms-of-service as of generation date |
  | Attribution string for YT     | "Original cue 'Cornet — Found Him' generated with Suno Pro on YYYY-MM-DD; prompt: '1890s muted cornet single line, no accompaniment, slow, mournful'." |
  | Date downloaded               | YYYY-MM-DD                                                                                       |
  | Prompt                        | "1890s muted cornet single line, no accompaniment, slow, mournful"                                |
  | Model                         | Suno Pro v… (capture exact version string on /generate page that day)                            |
  | Generation date               | YYYY-MM-DD                                                                                       |
  | Paid-tier TOS screenshot path | assets/MUSIC_LICENSES/suno-tos-YYYY-MM-DD.png                                                    |
  | Blind-period-grain test       | A/B against UCSB cylinder cornet reference (e.g. cusb-cyl12821d) — UCSB CC BY-NC blocks shipping cylinder, but it's fine as a private blind reference; reject Suno cue if it fails. |

- **Why a stub at all:** L93 / L95 sit very tight against L97 [dry] (only 6–8 s window total per the locked cut). A modern late-romantic piano cue *might* read as "wrong instrument family" against a documentary about a 1888 RNC convention floor — a muted cornet single line solves both the texture and the period read in one move, IF the Suno cue passes blind-test. License expert needs to verify the Suno Pro commercial-rights grant covers ad-monetized YouTube specifically; this is exactly the open-question P2 raised about Internet Historian's Suno cues, and PLAN §2.5 / §3.6 are how we answer it.

**Top-pick defence (Cue B-1 against L21/L45/L63/L79/L93/L95):** see the per-line table under B-1 above. The reason B-1 wins over the cornet-stub is dependence — we can lock the picture against a real audio source today; we cannot lock against a Suno cue we haven't generated yet.

### Cue B ranking (TL;DR)
1. **B-1 Chopin Nocturne in C-sharp minor Op. posth. (Wikimedia Commons / IMSLP PD)** — single-line minor-mode parlor-piano fit; ships today.
2. **B-2 Chopin Nocturne in C minor B.108 (Musopen)** — second voice if B-1 is too iconic.
3. **B-3 Brahms Intermezzo Op. 76 No. 7 (Musopen)** — gravitas for L79 vote bleed if Chopin reads too sentimental.
4. **B-4 Schumann Träumerei (Musopen)** — major-mode flavour for L93/L95 McKinley-name reveal only; do NOT replace B-1 wholesale.
5. **B-5 Suno Pro muted cornet (stub)** — period-instrument win IF the cue passes blind-test AND the license expert clears the commercial-rights grant on the day-of-generation TOS.

---

## C. Cue C — closing-motif call (the open editorial decision)

**Recommendation: thinned reharmonization. Do not play full-volume over the end card.**

### Defence against L97 closing line + 3–4 s end card

L97 is "He didn't know it yet. But he had just found his president." This line is itself a [dry] climax — narration-annotated.txt §SCENE 4 marks it so explicitly. The cut therefore enters the end card from a place of voice-and-room-tone alone. There has been:

- ~12 s of cold-open dead air,
- 4 dry climaxes (L23, L67, L91, L97) that all played unscored,
- 1 silent-reveal at L81 with full music drop,
- the targeted 40–60% of the runtime unscored (~95–143 s of a 238 s piece per PLAN §3.3),
- and a re-entry at L83 on a single low piano note (transformed Cue A) that is the loudest the score gets in Act 3.

Coming out of all that restraint into a *full-volume* Cue C statement would announce that the score has been waiting to tell the audience how to feel. That contradicts PLAN §1.5 ("restraint reads as honesty; earn the swell") on this specific cut. The audience has just been respected for 238 s; a full swell at second 239 reads as the documentary breaking its own rules to say "now feel something." For a documentary about systemic political manipulation, that emotional manipulation reads as exactly the wrong author voice.

The thinned reharmonization is the correct move because:

1. **It honors the silence-as-cue rule already established.** The audience has been trained for ~95 s of the cut to read music's *thinness* as the doc telling them the truth. A thin Cue C lands inside that grammar, not outside it.
2. **It earns its swell on the recurrence, not the volume.** PLAN §1.2 (motif reuse beats cue variety) says the motif itself does the work by recognition. A thin reharmonization of Cue A into Cue B's minor-mode register makes the recognition land *because* it's quiet — the audience does the emotional work, not the mix.
3. **Project register matches LEMMiNO / Plainly Difficult, not Defunctland's emotional features.** P3's full-volume recommendation in OPINION.md is project-anchored to Defunctland's emotional-feature register where the topic earns full swells. Mark Hanna is a 5-min historical-corruption piece, not a 30-min emotional Disney park retrospective. The register difference is the whole game here.
4. **The end card is only 3–4 s.** A full statement of Cue A's contour reharmonized into Cue B's minor-mode register is ~6–8 s as a phrase. We cannot fit a full-volume statement in 3–4 s without truncating the phrase, which is exactly the §2.6 mid-phrase cut PLAN forbids. A thin reharmonization, by contrast, can be a single 3–4 s held chord — register and contour cited, no phrase truncated.
5. **P1 is right for THIS cut.** The 3-perspective synthesis already encodes the disagreement; the locked cut breaks the tie.

### Harmonic move (two sentences, per brief)

Cue C inherits Cue A's bell-strike contour (the descending 5–1 motion of the Liberty Bell opening) but reharmonizes it from A-major (Liberty Bell's home key) into C-sharp minor — Cue B-1's home key. The end card therefore plays a single sustained low piano note at C-sharp 1 with a thinned upper-voice fragment of the Liberty Bell descending 5–1, pp, decaying into 1 s of room tone before the final cut to black; one chord, one motif fragment, no full statement.

---

## Hand-off (links the editor needs first)

- A-1 Liberty Bell, Sousa's Band 1905 (Victor 1193): https://www.loc.gov/item/jukebox-118017/
- A-2 Liberty Bell, USMC Marine Band: https://www.marineband.marines.mil/Audio-Resources/The-Complete-Marches-of-John-Philip-Sousa/ (download from this index page)
- A-3 Liberty Bell, IMSLP Cypressdome 2013: https://imslp.org/wiki/File:PMLP06253-TheLibertyBell_March.mp3
- A-4 King Cotton, USMC Marine Band: same Marine Band index URL above
- A-5 Stars and Stripes Forever, Kendle's 1901 (Victor 1167): https://www.loc.gov/item/jukebox-213296/
- B-1 Chopin Nocturne C# minor Op. posth. (Wikimedia Commons / Musopen PD): https://commons.wikimedia.org/wiki/File:Chopin,_Nocturne_in_C-sharp_minor,_Op._Posth.ogg
- B-2 Chopin Nocturne C minor B.108: https://musopen.org/music/4428-nocturne-in-c-minor-b-108/
- B-3 Brahms Intermezzo Op. 76 No. 7: https://musopen.org/ (search "Brahms Intermezzo Op 76 No 7")
- B-4 Schumann Träumerei (Kinderszenen Op. 15 No. 7): https://musopen.org/music/2462-kinderszenen-op-15/
- B-5 Suno Pro muted cornet stub — generate at lock-time per PLAN §3.6

— Music expert, t_127ceb7f, 2026-06-06
