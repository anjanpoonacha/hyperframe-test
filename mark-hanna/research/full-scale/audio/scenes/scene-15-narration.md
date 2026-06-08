# Scene 15 — NOVEMBER 3, 1896
**Window:** 20:15–20:45 (30 s)
**Emotion:** resolution as quiet.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — silence 1.5 s (anullsrc -t 1.5)

### chunk 02 — text
```
And when November came, the ledger won.
```
