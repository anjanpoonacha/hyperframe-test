# Scene 09 — CHICAGO, 1888
**Window:** 11:30–14:00 (2:30)
**Emotion:** the lesson. Loyalty as a rare object.

## TTS render plan

Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).
Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.
Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.

### chunk 01 — text
```
The year was eighteen eighty-eight. The Republican National Convention. Chicago. Mark Hanna arrived not as a candidate, but as a kingmaker. His man was John Sherman. Ohio senator. Treasury veteran. The establishment choice. Hanna worked the convention floor for six days. Trading delegates. Promising postmasterships. Calling in markers from Ohio to Pennsylvania. Sherman peaked on the first ballot at two hundred and twenty-nine votes. Then he bled out. Ballot after ballot, until the nomination went to Benjamin Harrison on the eighth.
```

### chunk 02 — silence 0.8 s (anullsrc -t 0.8)

### chunk 03 — text
```
Hanna lost. But he saw something that week he would never forget. A forty-five year old congressman from Canton, Ohio had been chairing the resolutions committee. When delegates began breaking toward him as a dark-horse alternative, the congressman walked to the microphone, and refused. He told the convention he was bound to Sherman. And he sat down.
```

### chunk 04 — silence 1.0 s (anullsrc -t 1.0)

### chunk 05 — text
```
That kind of loyalty was rare in eighteen eighty-eight politics. It was almost extinct.
```

### chunk 06 — silence 0.6 s (anullsrc -t 0.6)

### chunk 07 — text
```
His name was William McKinley. Hanna walked across the floor, and introduced himself.
```

### chunk 08 — silence 0.4 s (anullsrc -t 0.4)

### chunk 09 — text
```
He didn't know it yet. But he had just found his president.
```
