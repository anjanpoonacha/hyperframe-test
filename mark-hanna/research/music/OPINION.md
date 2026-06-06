# Our Opinion — Music for the Mark Hanna Documentary

> Parent task `t_7a905503` answer. Written *after* reading all three perspectives and PLAN.md.
> The user's prompt asked for an opinion about *ourselves* and the best practices, not just a
> mechanical synthesis. This is that opinion, anchored in what's actually in the project today
> (DESIGN.md, narration.txt, renders/) — not in generic advice.

## Project facts (verified, not assumed)

- `narration.txt`: 719 words. At a documentary register (~140–150 wpm with pauses), this comes
  out around **4:45–5:15 of finished narration**. P3's "single-digit minutes" assumption is
  correct.
- `DESIGN.md` says: "Gilded Age investigative documentary. Dark editorial. Newsprint meets
  political thriller." The visual register is *grim and precise*, with explicit instructions
  like "No bounces, no elastic," "Decisive, not bouncy," "The energy is grim and precise."
- The current preview render (`renders/mark-hanna-ep01-preview.mp4`) confirms the silent /
  dry-narration register.
- Subject matter: a political investigation about how an 1896 election was "turned into a
  corporate purchase order." Real money, real coercion, real consequences. This is closer to
  Plainly Difficult's register than to Wendover's.

These facts are why the synthesis collapses around P3's recommendations and not around the
explainer-doc averages from P1.

## Yes, we need music. But not the way most YouTube docs use it.

The straight answer to the user's first question: **yes**, but the *role* of music in this
piece is narrower than usual. The DESIGN.md visual brief — "the visuals carry the weight; the
text does not shout" — applies to the score too. **The score does not shout, either.**

Concretely, the piece needs music in three structural places only:

1. **Title card** — Cue A ("Mechanism") in full statement for ~6–8 s. The only place a cue
   states itself uninterrupted. Establishes the period via instrumentation (parlor piano +
   subtle low-string drone, or sparse military-march snare ostinato — both period-correct
   for 1896).
2. **Inter-section transitions** — 1–2 s motif stings from a single sting family
   (low-piano-and-sub *or* a single muted-cornet hit; pick one and never mix). These do the
   work of fade-out/fade-in without the wallpaper.
3. **Closing card** — Cue C (reharmonized A in B's register, full volume over a static end
   card). The only place we let music tell the audience how to feel.

Everywhere else: silence, room tone, very thin Cue B ("Weight") under specific human-cost
B-roll beats. Target: **40–60% of the 5-minute runtime is unscored** (≈ 2:00–3:00 of pure
voice + room tone).

## Our opinion about *ourselves* — what we tend to get wrong

The user asked for an opinion about ourselves. Here it is, blunt:

1. **Our default failure mode would be "atmospheric synth pad behind everything."** It's the
   easy choice when the visual brief is dark and grim. It's also the wrong choice for a
   topic that has real moral weight. A Lemmino-style sub-bass drone behind every fact would
   flatten the piece — turn a political indictment into a vibes piece. Plainly Difficult's
   restraint is the model, not LEMMiNO's atmosphere.

2. **We over-trust AI music as a shortcut.** Suno/Udio are listed as the second tier in
   PLAN.md, but the *real* discipline is using AI cues only for original motifs that
   couldn't exist as period recordings — and never as a wholesale replacement for a
   library track. Easy to get lazy here. The project should use AI cues for at most 1–2
   original Cue B / Cue C variants, generated against the strict prompt scaffold, logged
   with full provenance, and *edited by hand* before they ship.

3. **We'd be tempted to "earn the swell" too early.** The narration's most dramatic line is
   probably the one about the Hanna political machinery — "he turned the American
   presidential election into a corporate purchase order." That is the *thesis statement*,
   not the climax. Score it dry. The actual swell goes at the end, after the audience has
   absorbed the mechanisms (the bank-assessment percentage, the half-million transported
   voters, the McKinley vote count). If we score the thesis, the audience gets emotional
   permission to stop thinking. We don't want that.

4. **We'd be tempted to use stingers as decoration.** "$3,500,000" landing on a screen does
   not need a percussive hit. The number lands. A stinger on top is the equivalent of
   underlining what's already in bold — it tells the audience we don't trust the typography
   to do its job. DESIGN.md is explicit about this: "Numbers and dates land like
   indictments." They land. Don't add a sting.

