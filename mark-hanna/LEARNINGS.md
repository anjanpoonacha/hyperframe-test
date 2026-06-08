# Mark Hanna — Voice & Render Learnings

Plain log of mistakes/quirks discovered while producing this episode. Not instructions — just observations to consult when something sounds off.

## Voice: bm_george (Kokoro)

- **Year digits read as cardinals.** "1896" is spoken as "one thousand eight hundred ninety-six" instead of "eighteen ninety-six". Workaround: spell years out as words ("eighteen ninety-six"). Adding "year" before the digits ("in year 1896") does NOT help — still cardinalised.
- **Leading word + comma gets clipped.** "Banks, assessed at a quarter..." came out as a stutter on "Banks" with an awkward stop before the rest of the sentence. Removing the comma so it reads as one continuous clause ("Banks assessed at a quarter...") fixes it. Likely applies to any `Word, descriptor...` opener.
- **Comma-listed nouns blur into a proper name.** "Coal, iron." after "Daniel Rhodes." was read as "Cole Iron" (sounds like a person). Fix: replace the staccato list with a connector — "Coal and iron." reads naturally.

## Voiceover vs on-screen typography (M14 — dual-channel rule)

- **Voiceover spells everything; on-screen typography uses numerals.** TTS gets prose ("eighteen ninety-six", "fifty-nine years old", "three and a half million dollars"). The composition HTML displaying the same beat uses numerals/symbols ("1896", "59", "$3,500,000"). They land together — voice carries emotion, screen carries credibility. Caught in scene-01 cold open: had `Eighteen Ninety-Six` in the headline strip and `Fifty-nine years old` in the bio stamp; corrected to `1896` and `59`. **Rule for every scene authoring pass:** grep the composition HTML for spelled-out numbers (`Eighteen|Nineteen|Twenty|Thirty|...|Fifty|Sixty|...|hundred|thousand|million`) and convert to numerals before sign-off. Voice ALWAYS spells, screen ALWAYS numerals.

## Pipeline

