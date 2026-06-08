# Scene 06 — CHARLOTTE
**Window:** 7:30–8:30 (1:00)
**Emotion:** the only love beat. Quiet. Permission to feel.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — silence 0.8 s (anullsrc -t 0.8)

### chunk 02 — text
```
And married a woman named Charlotte Rhodes. Her father was Daniel Rhodes. Coal and iron. One of the men quietly getting rich off everything Cleveland was becoming.
```
