# Sound Design Plan — full-scale Mark Hanna documentary (24:00)

> Sibling task: t_be6c1904. SFX layer is a deliberate minimalism, not a "where do we put boom hits" exercise.
> The DESIGN.md mandate ("Decisive, not bouncy. No movie-trailer brass. No bouncy / elastic eases.") binds
> the sound design as much as it binds the visuals.

## 1. Aesthetic posture

This is an HBO investigative documentary in register, not a YouTube explainer. Three rules:

1. **The SFX library is austere.** The whole 24-min cut uses fewer than ~20 distinct sound-effect events. If a hyperframe transition can read clearly as motion without a sound, it gets no sound.
2. **Period-grain over modernity.** Every effect is texturally believable to 1896: paper rustle, ledger pen scratch, telegraph chatter, snare drum, hammer-on-iron, cornet/whistle, distant carriage, mechanical clock. **No** synthesized whooshes, **no** sub-drops, **no** modern UI clicks, **no** "trailer impact hits." The DESIGN.md "no bouncy" rule applies to the sound stems too.
3. **Voice is sovereign — same as music.** SFX duck under VO at the same depth as the music bed. Any SFX that competes with a sentence loses; we re-time the SFX, not the line.

## 2. Effect families (the entire SFX inventory)

Eight effect families cover all 19 scenes. Source order: period-PD library recordings first (LoC + Internet Archive), CC-BY secondary, custom Foley last. No paid stock libraries (PLAN.md §3.1 forbidden list applies).

