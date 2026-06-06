# Kokoro bm_george — Punctuation, Pacing & Pronunciation Reference

Empirical findings from /tts-spike/. All tests rendered with `npx hyperframes tts --voice bm_george`. Silence durations measured by ffmpeg `silencedetect=noise=-40dB:d=0.05`. Raw data: `tts-spike/results.json`.

---

## TL;DR — what actually works

| Goal | Technique | Real impact |
|------|-----------|-------------|
| Slow the whole paragraph | `--speed 0.85` flag on the CLI | **13% longer** (works) |
| Long pause at sentence boundary | Render two separate clips, splice with ffmpeg silence | **Reliable** |
| Long pause mid-sentence | Comma or period | **~0.17s** (you can't get more) |
| Read year correctly | Spell out: "eighteen ninety-six" | **Mandatory** |
| Avoid stutter on initials | Drop the dots: "JP Morgan" not "J.P. Morgan" | **Confirmed** |
| Avoid proper-noun confusion in lists | Connect with "and", drop the comma | **Reliable** |

## What does NOT work — stop trying

- **Adding ellipses, em-dashes, semicolons.** All sentence terminators produce identical pauses (0.147–0.169s — a 22ms range across 9 different terminators in identical sentences). The model normalizes punctuation aggressively.
- **Adding paragraph breaks (`\n\n`), double spaces, single newlines.** Identical pause to a single space (0.152s). Whitespace is fully ignored.
- **"Inserting" silence by breaking into separate sentences.** Same paragraph rendered as 4 sentences vs. 6 sentences vs. 4 sentences-with-ellipses all came out 11.8–12.0s — within rendering noise of each other.
- **Mid-sentence em-dash for emphasis.** The em-dash actually produces a *shorter* pause (0.14s) than a comma (0.17s). The visual gap doesn't translate.

If a passage feels rushed and you want real breathing room, you have two real options:

1. **`--speed 0.85`** on the whole render (or that scene) — actually slows speech.
2. **Render in chunks and splice** — generate sentence A as one clip, sentence B as another, and use ffmpeg to insert N seconds of silence between them. This is the only way to get pauses longer than ~170ms.

---

## Sentence-gap tests (terminator effect on pause length)

Same content `"He came home<X> He left."` with X varied:

| Terminator | Pause |
|------------|-------|
| `.` (period) | 0.152s |
| `?` | 0.155s |
| `!` | 0.147s |
| `...` (ellipsis) | 0.169s |
| `—` (em-dash) | 0.155s |
| `;` (semicolon) | 0.159s |
| `.` + double space | 0.152s |
| `.` + `\n` | 0.152s |
| `.` + `\n\n` | 0.152s |

**Conclusion: every variant lands inside a 22ms band.** Punctuation is normalized before phonemization. The model decides pause length from prosodic context, not the symbol you typed.

## Mid-sentence pause tests

Same content `"He paused<X> then he spoke."` with X varied:

| Separator | Pause |
|-----------|-------|
| `,` | 0.168s |
| `—` | 0.141s |
| `...` | 0.161s + 0.051s |
| `;` | 0.169s |
| `.` (treated as sentence break) | 0.166s |
| (no punctuation) | 0.151s |

Comma is slightly stronger than em-dash. Ellipses produce a tiny secondary blip but no real extra pause.

## Year-digit tests

| Text | Duration | Outcome |
|------|----------|---------|
| `"And in 1896 he did it."` | 3.95s | Reads "one thousand eight hundred ninety-six" — wrong |
| `"And in 1896, he did it."` | 3.82s | Same problem |
| `"And in the year 1896 he did it."` | 4.37s | Same problem (the word "year" doesn't help) |
| `"And in eighteen ninety-six he did it."` | **2.54s** | ✅ correct |
| `"It happened in '96."` | 1.98s | Reads "ninety-six" — correct |
| `"By 1880 he was rich."` | 3.63s | Bare 1880 also cardinalized |
| `"Born in 1837."` | 3.61s | Same |

**Rule: never write a 4-digit year as digits in narration. Always spell out as English words ("eighteen ninety-six").** Adding the word "year", a comma, or sentence position does not change the model's behavior. Two-digit apostrophe form (`'96`) is read correctly.

## Initials / "J.P. Morgan"

| Text | Duration | Inner pause |
|------|----------|-------------|
| `"J.P. Morgan paid."` | 1.98s | 0.148s |
| `"J. P. Morgan paid."` | 1.98s | 0.148s |
| `"j.p. Morgan paid."` | 1.98s | 0.148s |
| `"JP Morgan paid."` | **1.83s** | 0.089s |

**Rule: drop the dots in initials.** `J.P.` adds 150ms of awkward pause and the word emerges clipped. `JP` flows.

## List-as-fragment ("Coal, iron")

| Text | Duration |
|------|----------|
| `"His business: Coal, iron."` | 1.98s |
| `"His business: coal, iron."` | 1.98s |
| `"His business: coal and iron."` | 2.09s |
| `"His business: coal, iron, steel."` | 2.43s |

Capitalization had no measurable effect on duration. The "Cole Iron" misreading we hit earlier is auditory, not timing — but the **reliable fix is connecting with "and"** because:

- Two-item lists with "and" sound like a normal conjunction, not a proper noun ("coal and iron").
- Three-item lists with commas sound fine ("coal, iron, steel") because the third item disambiguates.
- The bug case is *exactly* a two-item comma list — the model has no third item to lock in "this is a list".

**Rule: avoid bare two-item comma lists. Use "X and Y" instead.**

## Leading word + comma ("Banks, ...")

| Text | Duration |
|------|----------|
| `"Banks, assessed at a quarter percent."` | 2.54s |
| `"Banks — assessed at a quarter percent."` | 2.52s |
| `"Banks assessed at a quarter percent."` | 2.54s |

Duration is identical across all three. So the "Banks stutter" we heard before was perceptual — the model treats `Banks,` as a one-word fragment when followed by a longer descriptor and gives it falling intonation, which sounds like a clipped stop. **Removing the comma fixes the prosody, not the timing.** The fix works because it forces the model to read "Banks assessed at..." as a single noun phrase, not "Banks." + "assessed at...".

**Rule: don't open a sentence with `Word, descriptor...`. Make it flow as one clause.**

---

## How to actually slow a passage down

The user's real complaint at 2:10–2:30 was pacing. Here's what actually works:

```bash
# Slow the whole render (or a per-scene render) by 15%
npx hyperframes tts narration.txt --voice bm_george --speed 0.85 --output slow.wav
```

`--speed 1.0` (default) → 12.0s for our test paragraph
`--speed 0.85`              → 13.6s (+13%)

For a 35-min documentary this is the cheapest knob: re-render any rushed scene at `--speed 0.92` (subtle) or `--speed 0.85` (noticeable). No script changes.

For surgical extra silence between specific sentences (e.g. dramatic beat before a key fact), the only way is:

```bash
# Render two clips, concat with N seconds of silence between
ffmpeg -f lavfi -t 0.8 -i "anullsrc=r=24000:cl=mono" silence.wav
# ffmpeg concat: clip1 + silence + clip2 -> dramatic_pause.wav
```

This is what the splice pipeline already does for fixes; it's also the only reliable mechanism for engineered pauses.

---

## Voice pronunciation pitfalls (catalog)

These are the specific token shapes that misbehaved during the Mark Hanna episode. None of them change duration meaningfully — they all change *correctness* or *prosody*.

| Pattern | Bad output | Fix |
|---------|------------|-----|
| `1896` (bare 4-digit year) | "one thousand eight hundred ninety-six" | spell out: `eighteen ninety-six` |
| `J.P. Morgan` | clipped letters with awkward pause | `JP Morgan` |
| `Coal, iron.` | "Cole Iron" (proper-noun blur) | `coal and iron.` |
| `Banks, assessed at...` | leading-word stutter | `Banks assessed at...` |
| `M.A. Hanna` | (worked correctly — no fix needed) | leave as-is |

## Process notes

- **CLI iteration time: ~19s per test clip** (cold start + render + ffprobe). Acceptable for spike work; would be brutal for production at scale. For the next episode, set up a persistent kokoro Python REPL so the model loads once and tests run in <1s each.
- **Silence detection threshold matters.** Used `-40dB:d=0.05` (50ms minimum, -40dB noise floor). Lower the threshold (e.g. `-50dB`) to catch softer "breath" pauses; raise it (`-30dB`) to only catch real silences.
- **Inner silences** = silences excluding leading and trailing edge silence (which are wav file padding, not speech pauses). The python parser in `results.json` filters those out automatically.

## Test artifacts

All wavs and txts in this directory are reproducible — re-run `bash run_all.sh` to regenerate.

| File | Purpose |
|------|---------|
| `run_test.sh` | Single-test helper |
| `run_all.sh` | Batch all 34 tests |
| `results.json` | Structured measurements (parse with python) |
| `*.wav` / `*.txt` | Per-test inputs and outputs |
| `pacing_*.wav` | Paragraph-level pacing comparisons |
