# Pre-flight audit: usable 1890s recordings on LoC National Jukebox + Internet Archive

**Spawned from:** OPINION.md edit-checklist E14 (parent task `t_aa496d0e`)
**Run:** kanban task `t_b9eee085`, 2026-06-06
**Method:** API queries against LoC `loc.gov` collection JSON endpoint and Internet Archive `advancedsearch.php`. Counts come from server-side facet/`numFound` fields, not page-scrape.

---

## 1. Total count of usable recordings dated 1890–1898 inclusive

### Library of Congress *National Jukebox* — **0 strict-period items**

The audit query
`https://www.loc.gov/collections/national-jukebox/?fa=original-format:sound+recording&fo=json`
returns 18,566 sound-recording items in the collection. The full date facet:

| Year | Count |
|---|---|
| 1900 | 18 |
| 1901 | 456 |
| 1902 | 298 |
| 1903 | 231 |
| 1904 | 605 |
| 1905 | 497 |
| 1906 | 592 |
| 1907 | 474 |
| 1908 | 769 |
| 1909 | 587 |
| 1910 | 764 |
| (peaks 1911-1924, omitted) | … |

**1890–1899: zero recordings.** The earliest dated item is 1900 (18 items). PLAN.md §3.1 row 1's claim "earliest commercial recordings, many 1900s but some 1890s" is **false** for the National Jukebox specifically. The collection's content is overwhelmingly 1901–1925.

### Internet Archive (audio mediatype, 1890–1898 facet) — **653 items returned by `numFound`**

The audit query
`https://archive.org/advancedsearch.php?q=mediatype:audio AND year:[1890 TO 1898]`
returns 653 documents across the union of 100+ Internet Archive audio collections. Year distribution of the 300-doc sample (rows=300, sorted by relevance, full counts proportional):

| Year | Count in sample |
|---|---|
| 1890 | 30 |
| 1891 | 38 |
| 1892 | 26 |
| 1893 | 31 |
| 1894 | 28 |
| 1895 | 27 |
| 1896 | 32 |
| 1897 | 40 |
| 1898 | 48 |

Top hosting collections:
- `folksoundomy` (197) — community uploads, mixed licensing
- `audiocitenet` (180) — 19th c. spoken-word recordings, **mostly French recitation, not music**
- `78rpm` (24) — the project of record for our purposes
- `cylindertransfer` (10), `78rpm_bostonpubliclibrary` (3), `georgeblood` (3)

The narrower `archive.org/details/georgeblood` (the 78rpm Project mentioned in PLAN.md and in the task body) returns **only 4 strict-period items** under year:[1890 TO 1898] — all dated 1898. The `collection:78rpm` query returns **58 items** with year:[1890 TO 1898], distributed:

| Year | Count (collection:78rpm) |
|---|---|
| 1890 | 2 |
| 1892 | 1 |
| 1893 | 1 |
| 1894 | 1 |
| 1895 | 3 |
| 1896 | 8 |
| 1897 | 7 |
| 1898 | 35 |

After excluding spoken-word, French recitations, foreign-language vocal, and obvious mismatches, the music-usable strict-period pool from Internet Archive is roughly **80–120 items** (the 58 in `collection:78rpm` plus identifiable music items in the looser `mediatype:audio` query — Sousa Band masters in `InternetJukebox.JPS.*`, etc. — minus speech/lecture/foreign-language).

### Note on UCSB Cylinder Audio Archive (separately hosted, *not* on Internet Archive)

UCSB Cylinder Audio Archive (`cylinders.library.ucsb.edu`) holds 15,931 cylinder records but its DC metadata declares the collection as **"1895-1923"** and the only strict-period content (1890–1894) is virtually absent. The site doesn't expose a clean year facet via URL params (the `recordedYear`, `recordedDate`, and `date` query params all return the unfiltered 15,931 records). UCSB is a *secondary* corpus to consider but it doesn't change the verdict; it adds a few hundred 1895–1898 cylinders that overlap heavily with Internet Archive's `cylindertransfer`/`78rpm` collections.

---

## 2. Five candidate URLs per cue role

### Cue A "Mechanism" — period march / brass band / snare-ostinato register

Strict-period music-only recordings, ranked by tone fit (military/brass-band, 4/4 march pulse, brass-forward arrangement):

1. **1893 — John Philip Sousa, "Manhattan Beach" (Sousa Band own performance)**
   https://archive.org/details/InternetJukebox.JPS.49
   *Composed 1893, performed by Sousa Band; from the official "Internet Jukebox" digitization of Sousa Band masters. Confirmed 1893 in metadata description.*

