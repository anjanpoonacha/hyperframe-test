# Scene 11 — THE MECHANISM
**Window:** 16:00–17:45 (1:45)
**Emotion:** the math is on screen. Nothing is hidden any more.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
Here is how the ledger worked.
```

### chunk 02 — silence 0.6 s (anullsrc -t 0.6)

### chunk 03 — text
```
Every national bank in America was assessed at a quarter of one percent of its paid-in capital. Not asked. Assessed. Every railroad, by line-mile.
```

### chunk 04 — silence 0.4 s (anullsrc -t 0.4)

### chunk 05 — text
```
Standard Oil — two hundred and fifty thousand dollars. JP Morgan — two hundred and fifty thousand dollars. New York Life. Equitable. Metropolitan Life. The big three insurers, fifty thousand each, billed to policy holders.
```

### chunk 06 — silence 0.8 s (anullsrc -t 0.8)

### chunk 07 — text
```
Three and a half million dollars. Twenty times what William Jennings Bryan would raise.
```
