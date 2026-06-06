# Perspective: License Expert

> 3-perspective audition for the Mark Hanna documentary score (Music / License / Technical).
> Written *before* the music-expert paper landed — `research/music/PERSPECTIVE-MUSIC.md`
> did not exist when this audit ran. This is therefore a **per-source PD/license pre-flight
> checklist** the music expert can apply to whatever they pick, plus a Content ID dispute
> kit. Sources audited per PLAN §3.5: LoC National Jukebox, IMSLP, Musopen, Internet
> Archive (Great 78 Project), Free Music Archive, Suno Pro.
>
> Constraints honored: no fair-use language anywhere; no paid subscriptions added; PLAN
> §3.1 strict period window 1890–1898 (1899–1902 texture-only) treated as binding.

---

## TL;DR verdict (per-source)

| Source                              | Verdict     | One-line reason |
|---|---|---|
| LoC National Jukebox                | **TRAP**    | Recording layer is PD pre-1923 under MMA, **but** the LoC explicitly licenses some items from rightsholders (Sony) — must verify per item. Period-window match is partial (collection dates 1900–1925; some 1890s items exist but are rare). |
| IMSLP (recordings tab)              | **TRAP**    | Score license ≠ recording license. Naxos masters of PD Sousa are still under label copyright. Many IMSLP files are "Public Domain in Canada / Non-PD in US" — wrong jurisdiction for a US-uploaded YouTube doc. |
| Musopen                             | **CLEAN-ish** | Most recordings dedicated CC0 or PD per-track, but license is per-item — must check each track page. Repertoire skews late-romantic / classical, not 1890s march/parlor; period-window fit is weak for Cue A. |
| Internet Archive (Great 78 Project) | **TRAP**    | Per-item rights labels (often "Public Domain Mark 1.0" or "CC0 1.0"), but transfers can fingerprint-match modern label remasters and trigger Sony/Naxos auto-claims on YouTube. Period match is the strongest of any source for Cue A base material. |
| Free Music Archive                  | **TRAP**    | Per-track CC license — may be CC-BY, CC-BY-NC, CC-BY-SA, CC0, etc. NC variants are disqualifying for ad-monetized YouTube. PLAN §3.1 already restricts FMA to **named composers** as tertiary fallback. |
| Suno Pro                            | **BLOCKER until on-cue** | ToS grants paid users ownership + commercial rights, but Suno explicitly reserves the right to enroll outputs into Content ID. Means *another* Suno user could already be claiming a similar generation. AI-cue blind-test in PLAN §3.5 footnote is mandatory. |

**Summary for the editor:** there is no source on the §3.5 shortlist that is "drop-in safe."
Every cue must clear the four-field provenance log in `assets/MUSIC_LICENSES.md` (skeleton
delivered alongside this paper) and then survive the unlisted-upload Content ID scan
before public publish (PLAN §3.6). The dispute kit at the bottom of this file is the
fallback when (not if) a claim arrives.

---

## Per-source detail

### 1. Library of Congress — National Jukebox

**Live license page:** `https://www.loc.gov/collections/national-jukebox/about-this-collection/rights-and-access/`

**Quoted clause (collection-level rights statement):**

> "The Library makes the sound recordings in the National Jukebox available pursuant to permission from the rightsholders. … Under the Music Modernization Act, many of these recordings will begin entering into the public domain on January 1, 2022, when all recordings published prior to 1923 will enter the public domain and will be free to use and reuse. Recordings published between 1923 and 1946 are then protected for 100 years, and recordings published between 1947 and 1956 are protected for 110 years. … You are responsible for deciding whether your use of the items in this collection is legal. You will need written permission from the rightsholders to copy, distribute, or otherwise use copyrighted materials except as allowed by fair use or other statutory exemptions."

**Composition vs. recording — the Jukebox trap.** The Music Modernization Act (17 U.S.C.
§1401) only addresses the *sound recording* layer. A pre-1923 recording is PD under the
MMA, but the *underlying composition* could still be under copyright if the song was
published more recently than the recording (rare for 1890s repertoire) or if someone
later registered an arrangement. LoC's own Citizen DJ guide spells this out:

> "In order to use a sound recording for free without permission, you need to look at the copyright of (1) the sound recording itself, and (2) underlying compositions or texts, such as song composition and lyrics."  
> — `https://github.com/LibraryOfCongress/citizen-dj/blob/master/guide.md`

**For the Mark Hanna 1890s-repertoire case** the composition layer is almost always
clean (Sousa marches published 1888–1898 are pre-1929 → PD by composition term too;
parlor songs from the same window same story). The trap to check: any item where the
composer died after 1955 or the composition was first published after 1929.

**Period window:** the National Jukebox is dated **1900–1925** by the LoC's own
description — not 1890s. There are some 1898–1900-edge items (early Berliner discs,
Edison cylinders) but the bulk of the collection is post-1900. **PLAN §3.1 item 5 says
1899–1902 is texture-only, not Cue A base material.** Most National Jukebox items
*disqualify themselves on period grounds before licensing even matters.*

**Action:** for any candidate the music expert pulls from National Jukebox, verify
**publication date ≤ 1898** before doing anything else. If 1899–1902, demote to
texture-only / sting-fodder. If post-1902, reject outright.

**Attribution string template (YouTube description):**

```
"<Title>" performed by <Performer>, recorded <Year>.
Source: Library of Congress National Jukebox (https://www.loc.gov/jukebox/recordings/detail/id/<ID>/).
Sound recording in the public domain in the United States under the Music Modernization Act
(17 U.S.C. §1401), pre-1923 published.
```

**Content ID failure modes specific to LoC:**
- Sony Music co-curated National Jukebox at launch (the SCE/SME deal). Sony's ContentID
  catalog includes many remasters of the same Edison/Victor masters the Jukebox
  digitized. **Auto-claim by Sony on a Sousa march pulled from LoC is the textbook
  case.** It is not evidence of bad provenance — it's a fingerprint collision.
- Naxos has issued historical-recordings remasters of much of the same period
  repertoire (Naxos Historical line). Same auto-claim mechanism.
- Some uploads have triggered claims from third-party "rights administrators" who
  ingested public-domain transfers into ContentID under their own label name. These
  are aggregator parasites; the dispute kit below handles them.

**Dispute language to paste into YouTube's dispute form (for an LoC item):**

```
This recording is in the United States public domain. Sound recording published in
<YEAR>, which is pre-1923 and therefore in the public domain under 17 U.S.C. §1401 (the
Music Modernization Act of 2018) effective 1 January 2022.

Source: Library of Congress National Jukebox, item URL <LoC item URL>.
LoC rights statement: "all recordings published prior to 1923 will enter the public
domain and will be free to use and reuse"
(https://www.loc.gov/collections/national-jukebox/about-this-collection/rights-and-access/).

The composition <COMPOSITION TITLE> by <COMPOSER> was published in <YEAR>, before 1929,
and is therefore also in the United States public domain (17 U.S.C. §302).

I assert that this Content ID claim is in error and that I have the right to use this
public-domain recording.
```

---

### 2. IMSLP (Petrucci Music Library)

**Live license page:** `https://imslp.org/wiki/IMSLP:Copyright_Made_Simple`

**Quoted clause:**

> "IMSLP is hosted in Canada. Canadian copyright law generally protects works for 70 years after the death of the composer or editor. Works that are public domain in Canada may still be under copyright in other countries, including the United States."

**The two-jurisdiction trap.** A typical IMSLP file page tags rights as:

> "Public Domain — Non-PD US"

This is the single biggest IMSLP gotcha for a US-uploaded YouTube documentary. An item
that's PD in Canada but **Non-PD US** is a copyright violation if you upload from / to
US-jurisdiction infrastructure. **For this project, only use IMSLP items tagged
"Public Domain" with no "Non-PD US" qualifier**, OR items where IMSLP shows the file
is PD in the US specifically (composer died ≥ 95 years before publication, or
publication ≥ 1929).

**Composition vs. recording.** IMSLP hosts both. A 1896 Sousa march **score** can be
PD (composition published pre-1929, definitely US-PD), but a **2003 Naxos recording
of that score** hosted on IMSLP is fully copyrighted by Naxos and only available for
streaming, not download/reuse. PLAN §3.1 item 1 says "Use the *recording* license, not
just the score license." This is what it means.