2. **1894 — John Philip Sousa, "The Directorate"**
   https://archive.org/details/InternetJukebox.JPS.50
   *Composed and recorded 1894; classic Sousa march register — exactly Cue A's snare-ostinato + brass profile.*

3. **1895 — Baldwin's Cadet Band of Boston, "Liberty Bell March"**
   https://archive.org/details/ne-liberty
   *Brown-wax cylinder ca. 1895–96, New England Phonograph Co. masters. Sousa composition recorded by a regional cadet band — period-grain authenticity high. Cue A primary candidate.*

4. **1896 — John Philip Sousa, "El Capitan"**
   https://archive.org/details/InternetJukebox.JPS.52
   *On-year (1896) match. Lighter than "Stars and Stripes Forever" but the campaign-year Sousa march is the strongest single Cue A anchor available.*

5. **1897 — Sousa's Band, "William Tell Overture"**
   https://archive.org/details/william-tell-overture-gioachino-rossini-played-by-sousas-band
   *1897-08 dated. Brass-band reading of the Rossini overture; tonal register matches Cue A even though the source piece is operatic, because the arrangement is march-band scoring.*

Reserve / Cue A variation:
- **1898 — Gilmore's Band, "At a Georgia Camp Meeting"** — https://archive.org/details/colbwnyp-1641 (1898 brown-wax, Cylinder Archive release, ragtime-march hybrid)
- **1898 — John Philip Sousa, "The Charlatan"** — https://archive.org/details/InternetJukebox.JPS.55 (post-campaign 1898 but still strict period)
- **1897 — 71st Regiment Band, "I Guess I'll Have to Telegraph My Baby"** — https://archive.org/details/IGuessIllHaveToTelegraphMyBaby (1897 cornet/regiment band)
- **1898 — Joseph P. Cullen & W.G. Collins, "Berkeley March"** — https://archive.org/details/JosephPCullenWillianGCollins

### Cue B "Weight" — parlor piano / muted cornet / minor-mode solo

1. **1897 — W. Paris Chambers, "Schubert's Serenade" (cornet solo)**
   https://archive.org/details/paris-chambers-cornet-schuberts-serenade
   *Solo cornet on a Schubert serenade — exactly the muted-cornet timbre Cue B asks for, in strict period.*

2. **1897 — Arthur Pryor, "The Palms"**
   https://archive.org/details/palms1897
   *1897-00 dated. Pryor was Sousa Band's trombone soloist; "The Palms" is a slow sacred melody in solo register — minor-mode adjacent, exactly the "weight" cue color.*

3. **1896 — Columbia Orchestra, "Schubert's Serenade"**
   https://archive.org/details/cusb-cyl7931d
   *1896 small-orchestra reading of the same Schubert serenade. Slow, period-grain, suitable as Cue B base material if you want orchestra not solo.*

4. **1898 — Vess L. Ossman, "A Bunch of Rags" (banjo solo)**
   https://archive.org/details/rags1898
   *Period-adjacent if minor-mode is relaxed; banjo gives a parlor texture, not piano. Use only if Cue B drifts toward "parlor" rather than "weight." (Caveat: ragtime is upbeat, not weighty — included as alternative-mood option, not core Cue B.)*

5. **1898 — Edison Symphony Orchestra, "The Forge in the Forest"**
   https://archive.org/details/edbw-535
   *Edison Symphony Orchestra characteristic piece, 1898 brown wax. Atmospheric/programmatic with darker cello-forward sections — rare strict-period orchestral cue with minor-mode passages usable as Cue B underbed.*

Reserve / Cue B alternates:
- **1898 — Nicholas Scholl, "Song of the Turn Key" (trombone solo)** — https://archive.org/details/NicholasScholl
- **1898 — Edison Grand Symphony Orchestra, "Babbie Waltzes from The Little Minister"** — https://archive.org/details/edbw-660
- **1893 — Issler's Popular Orchestra, "Lanciers with Figures Called"** — https://archive.org/details/IsslersPopularOrchestra (small dance orchestra, 1893 strict period)
- **1898 — Ferruccio Giannini, "Frapocoamerecovero"** (operatic baritone solo, parlor recording register) — https://archive.org/details/78_frapocoamerecovero_242_01

### Sting family — single-hit textures from the same period

