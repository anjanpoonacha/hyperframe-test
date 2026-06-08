# Scene 12 — THE FRONT PORCH
**Window:** 17:45–18:30 (45 s)
**Emotion:** delivery as theater; scale as choreography.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
Bryan tours.
```

### chunk 02 — silence 0.4 s (anullsrc -t 0.4)

### chunk 03 — text
```
McKinley does not. McKinley sits on his front porch in Canton, Ohio, because his wife is too ill to be left alone for a campaign trip, and because Hanna has decided that staying still is more presidential than running. Hanna brings the country to the porch.
```

### chunk 04 — silence 0.6 s (anullsrc -t 0.6)

### chunk 05 — text
```
Half a million voters. By train. To Canton. Each one shakes McKinley's hand. Each one goes home and tells a story.
```
