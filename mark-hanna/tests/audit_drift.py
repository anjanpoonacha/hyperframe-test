#!/usr/bin/env python3
"""Independent drift audit: re-derives expected cue.start from transcript.json
without using the regenerator's verifier. Reports per-cue and aggregate skew."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
groups = json.loads((ROOT/"assets/caption-groups.json").read_text())
words  = json.loads((ROOT/"assets/transcript.json").read_text())

norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())

wi = 0
skews = []  # (idx, skew_ms, expected_start, actual_start, text)
unmatched = []
last_audio_end = max(w["end"] for w in words)

for gi, g in enumerate(groups):
    toks = g["text"].split()
    # find run of len(toks) consecutive words starting at wi
    target = [norm(t) for t in toks]
    found = None
    for j in range(wi, min(len(words) - len(toks) + 1, wi + 12)):
        if [norm(words[j+k]["text"]) for k in range(len(toks))] == target:
            found = j; break
    if found is None:
        # try just first word
        for j in range(wi, min(len(words), wi + 12)):
            if norm(words[j]["text"]) == target[0]:
                found = j; break
    if found is None:
        unmatched.append((gi, g["text"]))
        continue
    expected_start = words[found]["start"]
    expected_end   = words[found + len(toks) - 1]["end"] if found + len(toks) - 1 < len(words) else words[-1]["end"]
    skew_start = round((g["start"] - expected_start) * 1000)
    skew_end   = round((g["end"]   - expected_end)   * 1000)
    skews.append((gi, skew_start, skew_end, g["text"][:40]))
    wi = found + len(toks)

over = [s for s in skews if abs(s[1]) > 100 or abs(s[2]) > 100]
print(f"audited {len(groups)} cues against {len(words)} words")
print(f"unmatched cues: {len(unmatched)}")
if unmatched:
    for u in unmatched[:5]: print("  unmatched", u)

start_skews = [abs(s[1]) for s in skews]
end_skews   = [abs(s[2]) for s in skews]
print(f"start skew  max={max(start_skews):4d}ms  mean={sum(start_skews)/len(start_skews):.1f}ms")
print(f"end   skew  max={max(end_skews):4d}ms  mean={sum(end_skews)/len(end_skews):.1f}ms")
print(f"cues over 100ms tolerance (start or end): {len(over)}")
for o in over[:10]: print("  OVER", o)

# Spot checks: start/middle/end
for label, idx in [("start", 0), ("near 1min", next(i for i,g in enumerate(groups) if g['start']>=60)),
                   ("midpoint", next(i for i,g in enumerate(groups) if g['start']>=120)),
                   ("near 3min", next(i for i,g in enumerate(groups) if g['start']>=180)),
                   ("end", len(groups)-1)]:
    g = groups[idx]
    s = next((s for s in skews if s[0]==idx), None)
    print(f"\n{label}: cap-{idx}  start={g['start']:.2f}s end={g['end']:.2f}s  text={g['text']!r}")
    if s: print(f"  skew start={s[1]}ms end={s[2]}ms")

print(f"\naudio extends to {last_audio_end:.2f}s (narration.wav is 239.35s)")
print(f"final cue ends at {groups[-1]['end']:.2f}s")
sys.exit(0 if not over and not unmatched else 1)