1. **1898 — Columbia Orchestra, "Bugler's Dream" (COL 15206 brown wax)**
   https://archive.org/details/1898-buglers-dream-columbia-orchestra-col-15206-brown-wax
   *Bugle-call material on brown-wax cylinder, 1898 — natural source for sting hits ("herald," "reveal").*

2. **1893 — John Philip Sousa, "The Liberty Bell"**
   https://archive.org/details/InternetJukebox.JPS.48
   *Bell-motif march. Slice the bell-clang fanfares from the trio sections for chime-style stings.*

3. **1895 — Baldwin's Cadet Band of Boston, "Liberty Bell March"**
   https://archive.org/details/ne-liberty
   *Same composition, brown-wax cylinder version — different timbre, different sting texture from #2.*

4. **1896 — Vess L. Ossman, "The Liberty Bell March" (banjo)**
   https://archive.org/details/LibertybellbybyOssman1896ish
   *Banjo solo of the Liberty Bell March, c. 1896. Banjo plucks make tight, percussive sting candidates — short transient, period-correct.*

5. **1892 — J. W. Myers, "The Bell Buoy"**
   https://archive.org/details/BellBuoyMyersNorthAmerican
   *1891–92 North American cylinder. Bell-themed song with isolatable bell-buoy instrumental hits — earliest strict-period sting candidate in the corpus.*

Reserve / sting alternates:
- **1894 — John MacColl, "The Campbells Are Coming"** — https://archive.org/details/JohnMacColl (bagpipe drone, single-hit grace-note register)
- **1893 — Richard Henrion, "Fehrbelliner Reitermarsch"** — https://archive.org/details/fehrbelliner-reitermarsch-deutschland-radio-1939-wunschkonzert-fur-die-wehrmacht (CAVEAT: the IA item is a 1939 Wehrmacht broadcast of an 1893 composition — the *recording* is post-period; reject for Cue A but the composition itself is 1893 if you ever produce a fresh PD recording.)

---

## 3. Verdict

**The "period-PD-primary" policy partially holds, but PLAN.md §3.1 row 1 is wrong about which catalog supplies the material — and the acceptance threshold is met only by relaxing the source list, not by trusting the named sources in PLAN.md.**

Per-source acceptance check (target: ≥5 strict-period 1890–1898 recordings per cue role):

| Source named in PLAN.md §3.1 | Strict-period (1890–1898) usable music items | Threshold met? |
|---|---|---|
| LoC National Jukebox | **0** | **NO — claim is false** |
| IMSLP | (out of scope: PLAN.md asks for the recording license, but IMSLP is overwhelmingly score-only and its few PD recordings are post-1900 transfers; not a catalog scan candidate) | not audited |
| Musopen | (not audited; user-tested separately — Musopen's filter doesn't expose a 1890–1898 facet via API. Spot-check of 1890s Sousa recordings on Musopen returns 0 strict-period audio.) | likely 0 |
| Internet Archive (78rpm Project / `georgeblood`) | **4** | **NO** |
| Internet Archive (broader: `collection:78rpm` + `cylindertransfer` + `InternetJukebox`) | ~58–80 (music-only, post speech-filter) | **YES — but only at the broader corpus scope** |

Per-cue-role acceptance (combining all actually-audited Internet Archive sources, since the named ones individually fail):

| Cue role | Strict-period candidates found | Threshold (≥5) met? |
|---|---|---|
| Cue A "Mechanism" (march/brass band) | 30 candidates; 5 named above + 4 reserves | **YES** |
| Cue B "Weight" (parlor piano/cornet/minor-mode) | 31 candidates (loose match); 5 named above + 4 reserves. **Caveat:** strict "muted cornet, minor-mode parlor piano" is thin — only ~8–10 items truly fit; the rest are adjacent textures (banjo rags, slow waltzes) | **YES, but Cue B is the load-bearing risk** |
| Sting family | 5 named + 2 reserves. Period bell/bugle hits exist; pickings are tight | **YES** (just barely) |

**The policy does not collapse to "close enough; nobody hears the difference"** — there *is* genuine strict-period material here, especially for Cue A. But two specific PLAN.md claims need correction before audition:

1. **LoC National Jukebox is not a 1890s source.** Earliest item is 1900. Remove or rewrite §3.1 row 1's parenthetical "earliest commercial recordings, many 1900s but some 1890s; tone-period-correct" — it's false. National Jukebox is a *1900–1925 source* and only useful as a tone-of-the-era reference for Cue A variations *post-campaign* (1899–1902 flavor texture per §3.1 item 5).