- **Voice swap drifts every hardcoded GSAP timing.** bm_george is ~12% faster than am_michael (238s vs 269s for the same script). All scene boundaries in `index.html` and every `tl.to(... , N)` position inside `compositions/scene-*.html` need to be re-warped against the new transcript. Keep `*.am_michael.bak` files around so the warp can be redone from the clean source instead of compounding.
- **`hyperframes validate` falsely flags `?v=2` cache-busters as 404.** File exists; the query string trips the validator. Pre-existing, not voice-related.
- **TTS engine alternatives.** Hyperframes ships only Kokoro-82M (no bigger model flag). User has the local **Voicebox** app installed for higher-quality TTS — uses Chatterbox/LuxTTS underneath, sounds noticeably better than Kokoro George. ElevenLabs free tier (~10k chars/month) is also viable but user declined.
- **Voicebox `personality=true` is just an LLM rewrite step.** It runs the input through a local Qwen3 with a "roleplay this character" system prompt (temperature 0.3, restate every idea in character) before TTS. Replicable in our own scripts with any LLM — no special voice magic. The actual audio quality boost comes from Voicebox's TTS engine choice, not personality.
- **Don't port to MLX.** Voicebox uses Apple MLX for ~30-40% speedup over MPS PyTorch. Porting Chatterbox to MLX ourselves would be days of work for marginal gain. Standalone Chatterbox via PyTorch+MPS is fast enough; iteration time is the real cost, not raw inference.
- **For long renders (35-min doc), split narration per scene.** Re-rendering an affected scene takes 1-2 min vs 10-15 min for the whole thing. Combined with the splice trick for one-word fixes (render 3-5s clip, ffmpeg concat into existing wav), iteration stays fast. Cost: scene-boundary intonation reset (George won't carry a thought across the join), N audio files to manage, possible voice consistency drift between renders.
- **Audio splices silently break captions.** Editing `assets/narration.wav` (splice graft, voice swap, full re-render) shifts every word boundary downstream of the cut. The cue file pair `assets/caption-groups.json` + `compositions/captions.html` is generated against a specific audio snapshot; if you don't regenerate after touching audio you accumulate progressive drift (saw -1520 ms cumulative skew at end-of-track in the wild). Rule: any time `narration.wav` changes, run `python3 scripts/make-captions.py`. The regenerator runs whisper word-level alignment on the current wav, regroups using the project rule (≤5 words, break on `.!?`), rewrites both the JSON and the inline `groups[]` + `<div class="cap-group">` block. Drift target ≤100 ms; in practice it lands at 0 ms.
- **Verifying caption sync needs three independent checks.** The regenerator's own drift verifier always reports 0 ms when the cues were just written from the same transcript — that's a tautology, not a sync proof. Real verification is: (a) re-run whisper fresh on current wav and re-fold; (b) independent audit script that re-walks each cue against transcript.json *without* reusing the regenerator's matcher; (c) live snapshot of the composition at start/middle/end timestamps and visual confirmation that each frame's rendered caption matches the cue file's text for that timestamp. `tests/audit_drift.py` does (b) for this project; `npx hyperframes snapshot --at "<csv of seconds>"` does (c).
- **Renders predate the fix unless you re-render.** `renders/*.mp4` was rendered 11:49 against the pre-fix caption file; the regenerator fix landed 14:36. Don't visually verify against an old MP4 — `hyperframes snapshot` at the timestamps you care about renders fresh from the *current* composition.
- **Final-cue endpoint can sit ~150 ms past the container's reported audio duration.** ffprobe says narration.wav is 239.35s; whisper's last-word.end is 239.50s; cap-159 ends at 239.50s. That's outside the 100 ms tolerance but it's measured against the *container header*, not against any actual word boundary — the cue still aligns at 0 ms with its source word. Not a sync defect, but worth knowing if `data-duration` on the captions layer is ever tightened to the container value.
- **Long-form (>20 min) is untested for the caption regenerator.** Episode 01 is a ~4-min preview; verification only covers short and medium length buckets. The pipeline is length-agnostic by design (whisper word-level alignment + rule-based folding), but no real >20-min sample has been pushed through it. When the first long-form episode lands, re-run `tests/audit_drift.py` plus snapshots every 2–3 minutes before trusting the regenerator at that scale.
- **Caption safe-zone is ~150 px from bottom.** `compositions/captions.html` puts cues at `bottom:32px` with 36 px / 1.25 line-height + 14 px vertical padding; a 2-line caption (e.g. "A 45-year-old congressman from Canton,") occupies roughly y930..1055. Any scene element living below y≈900 will collide once captions wrap to two lines. Fix in scene-04: lifted `.verdict` (the "Hanna lost" beat) out of flow and bottom-anchored it at 200 px, then dimmed the ballot rows above it on the same beat so the verdict still has visual stage. Rule going forward: anchor scene-bottom UI no lower than y≈880, or test against the worst-case 2-line cue, not just single-line samples.
- **Punctuation does not control Kokoro pacing.** Spike `tts-spike/` measured 87 clips: every sentence terminator (`.`, `?`, `!`, `...`, `—`, `;`, double space, `\n`, `\n\n`) lands inside a 22 ms band (~0.15 s). Whitespace is fully ignored. The 2:10–2:30 "rushed" stretch can NOT be fixed by adding ellipses or paragraph breaks — only `--speed 0.85` on the whole render or per-scene splice with `anullsrc` silence between clips will produce real breathing room. So that pending task is reframed: either accept the current pace, drop `--speed` per scene, or splice in custom silence — but stop trying to fix it with punctuation.
- **`J.P.` initials clip; `JP` flows.** Spike measured "J.P. Morgan paid." vs "JP Morgan paid." at identical 1.98s vs 1.83s with the inner pause shrinking 0.148s → 0.089s. Applied to narration.txt + spliced into existing wav as the JP Morgan fix.
- **Sentence-merge via comma works fine.** "brokers like him. He took a cut." → "brokers like him, he took a cut." renders with no audible stutter and the natural prosody the user wanted. The whisper retranscribe re-applied its own period/cap ("him. He"), which is fine — that's a recognition artifact, not the audio. Don't chase whisper output back into narration.txt.
- **Localized splices stay cheap.** Combined splice (JP + brokers) added +0.93s to total runtime. Per-scene `data-start` shifts: scene-01 unchanged, scene-02 +0.66, scene-03 +0.66, scene-04 +0.93. Scene-01 internal GSAP positions warped (11 rewrites; fix1 falls inside it). Scene-03 internal warped (14 rewrites; fix2 falls inside it). Scene-02 and scene-04 internal timings untouched (no splice landed in them — only their data-start shifted). Wrote a closed-form warp script (`tmp/warp_jp_brokers.py`) for splice-specific geometry instead of running the general anchor-based warp; cheaper when there are 2 known splices.
- **Splices accumulate audible stutter at boundaries.** After 5 sequential splices stacked over the bm_george base render (1896, Banks, Coal/iron, JP Morgan, brokers/he-took-a-cut), the user reported "bro broker" and "Co Coal" stutter at the brokers and coal locations. Root cause: whisper word boundaries aren't phonetically tight (~70 ms slop). Cuts at 139.55s and 112.4s captured the leading consonant attacks of the original "brokers" / "coal" into the pre-segment — when the new fragment plays, you hear the truncated "br..." / "Co..." attack, then the new word in full. silencedetect at -40dB shows the regions look like silence between words, but the consonant onset energy that defines the next word's start is below that threshold. **Lesson:** the splice-fix trick is fine for ONE or TWO localized fixes, but stacking 4+ splices over the same base wav compounds the boundary slop until you hear stutters. Once the splice count is high or the artifacts are audible, the cleanest cure is a full re-render: `bunx hyperframes@latest tts narration.txt -o assets/narration.wav -v bm_george` then regenerate captions and rewarp scene timings (~60s + 30s + 5s = under 2 minutes of compute total). Worth the time once you've already got 4+ splices in flight.
- **Whisper transcribes spelled-out years/numbers as digits, mishears proper-noun-adjacent commas.** "eighteen ninety-six" → "1896,". "Coal and iron" after a comma-pause becomes "Cole and Ian,". "Marcus Alonzo Hanna" → "Marcus Alonso". The audio is correct; whisper is normalizing/misrecognizing. For caption text we want the source script wording, not whisper's flattened/wrong forms. Fix: align narration.txt token stream against the whisper word stream (Needleman-Wunsch) and substitute source text at every position while keeping whisper's timings — `tmp/align_caps.py`. With this project's render: 27 substitutions, 27 source-only words (whisper missed), 3 whisper-only words (whisper hallucinated), out of 719 source tokens. Drift stays at 0 ms because we only swap text, not timings. Run order: re-render → make-captions.py (whisper) → align_caps.py (source override) → make-captions.py --skip-whisper.

## Hand-tuning vs generator vocabulary (scenes 4, 9, 10)

Per RELEASE_NOTE.md fidelity grading, scenes 4/9/10 were called out as "simpler than the boards" because the build_scenes.py generator vocabulary couldn't express what SHOT_BOARDS.md prescribed. Pass-2 hand-tune notes:

- **Scene 4 (Rockefeller diptych).** Generator emitted scale `0.55→0.561` Ken Burns (1.001× — invisible). Boards call for real push 1.00→1.02 over 12s plus pull-out 1.04→1.00 over 25s on the diptych. Hand-authored: scale 0.55→0.572 push (24.5s) + 0.572→0.55 pull (25s) per portrait, both `sine.inOut`. Added the 1px Hanna Amber hairline draw between portraits at @9s (240px width, 0.6s power2.out, glow via box-shadow). Added Rockefeller's `x+60` slide-in on the entry per board KF @8. Added scene-relative typography re-anchoring: portraits raised to top:40%, max-height 620px so the bottom-anchored name plate at y=80% clears them with ~15% gap. Generator-grade kept: chapter card, year strap, verdict line. Scene-relative timing preserved (LEARNINGS line 13).

- **Scene 9 (Chicago 1888 / vote tally / hard cut).** Generator emitted single static name plate for Sherman; boards call for the plate to corner-pin shrink to a tag-size mono entry (`SHERMAN, JOHN — OHIO · TREAS.`) that persists through the tally crawl, then dim 30% at @42s. Hand-authored: Sherman big plate exits at @14 with translateX +600 / translateY -120 / scale 0.3 over 1.0s `power2.in`, while a separate `#s9-sherman-tag` element fades in upper-right at @14.6 and dims to 0.3 opacity at @42-46s. Convention image gains real push 1.00→1.04 (18s) + pull 1.04→1.00 (40s) and a brightness/saturate filter dim @42 paired with the tag dim ("the floor of the convention image dims with it"). Hard cut to black at @60-61: dedicated `#s9-blackout` div opacity 0→1→0 over 1.3s. McKinley name plate gets letter-spacing tighten 0.05em → -0.02em over 1.4s `power3.out`. Ballot 8 gets a 1.06× scale pulse on its row (entries land at @28.3 + n×1.4s; ballot 8 lands at @38.1). Generator-grade kept: tally row stagger duration, hero text/verdict typography. The `gsap.set` ownership pattern for the convention image, McKinley portrait, and Sherman name — `xPercent: -50, yPercent: -50, scale: <init>` — keeps the lint clean (no gsap_css_transform_conflict warnings).

- **Scene 10 (Panic / 2-pane).** Generator emitted Ida + McKinley as overlapping center-stacked elements; boards call for a true 2-pane layout (McKinley portrait cols 1-6, Ida typography plate cols 7-12). Hand-authored: McKinley portrait positioned at left:25% with capped 680×780px, scale 0.85→0.872 push during the 12s hold; Ida typography plate `#s10-ida-plate` at left:75% width 760px with vertical amber accent rule, slides in from `x:240` over 1.0s `power3.out`. Newspaper composite gains sub-headline (`1,500 BUSINESSES UNDER. 640 BANKS FAIL.`) that animates in below the headline at +4s, and a Cleveland Plain Dealer topline. Hard cut to black at @28-28.6 via `#s10-blackout`. "I am a beggar." plate gets letter-spacing tighten 0.05em → -0.02em over 0.7s, vertically centered at top:50% with translateY -50%. Verdict pair @75 uses pure crossfade (no y-rise) per board KF specifying "cross-fade in over 1.0s". Generator-grade kept: rescue ledger row stagger (now 1.0s/line per board), verdict color pairing (Blood Oxide / Hanna Amber). Ida photograph remains a typography fallback (procurement gap noted in RELEASE_NOTE.md §known-gaps).

- **Generator regeneration safety.** Added `HAND_TUNED_SKIP = {4, 9, 10}` guard in `research/full-scale/build_scenes.py main()` so re-running the generator won't clobber the bespoke keyframes. The skipped scenes still appear in `SCENES_INDEX.json` so `index.html` resolves them. Verified: regeneration leaves all three hand-tuned files byte-identical.

- **Lint guard for GSAP-CSS transform conflicts.** When a CSS rule sets `transform: translate(-50%,-50%) scale(N)` on an element and GSAP later animates `scale`, GSAP overwrites the entire CSS transform — discarding the centering. Fix used in scenes 4/9/10: drop the CSS `transform` from the inline style and prepend `gsap.set("#id", { xPercent: -50, yPercent: -50, scale: N })` before any tweens. This way GSAP owns the transform stack and the lint stays clean (only the 2 pre-existing intentional-overlap warnings on `index.html`/`captions.html` remain).

## SFX layer (procedural Tier-4 Foley) — t_1fc72c12

- **VO collision verification has to come from the actual master, not the
  preview transcript.** `assets/transcript.json` is a 5-min preview transcript
  (237 s of words). The full-scale narration is 1440 s; word boundaries below
  237 s in the preview transcript do not correspond to word starts in the
  full-scale master. The SFX placement validator must call ffmpeg
  `silencedetect` on `assets/narration.fullscale.wav` directly to know where
  inter-word silences live. `_sfx_placements.py` does this; running the
  placement script against the preview transcript produced 5 phantom
  "violations" that disappeared once we re-anchored to silencedetect.

- **The plan's per-scene placement table sometimes calls hits inside scenes
  whose VO occupies the full window.** SOUND_DESIGN_PLAN.md §3 prescribes
  snare hits in scenes 14 + 16 to sync with the visual counters/timeline.
  Reading the plan against `narration.fullscale.wav` showed those scenes have
  no usable inter-word silence wide enough to land a snare hit cleanly
  without violating the §4 rule "no event masks VO during a spoken word."
  Resolution: drop the s14 and s16 snare hits, keep the structurally
  important snare cluster at the scene-11 mechanism reveal (hits 985/986/987 s,
  in the 80-second post-VO silence). The plan's intent (snare = mechanism
  motif) is preserved; the literal scene assignment is not. Logged in
  MIX_MANIFEST.md so future renderers don't re-add them.