**Period window:** IMSLP scores match the 1890s window cleanly for Sousa (Liberty Bell
1893, Stars and Stripes Forever 1896, Manhattan Beach 1893), Joplin's Original Rags
1899 (period-adjacent — texture-only per PLAN §3.1 item 5), period band arrangements,
and parlor-piano collections. **For recordings**, IMSLP's coverage of the 1890s is
weak — most recordings hosted there are mid-20th-century or modern, not period
transfers. Do not pull recordings from IMSLP for Cue A.

**Attribution string template:**

```
Score: <Title> by <Composer>, published <Year>. Public domain in the United States
(published before 1929, 17 U.S.C. §302). Source: IMSLP / Petrucci Music Library
(https://imslp.org/wiki/<page>).
```

**Content ID failure modes specific to IMSLP:**
- If you record your own performance of a PD IMSLP score, you control the master and
  ContentID claims are easy to dispute (the recording is yours).
- If you reuse a recording hosted on IMSLP, see above — most are stream-only Naxos /
  label content and you should not be reusing them in the first place.
- IMSLP audio uploads under CC-BY are the safer reuse path; check the file page CC tag.

**Dispute language for an IMSLP-sourced score recorded in-house:**

```
This recording is an original performance of a public-domain composition. The
underlying composition <TITLE> by <COMPOSER> was published in <YEAR>, before 1929, and
is in the United States public domain (17 U.S.C. §302). Score source: IMSLP
(https://imslp.org/wiki/<page>).

The sound recording is original to this video, recorded by <YOUR NAME> on <DATE>; I
own the recording rights in full. Any Content ID match is a false positive against
the underlying public-domain composition or against a separate recording of the same
work.
```

---

### 3. Musopen

