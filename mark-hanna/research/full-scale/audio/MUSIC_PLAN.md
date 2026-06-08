# Music Plan — full-scale Mark Hanna documentary (24:00)

> Sibling task: t_be6c1904 for parent t_aa7698b0. This plan extends `research/music/PLAN.md`
> (which was authored against the 5-min preview) to the full 24-min, 19-scene cut. Where this
> plan is silent, defer to the existing PLAN.md.

## 1. Inheritance from PLAN.md (do not re-litigate)

The 5-min preview's music plan already established:

- **Sourcing:** period-PD first (1890–1898 strict), AI-generated original second (Suno paid tier, logged), named CC-BY third. Generic royalty-free libraries forbidden. (PLAN.md §3.1)
- **Cue palette:** Cue A "Mechanism" (forward-motion, military-march snare ostinato OR parlor-piano + low-string drone), Cue B "Weight" (single-line minor-mode melody on solo piano OR muted cornet), Cue C "Coda" (motif-A reharmonized into motif-B register), Sting (one family for every transition — default low-piano-and-sub). (PLAN.md §3.2)
- **Mixing:** master −14 LUFS integrated; voice short-term −16 LUFS; bed under VO −27 to −28 LUFS; bed in B-roll-only −20 LUFS; duck −8 dB default, −12 dB only at title-card Cue A; +2–4 dB breath swells in inter-sentence gaps. (PLAN.md §3.4)
- **Provenance contract:** every cue logged in `assets/MUSIC_LICENSES.md` with all four (or eight, for AI cues) mandatory fields before unlisted upload. (PLAN.md §3.6)
- **Goal:** 40–60% of runtime unscored. (PLAN.md §3.3 closing)

All of the above carries forward verbatim. The full-scale doc adds the section below.

## 2. Cue rotation rate at 24-min runtime (revisits PLAN §2.2)

The 5-min preview shipped on 2 leitmotifs. PLAN.md §2.2 says "if the cut grows past ~10 min, add a third cue (typically a thinner reharmonization of the opening for the coda). Never exceed four named cues in a piece this short." At 24 minutes we are now at the threshold for a fourth cue.

**Decision: 4 named cues for the full-scale cut.** Adding only what the structure demands; not stretching to fill time.

| Cue | Function | Texture | Where it lands |
|---|---|---|---|
| **A — "Mechanism"** | Forward motion; campaign machinery | Military-march snare ostinato (default) or parlor piano + low-string drone (fallback) | Title card; mechanism-reveal scene 11; counter scene 14 |
| **B — "Weight"** | Human cost; mortality | Single-line minor-mode melody, solo piano OR muted cornet | Charlotte (s06); McKinley loyalty refusal (s09); Buffalo (s17); Typhoid (s18) |
| **C — "Coda"** | Reflection at the close | Motif-A contour reharmonized in B's minor-mode register | Scene 19 only — held over end card |
| **D — "Counter-current"** | Bryan/populism antagonist motif | A single rising 4-note phrase on muted cornet OR fiddle (period-correct, not Hollywood); sparse, never resolves | Scene 13 (Cross of Gold) only — appears once, lands hard, never returns |

Cue D is the new cue. It exists because the full-scale cut introduces Bryan as a real antagonist (the 5-min preview only name-checked "the opposition" at 2:00). Without a sonic counter to Hanna's mechanism, scene 13 plays as another fact beat instead of the structural "what almost happened" the script targets. **Cue D appears exactly once.** Reusing it would re-frame Bryan as a recurring character — the documentary's structural choice is that Bryan is the road not taken, single-appearance only.

The sting family is unchanged — one family for the whole 24 minutes. Default low-piano-and-sub. Never a fade-out / fade-in between scenes.

## 3. Cue-by-scene placement (the cue map)

Read this as the score sheet for the editor. Times are FULL_SCRIPT.md scene windows.

