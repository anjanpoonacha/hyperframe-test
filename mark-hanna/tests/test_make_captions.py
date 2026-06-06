#!/usr/bin/env python3
"""Tests for make-captions.py covering the offset + progressive drift cases.

Run from the project root:
    python3 -m pytest tests/test_make_captions.py -v
or:
    python3 tests/test_make_captions.py
"""
from __future__ import annotations

import json
import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import importlib
make_captions = importlib.import_module("make-captions")  # type: ignore[assignment]

group_words = make_captions.group_words
verify_alignment = make_captions.verify_alignment
patch_captions_html = make_captions.patch_captions_html


def make_words(text_with_times):
    """Build a word list. Input: [(text, start, end), ...]."""
    return [{"text": t, "start": s, "end": e} for t, s, e in text_with_times]


# ──────────────────────────────────────────────────────────────────────────
# Grouping rule
# ──────────────────────────────────────────────────────────────────────────


class GroupWordsTest(unittest.TestCase):

    def test_breaks_on_terminal_period(self):
        words = make_words([
            ("Hello", 0.0, 0.5),
            ("world.", 0.5, 1.0),
            ("Next", 1.2, 1.5),
            ("sentence.", 1.5, 2.0),
        ])
        groups = group_words(words)
        self.assertEqual(len(groups), 2)
        self.assertEqual(groups[0]["text"], "Hello world.")
        self.assertEqual(groups[1]["text"], "Next sentence.")

    def test_caps_at_5_words_when_no_punct(self):
        words = make_words([(f"w{i}", float(i), float(i) + 0.5) for i in range(12)])
        groups = group_words(words)
        # 12 words, no punctuation -> 5 + 5 + 2
        self.assertEqual([len(g["text"].split()) for g in groups], [5, 5, 2])

    def test_breaks_on_question_and_exclaim(self):
        words = make_words([
            ("Really", 0.0, 0.3),
            ("now?", 0.3, 0.6),
            ("Yes", 1.0, 1.2),
            ("indeed!", 1.2, 1.6),
        ])
        groups = group_words(words)
        self.assertEqual(len(groups), 2)

    def test_comma_does_not_break(self):
        words = make_words([
            ("apples,", 0.0, 0.5),
            ("oranges,", 0.5, 1.0),
            ("and", 1.0, 1.2),
            ("pears.", 1.2, 1.7),
        ])
        groups = group_words(words)
        # All 4 words land in one group (under 5-word cap, no terminal punct
        # before "pears.")
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]["text"], "apples, oranges, and pears.")

    def test_group_start_end_taken_from_first_and_last_word(self):
        words = make_words([
            ("alpha", 1.10, 1.50),
            ("bravo", 1.50, 1.95),
            ("charlie.", 1.95, 2.42),
        ])
        groups = group_words(words)
        self.assertEqual(len(groups), 1)
        self.assertAlmostEqual(groups[0]["start"], 1.10, places=2)
        self.assertAlmostEqual(groups[0]["end"], 2.42, places=2)


# ──────────────────────────────────────────────────────────────────────────
# Offset case (constant pre-roll added to every word)
# ──────────────────────────────────────────────────────────────────────────


class ConstantOffsetTest(unittest.TestCase):
    """If audio shifts by a fixed offset (e.g. someone prepended 500 ms of
    silence), regenerated cues should track the new word timings exactly.
    The pre-fix bug was that cues kept the OLD timings — that's what we're
    guarding against."""

    def test_groups_track_new_audio_after_constant_offset(self):
        baseline_words = make_words([
            ("The", 0.00, 0.20),
            ("cartoon", 0.20, 0.70),
            ("ran.", 0.70, 1.10),
            ("Next", 1.30, 1.55),
            ("scene.", 1.55, 2.00),
        ])
        OFFSET = 0.500  # 500 ms prepended silence
        shifted_words = [
            {"text": w["text"], "start": round(w["start"] + OFFSET, 2),
             "end": round(w["end"] + OFFSET, 2)}
            for w in baseline_words
        ]
        baseline_groups = group_words(baseline_words)
        shifted_groups = group_words(shifted_words)

        # Every cue.start should be exactly OFFSET higher in the shifted set
        for b, s in zip(baseline_groups, shifted_groups):
            self.assertAlmostEqual(s["start"] - b["start"], OFFSET, places=2)
            self.assertAlmostEqual(s["end"] - b["end"], OFFSET, places=2)

    def test_stale_cues_fail_alignment_after_offset(self):
        """Demonstrate the bug we're guarding against: keeping old cues after
        the audio shifted should be flagged by verify_alignment()."""
        baseline_words = make_words([
            ("The", 0.00, 0.20),
            ("cartoon", 0.20, 0.70),
            ("ran.", 0.70, 1.10),
        ])
        baseline_groups = group_words(baseline_words)

        # Audio drifted: every word now starts 500 ms later
        new_words = [
            {"text": w["text"], "start": round(w["start"] + 0.500, 2),
             "end": round(w["end"] + 0.500, 2)}
            for w in baseline_words
        ]
        # If we use the STALE cues against the NEW audio, drift should show up
        max_skew, bad = verify_alignment(baseline_groups, new_words, tolerance_ms=100)
        self.assertGreater(max_skew, 100)
        self.assertTrue(bad, "stale cues should be flagged as drifted")

        # Regenerating fixes it
        new_groups = group_words(new_words)
        max_skew2, bad2 = verify_alignment(new_groups, new_words, tolerance_ms=100)
        self.assertLessEqual(max_skew2, 10)
        self.assertEqual(bad2, [])