**Live license page:** `https://musopen.org/about/license/` (per-track licenses also
shown on each track's individual page).

**Per-track license model.** Musopen does not have a single blanket license. Tracks
are tagged per-item as one of:
- **Public Domain Mark** (composition + recording both PD)
- **CC0 1.0 Universal** (recording dedicated to public domain by performer)
- **Creative Commons Attribution** (CC-BY 3.0 or 4.0)
- occasional **CC-BY-SA**

**For ad-monetized YouTube** all of the above are safe. **Avoid CC-BY-NC** if it
appears (NonCommercial conflicts with monetization); confirm per-track that the tag
is *not* `-NC`.

**Composition vs. recording trap.** Performer dedicates the *recording* to the
public domain via CC0. The *composition* must independently be PD or properly
licensed. For Musopen's late-romantic / classical repertoire this is almost always
true (Brahms, Chopin, Beethoven, late-19th-century salon piano), but the rule still
applies — confirm composer death + publication date.

**Period window:** Musopen's catalog is broad classical/late-romantic. **For our
1890s window:** Brahms (d. 1897), Tchaikovsky (d. 1893), Dvořák (d. 1904) are all
in-window or period-adjacent for *composition*; recordings hosted on Musopen are
modern performances, so the *recording* dates are 20th–21st century. This means
Musopen recordings are **not period-grain authentic** (a 2010 recording of an 1893
Tchaikovsky piano piece sounds like 2010, not 1893). Per PLAN §3.2, Cue B "Weight"
allows "Single-line minor-mode melody on solo piano OR muted cornet" — Musopen
covers solo piano in this register cleanly. **Cue A "Mechanism" needs period-grain
texture (snare ostinato / military march); Musopen is the wrong source for Cue A.**

**Attribution string template:**

```
"<Title>" by <Composer>, performed by <Performer>. Source: Musopen
(https://musopen.org/music/<ID>/). Released under <CC0 / CC-BY 4.0 / Public Domain Mark>;
license terms at <license URL>.
```

**Content ID failure modes:**
- Musopen-hosted CC0 piano recordings have been claimed on YouTube by labels with
  competing modern recordings of the same composition (fingerprint collisions on
  shared melodic content). Less common than the LoC/Naxos pattern but it happens.
- Some Musopen tracks were re-uploaded to streaming services by aggregators who then
  claim them on YouTube. The Musopen license URL is the dispute weapon.

**Dispute language for a Musopen track:**

```
This recording is licensed under <CC0 1.0 Universal / CC-BY 4.0 / Public Domain Mark>
via Musopen. Source URL: https://musopen.org/music/<ID>/. License terms (live):
<paste exact license URL from track page>.

The underlying composition <TITLE> by <COMPOSER> (d. <YEAR>) was published in
<YEAR>, before 1929, and is in the United States public domain. The recording was
released by the performer under the cited Creative Commons license, which expressly
permits commercial use (with attribution where applicable; attribution is provided
in the video description).
```

---

### 4. Internet Archive — Great 78 Project / 78rpm collections

**Live archive home:** `https://great78.archive.org/`
**Per-item rights:** shown in the "Usage" field of each archive.org item page.

**Quoted clause (typical Usage label, per-item):**

> "Usage: Public Domain Mark 1.0"

or:

> "Usage: CC0 1.0 Universal"

The Great 78 Project does **not** have a blanket CC0 dedication. Each transfer's Usage
label is set per-item based on the recording's underlying status. Most pre-1923
American 78s are tagged **Public Domain Mark 1.0** (the recording is PD under MMA;
the IA transfer itself is treated as a non-creative reproduction, so no new copyright
attaches).

**Composition vs. recording.** Same MMA logic as LoC National Jukebox. Pre-1923
sound recording → PD. Composition → needs independent PD verification. For 1890s
march/parlor/early-78 repertoire the composition layer is essentially always PD by
publication-date term.

**Period window — this is the strongest Cue A match.** Great 78 hosts roughly
**400,000 transfers**, with deep coverage of the 1898–1925 commercial-recording
era. Items dated 1898–1902 (period-adjacent per PLAN §3.1 item 5) are common; items
strictly 1890–1898 are rarer but exist (early Berliner discs, some 1898 cylinders).
**Recommend the music expert filter Great 78 search by publication-year ≤ 1898 for
Cue A "Mechanism" base material**, and ≤ 1902 for sting-family / texture material
only.

**Attribution string template:**

```
"<Title>" performed by <Performer>, recorded <Year>. Source: Internet Archive,
Great 78 Project (https://archive.org/details/<item-id>).
Usage: <Public Domain Mark 1.0 / CC0 1.0 Universal> per item page.
Sound recording in the United States public domain (pre-1923, 17 U.S.C. §1401).
```

**Content ID failure modes specific to Internet Archive:**
- **The classic Great 78 trap:** modern label remasters (Naxos Historical, Sony
  Legacy Recordings, JSP Records) of the same wax cylinder / 78 master are in
  ContentID. An IA transfer fingerprints close enough to the remaster to trigger an
  auto-claim. The IA transfer is *unrestored* and the label remaster is *restored*,
  but acoustic-fingerprint algorithms collapse the two.
- The RIAA-aligned Great 78 lawsuit (UMG et al. v. Internet Archive, 2023, settled
  September 2025 — see `https://www.digitalmusicnews.com/2025/09/16/great-78-project-lawsuit-settlement/`)
  was about *post-1923* transfers IA had hosted under the same project. **Pre-1923
  transfers from Great 78 are explicitly outside the settlement's scope and remain
  hosted with their PD/CC0 Usage labels intact.** This is good — but the existence
  of the settlement means labels are paying attention to Great 78 specifically;
  ContentID enforcement on IA-sourced material is more aggressive than on LoC.
- Aggregator parasites (small "labels" that re-upload PD transfers and claim them)
  are common on Great 78 material. Same dispute pattern.

**Dispute language for a Great 78 item:**

```
This recording is in the United States public domain. The sound recording was
published in <YEAR>, which is pre-1923 and therefore in the United States public
domain under 17 U.S.C. §1401 (Music Modernization Act of 2018) effective 1 January
2022.

Source: Internet Archive, Great 78 Project, item URL <item URL>.
Item Usage label: "<Public Domain Mark 1.0 / CC0 1.0 Universal>" as displayed on
the item page.

The composition "<TITLE>" by <COMPOSER> was published in <YEAR>, pre-1929, and is
in the United States public domain (17 U.S.C. §302).

This Content ID claim appears to match against a modern remaster of the same
underlying public-domain master recording. The transfer used in this video is the
unrestored Internet Archive transfer, not the claimant's remaster, and is in the
public domain in its own right. I assert that the claim is in error.
```

---

### 5. Free Music Archive (FMA)

**Live license page:** `https://freemusicarchive.org/terms-of-use/`

**Quoted clause:**

> "All music on Free Music Archive is either in the public domain or licensed under Creative Commons licenses."

> "Each track on Free Music Archive has its own license, selected by the artist or rightsholder. You must follow the specific license terms indicated on the track page."

> "Free Music Archive does not own the copyrights in the music; rights remain with the artists/labels. We provide a platform where they can share their work under open licenses."

**License variants on FMA:**
- CC0
- CC-BY (Attribution)
- CC-BY-SA (ShareAlike)
- CC-BY-NC (NonCommercial — **disqualifying** for ad-monetized YouTube)
- CC-BY-NC-SA (also disqualifying)
- CC-BY-NC-ND (disqualifying)
- CC-BY-ND (technically allowed but conflicts with our edit-as-needed workflow;
  prefer to avoid)

**For the Mark Hanna doc the only acceptable FMA licenses are CC0 and CC-BY (any
version).** Anything containing `-NC` is excluded by ad-monetization; anything
containing `-ND` is excluded by the need to edit / fade / phrase-cut per PLAN §3.4.

**Composition vs. recording.** FMA tracks are typically original works by the
artist who uploaded them — both composition and recording rights are granted by
the same CC license. The trap is FMA tracks that are **covers of copyrighted
songs**: the artist can release their *recording* under CC-BY, but they cannot
release the *composition* (which they don't own). For a 19th-century-aesthetic
documentary this is unlikely to come up, but if a track sounds like a cover of
something contemporary, audit before using.

**Period window.** FMA has **zero** authentic 1890s recordings (the format didn't
exist for community uploads). FMA's role is **named-composer modern works in a
period-evocative style** — period band arrangements, parlor-piano-aesthetic
originals, modern Sousa-style marches. PLAN §3.1 item 3 already restricts FMA to
"named CC-BY artists … (not the anonymous keyword-stuffed kind)." **FMA is
tertiary fallback only.** Do not use FMA for Cue A or Cue B unless PD and AI both
fail; if it ships, the composer's name goes in the description with a CC-BY
notice and a link to the track page.

**Attribution string template (CC-BY):**

```
"<Title>" by <Artist Name>, source: Free Music Archive
(https://freemusicarchive.org/music/<artist>/<album>/<track>). Licensed under
Creative Commons Attribution <version> (https://creativecommons.org/licenses/by/<version>/).
Used with attribution per the license.
```

**Content ID failure modes:**
- Some FMA tracks have been ingested into ContentID by aggregators (DistroKid,
  TuneCore) at the artist's request, then re-claimed when used by third parties.
  Dispute with the FMA URL + license tag.
- CC-BY-SA tracks are technically ShareAlike-compatible with our usage, but if
  the documentary is uploaded under YouTube's standard license (not CC-BY), some
  argue this is a license violation. **Safer to stick to CC-BY (non-SA) and CC0
  on FMA for this project.**

**Dispute language for an FMA track:**

```
This track is licensed under Creative Commons <CC-BY-3.0 / CC-BY-4.0 / CC0> by the
artist <ARTIST NAME>. Source URL: <FMA track page>. License terms (live):
<https://creativecommons.org/licenses/by/4.0/>.

Attribution to the artist is provided in the video description as required by the
license. The license expressly permits commercial use. I assert that this Content
ID claim is in error or that the claimant does not have rights superior to the
artist's CC license.
```

---

### 6. Suno (paid Pro tier)

**Live ToS:** `https://suno.com/terms`

**Quoted clauses (paid-tier, current as of audit date — re-screenshot at generation
time per PLAN §3.6):**

> "If you are using a paid plan, you own all rights, title and interest in and to the Outputs you create, including all intellectual property rights therein, to the fullest extent permitted by applicable law."

> "Users on paid plans may use their Outputs for any lawful purpose, including for commercial purposes, such as distribution, public performance, synchronization with audiovisual content, and monetization, subject to these Terms."

> "You acknowledge and agree that Suno may submit or allow the submission of Outputs to content identification systems (including YouTube Content ID or similar services) for the purpose of helping you manage your rights and enforce against unauthorized uses."

> "Suno reserves and retains all rights, title and interest in and to the Services, the Suno Materials, and any Outputs to the extent they incorporate Suno Materials or other content owned by Suno or its licensors."

**The Suno paradox.** Paid users get ownership of outputs *and* Suno reserves the
right to enroll outputs into ContentID. This means:
1. You can monetize your Suno cue on YouTube under the paid-plan license.
2. **Another Suno user could generate a near-identical cue and submit it to
   ContentID through DistroKid / TuneCore / direct ingestion**, which then claims
   *your* upload as theirs.
3. ContentID treats the first-claimant as the owner until disputed.

This is the failure mode PLAN §2.5 alluded to ("Internet Historian's recent Suno
cues as a wildcard with unsettled licensing"). PLAN §3.6 answers it: log
prompt + model + generation date + paid-tier TOS screenshot, upload unlisted,
wait for ContentID scan, dispute if claimed.

**Period window.** Suno can produce period-style instrumental output, but
**period-grain authenticity** (wax cylinder hiss, 1890s recording artifacts) is
hard to prompt for and easy to over-do (uncanny-valley territory). PLAN §3.5
footnote *: AI cues require an A/B audition against an LoC reference recording
from row 1; reject any AI cue that fails a blind period-grain test. **License
expert agrees with this rule.** If the AI cue fails blind-test, the cue is not
just inauthentic, it's *also* more likely to fingerprint-collide with mainstream
Suno-style outputs already in ContentID.

**License-expert specific recommendation for Suno cues:**
- Generate exclusively on a paid (Pro/Premier) plan.
- **Screenshot the paid-tier TOS** (`https://suno.com/terms`) on the *day of
  generation*, save it as `assets/suno-tos-screenshot-<YYYY-MM-DD>.png`. Per
  PLAN §3.6 this screenshot is one of four mandatory provenance fields for
  AI cues.
- Save the Suno generation URL (the `https://suno.com/song/<id>` page).
- Save the prompt, model name (e.g. "Chirp v4.5" or whatever's current at
  generation time), and generation timestamp.
- Toggle off any "share publicly" / distribution-to-streaming setting in your
  Suno account so your cue is not auto-ingested into anyone's ContentID
  catalog by Suno-side enforcement.
- Treat the cue as Cue B "Weight" original motif only (PLAN §3.5 row 5–6),
  never as Cue A base material.

**Attribution string template (Suno cue, YouTube description):**

```
Original instrumental cue generated with Suno (paid plan, model <Chirp version>),
prompt: "<exact prompt>". Generated <YYYY-MM-DD>. Used under Suno's paid-plan
terms (https://suno.com/terms), which grant the paid user commercial rights to
generated outputs.
```

**Content ID failure modes specific to Suno:**
- Suno-side enforcement: another user has uploaded the same/similar generation
  to streaming services, which ingested it into ContentID under their distributor
  name. You then upload your cue and get claimed.
- Distributor parasites: aggregators ingest large numbers of Suno generations
  into ContentID indiscriminately to claim future uses.
- Stylistic-similarity false positive: ContentID flags your Suno cue against an
  unrelated track that shares melodic / harmonic content.

**Dispute language for a Suno-generated cue:**

```
This is an original instrumental composition generated by me using Suno's paid-plan
service on <YYYY-MM-DD>, prompt: "<exact prompt>", model: <model name>.

Under Suno's Terms of Service for paid users (https://suno.com/terms): "If you are
using a paid plan, you own all rights, title and interest in and to the Outputs you
create, including all intellectual property rights therein, to the fullest extent
permitted by applicable law."

Source generation URL: https://suno.com/song/<id>.
Generation date: <YYYY-MM-DD> (TOS as of that date archived: <screenshot path>).

I own the rights in this output. The Content ID claim is either a stylistic false
positive or an unauthorized re-claim by a third party who does not have rights
superior to my paid-plan license. I assert that this claim is in error.
```

---

## Cross-source: composition-vs-recording PD trap, restated

Two layers of copyright apply to any music file:

| Layer | Source of protection | PD test for our 1890s window |
|---|---|---|
| **Composition** (melody + lyrics + arrangement) | 17 U.S.C. §302; lasts life-of-author + 70 years for post-1978 works, or 95 years from publication for pre-1978 works | Published before 1929 → PD US (covers all 1890–1898 compositions cleanly, plus 1929-cutoff captures any periods up to 1928) |
| **Sound recording** (the master) | 17 U.S.C. §1401 (MMA, post-2022) | Published before 1923 → PD US. (A 1925 recording of an 1893 PD composition: composition PD, recording **NOT** PD until 2025-2026 under the rolling MMA terms) |

**The trap that bites us:** an 1893 Sousa composition (Liberty Bell) is bulletproof
PD. But a 1944 Boston Pops recording of Liberty Bell is a fully copyrighted Sony
master. If you grab a recording without checking the recording date, you can ship
PD-by-composition with a copyrighted master and get claimed (correctly) by Sony.

**Per-asset verification rule for the editor:**
1. What's the composition title and composer? Was it published ≤ 1928? (Yes → PD US
   composition layer.)
2. What's the recording date? Was the recording published ≤ 1922? (Yes → PD US
   recording layer.)
3. If both yes → CLEAN. If composition yes / recording no → blocked, find a
   different recording. If composition no / recording yes (rare) → blocked, find
   a different composition.

Log composition publication year + recording year in
`assets/MUSIC_LICENSES.md` per cue. The skeleton (delivered alongside this paper)
has fields for both.

---

## Period-window recap (PLAN §3.1 item 5, applied per-source)

PLAN §3.1 item 5: "1890–1898 inclusive is strict period; 1899–1902 is post-campaign
and acceptable only as flavor texture for Cue B or sting variants — never as Cue A
'Mechanism' base material."

| Source | 1890–1898 coverage | Verdict for Cue A (strict) | Verdict for Cue B / sting (texture-OK 1899–1902) |
|---|---|---|---|
| LoC National Jukebox | Thin (collection 1900–1925; few 1898-edge items) | Mostly disqualifies on date | OK for 1899–1902 items |
| IMSLP scores | Strong (Sousa marches 1888–1898 are the canon) | OK if you record in-house | OK |
| IMSLP recordings | Weak (mostly modern) | Disqualified | Disqualified |
| Musopen | Weak for period-grain (modern recordings) | Disqualified for Cue A | OK for Cue B solo-piano texture (composition-period appropriate) |
| Internet Archive Great 78 | **Strongest** (deep 1898–1925 coverage; some pre-1898 cylinders) | OK for ≤ 1898 items | OK for 1899–1902 |
| Free Music Archive | Zero authentic period | Disqualified | Disqualified for period-grain; OK as named-composer fallback only |
| Suno Pro | N/A (synthetic) | Disqualified for Cue A by PLAN §3.5 footnote * blind-test | OK for Cue B original motif only |

---

## Content ID dispute kit — step-by-step for the unlisted-upload phase

PLAN §3.6 protocol: upload unlisted → wait for ContentID scan → if claim, dispute
with the source URL + quoted license text already logged. Below is the operational
runbook.

### 0. Before you upload anything

- Confirm `assets/MUSIC_LICENSES.md` has all four fields filled per cue (and AI-cue
  fields filled for any Suno cue): source URL, license text quoted, attribution
  string, date downloaded; AI cues add prompt / model / generation date / TOS
  screenshot path.
- Confirm the YouTube description of the unlisted video already contains the
  attribution strings from `assets/MUSIC_LICENSES.md`. (This makes the dispute
  faster — the evidence is on the public-facing artifact, not buried in a project
  folder.)

### 1. Upload as unlisted

In YouTube Studio: Visibility → Unlisted. Don't tick "schedule public release";
keep it indefinite. Upload, then wait — **do not click publish**.

### 2. Wait for the ContentID scan

The scan typically completes within 5–60 minutes for a short-form (≤ 5 min) video.
If you don't see a "no copyright issues found" or "copyright claims" notice within
24 hours, the scan didn't run; re-upload (rare, but it happens).

### 3. Read the result

- **No claims:** publish. Done.
- **Claim with monetization but no other restriction:** the claimant is taking
  ad revenue on your video. Dispute (steps 4–6).
- **Claim with block in country / worldwide block:** dispute (steps 4–6) and do
  not publish until resolved.
- **Strike (not a claim):** different and worse. Strikes are almost never
  fingerprint-based; they come from manual takedowns. If a strike lands on a
  PD/CC cue, dispute via the counter-notification process, not the ContentID
  dispute form. Get a lawyer if it's anything more than a clear-cut PD case.

### 4. Click "Dispute" on the claim

YouTube Studio → Content → click the affected video → Restrictions column →
"Copyright claim" → "SEE DETAILS" → "SELECT ACTION" → "Dispute".

### 5. Pick the right reason

The form will offer reasons. Use:
- For LoC / IA Great 78 / Musopen-PD / IMSLP-PD-recorded-in-house →
  **"Public domain"**
- For FMA-CC / Musopen-CC / Suno paid-plan output → **"License"** (you have a
  license to use this content)

Do **not** pick "Fair use." PLAN §3.1 item 4: fair use is a legal defense, not a
release valve, and disputes filed under fair-use grounds are rejected fastest by
ContentID claimants.

### 6. Paste the dispute language

Use the source-specific dispute templates in this paper. The form has a free-text
"Rationale" field; paste the entire template, filled in with the specific
composition title, composer, year, source URL, license URL, and (for Suno)
generation URL + date + prompt.

**The rationale must contain:**
- The exact source URL (LoC item, IA item, Musopen track page, IMSLP file page,
  Suno song page, FMA track page).
- The exact license / rights statement, quoted (already logged in
  `assets/MUSIC_LICENSES.md`).
- For PD claims: the relevant statute (17 U.S.C. §1401 for sound recordings,
  17 U.S.C. §302 for compositions) and the publication-year arithmetic.
- For licensed claims: the license URL (e.g. CC-BY 4.0 link, Suno ToS
  URL) and a one-line statement that the license expressly permits commercial use.

### 7. Submit, then wait

Claimant has 30 days to respond. Possible outcomes:
- **Claim released:** done. Publish.
- **Claim upheld (claimant disagrees):** you can appeal. Appealing escalates to
  YouTube's review and potentially to a copyright strike if the claimant is
  willing to file a takedown. **For our project, if a claim is upheld on a
  pre-1923 LoC/IA recording, escalate by filing a counter-notification under
  17 U.S.C. §512(g) — but only if the provenance log is rock-solid.** If
  provenance is shaky, swap the cue per PLAN §3.6 ("Cue swap is only correct if
  the dispute is rejected on appeal").
- **Claim auto-released (no response in 30 days):** done. Publish.

### 8. If multiple cues are claimed

Dispute each separately. Do not bundle disputes into one rationale; ContentID
processes claims independently and a bundled dispute often gets misrouted.

### 9. Document outcomes

Append a row to `assets/MUSIC_LICENSES.md` per claim: claim date, claimant name,
disposition (released / upheld / no-response), date resolved. This builds a
record for future episodes and makes the next dispute cycle faster.

---

## Open questions (no paid access available, route around)

- **Specific Suno ToS clause changes between audit-date and generation-date.**
  Mitigation: PLAN §3.6 already requires a TOS screenshot at generation time.
  Re-read on generation day.
- **Naxos Historical individual track ContentID inclusion.** Naxos doesn't publish
  a public list of which masters are in ContentID; we only learn when a claim
  fires. Mitigation: the unlisted-upload pre-flight catches it before public
  release.
- **Whether Sony Music Entertainment will dispute a Sousa pre-1923 LoC
  attribution under the "rights administrator" theory.** No way to know in
  advance; the dispute kit handles it if it happens.

---

— License expert perspective, t_b48551d0
