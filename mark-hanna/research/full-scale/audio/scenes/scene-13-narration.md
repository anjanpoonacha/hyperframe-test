# Scene 13 — CROSS OF GOLD
**Window:** 18:30–19:30 (1:00)
**Emotion:** contrast. The thing the ledger is buying *against*.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
The opposition had a thirty-six year old preacher who could move a crowd to tears.
```

### chunk 02 — silence 1.0 s (anullsrc -t 1.0)

### chunk 03 — text
```
William Jennings Bryan walked into the Democratic convention an unknown congressman from Nebraska. He walked out, the nominee. On one speech.
```

### chunk 04 — text
```
The crowd in Chicago carried him on their shoulders. The newspapers wrote that the silver-tongue had broken thirty-six years of political quiet in two thousand words.
```

### chunk 05 — silence 0.6 s (anullsrc -t 0.6)

### chunk 06 — text
```
Hanna read the speech in Cleveland that night, and went, the next morning, to the bank.
```
