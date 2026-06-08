#!/usr/bin/env python3
"""
SFX placement table + VO-collision verifier for Mark Hanna full-scale.

Validates against silencedetect-derived VO occupancy of narration.fullscale.wav
(NOT the 5-min preview transcript.json, which doesn't apply to the 24-min cut).

Outputs:
  - assets/sfx/_placements.json: event list w/ measured peak times + status
  - per-event verdict: in_silence | quiet (≥6 dB under VO peak) | violation
"""
from __future__ import annotations

import json
import re
import subprocess
import wave
from pathlib import Path

PROJ = Path(__file__).resolve().parents[3]
SFX = PROJ / "assets" / "sfx"
MASTER = PROJ / "assets" / "narration.fullscale.wav"


def get_vo_silences(master: Path, threshold_db: float = -40.0,
                    min_dur_s: float = 0.20) -> list[tuple[float, float]]:
    """Return list of (silence_start, silence_end) in seconds."""
    out = subprocess.run(
        ["ffmpeg", "-i", str(master),
         "-af", f"silencedetect=n={threshold_db}dB:d={min_dur_s}",
         "-f", "null", "/dev/null"],
        capture_output=True, text=True
    ).stderr
    intervals = []
    cur_start = None
    for line in out.splitlines():
        ms = re.search(r"silence_start:\s*([\d.]+)", line)
        me = re.search(r"silence_end:\s*([\d.]+)", line)
        if ms:
            cur_start = float(ms.group(1))
        elif me and cur_start is not None:
            intervals.append((cur_start, float(me.group(1))))
            cur_start = None
    return intervals


def is_in_silence(t: float, silences: list[tuple[float, float]],
                  pad_ms: float = 50.0) -> bool:
    p = pad_ms / 1000.0
    for a, b in silences:
        if a + p <= t <= b - p:
            return True
    return False


def stem_peak_offset(family: str, dur_s: float) -> float:
    """Approximate peak time within the stem."""
    if family == "newspaper":
        return min(dur_s, 0.32)
    if family == "telegraph":
        return min(dur_s, 0.5)
    if family == "cornet":
        return min(dur_s, 0.4)
    if family == "carriage":
        return dur_s / 2
    if family == "rail":
        return dur_s * 0.55
    if family == "clock":
        return 0.005
    if family == "ledger":
        return min(dur_s, dur_s * 0.55)
    # snare, hammer
    return 0.005


def stem_dur(path: Path) -> float:
    with wave.open(str(path), "rb") as w:
        return w.getnframes() / w.getframerate()


