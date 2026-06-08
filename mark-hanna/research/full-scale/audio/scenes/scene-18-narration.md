# Scene 18 — TYPHOID
**Window:** 23:00–23:30 (30 s)
**Emotion:** a small ending for a large life.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
Hanna runs against Roosevelt for the Republican nomination in nineteen oh four. He has the donors. He has the senate. He does not have the time.
```

### chunk 02 — silence 0.4 s (anullsrc -t 0.4)

### chunk 03 — text
```
Typhoid fever takes him on February fifteenth, nineteen oh four. He is sixty-six. Roosevelt walks the nomination.
```
