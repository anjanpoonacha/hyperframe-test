#!/usr/bin/env python3
"""Find data-start seconds for each Cue A/B entry beat against the narration transcript."""
import json, re, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
words = json.load(open(os.path.join(ROOT, 'assets/transcript.json')))

def find_phrase(phrase, words, start_idx=0):
    target = re.findall(r"[A-Za-z']+", phrase.lower())
    n = len(target)
    for i in range(start_idx, len(words) - n + 1):
        ok = True
        for j in range(n):
            wt = re.sub(r"[^A-Za-z']", "", words[i+j]['text']).lower()
            if wt != target[j]:
                ok = False; break
        if ok:
            return words[i]['start'], words[i+n-1]['end']
    return None, None

queries = [
    ("L9 titlecard",                "And in eighteen"),
    ("L13 mechanism",               "Three and a half million dollars"),
    ("L21 weight (Cue B)",          "The opposition had a thirty-six"),
    ("L23 [dry] Hanna had a ledger","Hanna had a ledger"),
    ("L25 indictment",              "And when November came"),
    ("L27 scene2 start",            "He wasn't born with money"),
    ("L33 mechanism",               "When Mark was fifteen"),
    ("L41 mechanism",               "Hanna lasted one year"),
    ("L45 weight",                  "Then the Civil War came"),
    ("L51 mechanism",               "Hanna walked into that business"),
    ("L59 mechanism",               "Then he bought the newspaper"),
    ("L63 weight",                  "And he was bored"),
    ("L65 mechanism",               "Because Hanna had figured out"),
    ("L67 [dry] most powerful",     "The most powerful thing"),
    ("L69 indictment",              "That was politics"),
    ("L71 scene3 start",            "The year was eighteen eighty-eight"),
    ("L77 mechanism",               "Hanna worked the convention floor"),
    ("L79 weight",                  "Sherman peaked on the first ballot"),
    ("L81 [SILENT-REVEAL] Hanna lost", "Hanna lost"),
    ("L83 mechanism re-entry",      "But he saw something"),
    ("L91 [dry] loyalty rare",      "That kind of loyalty was rare"),
    ("L93 scene4 start",            "His name was William McKinley"),
    ("L95 weight",                  "Hanna walked across the floor"),
    ("L97 [dry] final",             "He didn't know it yet"),
]

print(f"narration words: {len(words)}; first start={words[0]['start']:.2f}; last end={words[-1]['end']:.2f}\n")
print(f"{'marker':<40} {'start':>8} {'end':>8}")
print("-" * 60)
results = {}
for name, phrase in queries:
    s, e = find_phrase(phrase, words)
    results[name] = (s, e)
    if s is None:
        print(f"{name:<40} {'NOT FOUND':>17}")
    else:
        print(f"{name:<40} {s:>8.2f} {e:>8.2f}")

print("\n--- All occurrences of 'Hanna lost' ---")
for i in range(len(words)-1):
    if (re.sub(r"[^A-Za-z']","",words[i]['text']).lower() == "hanna" and
        re.sub(r"[^A-Za-z']","",words[i+1]['text']).lower() == "lost"):
        print(f"  i={i} start={words[i]['start']:.2f} end={words[i+1]['end']:.2f}")
