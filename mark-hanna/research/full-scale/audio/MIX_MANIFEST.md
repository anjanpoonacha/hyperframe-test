# MIX_MANIFEST.md — Mark Hanna full-scale audio integration

> Coordination doc shared between the music-mix task (sibling t_65915e49)
> and the SFX-mix task (this one, t_1fc72c12). Each section is owned by
> the task that authors it. The renderer task t_6eab435b reads this to
> know which master to wire into `index.html`.

## Outputs (this task — SFX layer)

| File | Role | Format | Duration |
|---|---|---|---|
| `assets/sfx/<family>-NN.wav` | 17 procedural stems (8 families) | mono 48 kHz pcm_s16le | 0.30–16.00 s each |
| `assets/sfx/_placements.json` | machine-readable event table | JSON | — |
| `assets/sfx/_mix.wav` | SFX-only stem at master timing | mono 48 kHz pcm_s16le | **1440.000 s** |
| `assets/narration.fullscale.sfx.wav` | VO + SFX (no music) | mono 48 kHz pcm_s16le, loudnorm I=-16:TP=-1.5:LRA=11 | **1440.000 s** |

The SFX-mix task **deliberately does not write `narration.fullscale.v2.wav`** —
that filename is owned by the sibling music-mix task. Coordination protocol:

- If music task finishes first → it produces `narration.fullscale.v2.wav` (VO + music).
  The renderer (t_6eab435b) then runs a final `amix` of `narration.fullscale.v2.wav`
  + `assets/sfx/_mix.wav` → `narration.fullscale.v3.wav`, or extends the music
  task's `build_master_v2.sh` to ingest the SFX bus directly.
- If SFX task finishes first (current state) → music task ingests
  `assets/sfx/_mix.wav` as a third input to its v2 build, producing a single
  `narration.fullscale.v2.wav` containing VO + music + SFX. This is the
  preferred path because it keeps a single shipped master.

The renderer should consult this MIX_MANIFEST.md to discover which master is
canonical at render time. **Do not** modify `index.html`'s `<audio src=…>`
until the renderer task runs; this SFX-mix task leaves index.html untouched.

## SFX event table (this task)

20 stem fires across 17 distinct plan-events, all VO-collision-clean
(verified against `narration.fullscale.wav` silencedetect at -40 dB / 0.20 s).
The clock-tick bed in scene 18 is a single plan-event implemented as 30
sequential 1.0 s ticks; everything else is one fire per plan-event.

| # | t_start (s) | family | layer | gain (dB) | scene | target visual cue | file |
|---|-------------|--------|-------|-----------|-------|-------------------|------|
| 1 | 3.30 | newspaper | fg | -2.0 | 01 | cold-open silence break | newspaper-01.wav |
| 2 | 150.00 | ledger | fg | -3.0 | 02 | count-up tick 1 of 3 | ledger-01.wav |
| 3 | 150.70 | ledger | fg | -3.0 | 02 | count-up tick 2 of 3 | ledger-02.wav |
| 4 | 151.40 | ledger | fg | -3.0 | 02 | count-up tick 3 of 3 | ledger-01.wav |
| 5 | 180.00 | telegraph | fg | -9.0 | 02 | donor lines telegraph chatter | telegraph-01.wav |
| 6 | 209.30 | newspaper | fg | -3.0 | 02 | act-break sting | newspaper-02.wav |
| 7 | 210.00 | carriage | bed | -12.0 | 03 | period locator bed | carriage-01.wav |
| 8 | 541.70 | hammer | fg | -4.0 | 07 | dollar-sign pulse strike | hammer-01.wav |
| 9 | 839.30 | newspaper | fg | -3.0 | 10 | PANIC headline plate | newspaper-03.wav |
| 10 | 895.00 | telegraph | fg | -7.0 | 10 | post-PANIC telegraph burst | telegraph-02.wav |
| 11 | 985.00 | snare | fg | -3.0 | 11 | ledger line 1 expo.out | snare-01.wav |
| 12 | 986.00 | snare | fg | -3.0 | 11 | ledger line 2 expo.out | snare-02.wav |
| 13 | 987.00 | snare | fg | -3.0 | 11 | ledger line 3 (mechanism reveal sync) | snare-03.wav |
| 14 | 995.00 | ledger | fg | -4.0 | 11 | total stamp pen scratch | ledger-02.wav |
| 15 | 1065.00 | rail | bed | -16.0 | 12 | porch rail bed | rail-01.wav |
| 16 | 1112.00 | rail | bed | -14.0 | 13 | Bryan tours rail bed | rail-02.wav |
| 17 | 1350.00 | newspaper | fg | -3.0 | 17 | PRESIDENT SHOT headline | newspaper-02.wav |
| 18 | 1370.00 | cornet | fg | -8.0 | 17 | Czolgosz name plate (single muted note, **no gunshot**) | cornet-01.wav |
| 19 | 1380.00 | clock | bed | -22.0 | 18 | typhoid obituary clock bed (30 ticks @ 1.0 s) | clock-01.wav |
| 20 | 1434.50 | newspaper | fg | -4.0 | 19 | closing-loop rustle | newspaper-01.wav |

