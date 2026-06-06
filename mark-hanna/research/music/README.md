# Music Research — Mark Hanna documentary

This folder contains the deliverables of kanban task `t_7a905503`:
*"Don't you think we need the music for the documentary? Research with other youtube channels.
Have an opinion about ourselves and the best practices. We need 3 eyes. Always remember the
MACI principle (confidence can't be checked by the model itself)."*

The task was decomposed into 4 children and synthesized via MACI (Multi-Agent Collaborative
Intelligence) — three independent reviewers generated perspectives without seeing each other's
work, then a synthesizer merged them. Confidence is **derived from agreement across reviewers**,
not self-reported.

## Files

- `PLAN.md` — final synthesized plan. **Read this first.** Includes a confidence section (§4)
  showing where the three reviewers converged (HIGH), partially overlapped (MEDIUM), or
  genuinely disagreed (LOW, resolved by project context).
- `perspective-1.md` — mainstream/explainer axis (Johnny Harris, Vox, Kurzgesagt, Wendover/HAI,
  Veritasium + 3 lighter samples).
- `perspective-2.md` — indie/auteur axis (LEMMiNO, Defunctland, Internet Historian, Mustard,
  Plainly Difficult + 3 contrast points).
- `perspective-3.md` — independent position paper, project-anchored to the Mark Hanna 1896 doc.
- `OPINION.md` — the parent task's *own* opinion: a direct answer to "do we need music?" and
  "what should we do about ourselves?", written *after* reading all three perspectives.

## Lineage

```
t_7a905503 (this task — root)
├── t_771d1fd4  Perspective 1 → perspective-1.md
├── t_2c9e421d  Perspective 2 → perspective-2.md
├── t_8913164a  Perspective 3 → perspective-3.md
└── t_6450d679  Synthesis     → PLAN.md
```

Source files originally lived in per-task scratch workspaces under
`~/.hermes/kanban/boards/sap-standup/workspaces/<task>/` but were GC'd; recovered from
session-store transcripts and persisted here so they survive future scratch GC.

## MACI confidence summary (TL;DR from PLAN.md §4)

**HIGH confidence (3 of 3 converged):**
1. Silence is structural, not absence — plan one "silent reveal" with full music drop-out.
2. Motif reuse beats cue variety.
3. Score function (narrative role), not timecode.
4. Voice is sovereign.
5. Earn the swell — restraint reads as honesty.

**MEDIUM confidence (1–2 reviewers, the rest don't contradict):**
- Concrete loudness numbers (–14 LUFS integrated, voice –16 LUFS short-term, bed –27 to –28 LUFS).
- Single sting family for transitions.
- AI music acceptable with strict logging.
- Breath ducking (+2–4 dB swells in inter-sentence gaps).

**LOW confidence (genuine disagreement, resolved by project context):**
- Primary sourcing tier (P3 wins for 1896 setting → period public-domain).
- Cue rotation rate (P3 wins for short-form → two leitmotifs).
- Duck depth (split by cue density: –8 dB sparse, –12 dB dense).

**Needs human decision:**
1. Project-scope confirmation. If period/runtime/budget assumptions flip, several recommendations flip.
2. Closing-motif (Cue C) treatment — full-volume vs thinned reharmonization. Cut both, audition.
