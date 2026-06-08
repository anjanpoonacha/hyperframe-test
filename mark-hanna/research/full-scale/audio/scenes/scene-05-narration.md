# Scene 05 — THE PRICE OF THINGS
**Window:** 6:00–7:30 (1:30)
**Emotion:** education through the eye, not the book.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
Hanna lasted one year at Western Reserve before he quit. Not because he was failing. Because he had already figured out something the professors couldn't teach. The real education, was in the price of things. He went back to the store. Worked the floor. Watched how men negotiated. Watched who paid on time and who didn't. Watched which suppliers had leverage, and which ones begged. Then the Civil War came. He served briefly. Came home.
```
