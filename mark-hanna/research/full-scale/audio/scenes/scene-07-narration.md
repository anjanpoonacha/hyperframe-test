# Scene 07 — THE CHOKEPOINT
**Window:** 8:30–10:00 (1:30)
**Emotion:** geometric inevitability. The position was the prize.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
Hanna walked into that business, and never walked out.
```

### chunk 02 — silence 0.4 s (anullsrc -t 0.4)

### chunk 03 — text
```
By eighteen sixty-seven, Marcus Alonzo Hanna had built MA Hanna and Company. A coal and iron brokerage, sitting at the exact pivot point where Lake Erie ore boats unloaded for the Pittsburgh steel mills. Cleveland was the chokepoint. And Hanna sat on it. Every ton of iron ore that crossed Lake Erie in the eighteen seventies, passed through brokers like him, he took a cut. Then he bought the newspaper, the Cleveland Herald. Then a theater. Then banking interests. Then a streetcar line. By eighteen eighty, he controlled enough of Cleveland that when he walked into a room, the room changed temperature.
```