- **Snare hits had to slide past the visual KF arrival.** Boards put the
  ledger-line write-ins at scene-relative t=22.0 s (= 982 s absolute), but
  scene-11 VO doesn't end until 984.85 s. We pushed the snares to 985/986/987 s
  and document that the renderer should schedule the ledger-line write-in
  to land on the snare beat (not the literal board t=22), because the SFX
  layer is binding for hit timing and the music+visual layers absorb the
  ~2-second offset via their own dynamics (Cue A rest, KF easing). This is
  consistent with SOUND_DESIGN_PLAN §6 "snare hits land within ±33 ms of
  the visual `expo.out` arrival point" — the renderer schedules the visual
  to the SFX, not the other way around.

- **macOS bash 3.2 has no `mapfile`.** The mix script reads ffmpeg args from
  a file via a python helper instead. Don't use `mapfile -t arr <file` in
  scripts that need to run on stock macOS.

- **Procedural synthesis sidesteps Tier-1/2/3 procurement entirely.** All 17
  stems are deterministic numpy synthesis (seeded RNGs in `_synth_sfx.py`).
  This satisfies the Tier-4 "Custom Foley by editor" path in
  SOUND_DESIGN_PLAN.md §5 with three concrete wins: (a) zero attribution /
  Content ID risk under the unlisted upload contract, (b) byte-identical
  reproducibility across machines and re-renders, (c) period-grain control
  — no anachronistic room tones from real recordings. Trade-off: stems lack
  the random microvariation of field recordings, mitigated by the gain
  staging keeping every event under the duck floor where the listener never
  auditions them dry. The swap path to a real-recording stem (most likely
  cornet for s17 Buffalo if a v3 wants warmth) is documented in
  `assets/SFX_LICENSES.md`; it's a single-file replace + license-fields
  update + `build_sfx_mix.sh` re-run.

