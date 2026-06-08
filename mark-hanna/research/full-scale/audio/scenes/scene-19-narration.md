# Scene 19 — THE INHERITANCE
**Window:** 23:30–24:00 (30 s)
**Emotion:** the template. The thesis closing.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
The man you've seen in a thousand cartoons — the dollar suit, the cigar — invented something that outlived him by a hundred and twenty years. The assessment system. The corporate mail. The candidate as product. The convention as choreography.
```

### chunk 02 — silence 0.6 s (anullsrc -t 0.6)

### chunk 03 — text
```
Every American presidential campaign since nineteen hundred has used a piece of his ledger. Most use the whole thing.
```

### chunk 04 — silence 1.0 s (anullsrc -t 1.0)

### chunk 05 — text
```
His name was Mark Hanna.
```

### chunk 06 — text
```
The cartoon ran in every Hearst paper in America.
```