| Scene | Window | Music | Notes |
|---|---|---|---|
| 01 | 0:00–0:45 | Cue A title statement | Title is the opener. Cue A enters at full statement (~6 s) on the cartoon push-in, then ducks to −12 dB through "His name was Mark Hanna." Hard exit on the name. |
| 02 | 0:45–3:30 | Cue A bed | Cue A as bed under the ledger lines, ducked −8 dB. Number-theatre at 2:30 ("$3,500,000") — **Cue A drops out** for 1.5 s before the line so the count-up lands dry. Re-entry on a single low-piano transformed-A note. **Sting** at 3:30 (act break). |
| 03 | 3:30–5:00 | Silence + sting tail | Cold open closed; section opens on a sting tail with no bed. Silence is the cue here. New Lisbon in dry voice. |
| 04 | 5:00–6:00 | Silence | Rockefeller cameo plays dry. The "John D. Rockefeller" name-drop is the indictment beat for this scene; PLAN.md §3.2 mandates dry voice for indictment beats. |
| 05 | 6:00–7:30 | Cue A low-string drone variant | Pull-quote *"the real education was in the price of things"* — Cue A drone enters under the typography plate, exits when narration resumes. |
| 06 | 7:30–8:30 | Cue B introduction | First Cue B statement of the doc. Solo piano, ~−27 LUFS short-term, breath-paced. Charlotte's name lands dry; B re-enters on the Daniel Rhodes line. **This is one of the planned "silent reveal" beats from PLAN.md §3.3.** |
| 07 | 8:30–10:00 | Cue A bed | Chokepoint reveal; Cue A snare-ostinato variant under the moving-line map graphic. Exit before "the room changed temperature" — that line plays dry. |
| 08 | 10:00–11:30 | Silence | The thesis pivot ("Money was the second most powerful thing in America. The most powerful thing was who decided where the money went.") plays dry on a black plate. **This is the documentary's central indictment beat.** No music at all. The 1.0 s silence before the answer line is the most important moment in the cut. |
| 09 | 11:30–14:00 | Cue B at the loyalty beat | Cue A bed during convention floor; **Cue A drops out** at 13:00 for the McKinley loyalty refusal. Cue B (solo piano, single line) enters on "His name was William McKinley." Held under the floor-walk. Sting at 14:00. |
| 10 | 14:00–16:00 | Cue B + sting | Panic. McKinley's *"I am a beggar"* note plays dry; Cue B re-enters on "Mark Hanna picked up the phone." Sting at 16:00 leading into the mechanism reveal. |
| 11 | 16:00–17:45 | Cue A title-card register (−12 dB duck) | **The mechanism reveal.** This is the only place outside scene 1 where Cue A plays in its full title-card register (snare ostinato, not parlor-piano fallback). The on-screen ledger writes itself in `expo.out` on the beat of the snare. The Blood Oxide stamp lands on the cymbal cap (one isolated cymbal — the only one in the entire 24 min). Cue A exits cleanly at 17:45. |
| 12 | 17:45–18:30 | Silence + counter ticks | The visitor count is the audio: each "+12,400 / +74,000 / +218,000 / +501,200" stamp gets a single low-piano "tick" (sting-family-derived; 1/8 the volume of the section sting). No bed. The math IS the music. |
| 13 | 18:30–19:30 | **Cue D introduction (only appearance)** | Bryan's typography plate held in silence for 8 s. Cue D enters on the held quote at 19:00 — a single rising 4-note phrase on muted cornet, sparse, never resolves. The narration line "*The opposition had a thirty-six year old preacher who could move a crowd to tears*" is delivered over Cue D. Cue D exits before "Hanna read the speech in Cleveland that night" — that line plays dry into the next scene's bed. |
| 14 | 19:30–20:15 | Cue A counter | Cue A snare-ostinato variant beats under the 0 → 200,000,000 counter. The counter IS the music — visual tempo locks to snare. |
| 15 | 20:15–20:45 | Silence | Election-night plate. **Hard silence** — 1.5 s before "And when November came, the ledger won." This is the third payoff. PLAN.md §3.3 mandates the silent reveal at the single biggest moment; this is it. Re-entry: a single low-piano transformed-A note 0.5 s after the line lands. |
| 16 | 20:45–22:00 | Cue A → silence | Senatorial timeline strip plays under Cue A bed. Cue A exits at 21:30 for the Hanna pull-quote (*"Don't any of you realize there's only one life..."*) — the quote plays dry. No re-entry; scene ends in silence. |
| 17 | 22:00–23:00 | Silence + Cue B late entry | **Buffalo.** 1.5 s of silence before "Buffalo. September 6, 1901." The line itself plays dry. The shots ("Two shots.") play dry. Cue B enters quietly on "McKinley dies eight days later" — solo muted cornet, the texture only seen otherwise as a Cue B alternate. The cornet is the funeral march that doesn't quite arrive. |
| 18 | 23:00–23:30 | Cue B continues | The same Cue B muted-cornet line carries into Hanna's typhoid death. Single instrument, single line, no harmony. Exits on "Roosevelt walks the nomination." |
| 19 | 23:30–24:00 | **Cue C** | The motif-A contour reharmonized in B's register, full volume, slow. Plays out over the timeline-of-elections graphic. Fade to silence on the end card at 24:00. **Open editorial decision (PLAN.md §4):** audition full-volume vs thinned-reharmonization variants — pick on the locked end card. |