- **Coordinate the v2-master filename with the music task.** Both audio
  tasks (music t_65915e49 and SFX t_1fc72c12) target
  `narration.fullscale.v2.wav`. Whichever finishes first owns the filename.
  The SFX task deliberately writes `narration.fullscale.sfx.wav` (VO+SFX,
  no music) and exposes the SFX-only stem at `assets/sfx/_mix.wav`, so the
  music task can ingest it as a third input to its v2 build (single shipped
  master). MIX_MANIFEST.md is the coordination doc.

---

## 2026-06-07 — Runtime contract audit (the v2.1 9-min discovery)

**Mistake:** I treated `FULL_SCRIPT.md`'s 6,479-word claim as the spoken script, then v2.1 inherited that assumption. When `script-to-vo.ts` extracted just the narration prose, the actual spoken word count was **1,541 words** — 9:07 of audio at bm_george default speed (172 wpm avg). The 6,479-word figure was the whole file including scene descriptions, character bios, beat sheets, visual notes — NOT just the spoken text.

**The earlier hint was in plain sight:** v1 RELEASE_NOTE.md said "459s spoken across 19 scenes against 1440s runtime — 34% spoken / 66% visual hold." That's the ratio that should have been a red flag — a documentary spoken at 34% of its runtime was getting padded heavily by silence + visual holds, not by dense narration. CHANNEL.md §3 assumes 160 wpm with normal pauses, not 34% spoken time.

