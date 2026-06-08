# Mark Hanna ep01 — HyperFrames Composition (source-of-truth)

> ⚠️ **This directory is the source-of-truth for the Mark Hanna ep01 composition and renders.**
>
> Editorial inputs (script, voiceover text, narration audio, transcript, PD assets) live in the
> sibling `american-audacity` repo. Do not author composition HTML there — `american-audacity/video-projects/mark-hanna-e01/`
> is an abandoned stub.

---

## Where things live

### This repo (composition + renders)

    ~/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna/
    ├── index.html                         ← root composition
    ├── compositions/                      ← per-scene .html (scene-01..19, fs = full-scale)
    ├── assets/                            ← media wired into the composition (audio, images)
    ├── meta.json                          ← { id: "mark-hanna", name: "Mark Hanna — The Ledger (24-min full-scale)" }
    ├── hyperframes.json                   ← CLI config
    ├── package.json                       ← npm run dev / check / render / publish
    ├── DESIGN.md                          ← visual identity for this composition
    ├── LEARNINGS.md                       ← per-project observations log
    ├── RELEASE_NOTE.md                    ← release notes
    ├── STYLE_REUSE_AUDIT.md               ← audit of style reuse from sibling projects
    ├── TTS_PUNCTUATION_REFERENCE.md       ← TTS punctuation reference for narration
    ├── research/                          ← composition research (full-scale scene index, build scripts)
    ├── qa/                                ← frame extracts for visual verification
    ├── snapshots/                         ← preview snapshots
    ├── tests/                             ← composition tests
    ├── tts-spike/                         ← TTS experiments
    └── renders/                           ← rendered MP4 outputs (see canonical artifacts below)

### Sibling repo (editorial inputs — read-only from here)

    ~/SAPDevelop/github.com/personal/american-audacity/
    └── episodes/mark-hanna/
        ├── brief.md                       ← story brief, pipeline scores, title
        ├── research.md                    ← verified facts, quotes, timeline, anchor scenes
        ├── outline.md                     ← beat-by-beat 35-min structure with timestamps
        ├── script.md                      ← full narration (5,089 words, lint clean)
        ├── voiceover.txt                  ← TTS-ready text with pause cues
        ├── assets.md                      ← PD asset manifest with LoC IDs and URLs
        └── assets/
            ├── narration.wav              ← Edge TTS render, en-US-AndrewNeural
            ├── transcript.json            ← word-level timestamps (4,966 words)
            └── [15 photos, 4 cartoons, 2 maps, 6 newspaper pages]

If the script / narration / transcript / PD assets need to change, edit them in the sibling repo and
re-sync to `assets/` here. This directory is downstream of editorial.

---

## Canonical render artifacts

| Artifact | Duration | Path |
|---|---|---|
| 4:30 reference preview (the original "good first video") | 270s (4:30) | `renders/mark-hanna-ep01-preview.mp4` |
| 24:00 full-scale episode render | 1440s (24:00) | `renders/mark-hanna-fullscale.mp4` |
| Short cut (9:16, ships to `@TheAmericanAudacity` shorts channel) | — | `../mark-hanna-shorts/mark-hanna-short.mp4` |

The shorts channel is a separate sibling project (`../mark-hanna-shorts/`) with its own composition,
package, and AGENTS.md. See `american-audacity/CHANNEL.md` §11 for the publishing-destination contract:
shorts ship to `@TheAmericanAudacity` (`UCB0HZvdBl6s6as4HwFHiIVw`), long-form to `@AmericanAudacity` (`UCJtAf5PViltW9_Vi6h7f0CQ`).
Never publish a short to the long-form channel and vice versa.

---

## Working in this directory

```bash
cd ~/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna

npm run check          # lint + validate + inspect
npm run dev            # preview server (long-running — run in background)
npm run render         # render to MP4
npm run publish        # publish + shareable link
```

Rules: every timed element needs `data-start`, `data-duration`, `data-track-index`; visible timed
elements need `class="clip"`; GSAP timelines paused, registered on `window.__timelines`; `<video>` muted
with sibling `<audio>`; sub-compositions via `data-composition-src`; no `Date.now()`, no
unseeded `Math.random()`, no render-time network fetches.

Per-project observations (mistakes hit, splice patterns, engine quirks) live in `LEARNINGS.md`.
