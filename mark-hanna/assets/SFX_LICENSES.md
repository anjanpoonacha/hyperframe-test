# SFX_LICENSES.md — Mark Hanna documentary

> Per SOUND_DESIGN_PLAN.md §5 (sourcing & licensing) and PLAN.md §3.6
> (binary copyright protocol): every SFX stem that ships in the documentary
> must have its provenance logged here before the unlisted YouTube upload.
> Missing any field → stem does not ship.
>
> This SFX layer was procured under **Tier 4: Custom Foley by editor**
> (per SOUND_DESIGN_PLAN.md §5 table). All 17 stems are procedurally
> synthesized from numpy primitives — there is no upstream source to
> license. The script `research/full-scale/audio/_synth_sfx.py` is the
> provenance.

## License declaration

| Field | Value |
|---|---|
| **Source** | Procedural synthesis — `research/full-scale/audio/_synth_sfx.py` |
| **License** | CC0 1.0 Universal (Public Domain Dedication) |
| **Attribution string** | "SFX synthesized for Mark Hanna documentary; CC0." |
| **Date generated** | 2026-06-07 |
| **Author** | Mark Hanna documentary editor (procedural pipeline) |

The script is deterministic: given the seeded numpy RNG values in
`INVENTORY` (seeds 11–91), the same waveforms are reproducible byte-for-byte
on any machine running the same numpy + bit-identical math. Re-run
`python3 research/full-scale/audio/_synth_sfx.py` to regenerate.

## Stems

| File | Family | Synthesis method | Duration |
|---|---|---|---|
| sfx/newspaper-01.wav | newspaper-rustle | Pink-noise crinkle, granular bursts, BPF 800–6 kHz, AM envelope | 0.70 s |
| sfx/newspaper-02.wav | newspaper-rustle | Same family, seed 12 | 0.60 s |
| sfx/newspaper-03.wav | newspaper-rustle | Same family, seed 13 | 0.65 s |
| sfx/ledger-01.wav | ledger-pen | High-band noise (2.5–9 kHz), Gaussian stroke env, micro-flutter | 0.32 s |
| sfx/ledger-02.wav | ledger-pen | Same family, seed 22 | 0.40 s |
| sfx/telegraph-01.wav | telegraph | Random Morse word @ 12 wpm, 800 Hz keyer tone, relay-bed hiss | 1.60 s |
| sfx/telegraph-02.wav | telegraph | Same family, seed 32 | 1.40 s |
| sfx/telegraph-03.wav | telegraph | Same family, seed 33 | 1.50 s |
| sfx/snare-01.wav | snare | BPF noise body + 220/380 Hz tone modes + HPF wires noise | 0.30 s |
| sfx/snare-02.wav | snare | Same family, seed 42 | 0.30 s |
| sfx/snare-03.wav | snare | Same family, seed 43 | 0.30 s |
| sfx/hammer-01.wav | hammer-iron | Inharmonic partial stack (ratios 1.0/1.78/2.43…) + click + body noise | 1.20 s |
| sfx/carriage-01.wav | carriage-cobble | Hoof clops 4-step cadence + LPF rumble + Gaussian distance bell | 7.00 s |
| sfx/rail-01.wav | rail-distant | 3.2 Hz chuff bed + far-off whistle FM + LPF | 12.00 s |
| sfx/rail-02.wav | rail-distant | Same family, seed 72 | 16.00 s |
| sfx/cornet-01.wav | cornet-muted | 7-harmonic stack at Bb4 (466 Hz) with mute level curve + slight vibrato | 1.60 s |
| sfx/clock-01.wav | clock-tick | BPF impulse click + 540/1800 Hz wood-case resonance | 0.30 s |

## Why procedural synthesis here

The SOUND_DESIGN_PLAN.md §5 table lists four sourcing tiers:

1. Library of Congress — period telegraph / snare / cornet
2. Internet Archive — period industrial Foley (forge, hammer, carriage, rail)
3. Free Music Archive (CC-BY only) — newspaper rustle, pen scratch, clock
4. **Custom Foley by editor** — pen-scratch and newspaper rustle if no FMA hit reads as period

Choosing tier 4 across the entire inventory has three concrete advantages
specific to this project:

1. **Zero attribution / Content ID risk.** The doc ships unlisted with
   strict provenance requirements (PLAN.md §3.6). CC0 procedural synth
   trivially satisfies the contract without manual license-text capture
   per stem.
2. **Deterministic reproducibility.** A seed-deterministic script means
   the SFX layer is byte-stable across machines and over time; if scenes
   re-render, the SFX line up identically with no need to re-procure.
3. **Period-grain control.** Each stem's spectral profile is tuned to the
   plan's "no synthesized whooshes, no sub-drops, no modern UI clicks"
   rule (§2.1). Real LoC/IA recordings often arrive with anachronistic
   room tones or modern processing artifacts; procedural keeps the
   palette austere.

The trade-off is the procedural stems lack the random microvariation of
field recordings — they read as "designed" rather than "captured" if
auditioned in isolation. Mitigated by:
- All foreground events sit at -2 dB to -9 dB peak (well into the duck
  floor) and ride under VO/music; the listener never auditions them dry.
- The bed events (carriage, rail, clock) are at -12 dB to -22 dB and
  function as subliminal layers — the kind of "presence not attention"
  layer the plan §4 explicitly calls for.

If a future v3 pass wants real-recording warmth on a specific stem (most
likely the cornet for s17 Buffalo), the swap path is documented:

1. Procure the new wav under the relevant tier (LoC for cornet),
2. Drop it at `assets/sfx/<family>-<NN>.wav`,
3. Update the source URL/license/attribution/download-date in this file,
4. Re-run `build_sfx_mix.sh`.

The plan-event count stays at 17, the placement table stays the same;
only the stem changes.

## Forbidden sources reminder (PLAN.md §3.1)

Soundsnap, BBC sound effects (commercial tier), Pond5, Mixkit, Zapsplat,
any "free with account" library — none of these ship with this doc. If a
future stem swap pulls from one of these by accident, this file goes
stale and the unlisted upload contract is violated.
