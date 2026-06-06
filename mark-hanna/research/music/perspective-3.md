# Music Best Practices for Our Documentary — Perspective 3

> Independent position paper. Written without reading the other two reviewers.

## Stated assumptions

I'm writing for the documentary currently being produced in `~/SAPDevelop/.../hyperframe-test/mark-hanna/` — a short-form, dialogue-and-caption-driven historical documentary about Mark Hanna and the 1896 election. Tone: dry, archival, slightly forensic; target audience: politically-literate adults watching on YouTube/web at 1×, often muted with captions on. Runtime is short (single-digit minutes). Budget: zero cash, generous time, full creative control. Distribution: ad-supported / monetized YouTube.

Everything below is reasoned from those assumptions. Change the assumptions and several recommendations flip.

## The core opinion in one sentence

For a short, captioned, archival-feeling political-history documentary, **music is a structural tool, not a mood blanket** — its job is to mark beats and carry transitions, not to tell the audience how to feel about facts the captions are already delivering.

## Recommendations

### 1. Score for silence first, then add music only where silence is failing

Most documentaries with our shape over-score. The default failure mode is wall-to-wall bed music that tries to sustain attention the writing should be sustaining. Cut a full pass with no music and watch it. Where attention drifts, the writing or pacing is the problem — fix that. Where the cut genuinely lands flat (transitions, the cold open's first 10 seconds, the closing card), *then* place music. Roughly: aim for **40–60% of runtime unscored**. This also doubles as a quality forcing function — if a scene needs music to work, it usually needs a rewrite.

Reasoning: the audience trusts a documentary that lets facts breathe more than one that emotionally narrates them. Ken Burns gets credit for music; the actual craft is his use of room tone and silence between cues. Also: muted YouTube viewers (a real chunk of our audience) get nothing from a music bed but everything from clean captions on a clean visual.

### 2. Pick exactly two musical motifs and reuse them — no library-of-the-week scoring

Decide on **two cues max**: one "investigation / forward motion" theme and one "weight / consequence" theme. Use them as leitmotifs tied to ideas (e.g., the forward-motion cue every time we name a structural mechanism of the 1896 campaign; the weight cue every time we name a human cost). Reuse is a feature: by the third recurrence the audience has built an associative shortcut and the cue does narrative work for free.

Reasoning: ten different royalty-free tracks across a five-minute doc reads as a corporate explainer. Two recurring motifs reads as authored. The constraint also makes licensing trivially manageable.

### 3. Source: period-licensed or original-generated, in that order — never generic royalty-free libraries

Concrete preference order:

1. **Public-domain period music** (1890s march/parlor/ragtime, IMSLP / Library of Congress / Musopen). Period-correct music is the cheapest authenticity signal a historical doc can buy, and the copyright surface is zero.
2. **Original instrumental motifs** generated locally (Suno/Udio with explicit "instrumental, sparse, no vocals, public-domain-feel" prompts; or hand-arranged in DAW). Treat AI-generated music as a draft tool — every cue gets human editing, EQ, and a deliberate fade.
3. **Curated CC-BY tracks** from named artists (Free Music Archive, Pixabay's *named composer* uploads — not the anonymous-keyword-stuffed kind). Always credit in description.
4. **Avoid** YouTube Audio Library / Epidemic / Artlist / etc. for foreground cues. They're fine for talking-head bed music in corporate work; they're audibly the same tracks every other YouTube history channel uses, and they will date our work.

Reasoning: aesthetic distinctiveness compounds. Generic royalty-free audio is the visual equivalent of a stock photo on a slide — technically free, narratively expensive.

### 4. Treat copyright strike risk as binary, not graduated — one strike kills the channel's trust

Hard rules, no exceptions:

- **No commercial recordings** under any "fair use" theory. Fair use is a legal defense, not a release valve. We cannot afford a Content ID dispute even if we'd "win."
- Every cue logged in `assets/MUSIC_LICENSES.md` with: source URL, license text quoted, attribution string we'll put in the description, date downloaded. If a cue can't produce all four, it doesn't ship.
- AI-generated cues: keep the prompt, model name, and generation date in the same log. Suno/Udio's TOS as of late 2025/2026 give us commercial rights on paid tiers; verify the tier *that day* and screenshot it.
- Run the final cut through YouTube's copyright check (upload as unlisted, wait for Content ID scan, then publish) before going public. Cheap and dispositive.

Reasoning: monetization isn't the issue — *channel trust* is. A single takedown on a history doc with our framing turns the comments section into a referendum on whether we're sloppy. Asymmetric downside, no upside to cutting corners.

### 5. Lock musical form to documentary form — score the structure, not the seconds

Build the score around documentary beats, not timecodes:

- **Cold open (0:00–0:15)**: silence or a single sustained low drone. No melody. Lets the first caption do its work.
- **Title card**: the only place the "investigation" motif states itself in full, ~6–8 seconds, then ducks under narration.
- **Body sections**: motifs enter at section starts and exit before the section's most important factual claim — never under it. The most important sentence in any section plays *dry*.
- **Ad-break / chapter transitions**: a 1–2 second motif sting, not a fade-out-fade-in.
- **Closing**: "weight" motif, full-volume, over a static end card. This is the one place we let music tell the audience how to feel — because the facts have already been delivered and the score is now reflecting on them, not coloring them.

Reasoning: scoring to runtime ("we need 90 seconds of bed here") produces wallpaper. Scoring to structural function ("this motif means *we are now examining a mechanism*") produces meaning. Same number of music minutes, completely different viewer experience.

## What I'm explicitly rejecting

- **Generic "epic cinematic trailer" cues.** Wrong genre, wrong tone, wrong century. They flatten political history into Marvel-trailer texture.
- **Continuous bed music behind narration.** Either the narration is interesting enough to carry alone (then the bed is noise) or it isn't (then fix the narration).
- **Stingers on every fact reveal.** Treats the audience like they can't recognize a beat without a percussive cue. Insulting and dating.
- **Outsourcing the music decision to "vibe."** Every cue should have a one-sentence written justification ("this enters here because the next section pivots from cause to consequence") in our project notes. If we can't write the sentence, we don't ship the cue.

## TL;DR firm recommendations

1. Score from silence outward; aim for 40–60% of runtime unscored.
2. Two leitmotifs total — one "motion," one "weight" — reused with intent.
3. Source order: period public-domain → original/AI-generated (logged) → named CC-BY artists. Skip generic royalty-free libraries.
4. Copyright is binary: commercial recordings are off-limits, every cue is logged with full license provenance, final cut passes Content ID before going public.
5. Score documentary structure, not timecodes — motifs mark function (investigation, weight, transition), and the most important factual claim of each section always plays dry.

— Perspective 3, independent