**Why I missed it for hours:**
- Trusted the FULL_SCRIPT.md header's "6,479 words" without splitting prose vs metadata
- The two-agent MACI review caught voice/style issues but not word-count budget (their focus was prose quality, not channel-contract compliance)
- I never measured spoken word count against CHANNEL.md's 5,000-6,500 target until AFTER TTS render

**Corrected procedure (from now on):**
1. Before any TTS pass, run `script-to-vo.ts --dry-run` and count words in the extracted scene .txt files only
2. Compare to the channel runtime contract (CHANNEL.md §3 — 5,000-6,500 words for 30-40 min)
3. If gap > 20%, expand the script first; do NOT render to find out

**Word-count-to-runtime conversion for bm_george (default speed):**
- Measured: 172 wpm average across all 19 scenes
- 5,000 words → ~29 min of speech (without any silence padding)
- 6,500 words → ~38 min of speech
- Adding ~10% silence for natural pauses: 5,000 → ~32 min, 6,500 → ~42 min
- Channel sweet spot 35 min → ~5,500-5,800 spoken words

**The v2.1 data preserved as baseline** (do NOT delete; v3 expands from this):
- 1,541 spoken words across 19 scene .txt files
- 9:07 master audio at -15 LUFS
- Per-scene word counts measured (see git history)