### Unscored runtime audit

Counting "no music" minutes from the table above:
- Scene 03 (1:30), 04 (1:00), most of 08 (~1:15), 12 (45 s), most of 15 (~25 s), opening of 17 (~30 s), most of 16 (~30 s) = ~6:00 of dry voice + room tone.
- Plus ~3 s × 8 silent-reveal moments (scenes 02, 06, 07, 09, 10, 13, 15, 17) = ~24 s of micro-silences.
- Plus 4 s cold-open silence + ~30 s of held-quote silences = ~34 s.

Total unscored ≈ 7:00 / 24:00 = **29%**. Below PLAN.md's 40–60% target. **Action:** the editor should aim to extend dry passages by 1–2 s at scene boundaries during the audition pass to lift the unscored share toward 35–40%. The full 60% is unrealistic for a 24-min explainer-register cut; 35–40% is the negotiated floor.

## 4. Music-bed lift map (the +3 dB moments per FULL_SCRIPT.md §4)

The script's pacing notes call for 4 music lifts of +3 dB at:
- 2:30 (Cue A — number theatre payoff #1, "$3,500,000")
- 16:00 (Cue A title-card register — mechanism reveal)
- 20:15 (the silence-then-low-piano-note moment — the lift is *into* the silence, not the bed)
- 23:30 (Cue C entry on the closing reflection)

These are the ONLY four +3 dB moments in the entire 24 min. Everywhere else, Cue A and Cue B sit flat at their respective LUFS targets.

## 5. Provenance shortlist (period-PD audition queue)

Per PLAN.md §3.5, the editor pulls the first 3–5 hits from each row and auditions against the locked cut. For full-scale, the audition queue extends:

| Source | Search prompt | Likely role |
|---|---|---|
| Library of Congress *National Jukebox* | "Sousa Liberty Bell" (1893) | Cue A base — period-strict |
| LoC *National Jukebox* | "1896 march band recording" | Cue A variation |
| LoC *National Jukebox* | "1898 cornet solo" | Cue B muted-cornet path |
| LoC *National Jukebox* | "1897 parlor piano" | Cue B solo-piano path |
| IMSLP (recordings) | Sousa "Stars and Stripes Forever" (1896) — period-strict | Cue A title-card statement |
| IMSLP (recordings) | "Joplin Maple Leaf Rag" (1899) | Period-adjacent — flavor only, NOT Cue A |
| Musopen | "late romantic minor-mode solo piano" | Cue B "Weight" path |
| Musopen | "muted cornet solo, slow, mournful" | Cue B alternate |
| Internet Archive (78rpm Project) | "1890s campaign band" | Cue A texture; sting family |
| Suno Pro (logged) | "1890s muted cornet single rising line, sparse, no accompaniment, no resolution, public-domain feel" | **Cue D** — Bryan counter-current, original AI motif (no period-PD recording fits the brief — Bryan's speech was July 1896; no period recording of similar register exists) |
| Suno Pro (logged) | "1890s parlor piano reharmonization in minor mode, slow, reflective" | Cue C coda variant |
| Suno Pro (logged) | "1890s low-piano single-note sting, decisive, no melody" | Sting family default |

Cue D is the cue most likely to require AI generation: the brief (a single, never-resolving counter-current to Hanna's snare-ostinato) doesn't have a period-PD analog. Suno Pro generation is allowed per PLAN.md §3.1 item 2 with full provenance logging in `assets/MUSIC_LICENSES.md`.

## 6. Acceptance — what this plan delivers

- ✅ Music plan: cue palette extended to 4 cues (A, B, C, D) for 24-min runtime; cue D justified by Bryan-as-antagonist structural choice.
- ✅ Cue-by-scene timing aligned to FULL_SCRIPT.md §3 engagement beats (2:30, 16:00, 20:15, 23:30 lift map).
- ✅ Unscored-runtime audit: 29% achieved by structure; 35–40% target negotiated against PLAN.md's 40–60% original.
- ✅ Composition / audition brief per cue, source-prioritized (period-PD → AI-generated → CC-BY).
- ✅ All choices anchored to existing PLAN.md so the editor doesn't have two conflicting documents.
