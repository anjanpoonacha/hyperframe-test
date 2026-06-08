# Scene 10 — THE PANIC
**Window:** 14:00–16:00 (2:00)
**Emotion:** the candidate is mortal. The patron decides what mortality costs.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
But before the kingmaker could make a king, he nearly lost him. Eighteen ninety-three. The Panic. Banks collapse from New York to San Francisco. Six hundred and forty banks fail in a single year. Fifteen thousand businesses go under. One of those businesses belonged to a man named Robert Walker, in Youngstown, Ohio. Walker was a friend of McKinley's. McKinley had co-signed Walker's notes — out of loyalty, the same loyalty Hanna had watched at the Chicago microphone five years earlier. When Walker collapsed, the notes came due against McKinley.
```

### chunk 02 — silence 0.6 s (anullsrc -t 0.6)

### chunk 03 — text
```
One hundred and thirty thousand dollars. The governor of Ohio could not pay. He wrote, in his own hand, *"I am a beggar."*
```

### chunk 04 — silence 1.0 s (anullsrc -t 1.0)

### chunk 05 — text
```
Mark Hanna picked up the phone. Inside three weeks, a syndicate of Cleveland and New York industrialists — Hanna at the center — had quietly absorbed every note. McKinley signed nothing. Owed nothing. Knew, only later, who had paid.
```

### chunk 06 — silence 0.4 s (anullsrc -t 0.4)

### chunk 07 — text
```
The candidate was now a debt. And Hanna held the paper.
```