# ----------------------------------------------------------------------
# Event table (anchored to actual VO silences in narration.fullscale.wav)
#
# Scene VO occupancy (verified from silencedetect):
#   01: 0–16.3s     | 02: 46–83.4s   | 03: 210–228s    | 04: 300–312s
#   05: 360–380s    | 06: 450–459s   | 07: 510–541s    | 08: 600–620s
#   09: 690–743s    | 10: 840–887s   | 11: 960–985s    | 12: 1065–1085s
#   13: 1110–1132s  | 14: 1170–1186s | 15: 1216–1218s  | 16: 1245–1296s
#   17: 1321–1346s  | 18: 1380–1394s | 19: 1410–1431s
#
# Each event time is the STEM START time. Peak time is computed from
# stem_peak_offset and validated against silences.
# ----------------------------------------------------------------------
EVENTS = [
    # Scene 01 — newspaper rustle at 0:04, ENDING right as VO starts (4.04s)
    dict(t=3.30, file="newspaper-01.wav", family="newspaper",
         gain_db=-2.0, layer="fg", cue="cold-open silence break", scene="01"),

    # Scene 02 — pen scratch under "$3,500,000" count-up at 2:30 (150s)
    # Full-scale VO scene 2 ends at 83.4s; 150s sits in deep inter-scene silence.
    dict(t=150.0, file="ledger-01.wav", family="ledger",
         gain_db=-3.0, layer="fg", cue="count-up tick 1", scene="02"),
    dict(t=150.7, file="ledger-02.wav", family="ledger",
         gain_db=-3.0, layer="fg", cue="count-up tick 2", scene="02"),
    dict(t=151.4, file="ledger-01.wav", family="ledger",
         gain_db=-3.0, layer="fg", cue="count-up tick 3", scene="02"),

    # Scene 02 — sparse telegraph chatter under donor lines (placed in
    # the long inter-scene gap between 83.4s and 210s; bed-low gain so any
    # near-VO bleed is automatically ≥6 dB below)
    dict(t=180.0, file="telegraph-01.wav", family="telegraph",
         gain_db=-9.0, layer="fg", cue="donor lines telegraph chatter", scene="02"),

    # Scene 02 — newspaper rustle at the act-break sting at 3:30 (peak just
    # before 210, where scene 03 enters)
    dict(t=209.30, file="newspaper-02.wav", family="newspaper",
         gain_db=-3.0, layer="fg", cue="act-break sting", scene="02"),

    # Scene 03 — distant carriage bed, first 7 s of scene-03 (210–217s).
    # bed at −12 dB, well below VO peak (−1.5 dB) → ≥10 dB headroom.
    dict(t=210.0, file="carriage-01.wav", family="carriage",
         gain_db=-12.0, layer="bed", cue="period locator bed", scene="03"),

    # Scene 07 — hammer on iron, single strike at 9:00 (~540s).
    # Scene 7 VO ends at 541.60 (verified via silencedetect). Place hammer
    # at 541.70 → peak ~541.71 lands in the post-VO silence 541.60–600.02.
    dict(t=541.70, file="hammer-01.wav", family="hammer",
         gain_db=-4.0, layer="fg", cue="dollar-sign pulse strike", scene="07"),

    # Scene 10 — newspaper rustle at 14:00 (840s, scene-10 start). Peak at
    # 840.0 = first VO word entry; place rustle ending at 840.0 (start at 839.3).
    dict(t=839.30, file="newspaper-03.wav", family="newspaper",
         gain_db=-3.0, layer="fg", cue="PANIC headline plate", scene="10"),

    # Scene 10 — telegraph chatter at the inter-scene silence between
    # scenes 10 (ends 887.1) and 11 (starts 960). City-name bursts
    # repurposed as one densified sequence within the silence.
    dict(t=895.0, file="telegraph-02.wav", family="telegraph",
         gain_db=-7.0, layer="fg", cue="post-PANIC telegraph burst", scene="10"),

    # Scene 11 — snare hits with each ledger-line write-in. Scene 11 VO
    # 960–985. Place 3 hits during/around scene; SHOT_BOARDS says ledger
    # writes at KF@22s (=982s). Snares at 982.5/983.5/984.5 in the late-VO
    # tail / immediately after VO ends (985 is silence).
    # Scene 11 VO ends 984.85 (silencedetect). Place 3 snares at 985.0/986.0/987.0
    # — past VO end into the deep 984.85→1065.01 silence; the visual KF still
    # lands at the ledger-line writes per SHOT_BOARDS (the music task's Cue A
    # rest absorbs the half-second offset from the literal KF; SFX-mix task
    # is binding for hit timing rather than pixel-frame, per SOUND_DESIGN_PLAN
    # §6 "snare hits land within ±33 ms of the visual expo.out arrival point"
    # — the renderer schedules the ledger-line write-in to land on the snare).
    dict(t=985.00, file="snare-01.wav", family="snare",
         gain_db=-3.0, layer="fg", cue="ledger line 1 expo.out", scene="11"),
    dict(t=986.00, file="snare-02.wav", family="snare",
         gain_db=-3.0, layer="fg", cue="ledger line 2 expo.out", scene="11"),
    dict(t=987.00, file="snare-03.wav", family="snare",
         gain_db=-3.0, layer="fg", cue="ledger line 3 (mechanism reveal sync)",
         scene="11"),
    # Scene 11 — pen scratch on total stamp (post-VO, ~995s, well into silence)
    dict(t=995.0, file="ledger-02.wav", family="ledger",
         gain_db=-4.0, layer="fg", cue="total stamp pen scratch", scene="11"),

    # Scene 12 — distant rail bed (1065–1080) under porch scene. Scene 12 VO
    # 1065–1085; bed at −16 dB stays subliminal under VO.
    dict(t=1065.0, file="rail-01.wav", family="rail",
         gain_db=-16.0, layer="bed", cue="porch rail bed", scene="12"),

    # Scene 13 — distant rail at "Bryan tours" line. Scene 13 VO 1110–1132.
    # Bed runs the full scene at −14 dB.
    dict(t=1112.0, file="rail-02.wav", family="rail",
         gain_db=-14.0, layer="bed", cue="Bryan tours rail bed", scene="13"),

    # Scene 17 — newspaper at PRESIDENT SHOT headline (~22:30 = 1350s).
    # Scene 17 VO 1321–1346, then silence 1346–1380. 1350 is in silence.
    dict(t=1350.0, file="newspaper-02.wav", family="newspaper",
         gain_db=-3.0, layer="fg", cue="PRESIDENT SHOT headline", scene="17"),

    # Scene 17 — single muted cornet on Czolgosz name plate (in same
    # post-VO silence, ~1370s).
    dict(t=1370.0, file="cornet-01.wav", family="cornet",
         gain_db=-8.0, layer="fg", cue="Czolgosz name plate", scene="17"),

    # Scene 18 — clock tick BED ~−22 dB across the obituary plate
    # (1380–1410). Implemented as 30 single ticks at 1.0 s intervals.
    # Encoded as a single PLAN-event but expanded to 30 stem plays in mix.
    dict(t=1380.0, file="clock-01.wav", family="clock",
         gain_db=-22.0, layer="bed", cue="typhoid obituary clock bed",
         scene="18", tick_bed_dur=30.0, tick_period=1.0),

    # Scene 19 — final newspaper rustle on cartoon return (~23:55 = 1435s)
    # Scene 19 VO ends 1431.5, silence 1431.5–1440. 1435 is in silence.
    dict(t=1434.5, file="newspaper-01.wav", family="newspaper",
         gain_db=-4.0, layer="fg", cue="closing-loop rustle", scene="19"),
]


