# Scene 03 — NEW LISBON, OHIO. 1837.
**Window:** 3:30–5:00 (1:30)
**Emotion:** small. Beginnings as small.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
He wasn't born with money. He was born in a grocery. New Lisbon, Ohio. Eighteen thirty-seven.
```

### chunk 02 — silence 0.4 s (anullsrc -t 0.4)

### chunk 03 — text
```
His father, Doctor Leonard Hanna, was a country physician who ran a wholesale grocery on the side. Flour, salt, dry goods to Ohio farmers. When Mark was fifteen, the family moved to Cleveland. He enrolled at Western Reserve College.
```