| # | Family | Texture / source | Used in scenes |
|---|---|---|---|
| 1 | **Newspaper rustle** | Single sheet of broadsheet folding/turning, dry close-mic, pre-1900 pulp paper | s01, s02, s10, s17, s19 |
| 2 | **Ledger pen scratch** | Steel nib on rag paper, rhythmic single strokes, no scribble | s02, s11 (hero), s14 |
| 3 | **Telegraph dot-dash chatter** | Period telegraph key recording, sparse not continuous | s02 (under bed), s10 (Panic) |
| 4 | **Snare drum hit** | Period military snare, tight head, single hits — never rolls or rudiments | s11 (hero — beats with the typography), s14 (under counter), s16 (timeline strip) |
| 5 | **Hammer on iron / forge** | Industrial Cleveland 1880 — single metal-on-metal strike, low-mid resonance | s07 (chokepoint reveal — once on the dollar-sign pulse) |
| 6 | **Distant carriage / rail** | Period horse-and-carriage cobblestone OR 1890s steam locomotive far-off whistle | s03 (carriage on cobble — sets the New Lisbon time), s12 (distant rail under the visitor counter), s13 (Bryan tour rail) |
| 7 | **Cornet / whistle** | Single isolated muted-cornet note OR steam-whistle; period-PD only | s17 (Buffalo — one whistle on the assassin's name beat — *never* on the bullet itself) |
| 8 | **Mechanical clock tick** | Pendulum clock, single tick interval ~1.0 s | s18 (Hanna's typhoid death — clock under the obituary plate) |

## 3. Per-scene SFX placement

Not every scene gets an effect. **No-SFX scenes**: 04 (Rockefeller), 05 (price of things), 06 (Charlotte — silence is the cue), 08 (the thesis — silence is the cue), 09 (until sting), 15 (election night — silence is the cue). These scenes are deliberately bare; adding any sound effect breaks the engagement engineering.

| Scene | SFX events | Notes |
|---|---|---|
| 01 — THE CARTOON | (1) **Newspaper rustle** at 0:04 (the 4-second cold-open silence ends with one sheet turning) | Sets the period and breaks the silence into the first narration line. |
| 02 — THE LEDGER | (1) **Ledger pen scratch** beats under "$3,500,000" count-up at 2:30 (one stroke per million); (2) **Telegraph chatter** sparse under the donor lines (one dot-dash burst per donor line, ~3 s spacing); (3) **Newspaper rustle** at the act-break sting at 3:30 | The pen-scratch sells the count-up as bookkeeping. The telegraph sells the assessment system as networked. |
| 03 — NEW LISBON, OHIO. 1837. | (1) **Distant carriage on cobblestone**, low-mix bed for the first 6 s of the scene, fades to silence | Period-locator. Exits before "His father, Doctor Leonard Hanna…" |
| 07 — THE CHOKEPOINT | (1) **Hammer on iron**, single strike at 9:00 on the dollar-sign pulse over the Cleveland-node map | One hit, not a rhythm. Foley sells the industrial reality the visual abstracts. |
| 10 — THE PANIC | (1) **Newspaper rustle** at 14:00 on the headline plate; (2) **Telegraph chatter** sparse under "Banks collapse from New York to San Francisco" — one burst on each city name | The telegraph is now alarm, not bookkeeping. |
| 11 — THE MECHANISM | (1) **Snare drum hit** beats with each ledger line writing in (`expo.out`) — one hit per line; (2) **Ledger pen scratch** under the total stamp at the end of the scene | Snare matches Cue A's title-card register. Pen-scratch returns to seal the math. |
| 12 — THE FRONT PORCH | (1) **Distant rail** bed ~−30 LUFS under the entire scene; (2) Counter-stamp ticks (low-piano, see music plan) sync with the visitor-count stamps | Rail bed = the half-million voters in transit. Audible only if you listen for it. |
| 13 — CROSS OF GOLD | (1) **Distant rail** at 19:00 entering on "Bryan tours" line; exits at the held quote | The rail says Bryan is moving. The held quote silence says Hanna isn't. |
| 14 — TWO HUNDRED MILLION | (1) **Snare drum** beats with the 0 → 200,000,000 counter (4 s expo.out, ~16 hits decelerating); (2) **Ledger pen scratch** punctuates the final number | Snare and pen are doing the work the music's Cue A counter sells visually. |
| 16 — SENATOR HANNA. AND THE COWBOY. | (1) **Snare drum** single hit at 21:00 on each timeline-strip year (`1897`, `1899`, `1900`) — three hits total | Three hits = three years. The pull-quote that follows plays in dry voice, no SFX. |
| 17 — BUFFALO | (1) **Newspaper rustle** at 22:30 on the "PRESIDENT SHOT AT EXPOSITION" headline; (2) **Cornet/whistle** — one isolated muted-cornet note on the Czolgosz name plate (the assassin's name appears for 1 s and disappears) | **No gunshot SFX.** The bullet plays on the word "Two shots." in dry voice — the script line carries the impact, not the sound effect. The cornet is a funeral whisper, not a flourish. |
| 18 — TYPHOID | (1) **Mechanical clock tick** ~−32 LUFS bed under the obituary plate, ~1.0 s per tick, runs the full 30 s of the scene | The clock is the only SFX of the scene. It ends with Cue B's muted cornet from scene 17 still finishing — the two layers say "time runs out." |
| 19 — THE INHERITANCE | (1) **Newspaper rustle** at 23:55 on the final cartoon image return | Closes the loop with the same sound that opened the doc. The cut to black is silent. |

## 4. SFX mixing targets

- **Foreground SFX events** (snare hits, hammer-on-iron, newspaper rustle on the headline): −18 to −22 LUFS short-term. Sit slightly above the music bed but never above the voice.
- **Bed SFX** (distant carriage, distant rail, clock tick): −30 to −32 LUFS short-term. Subliminal layer; presence-not-attention.
- **Ducking:** every foreground SFX ducks under voice exactly as the music bed does — −8 dB sidechain. Bed SFX do NOT duck, because they're already below the duck floor.
- **Stereo:** all SFX rendered to dual-mono center. Voice is mono-center; music is stereo. The sound design layer matches the voice layer's mono-center placement so it reads as "in the same room as the narrator," not as "soundtrack."
- **HPF** at 80 Hz on every SFX bus — keeps the low end clean for the music's bass register and the voice's chest tones.
- **No reverb tails** beyond the source recording's natural ambience. Adding plate or hall reverb would announce the SFX as cinematic; period-grain demands they sound captured, not designed.

## 5. SFX provenance — sourcing & licensing

Same contract as music (PLAN.md §3.6 binary copyright protocol): every SFX cue logged in `assets/MUSIC_LICENSES.md` (or a parallel `assets/SFX_LICENSES.md` if the editor prefers — both work) with all four mandatory fields filled before unlisted upload. Source order:

| Tier | Source | Use |
|---|---|---|
| 1 | **Library of Congress** *American Folklife Center* / *National Jukebox* | Period telegraph recordings, snare drum, period band cornet hits |
| 2 | **Internet Archive** 78rpm Project + *Open Source Audio* | Period industrial Foley (forge, hammer, carriage, rail whistle) |
| 3 | **Free Music Archive** SFX section (CC-BY-only filter) | Newspaper rustle, ledger pen-scratch, mechanical clock tick |
| 4 | **Custom Foley** (recorded by editor) | Pen-scratch and newspaper rustle if no FMA hit reads as period — these two are easy to record on-mic |

Forbidden: paid stock libraries (Soundsnap, BBC, Pond5), generic free-with-account libraries (Mixkit, Zapsplat) — same reasoning as PLAN.md §3.1 forbidden list.

## 6. Sound-on-frame tolerances

For the hyperframe transitions specifically (where a sound pairs with a visual cut):

- **Snare hits** must land within ±1 frame (±33 ms at 30 fps) of the visual `expo.out` arrival point. Off-by-2-frame snare reads as out-of-sync.
- **Newspaper rustle** has a ~80 ms attack — the rustle's *peak* aligns with the visual cut, not its onset.
- **Hammer-on-iron** has a ~10 ms attack — frame-tight, like the snare.
- **Distant carriage / distant rail / clock tick** beds don't sync to anything visual; they enter on a fade and exit on a fade.

The assembly-task editor (`t_e781bf96`) does the final sync pass against the rendered visuals.

## 7. What this plan does NOT include

Things that might look like sound design oversights but are intentional:

- **No music sting on every scene break.** The music plan has stings only at major act-breaks (3:30, 16:00); the rest of the scene transitions ride on the music bed's own dynamics or silence.
- **No "voice processing" on the narrator.** Voicebox George + atempo + loudnorm is the only chain. No reverb, no de-esser-as-effect, no character coloring.
- **No room-tone bed during dry-voice passages.** "Dry voice + room tone" in the script means the recording's own captured room tone, not a layered wild-track. Adding a layer reads as "trying too hard to sound HBO."
- **No Foley for character actions.** The narrator says "Mark Hanna picked up the phone" — there is no phone-pickup sound. Per the documentary register: we describe, we don't dramatize.

## 8. Acceptance — what this plan delivers

- ✅ SFX list per scene, restricted to 8 period-grain families.
- ✅ Hyperframe-transition coverage: snare/pen/rustle hit the structurally important visual cuts; the rest are intentionally bare.
- ✅ Delivery-moment coverage: every script "delivery moment" (number theatre, mechanism reveal, ledger lines, the bullet) has either an SFX cue or a deliberate silence cue documented above.
- ✅ Mixing targets concrete (dB / LUFS), ducking strategy aligned to music plan.
- ✅ Provenance & sourcing tier with same logging contract as music.
