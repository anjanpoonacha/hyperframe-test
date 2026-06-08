# Scene 02 — THE LEDGER
**Window:** 0:45–3:30 (2:45)
**Emotion:** uncomfortable scale. Numbers as physical objects.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
And in eighteen ninety-six, he did something no one had ever done at that scale. He turned the American presidential election into a corporate purchase order.
```

### chunk 02 — silence 0.6 s (anullsrc -t 0.6)

### chunk 03 — text
```
Three and a half million dollars raised. Twenty times what his opponent spent. Banks assessed at a quarter of a percent of capital. Railroads, shaken down personally. Standard Oil, two hundred and fifty thousand dollars. JP Morgan, two hundred and fifty thousand dollars. Half a million voters, transported by train, to shake one man's hand. Two hundred million pieces of campaign literature, printed and mailed. The opposition had a thirty-six year old preacher who could move a crowd to tears. Hanna had a ledger.
```

### chunk 04 — silence 1.2 s (anullsrc -t 1.2)

### chunk 05 — text
```
And when November came, the ledger won.
```

### chunk 06 — silence 0.8 s (anullsrc -t 0.8)

### chunk 07 — text
```
To understand how — we go back fifty-nine years.
```
