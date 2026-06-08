# Scene 08 — THE THESIS
**Window:** 10:00–11:30 (1:30)
**Emotion:** a man crossing a line.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
And he was bored. Not with money, he had money. Bored with the ceiling.
```

### chunk 02 — silence 0.6 s (anullsrc -t 0.6)

### chunk 03 — text
```
Because Hanna had figured out, watching the men who supplied his coal, the politicians who regulated his railroads, the judges who settled his contracts, that money was the second most powerful thing in America.
```

### chunk 04 — silence 1.0 s (anullsrc -t 1.0)

### chunk 05 — text
```
The most powerful thing, was who decided where the money went.
```

### chunk 06 — silence 0.8 s (anullsrc -t 0.8)

### chunk 07 — text
```
That was politics. And no one had ever run it like a business. Not yet.
```
