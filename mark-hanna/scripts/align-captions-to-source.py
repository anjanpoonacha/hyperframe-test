"""Align narration.txt source words to whisper word timings to fix caption text.

Whisper sometimes mistranscribes (e.g. 'Coal and iron' -> 'Cole and Ian'). The
audio is correct (it's the SOURCE we read aloud). Use the source text as the
caption ground truth, but keep whisper's word timings.

Strategy: Needleman-Wunsch-style alignment between source tokens and whisper
tokens. For matched/substituted positions, replace whisper's text with source
text but keep timings. For inserted source tokens (whisper missed a word), give
them the time slice of the surrounding boundary. For deleted source tokens
(whisper hallucinated), drop them. In practice both transcripts have the same
695 words for this project, so this is mostly substitution.
"""
import json, re
from pathlib import Path

PROJ = Path("/Users/I548399/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna")

def tokenize_source(text: str):
    """Source tokenizer matches the spoken word stream — preserve trailing punctuation."""
    # Strip blank lines and split on whitespace.
    return [tok for tok in re.split(r"\s+", text.strip()) if tok]

src_text = (PROJ / "narration.txt").read_text()
src_words = tokenize_source(src_text)
print(f"source words: {len(src_words)}")

whisper_words = json.load(open(PROJ / "assets/transcript.json"))
print(f"whisper words: {len(whisper_words)}")

# Use Needleman-Wunsch: identical = +2, mismatch = -1, gap = -1
def core(t):
    return re.sub(r"[^\w']", "", t).lower()

n, m = len(src_words), len(whisper_words)
# DP grid is n+1 x m+1 — both 695, so 484k cells, fine.
INF = -10**9
dp = [[0]*(m+1) for _ in range(n+1)]
back = [[None]*(m+1) for _ in range(n+1)]
GAP = -1
MATCH = 2
MISMATCH = -1

for i in range(1, n+1):
    dp[i][0] = i * GAP
    back[i][0] = 'U'
for j in range(1, m+1):
    dp[0][j] = j * GAP
    back[0][j] = 'L'

for i in range(1, n+1):
    sw = core(src_words[i-1])
    for j in range(1, m+1):
        ww = core(whisper_words[j-1]['text'])
        score_diag = dp[i-1][j-1] + (MATCH if sw == ww else MISMATCH)
        score_up = dp[i-1][j] + GAP   # source-only (whisper missed)
        score_left = dp[i][j-1] + GAP # whisper-only (whisper hallucinated)
        best = max(score_diag, score_up, score_left)
        dp[i][j] = best
        if best == score_diag:
            back[i][j] = 'D'
        elif best == score_up:
            back[i][j] = 'U'
        else:
            back[i][j] = 'L'

# Backtrack to build corrected word list
i, j = n, m
ops = []
while i > 0 or j > 0:
    op = back[i][j]
    if op == 'D':
        ops.append(('match', src_words[i-1], whisper_words[j-1]))
        i -= 1; j -= 1
    elif op == 'U':
        ops.append(('src_only', src_words[i-1], None))
        i -= 1
    else:
        ops.append(('whisper_only', None, whisper_words[j-1]))
        j -= 1
ops.reverse()

# Build corrected list
corrected = []
last_end = 0.0
n_match, n_subst, n_src_only, n_whisper_only = 0, 0, 0, 0
for kind, src_tok, ww in ops:
    if kind == 'match':
        st = ww['start']; en = ww['end']
        if core(src_tok) == core(ww['text']):
            n_match += 1
        else:
            n_subst += 1
        corrected.append({'text': src_tok, 'start': st, 'end': en})
        last_end = en
    elif kind == 'src_only':
        # whisper missed it — borrow a sliver from the next match's start
        # Use last_end .. last_end+0.05 placeholder; will be adjusted post-hoc
        corrected.append({'text': src_tok, 'start': last_end, 'end': last_end})
        n_src_only += 1
    else:
        # whisper-only word — drop from caption stream
        n_whisper_only += 1

# Post-process: for any zero-length src_only word, redistribute time from neighbors.
for i, w in enumerate(corrected):
    if w['end'] - w['start'] < 1e-6 and i + 1 < len(corrected):
        nxt = corrected[i+1]
        gap = nxt['start'] - w['start']
        if gap > 0:
            w['end'] = w['start'] + min(gap * 0.5, 0.2)
            nxt['start'] = w['end']

print(f"matched: {n_match}, substituted: {n_subst}, source-only: {n_src_only}, whisper-only: {n_whisper_only}")

# Show first 30 substitutions for review
print("\nFirst substitutions (whisper text -> source text):")
shown = 0
for kind, sw, ww in ops:
    if kind == 'match' and core(sw) != core(ww['text']):
        print(f"  '{ww['text']}' -> '{sw}'  (at {ww['start']:.2f}s)")
        shown += 1
        if shown >= 30: break

# Write corrected transcript
out_path = PROJ / "assets/transcript.json"
json.dump(corrected, open(out_path, 'w'), indent=2)
print(f"\nwrote corrected transcript: {out_path}  ({len(corrected)} words)")