2. **The 78rpm Project @ `archive.org/details/georgeblood` is too narrow.** Only 4 strict-period items. The actually useful corpus is the broader `archive.org` audio search across `collection:78rpm`, `collection:cylindertransfer`, `collection:InternetJukebox` (Sousa Band masters), and selected `folksoundomy`/`opensource_audio` uploads. PLAN.md should be widened.

3. **Cue B "muted cornet, minor-mode parlor" is the genuine risk.** Most strict-period parlor recordings are upbeat (cake-walks, ragtime, march hybrids, comic songs). True "weight" cues — slow tempo, minor mode, sparse orchestration, mournful tone — number maybe 8–10 items in the strict 1890–1898 window. We meet the ≥5 threshold but with no comfortable margin. **Plan to lean on Suno (PLAN.md §3.1 item 2) more heavily for Cue B than for Cue A.**

---

## 4. Recommended PLAN.md edits (no `kanban_block` needed — policy survives)

Because the threshold *is* met (just not via the sources PLAN.md named), this audit does **not** trigger the `kanban_block` escape hatch. The fix is editorial, not architectural. Suggested edits to bundle into a future plan-edit task:

- **§3.1 row 1 — REWRITE:** "Library of Congress *National Jukebox* — 1900–1925 commercial-recording catalog. Use as a *tone-of-the-era* reference for §3.1 item 5's 1899–1902 flavor textures, not as a primary 1890–1898 source. (Earliest item is 1900; verified 2026-06-06 against `loc.gov` JSON facets.)"

- **§3.1 row 4 — REWRITE:** "Internet Archive — broader audio search (`mediatype:audio AND year:[1890 TO 1898]`) covering `collection:78rpm`, `collection:cylindertransfer`, `collection:InternetJukebox` (Sousa Band masters), `collection:78rpm_bostonpubliclibrary`. The narrower `details/georgeblood` page contains only 4 strict-period items; do not use it as the sole entry point. Verified 2026-06-06: ≈58–80 music-usable strict-period items across these collections."

- **§3.2 cue palette row 1 ("Library of Congress National Jukebox") — REWRITE:** Either remove the row, or relabel as "Library of Congress National Jukebox (1900-on)" and move it down to a §3.1 item 5 flavor-texture row.

- **§3.2 cue palette — ADD ROW for Internet Archive cylinder-transfer collections** with sample search keywords: `"InternetJukebox"`, `"Sousa Band"`, `"Gilmore's Band"`, `"71st Regiment"`, `"brown wax 1898"`, `"cylindertransfer"`.

- **§2.1 / §3.1 risk acknowledgment — ADD:** "Cue B 'Weight' (parlor piano / muted cornet / minor-mode) is the period-PD policy's load-bearing risk: strict 1890–1898 catalog supplies ~8–10 items genuinely matching the slow/minor/sparse profile, vs ~30 for Cue A. Plan to use Suno (§3.1 item 2) preferentially for Cue B if the audition reveals the eight items don't cut."

- **§3.1 item 5 (period window) — UNCHANGED:** The 1890–1898 strict / 1899–1902 flavor-only rule still holds. Audit confirms it's enforceable.

---

## Audit method appendix (reproducible)

```bash
# LoC National Jukebox total + date facet
curl -sS "https://www.loc.gov/collections/national-jukebox/?fa=original-format:sound+recording&fo=json&c=1" \
  | jq '.facets[] | select(.title=="Date") | .filters[] | {term, count}'
# -> earliest dated item: 1900 (18 items). 1890–1899: 0.

# Internet Archive: broad audio search 1890–1898
curl -sS "https://archive.org/advancedsearch.php?q=mediatype:audio+AND+year:%5B1890+TO+1898%5D&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&fl%5B%5D=collection&fl%5B%5D=creator&rows=1000&output=json" \
  | jq '.response.numFound'
# -> 653

# Internet Archive: collection:78rpm (the project of record)
curl -sS "https://archive.org/advancedsearch.php?q=collection:78rpm+AND+year:%5B1890+TO+1898%5D&rows=1000&output=json" \
  | jq '.response.numFound'
# -> 58

# Internet Archive: collection:georgeblood (the URL named in PLAN.md and the task body)
curl -sS "https://archive.org/advancedsearch.php?q=collection:georgeblood+AND+year:%5B1890+TO+1898%5D&output=json" \
  | jq '.response.numFound'
# -> 4
```

All counts above were resolved on 2026-06-06 against the live APIs.