5. **We'd be tempted to copy Lemmino's reveal-pacing.** Lemmino's silence-before-the-reveal
   move is correct in spirit (silence-as-cue) but the execution would feel mannered on a
   piece this short. We get one silent-reveal beat. Maybe two. Plan it before placing any
   cue, and resist the urge to add a third.

## The MACI principle, applied here

The user's prompt explicitly invoked MACI — "confidence can't be checked by the model itself."
Three independent reviewers + a synthesizer is exactly the architecture MACI prescribes for
this. The PLAN's confidence section (§4) ranks recommendations by *agreement across
reviewers*, not by reviewer self-report. That's the structural confidence.

But there's a second-order MACI move worth naming: **the synthesizer is also a single model**,
and its resolution of disagreements (§2.1–2.6) is its own opinion, not a triangulated answer.
It happened to side with P3 on the sourcing question — but that's a synthesizer judgment, not
a converging fact. Where the three reviewers genuinely disagreed, the PLAN says so out loud
(LOW-confidence tier) instead of hiding it under an averaged number. That's the MACI
discipline working as intended.

The two items flagged "needs human decision" in §4 are the honest residue:
1. **Project scope confirmation.** I checked: short-form (5 min), 1896 historical, captions-on
   YouTube, ad-monetized, zero cash budget — all hold. This unblocks itself.
2. **Closing motif (Cue C) treatment.** Full-volume over the end card vs thinned
   reharmonization. This needs an audition on the locked cut, not a model's guess. Editor
   call.

## What I want the editor to do next

Concrete, in order:

1. **Read** `PLAN.md` end-to-end. The synthesis matters more than this opinion file.
2. **Annotate** `narration.txt` (or a copy in `research/music/narration-annotated.txt`) with
   `[mechanism]`, `[weight]`, `[dry]` markers per beat. The single most important sentence in
   each section gets `[dry]`. Identify exactly one **silent reveal** beat for the entire
   piece.
