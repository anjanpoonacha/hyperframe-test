# Audio Plan — Mark Hanna full-scale documentary

Sibling kanban task: **t_be6c1904** (parent t_aa7698b0 — script).

This directory holds the complete audio layer plan for the 24-minute Mark Hanna documentary, plus the rendered per-scene voice-over stems ready to drop onto the assembly timeline (sibling task `t_e781bf96`).

## Files in this directory

```
VOICEOVER_PLAN.md       Voice direction, render procedure, splice budget,
                        outsourced-actor recording brief.
MUSIC_PLAN.md           4-cue palette (A/B/C/D), per-scene cue map,
                        +3 dB lift map, audition shortlist.
                        Extends the existing research/music/PLAN.md (5-min preview)
                        forward to 24 minutes.
SOUND_DESIGN_PLAN.md    8-family SFX inventory, per-scene placement,
                        mixing targets, frame-tight sync tolerances.
VO_MANIFEST.json        Machine-readable index for the assembly task —
                        per-scene window/duration/chunks/silence/wav_path.
scenes/
  scene-NN-narration.md   per-scene plan with TTS chunks + silence beats
  scene-NN-narration.txt  raw TTS input text (LEARNINGS-pre-flighted)
render_scenes.sh        Reproducible render script (Kokoro bm_george +
                        atempo 1.18 + loudnorm I=-16:TP=-1.5:LRA=11).
audit_durations.py      Compares rendered wav durations against script windows.
_parse_script.py        FULL_SCRIPT.md → per-scene text/plan parser.
_update_manifest.py     Adds rendered-wav metadata to VO_MANIFEST.json.
```

## Rendered VO stems (delivered to t_e781bf96)

Path: `mark-hanna/assets/scenes/scene-NN.wav` (NN = 01..19).
Format: 48 kHz / mono / PCM 16-bit, atempo 1.18, loudnorm-normalized to I=-16 LUFS / TP=-1.5 dBTP.

| Scene | Window | Spoken | + Silence | Visual hold | Title |
|---|---|---|---|---|---|
| 01 | 0:00–0:45 | 12.40 s | + 4.6 s | 28.0 s | THE CARTOON |
| 02 | 0:45–3:30 | 37.46 s | + 2.6 s | 124.9 s | THE LEDGER |
| 03 | 3:30–5:00 | 18.16 s | + 0.4 s | 71.4 s | NEW LISBON, OHIO. 1837. |
| 04 | 5:00–6:00 | 12.53 s | + 0.6 s | 46.9 s | THE BOY AT THE NEXT DESK |
| 05 | 6:00–7:30 | 20.40 s | + 0.0 s | 69.6 s | THE PRICE OF THINGS |
| 06 | 7:30–8:30 | 8.80 s | + 0.8 s | 50.4 s | CHARLOTTE |
| 07 | 8:30–10:00 | 31.66 s | + 0.4 s | 57.9 s | THE CHOKEPOINT |
| 08 | 10:00–11:30 | 20.01 s | + 2.4 s | 67.6 s | THE THESIS |
| 09 | 11:30–14:00 | 53.55 s | + 2.8 s | 93.6 s | CHICAGO, 1888 |
| 10 | 14:00–16:00 | 47.18 s | + 2.0 s | 70.8 s | THE PANIC |
| 11 | 16:00–17:45 | 24.91 s | + 1.8 s | 78.3 s | THE MECHANISM |
| 12 | 17:45–18:30 | 20.27 s | + 1.0 s | 23.7 s | THE FRONT PORCH |
| 13 | 18:30–19:30 | 22.21 s | + 1.6 s | 36.2 s | CROSS OF GOLD |
| 14 | 19:30–20:15 | 15.95 s | + 0.0 s | 29.1 s | TWO HUNDRED MILLION |
| 15 | 20:15–20:45 | 2.24 s | + 1.5 s | 26.3 s | NOVEMBER 3, 1896 |
| 16 | 20:45–22:00 | 51.12 s | + 3.2 s | 20.7 s | SENATOR HANNA. AND THE COWBOY. |
| 17 | 22:00–23:00 | 24.47 s | + 3.5 s | 32.0 s | BUFFALO |
| 18 | 23:00–23:30 | 14.19 s | + 0.4 s | 15.4 s | TYPHOID |
| 19 | 23:30–24:00 | 21.58 s | + 1.6 s | 6.8 s | THE INHERITANCE |
| **TOTAL** | **24:00** | **459.1 s** | **+ 31.2 s** | **949.7 s** | |

Spoken narration is **34% of runtime**; remaining 66% is held visuals, music-only passages, and silence — by design. Per `research/music/PLAN.md` §3.3, target ≥40% unscored; the engineered 66% visual-hold makes that easy to honour. Per FULL_SCRIPT.md §4 ("silence as a beat"), the held shots and silence stretches *are* the documentary's voice.

## Hand-off to assembly task t_e781bf96

The assembly task receives:

1. **19 per-scene VO wavs** at `assets/scenes/scene-NN.wav`. Drop each onto its scene window in the timeline; pad each scene's window with the script's silence beats (see `VO_MANIFEST.json` `silence_seconds`) and the `[BEAT]` markers in `scenes/scene-NN-narration.md`.
2. **Music cue placement** per `MUSIC_PLAN.md` §3 (cue-by-scene table) and §4 (lift map: 2:30, 16:00, 20:15, 23:30 only).
3. **SFX cue placement** per `SOUND_DESIGN_PLAN.md` §3 — period-grain only, ≤20 distinct events for the whole 24 min.
4. **Mixing targets** (master −14 LUFS, voice short-term −16 LUFS, music bed −27 to −28 LUFS under VO, SFX foreground −18 to −22 LUFS, SFX bed −30 to −32 LUFS). Same numbers across all three plans.

The assembly task should regenerate captions after concatenating the per-scene wavs into the master narration track, per `LEARNINGS.md` line 19 (any time `narration.wav` changes, regen captions and re-warp scene HTML timings).
