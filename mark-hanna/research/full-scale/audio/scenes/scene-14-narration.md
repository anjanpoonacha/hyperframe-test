# Scene 14 — TWO HUNDRED MILLION
**Window:** 19:30–20:15 (45 s)
**Emotion:** asymmetric warfare made visible.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
Two hundred million pieces of campaign literature, printed and mailed. One thousand four hundred speakers under contract. Pamphlets in German, in Polish, in Yiddish, in Italian. Bryan rode eighteen thousand miles by rail. Spoke to five million people in person. Hanna mailed a country.
```
