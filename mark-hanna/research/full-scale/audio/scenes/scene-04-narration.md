# Scene 04 — THE BOY AT THE NEXT DESK
**Window:** 5:00–6:00 (1:00)
**Emotion:** recognition; the long shadow.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
In his class, was a quiet, awkward boy who would grow up to control ninety percent of the oil refining capacity in the United States.
```

### chunk 02 — silence 0.6 s (anullsrc -t 0.6)

### chunk 03 — text
```
His name was John D. Rockefeller. The two would orbit each other for the next forty years.
```
