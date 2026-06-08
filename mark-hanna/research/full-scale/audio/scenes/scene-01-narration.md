# Scene 01 — THE CARTOON
**Window:** 0:00–0:45 (45 s)
**Emotion:** recognition, then unease. The cartoon is familiar; the name lands like an accusation.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — silence 4.0 s (anullsrc -t 4.0)

### chunk 02 — text
```
The cartoon ran in every Hearst paper in America. A fat man, in a suit covered in dollar signs, smoking a cigar the size of his forearm. The caption changed every week. The man did not.
```

### chunk 03 — silence 0.6 s (anullsrc -t 0.6)

### chunk 04 — text
```
His name was Mark Hanna.
```