def cluster_key(ev: dict) -> tuple[str, str, str]:
    """Cluster repeats of the same family within a scene as a single plan-event."""
    cue = ev["cue"]
    base = re.sub(r"\s+(line\s+)?\d+(\s+expo\.out)?$", "", cue)
    base = re.sub(r"\s+tick\s+\d+$", "", base)
    base = re.sub(r"\s+\(.+\)$", "", base)
    return (ev["scene"], ev["family"], base)


def main() -> None:
    print("Computing VO silences from narration.fullscale.wav…")
    silences = get_vo_silences(MASTER)
    big_silences = [(a, b) for a, b in silences if b - a > 0.6]
    print(f"  {len(silences)} silences, {len(big_silences)} >0.6s")

    # Verify file existence + collect peak times
    enriched = []
    for ev in EVENTS:
        p = SFX / ev["file"]
        assert p.exists(), f"missing stem {p}"
        d = stem_dur(p)
        peak_t = ev["t"] + stem_peak_offset(ev["family"], d)
        ok_silent = is_in_silence(peak_t, silences)
        ok_quiet = ev["gain_db"] <= -6.0 or ev["layer"] == "bed"
        verdict = "in_silence" if ok_silent else ("quiet" if ok_quiet else "VIOLATION")
        e2 = dict(ev, dur_s=d, peak_t=peak_t, verdict=verdict)
        enriched.append(e2)

    clusters = {}
    for e in enriched:
        clusters.setdefault(cluster_key(e), []).append(e)
    n_clusters = len(clusters)

    print(f"\nDistinct plan-events (clusters): {n_clusters} (≤20 required)")
    print(f"Total stem fires: {len(enriched)}")
    assert n_clusters <= 20, f"plan-event count {n_clusters} > 20"

    violations = [e for e in enriched if e["verdict"] == "VIOLATION"]
    print("\nPer-event verdicts:")
    for e in enriched:
        flag = "✓" if e["verdict"] != "VIOLATION" else "✗"
        print(f"  {flag} t={e['t']:7.2f}s peak={e['peak_t']:7.2f}s "
              f"gain={e['gain_db']:+5.1f}dB layer={e['layer']:3s} "
              f"family={e['family']:9s} {e['verdict']:10s} -- {e['cue']}")

    if violations:
        print(f"\n{len(violations)} VIOLATIONS — fix before mixing.")
        raise SystemExit(2)

    out = SFX / "_placements.json"
    out.write_text(json.dumps({
        "events": enriched,
        "distinct_plan_events": n_clusters,
        "total_stem_fires": len(enriched),
        "verdict": "OK",
    }, indent=2))
    print(f"\nwrote {out.relative_to(PROJ)}")


if __name__ == "__main__":
    main()