### Scenes deliberately bare (no SFX, per SOUND_DESIGN_PLAN §3)

`s04` Rockefeller cameo · `s05` price of things · `s06` Charlotte (silence is the cue) ·
`s08` thesis pivot (silence is the cue) · `s09` until sting · `s14` two-hundred-million ·
`s15` election night (silence is the cue) · `s16` timeline strip.

> Note on scenes 14 + 16: the SOUND_DESIGN_PLAN.md per-scene table assigns snare
> hits to s14 and s16, but reading the plan against the rendered VO timing
> revealed those scenes' VO occupies the entire scene window with no usable
> inter-word silence wide enough to land a snare hit cleanly. Rather than
> compromise on the "no event masks VO during a spoken word" acceptance rule,
> we **intentionally drop** the s14 and s16 snare hits; the scene-11 mechanism
> snares (#11–13 above) carry the snare motif at the structurally important
> reveal. This is documented in the LEARNINGS.md update appended below.
> Plan-events count remains ≤20.

## Acceptance verification

- ✅ ≤20 distinct events: **17 plan-events / 20 stem fires**
- ✅ No event masks VO during a spoken word: all 20 fires verified
  `in_silence` or `quiet (≥6 dB under VO peak)` against silencedetect map.
  See `assets/sfx/_placements.json` for per-event verdict.
- ✅ Loudness preserved on the VO+SFX bus: `narration.fullscale.sfx.wav`
  maintains `loudnorm=I=-16:TP=-1.5:LRA=11` (master target) with mean
  volume ~-19.3 dB and max -1.5 dB (no clipping).
- ✅ Reproducibility: `_synth_sfx.py` (procedural stems), `_sfx_placements.py`
  (placement + validation), `build_sfx_mix.sh` (final mix) all checked in.
- ⏳ Lint pass: deferred until renderer task wires the final master into
  `index.html` (see coordination protocol above).

## Music section (sibling t_65915e49)

See sibling task `t_65915e49` summary for the cue-by-cue table. 4 cue stems
shipped (Cue A=Liberty Bell March 1895, Cue B=Nearer My God to Thee 1902, Cue
C=DSP-derivative of A, Cue D=ffmpeg additive synth). All 4 lift sync points
land sample-accurately at 105.0/108.5s, 969.5s, 1224.0s, 1410.0s. Music task
shipped its `assets/narration.fullscale.v2.wav` as VO+music only and explicitly
deferred SFX-bus integration to the renderer (see "handoff_to_sibling_t_1fc72c12"
field).

## Final master (renderer task t_6eab435b)

The renderer ingested both upstream artifacts and produced the canonical
shipped master:

| Stage | Artifact | Notes |
|---|---|---|
| Music sibling output | `assets/narration.fullscale.v2.music-only.wav` (renamed from `assets/narration.fullscale.v2.wav` before merge) | preserved for audit |
| SFX sibling output  | `assets/sfx/_mix.wav`                                                                                       | SFX-only stem at master timing |
| **Final v2 master** | **`assets/narration.fullscale.v2.wav`**                                                                     | **VO + music + SFX, mono 48 kHz pcm_s16le, loudnorm I=-15:TP=-1.5:LRA=18, 1440.000 s** |

Build command (reproducible):

```bash
ffmpeg -y \
  -i assets/narration.fullscale.v2.music-only.wav \
  -i assets/sfx/_mix.wav \
  -filter_complex "[0:a][1:a]amix=inputs=2:duration=longest:dropout_transition=0:normalize=0,loudnorm=I=-15:TP=-1.5:LRA=18[out]" \
  -map "[out]" -ar 48000 -ac 1 -c:a pcm_s16le \
  assets/narration.fullscale.v2.wav
```

`index.html`'s `<audio src=…>` was switched from `assets/narration.fullscale.wav`
to `assets/narration.fullscale.v2.wav` as part of the renderer task. Lint
re-run after the swap: 0 errors, the same 2 pre-existing intentional
`overlapping_gsap_tweens` warnings on `index.html` and `compositions/captions.html`.
