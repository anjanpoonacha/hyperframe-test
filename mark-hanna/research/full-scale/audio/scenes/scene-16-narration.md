# Scene 16 — SENATOR HANNA. AND THE COWBOY.
**Window:** 20:45–22:00 (1:15)
**Emotion:** dramatic irony. We know what the room doesn't.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
Hanna takes McKinley's old Senate seat in Ohio. He is, at last, what he set out to be: a senator who runs the senate the way he ran a brokerage. McKinley wins again in nineteen hundred. The same ledger. The same machinery.
```

### chunk 02 — silence 0.4 s (anullsrc -t 0.4)

### chunk 03 — text
```
The vice-president on the second ticket is Garret Hobart, of New Jersey. A reliable man. A quiet man. Hobart dies in office in November of eighteen ninety-nine. The seat is open.
```

### chunk 04 — silence 0.6 s (anullsrc -t 0.6)

### chunk 05 — text
```
The New York Republican machine has a problem. Their reformist governor — a war hero, a moralist, a wildcard — keeps trying to break their patronage rings. They want him out of New York. They suggest the vice-presidency. The vice-presidency in nineteen hundred is widely understood to be a coffin.
```

### chunk 06 — silence 0.6 s (anullsrc -t 0.6)

### chunk 07 — text
```
Mark Hanna — who has watched men more carefully than any other man in American politics — sees what is coming, and tries to stop it.
```

### chunk 08 — silence 0.8 s (anullsrc -t 0.8)

### chunk 09 — text
```
*"Don't any of you realize there's only one life between this madman and the Presidency?"*
```

### chunk 10 — silence 0.8 s (anullsrc -t 0.8)

### chunk 11 — text
```
They do not listen. The madman is Theodore Roosevelt.
```
