# Scene 17 — BUFFALO
**Window:** 22:00–23:00 (1:00)
**Emotion:** the random event the ledger could not budget.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — silence 1.5 s (anullsrc -t 1.5)

### chunk 02 — text
```
Buffalo. September 6, 1901. William McKinley shakes hands at the Pan-American Exposition. A young man in line steps forward with a handkerchief over his right hand. Under the handkerchief is a revolver. Two shots.
```

### chunk 03 — silence 1.2 s (anullsrc -t 1.2)

### chunk 04 — text
```
McKinley dies eight days later, at two-fifteen in the morning, on September fourteenth. Theodore Roosevelt is sworn in that afternoon, in a borrowed library on Delaware Avenue.
```

### chunk 05 — silence 0.8 s (anullsrc -t 0.8)

### chunk 06 — text
```
Mark Hanna's project ends — eight years before Mark Hanna does.
```