3. **Audition** Cue A from Library of Congress National Jukebox first
   (https://www.loc.gov/collections/national-jukebox/) — search "1896 march", "Sousa Liberty
   Bell," "1898 parlor piano." Aim for 3–5 candidates, 30-second clips against the locked
   cut. Period-PD recordings are strictly dominant here for the reasons in PLAN §2.1.
4. **Audition** Cue B from Musopen (https://musopen.org) for "muted cornet" / "minor-mode
   parlor piano" / "late romantic solo piano." If nothing fits, generate one Suno Pro cue
   on the prompt scaffold from PLAN §3.5 row 5 and log it.
5. **Don't** subscribe to Epidemic / Artlist / Soundstripe. The DESIGN brief and the period
   setting both reject this tier; it would dilute everything else.
6. **Don't** ship anything until `assets/MUSIC_LICENSES.md` exists with full provenance for
   every cue. PLAN §3.6 lists the four mandatory fields.
7. **Don't** publish until the unlisted YouTube upload has cleared the Content ID scan.

## TL;DR

- Yes we need music; sparingly.
- Two leitmotifs (Mechanism + Weight) and one Coda; ~40–60% of runtime unscored.
- Period public-domain sourcing first; AI-generated original motifs second; named CC-BY third;
  zero generic royalty-free libraries.
- Score function, not timecode. Voice is sovereign.
- Our biggest risk is over-scoring out of "dark documentary" instinct. Plainly Difficult is
  the model, not LEMMiNO.

— Parent task t_7a905503, default profile, 2026-06-06

---

# Editorial synthesis of PLAN.md — 2026-06-06 (task t_3b56ad7d)

> Editorial read of `mark-hanna/research/music/PLAN.md` (213 lines, 20.8 KB,
> dated 2026-06-06, authored by t_6450d679). Not a summary — an opinionated
> assessment a downstream editor can act on. Cites concrete passages.

## 1. Stated goals (and the goal that should have been stated)

PLAN.md never declares its goal in a single sentence. It opens (lines 1–10)
with provenance — "Synthesis of three independent reviewer perspectives
(MACI triangulation)" — and the reader has to infer the goal from the
preamble's last sentence: "This plan is for the Mark Hanna / 1896 historical
documentary" (line 10). The implicit goal, reconstructed:

> Produce an actionable music plan for a short-form 1896 historical
> documentary, on zero cash budget, that resolves the three reviewers'
> disagreements through project context rather than averaging.

That goal *is* what the plan delivers, but a reader landing on §3 cold cannot
tell whether the plan is descriptive (what mainstream YouTube docs do) or
prescriptive (what *this* doc will do). **Recommendation:** lift the implicit
goal into a one-paragraph header above line 12.

## 2. Section flow — strong frame, redundant middle

Sections in order: §1 agreements (5 rules), §2 disagreements (6 items), §3
final plan (6 sub-sections), §4 confidence tiers, §5 editor checklist. The
overall arc (agree → disagree → resolve → tier confidence → hand-off) is
sound and is the right shape for a MACI-style synthesis.

The middle is where it bloats. **§1's rule-boxes and §3.3's structural
placement say the same thing twice.** Compare:

- §1.1 (line 24): "plan one (max two) 'silent reveal' moments in the locked
  cut and score around them."
- §3.3 (line 131): "The single biggest reveal: full music drop-out 1–2 s
  before the line. Line plays in dry voice + room tone. Re-enter on a single
  low piano note (transformed motif A)."

§3.3 is the operational version; §1.1 is the principle. An editor scanning
top-down hits the silence rule at lines 22, 24, 50, 131, and 134. **Recommendation:**
collapse §1 into a single "Five Defaults" bullet list above §3, and let §3
do the operational work without re-stating the principles.

## 3. Key claims and assumptions — what's load-bearing

The plan rests on five assumptions, all in §4 ("NEEDS HUMAN DECISION", lines
192–195):

1. Short-form (single-digit minutes) runtime.
2. 1896 historical period.
3. Captions-on YouTube viewership.
4. Ad-monetized.
5. Zero cash budget.

**These assumptions are now stale.** The earlier OPINION.md section above
(lines 8–23) verified all five against `narration.txt` (719 words → ~5:00),
`DESIGN.md`, and `renders/mark-hanna-ep01-preview.mp4`. The PLAN was written
2026-06-06 *and so was the OPINION*, but the PLAN's §4 still presents these
as open. **Recommendation:** strike the "Project scope confirmation" item
from §4 NEEDS HUMAN DECISION and add a one-line "verified by OPINION.md
2026-06-06" annotation to the §4 LOW-confidence header. Otherwise a future
editor will re-litigate a settled question.

The genuinely load-bearing claim — period-PD sourcing strictly dominates a
subscription library here — is in §2.1 (lines 58–63). It is defensible *if*
National Jukebox / IMSLP / Internet Archive actually have usable 1890s
recordings of the right tone. Which leads to gap #4 below.

## 4. Gaps, contradictions, and weak spots

### 4.1 The period-PD audition has not been pre-flighted

§3.5 (lines 148–161) lists "Library of Congress National Jukebox" with
search prompts like "1896 march band" and "1898 parlor piano," and
parenthetically notes (line 153/§3.5 row 1 verbiage in §3.1 line 105):
*"earliest commercial recordings, many 1900s but some 1890s; tone-period-correct."*

That parenthetical is the entire load-bearing risk. If National Jukebox is
overwhelmingly post-1900, the "1896-period-correct" claim collapses to
"close enough; nobody hears the difference." Possibly true, but the plan
doesn't say so. **An editor should not start auditioning until someone has
actually counted the 1890s recordings on National Jukebox / Internet
Archive 78rpm Project for the relevant catalog queries.** This is a 30-min
pre-flight that the plan implies but doesn't schedule.

### 4.2 The §3.2 cue palette hides a real texture choice

§3.2 (line 121) defines Cue A as:
> "Period-correct rhythmic figure: parlor piano with subtle low-string
> drone, OR sparse military-march snare ostinato without melody."

These are two different documentaries. *Parlor piano + drone* is interior,
contemplative, "vibes." *Military-march snare ostinato* is exterior,
mechanical, "decisive, not bouncy" — which matches DESIGN.md's stated
register. The OR conceals the choice the project has already made by virtue
of its visual brief. **Recommendation:** make the snare-ostinato the
default and the parlor-piano-drone a fallback, or commit to one. As
written, an editor will pick by mood on the day and the doc will lose
register coherence.

### 4.3 The −12 dB duck case may not exist in this project

§2.3 (lines 77–80) and §3.4 (line 141) prescribe two duck depths:
- −8 dB for sparse pad / drone / single-piano cues.
- −12 dB for "denser orchestral or full-arrangement cues."

But §3.2 forbids dense cues entirely: Cue A is "sparse"; Cue B has "no
accompaniment"; Cue C is "Motif A's contour, reharmonized into Motif B's
minor-mode register, full volume" — over an end card with no narration to
duck against. **The −12 dB rule has no operational target in this project.**
Either it should be removed (cleanup) or the plan should name the one
specific cue family it's reserved for (e.g. a Sousa march at the title card
where Cue A's "sparse military-march snare ostinato" actually plays as a
fuller arrangement).

### 4.4 Suno prompt scaffold is wishful

§3.5 row 5 (line 157) and §3.1 line 109 give the AI prompt scaffold:
> "1890s [instrument family], sparse, instrumental, no vocals,
> public-domain feel, [mood]"

Suno and Udio do not parse "1890s" or "public-domain feel" as period
markers — they pattern-match against the genre/instrument tokens and
produce a generic melancholic piano piece. The plan presents this scaffold
as if it controls the output; in practice it controls about 20% of it. The
editor will get cues that *sound contemporary but instrumented like 1890s*,
which is the worst of both worlds against period recordings. **Recommendation:**
add a §3.5 footnote: "AI cues require A/B audition against a Library of
Congress reference recording; reject any AI cue that doesn't pass a
blind-test for period-grain." If the AI tier can't pass blind-test, demote
it to "fallback only" and lean harder on PD.

### 4.5 The Content ID claim is overconfident

§3.6 (lines 166–167) says:
> "Final cut uploaded as unlisted on YouTube; wait for the Content ID scan
> to complete before publishing publicly. Cheap and dispositive against
> accidental matches."
> "One Content ID claim on a documentary of this register breaks viewer
> trust."

The first claim is half-right. Unlisted-then-scan catches *automatic*
matches but doesn't dispose of them — when a Sousa-on-modern-label rip in
the database matches the same melody from an LoC wax-cylinder transfer,
YouTube fingerprints both as the same recording; you still get a claim.
The PLAN doesn't have a "what if the scan flags it anyway" branch. **Recommendation:**
add a §3.6 sub-step: "If a claim arrives, dispute with the LoC URL +
license text from `MUSIC_LICENSES.md`. Do not swap cue first. The dispute
is the test of whether the provenance log is real."

### 4.6 Mechanism/Weight binary may under-serve the script

§3.2's two-leitmotif palette (Cue A "Mechanism", Cue B "Weight") is
elegant for the synthesis but the *narration* is structurally three-part:
mechanism description → human cost → indictment. Indictment is not Weight
— Weight is what happened *to* people; indictment is what happens *to*
Hanna and the donors when the audience integrates the facts. Right now
indictment plays dry (per §1.4 / OPINION lines 64–70, "the actual swell
goes at the end"). That's defensible but the plan should *name* it as
"there is a third narrative role; we deliberately leave it unscored
because dry voice is the strongest score available there." Otherwise the
editor will be tempted to add a third cue for indictment, and the
restraint argument (§1.5, lines 47–52) will be gone.

### 4.7 Cue C is presented as decided when §4 says it isn't

§3.2 (line 123): "Motif A's contour, reharmonized into Motif B's
minor-mode register, full volume, slow."
§3.3 (line 132): "Closing: Cue C at full volume over a static end card."
§4 (lines 196): "Closing motif (Cue C) — full statement or fade-thin?
P3 says full volume over end card; P1 implies thinned reharmonization.
Both work; the editor should cut both versions and pick on the locked
end card."

**The body of §3 reads as decided; §4 says it isn't.** An editor reading
top-down will set Cue C at full volume and never audition the thinned
version. **Recommendation:** annotate §3.2 and §3.3 with "(audition
both — see §4 NEEDS HUMAN DECISION)."

### 4.8 No measurement plan for the 40–60% unscored target

§1.1 / §3.3 / §4 all assert the 40–60% unscored target. §5's checklist
(line 207) says "Confirm 40–60% of runtime is unscored after first pass."
But there's no method. **Recommendation:** add a §5 sub-step: "Solo the
music bus, export the music-only render, sum the non-silent regions
against total runtime in DaVinci/Premiere project metadata." Without a
method this becomes a vibes check.

### 4.9 §3.4 mixes structural and mixing decisions

The "Sting family" rule (§3.4 line 145) — *"pick one stinger sound and
use it for every chapter transition. Mixing stinger families is the
fastest way to make the doc sound amateur"* — is a **cue-palette
decision**, not a mixing decision. It belongs in §3.2 alongside Cues
A/B/C. Buried in §3.4 between EQ specs and edit-point rules, an editor
will treat it as a mixing nicety and miss that it constrains the cue
palette to "A + B + C + one named sting."

## 5. What reads as stale or out of priority order

### 5.1 The "if runtime grows past ~8 minutes" branch is dead code

§3.2 (line 125): *"If the runtime grows past ~8 minutes, allow Cue A to
recur in two different period instrumentations…"*

Narration is 4:45–5:15 (verified). The 8-minute branch will not fire on
this project. **Recommendation:** move it to a "Scaling notes for future
episodes" appendix, or delete it. Currently it dilutes the cue-palette
section.

### 5.2 §4 NEEDS HUMAN DECISION lists two items; only one is actually open

Item 1 (project scope confirmation) is closed by OPINION.md.
Item 2 (Cue C treatment) is genuinely open and needs editor audition.
**Recommendation:** strike item 1; promote item 2 from a sub-bullet to a
top-level callout because it's the only real open question.

### 5.3 Forbidden list buries the most important item

§3.1 (lines 111–114) lists four forbidden items. Items 2–4 are
restatements of the licensing rule in different words; item 1 — *"Generic
royalty-free libraries (Epidemic Sound, Artlist, Soundstripe, Musicbed)"*
— is the policy choice that distinguishes this plan from every other
YouTube doc plan. **Recommendation:** lead the §3.1 forbidden list with
"Generic royalty-free libraries…" and explicitly cite §2.1 ("the resolution
in favor of P3 is what makes the rest of this plan internally
consistent"). Right now an editor under deadline pressure will subscribe
to Epidemic Sound and the plan's whole structure collapses silently.

### 5.4 §3.5 shortlist mixes period-correct and period-adjacent without flagging

§3.5 row 1 lists "Joplin Maple Leaf Rag (1899)" as IMSLP recording-tab
fodder. Maple Leaf Rag is 1899; the Hanna campaign is 1895–1896. Three
years post-campaign. Defensible *if* the editor knows it's a near-period
choice and not strict period; not defensible if "1896 historical" is
being read literally. The plan doesn't define the period window.
**Recommendation:** §3.1 should declare: "Period window: 1890–1898
inclusive. 1899+ is post-campaign and acceptable only as a flavor cue,
not as Cue A." Otherwise the editor will pull Joplin without knowing
they've drifted.

## 6. Priority list for the next editorial pass on PLAN.md

In strict order; each item is small enough to ship in one pass.

1. **Lift implicit goal into a header paragraph** above line 12. (§1)
2. **Strike §4 item 1 (project scope confirmation)** — closed by OPINION.md.
   Promote §4 item 2 (Cue C treatment) to a top-level callout. (§4)
3. **Define the period window (1890–1898)** in §3.1; flag Joplin 1899 as
   period-adjacent in §3.5 row 1.
4. **Resolve the §3.2 Cue A OR**: pick snare-ostinato as default, parlor
   piano as fallback. Cite DESIGN.md "Decisive, not bouncy."
5. **Add a Content ID claim-disposal sub-step** to §3.6.
6. **Move the sting-family rule** from §3.4 into §3.2.
7. **Add a measurement method** for the 40–60% unscored target in §5.
8. **Annotate §3.2/§3.3 Cue C** with "(audition both — see §4)."
9. **Pre-flight Library of Congress / Internet Archive** for 1890s
   recordings before audition starts. Spawn as a sub-task.
10. **Demote/delete the >8 min scaling branch** in §3.2 to a scaling
    appendix.
11. **Reorder §3.1 forbidden list** to lead with "generic royalty-free
    libraries."
12. **Remove or scope the −12 dB duck rule** in §2.3 / §3.4 — there is
    no cue family in this project that uses it.
13. **Add an AI cue blind-test footnote** to §3.5 row 5.

Items 1, 2, 3, 4, 6, 8 are pure-edit. Items 5, 9, 13 require new
content. Item 7 requires a tooling note. Items 10, 11, 12 are
deletions/reorderings.

## 7. What the plan gets right (so the editor doesn't over-correct)

The plan's structural decisions are sound and should not be relitigated:

- **Three-perspective MACI synthesis with confidence tiers (§4)** is the
  right epistemic frame and the right way to expose disagreements
  honestly rather than averaging them.
- **Period-PD sourcing as primary tier (§2.1, §3.1)** is strictly
  dominant on cost / license / authenticity for this specific project,
  and the resolution in P3's favor is justified, not arbitrary.
- **Two-leitmotif ceiling (§3.2)** with Cue A + B + Coda is the right
  ceiling for a 5-minute runtime and a Plainly-Difficult register.
- **Voice-sovereign mixing (§1.4, §3.4)** with concrete LUFS targets is
  the only quantitative anchor in the plan; the numbers are correct
  for YouTube normalization and should be preserved verbatim.
- **The §5 hand-off checklist** is the right artifact and the right
  order (lock picture first → annotate script → audition → mix last).

The edits in §6 above sharpen these strengths; they don't replace them.

— Editorial pass by default profile, t_3b56ad7d, 2026-06-06

---

# Proposed edits to PLAN.md — 2026-06-06 (task t_c1ac2703)

> Concrete revision checklist derived from the synthesis above (lines 140–429,
> task t_3b56ad7d). Each item names the affected PLAN.md section, the change
> type (REWRITE / REORDER / CUT / EXPAND / INSERT / ANNOTATE), the operative
> instruction, and a one-line justification. Items are ordered by edit cost —
> pure-edit items first, content-additions second, deletions/reorderings last —
> so a pass can ship in a single sitting and stop early if needed.
>
> Line numbers reference PLAN.md as of 2026-06-06 (213 lines, authored by
> t_6450d679). PLAN.md MUST NOT be edited during this task; this checklist is
> the deliverable. A subsequent task will execute these edits.

## Tier 1 — Pure edits (rewrite / reorder / cut existing prose; no new research)

- [x] **E1. INSERT goal-statement header above PLAN.md line 12.** Section: §1 preamble. Add a one-paragraph "Goal" block immediately after the bullet list (between lines 10 and 12) reading approximately: *"Goal: produce an actionable, prescriptive music plan for a short-form 1896 historical documentary on a zero-cash budget, that resolves three independent reviewers' disagreements via project context (DESIGN.md visual brief, narration runtime, captions-on YouTube ad-monetized distribution) rather than by averaging."* Justification: a reader landing on §3 cold cannot tell the plan is prescriptive; the goal is currently inferable only from the preamble's last sentence (synthesis §1, OPINION lines 148–161).

- [x] **E2. CUT §4 item 1 (project scope confirmation, lines 192–195) and PROMOTE §4 item 2 (Cue C treatment, line 196) to a top-level §4 callout.** Section: §4 NEEDS HUMAN DECISION. Replace the two-bullet structure with a single boxed/bolded callout naming Cue C as the only genuinely open editorial decision; add a one-line annotation to the §4 LOW confidence header reading *"(scope assumptions verified by OPINION.md 2026-06-06; do not re-litigate)."* Justification: scope was verified against narration.txt / DESIGN.md / preview render in OPINION.md lines 8–23; leaving it as "open" invites a future editor to re-litigate a settled question (synthesis §3, §5.2).

- [x] **E3. REWRITE §3.2 Cue A "OR" into a default + fallback (line 121, table row "A — Mechanism").** Section: §3.2 cue-palette table. Change the Texture cell from *"parlor piano with subtle low-string drone, OR sparse military-march snare ostinato without melody"* to *"sparse military-march snare ostinato (default — matches DESIGN.md 'Decisive, not bouncy'); parlor piano with subtle low-string drone as fallback if the snare-ostinato register fights the visual cut."* Justification: the OR conceals a register choice DESIGN.md already settled; leaving it open will cause the editor to pick by mood on the day and lose register coherence (synthesis §4.2, OPINION lines 226–239).

- [x] **E4. REORDER §3.1 forbidden list (lines 111–114) to lead with the generic-royalty-free-library prohibition.** Section: §3.1 sourcing strategy, item 4 ("Forbidden:"). Promote the current sub-bullet 1 ("Generic royalty-free libraries (Epidemic Sound, Artlist, Soundstripe, Musicbed)…") to the lead position, append a parenthetical *"(this is the policy choice that distinguishes this plan from every other YouTube doc plan; see §2.1 resolution)"*, and demote the licensing/provenance items to sub-bullets 2–4. Justification: items 2–4 are restatements of one licensing rule; item 1 is the load-bearing policy and an editor under deadline pressure currently sees it third (synthesis §5.3).

- [x] **E5. ANNOTATE §3.2 Cue C row (line 123) and §3.3 Closing line (line 132) with audition flag.** Section: §3.2 table row "C — Coda" and §3.3 final bullet. Append *"(audition both full-volume and thinned-reharmonization variants — see §4)"* to each. Justification: §3 currently reads as decided while §4 (line 196) says it isn't; an editor scanning top-down will set Cue C at full volume and never audition the alternative (synthesis §4.7).

- [x] **E6. MOVE the sting-family rule from §3.4 (line 145) into §3.2 as a fourth table row or trailing bullet.** Section: §3.4 mixing → §3.2 cue palette. Lift the entire *"pick **one** stinger sound (e.g. low-piano-and-sub, or a single muted-cornet hit) and use it for every chapter transition. Mixing stinger families is the fastest way to make the doc sound amateur."* sentence from §3.4 and place it as a "Sting (chapter transitions)" row in the §3.2 table, naming the chosen family in advance. Justification: this is a cue-palette decision, not a mixing decision — buried between EQ specs, an editor treats it as a nicety and misses that it constrains the palette to "A + B + C + one named sting" (synthesis §4.9).

## Tier 2 — Content additions (require small new prose, no external research)

- [x] **E7. INSERT period-window definition into §3.1.** Section: §3.1 sourcing strategy, immediately after item 1. Add a fifth top-level item: *"5. **Period window:** 1890–1898 inclusive is strict period; 1899–1902 is post-campaign and acceptable only as flavor texture for Cue B or sting variants — never as Cue A 'Mechanism' base material."* Then ANNOTATE §3.5 row 1 (line 153 IMSLP entry) by adding a *"(1899; period-adjacent — flavor only, not Cue A)"* tag after "Joplin 'Maple Leaf Rag'". Justification: PLAN currently treats "1896 historical" as fuzzy; Joplin 1899 is three years post-campaign and the editor will pull it without knowing they've drifted (synthesis §5.4).

- [x] **E8. INSERT Content ID claim-disposal sub-step into §3.6.** Section: §3.6 copyright/provenance protocol. Add a new bullet between lines 166 and 167: *"- If a Content ID claim arrives during the unlisted scan, **dispute** with the LoC/IMSLP/Archive source URL plus the license text already logged in `assets/MUSIC_LICENSES.md`. Do **not** swap the cue first — the dispute is the test of whether the provenance log is real. Cue swap is only correct if the dispute is rejected on appeal."* Justification: §3.6 currently says unlisted-scan is "dispositive against accidental matches" but YouTube fingerprints LoC wax-cylinder transfers as identical to modern-label rips; the plan has no "what if it claims anyway" branch (synthesis §4.5).

- [x] **E9. INSERT measurement method into §5 hand-off checklist.** Section: §5, after line 207 ("Confirm 40–60% of runtime is unscored"). Add a sub-bullet: *"Method: solo the music bus, export the music-only render, sum the non-silent regions (>−60 dBFS) against total runtime in DaVinci/Premiere project metadata. Vibes-check is not a method."* Justification: the 40–60% target is asserted four times across §1.1 / §3.3 / §4 / §5 with no method, so it currently functions as a vibes-check (synthesis §4.8).

- [x] **E10. INSERT AI cue blind-test footnote on §3.5 row 5 (line 157, Suno Pro entries).** Section: §3.5 shortlist table. Append a footnote/asterisk to the two Suno rows reading: *"AI cues require A/B audition against an LoC reference recording from row 1; reject any AI cue that fails a blind period-grain test. If row 5–6 cannot pass blind-test, demote to fallback only and lean harder on PD."* Justification: the prompt scaffold *"1890s [instrument family] … public-domain feel"* controls roughly 20% of Suno's output; the rest pattern-matches against modern genre tokens, producing contemporary cues with 1890s instrumentation — the worst of both worlds (synthesis §4.4).

- [x] **E11. EXPAND §3.2 with an indictment-as-dry annotation.** Section: §3.2 cue palette, immediately after the Cue C row (line 123). Add a non-table note: *"**Indictment beats are deliberately unscored.** The narration is structurally three-part — mechanism description → human cost → indictment. Mechanism = Cue A; human cost = Cue B; indictment plays in dry voice + room tone. This is not a missing fourth cue; the absence of a cue is the cue."* Justification: the two-leitmotif palette is elegant but the editor will be tempted to add a third cue for indictment unless the plan explicitly names "we leave it unscored because dry voice is the strongest score available there" (synthesis §4.6, OPINION lines 64–70).

## Tier 3 — Deletions and scope-reductions (cleanup, lowest risk)

- [x] **E12. CUT or DEMOTE the ">8 minutes" branch in §3.2 (line 125).** Section: §3.2, final paragraph after the cue table. Either delete the sentence *"If the runtime grows past ~8 minutes, allow Cue A to recur in two different period instrumentations…"* outright, or move it into a new §6 "Scaling notes for future episodes" appendix at the end of the doc. Justification: narration is verified at 4:45–5:15 (OPINION lines 10–12); the 8-minute branch is dead code that dilutes the cue-palette section (synthesis §5.1).

- [x] **E13. CUT or SCOPE the −12 dB duck rule in §2.3 (line 79) and §3.4 (line 141).** Section: §2.3 resolution + §3.4 mixing guidelines. Either delete the *"−12 dB duck for denser orchestral or full-arrangement cues"* line entirely, or replace it with: *"−12 dB duck is reserved for the title-card statement of Cue A only, when the snare-ostinato is allowed to play as a fuller arrangement; everywhere else, the −8 dB rule governs because §3.2 forbids dense cues."* Justification: §3.2 explicitly forbids dense cues (Cue A "sparse"; Cue B "no accompaniment"; Cue C is over an end card with no narration to duck against) — the −12 dB rule has no operational target as written (synthesis §4.3).

## Tier 4 — Pre-flight blocker (NOT a PLAN.md edit; a precondition)

- [x] **E14. SPAWN a child task** to count usable 1890s recordings on Library of Congress National Jukebox + Internet Archive 78rpm Project before audition begins. Section: this is not an edit to PLAN.md text — it's a precondition the plan currently elides. Approximate scope: 30-min audit, one-shot script or manual catalog scan, deliverable is a count + 5 candidate URLs per cue role, written to `mark-hanna/research/music/preflight-audit.md`. Justification: §3.5 row 1's parenthetical *"earliest commercial recordings, many 1900s but some 1890s; tone-period-correct"* is the entire load-bearing risk for the period-PD-primary policy in §2.1 / §3.1 — if the catalog is overwhelmingly post-1900, the "1896-period-correct" claim collapses to "close enough; nobody hears the difference," which is a different plan (synthesis §4.1).

## Execution notes for whoever runs the edits

- Tiers 1–3 are 13 atomic edits to PLAN.md; expect ~20–30 min for a careful pass.
- Tier 4 (E14) is a separate workstream and should be spawned as its own kanban task assigned to a research-capable profile, with PLAN.md item §3.5 row 1 as the input and `preflight-audit.md` as the output.
- Do **not** attempt these in a single edit session if Tier 4 is unresolved; E1–E13 stand on their own, but the period-PD-primary policy (E13's premise, §2.1 resolution) ultimately depends on E14's catalog count.
- Recommended ship order: E1 → E2 → E5 → E3 → E4 → E6 (pure-edit run, single pass) → E7–E11 (content-add run, separate pass with attention) → E12 → E13 (deletions, last so prior diffs stay reviewable). Spawn E14 in parallel with the pure-edit run since it's I/O-bound.

— Proposed-edits checklist by default profile, t_c1ac2703, 2026-06-06