# ──────────────────────────────────────────────────────────────────────────
# Progressive drift case — the actual production bug
# ──────────────────────────────────────────────────────────────────────────


class ProgressiveDriftTest(unittest.TestCase):
    """Audio splices add fractional seconds at multiple points; drift
    accumulates across the track. This is the diagnosis case (skew up to
    1880 ms in the real file)."""

    def _build_drifted_pair(self):
        # Original baseline: 30 words, each ~0.5 s long, sentence break every 5
        baseline = []
        t = 0.0
        for i in range(30):
            text = f"word{i}" + ("." if (i + 1) % 5 == 0 else "")
            baseline.append({"text": text, "start": round(t, 2),
                             "end": round(t + 0.4, 2)})
            t += 0.5
        # Splice events: 3 grafts that each add some duration past a given index
        splice_at = {7: 0.30, 15: 0.60, 22: 0.50}  # index -> seconds added
        drifted = []
        cumulative = 0.0
        for i, w in enumerate(baseline):
            if i in splice_at:
                cumulative += splice_at[i]
            drifted.append({
                "text": w["text"],
                "start": round(w["start"] + cumulative, 2),
                "end": round(w["end"] + cumulative, 2),
            })
        return baseline, drifted

    def test_stale_cues_fail_against_drifted_audio(self):
        baseline, drifted = self._build_drifted_pair()
        baseline_groups = group_words(baseline)
        max_skew, bad = verify_alignment(baseline_groups, drifted, tolerance_ms=100)
        self.assertGreater(max_skew, 100,
                           "stale cues against drifted audio should drift past tolerance")
        self.assertTrue(bad, "expected at least one cue out of tolerance")

    def test_regeneration_brings_drift_under_100ms(self):
        _baseline, drifted = self._build_drifted_pair()
        regen = group_words(drifted)
        max_skew, bad = verify_alignment(regen, drifted, tolerance_ms=100)
        self.assertLessEqual(max_skew, 10,
                             f"regenerated cues should match drifted audio; got {max_skew} ms")
        self.assertEqual(bad, [])

    def test_end_to_end_drift_target_under_100ms(self):
        """Top-level acceptance: whatever the audio looks like, regenerated
        cues sit at ≤100 ms drift everywhere."""
        _baseline, drifted = self._build_drifted_pair()
        groups = group_words(drifted)
        max_skew, bad = verify_alignment(groups, drifted, tolerance_ms=100)
        self.assertLessEqual(max_skew, 100)
        self.assertEqual(bad, [])


# ──────────────────────────────────────────────────────────────────────────
# captions.html patcher
# ──────────────────────────────────────────────────────────────────────────


SAMPLE_HTML = """\
<template id="captions-template">
  <div id="cap-stage">
      <div class="cap-group" id="cap-0">old text one</div>
      <div class="cap-group" id="cap-1">old text two</div>
      <div class="cap-group" id="cap-2">old text three</div>
    </div>
    <script>
      const groups = [{"id":"cap-0","start":0,"end":1},{"id":"cap-1","start":1,"end":2},{"id":"cap-2","start":2,"end":3}];
      // ...
    </script>
</template>
"""


class PatchCaptionsHtmlTest(unittest.TestCase):

    def test_patches_groups_array_and_divs(self):
        new_groups = [
            {"text": "Hello world.", "start": 0.10, "end": 1.20},
            {"text": "Goodbye now.", "start": 1.30, "end": 2.40},
        ]
        out = patch_captions_html(SAMPLE_HTML, new_groups)
        # New groups[] reflects new timing
        self.assertIn('"start":0.1', out)
        self.assertIn('"end":2.4', out)
        # Divs rebuilt — count matches new groups
        self.assertEqual(out.count('class="cap-group"'), 2)
        self.assertIn(">Hello world.</div>", out)
        self.assertIn(">Goodbye now.</div>", out)
        # Old text gone
        self.assertNotIn("old text one", out)
        self.assertNotIn("old text two", out)
        self.assertNotIn("old text three", out)

    def test_raises_when_groups_array_missing(self):
        bad_html = '<div class="cap-group" id="cap-0">x</div>'
        with self.assertRaises(RuntimeError):
            patch_captions_html(bad_html, [{"text": "a", "start": 0, "end": 1}])


# ──────────────────────────────────────────────────────────────────────────
# Integration: replay against the actual production transcript
# ──────────────────────────────────────────────────────────────────────────


class RealTranscriptIntegrationTest(unittest.TestCase):
    """Smoke test against the actual current narration transcript: regenerated
    cues must align to ≤100 ms across the full track."""

    def test_real_transcript_aligns_under_tolerance(self):
        transcript_path = ROOT / "assets" / "transcript.json"
        if not transcript_path.exists():
            self.skipTest("assets/transcript.json not present")
        words = json.loads(transcript_path.read_text())
        groups = group_words(words)
        max_skew, bad = verify_alignment(groups, words, tolerance_ms=100)
        self.assertLessEqual(max_skew, 100,
                             f"real transcript: max skew {max_skew} ms, bad cues {bad[:3]}")
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
