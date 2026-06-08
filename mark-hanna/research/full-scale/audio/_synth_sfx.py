#!/usr/bin/env python3
"""
Synthesize the 8-family SFX inventory for the Mark Hanna full-scale doc.

Tier-4 "Custom Foley by editor" per SOUND_DESIGN_PLAN.md §5. No procurement —
every stem is generated procedurally here; the script is the provenance.

Outputs (mono, 48 kHz, pcm_s16le):
  assets/sfx/<family>-NN.wav  one or more variants per family

numpy-only (no scipy) — biquad IIRs implemented by hand.
"""
from __future__ import annotations

import math
import wave
from pathlib import Path

import numpy as np

SR = 48000
PROJ = Path(__file__).resolve().parents[3]
OUT = PROJ / "assets" / "sfx"
OUT.mkdir(parents=True, exist_ok=True)


def write_wav(path: Path, x: np.ndarray) -> None:
    x = np.clip(x, -1.0, 1.0)
    pcm = (x * 32767.0).astype(np.int16)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


# ---- RBJ-style biquads (numpy-only) -----------------------------------
def _biquad_apply(x: np.ndarray, b: list[float], a: list[float]) -> np.ndarray:
    """Direct-form-I biquad applied in two passes for higher-order if asked."""
    y = np.empty_like(x, dtype=np.float64)
    x1 = x2 = y1 = y2 = 0.0
    b0, b1, b2 = b
    a1, a2 = a[1], a[2]  # a[0]=1
    for i, xi in enumerate(x):
        yi = b0 * xi + b1 * x1 + b2 * x2 - a1 * y1 - a2 * y2
        y[i] = yi
        x2, x1 = x1, xi
        y2, y1 = y1, yi
    return y


def _rbj_lp(fc: float, q: float = 0.707, sr: int = SR):
    w0 = 2 * math.pi * fc / sr
    cw = math.cos(w0); sw = math.sin(w0)
    alpha = sw / (2 * q)
    b0 = (1 - cw) / 2; b1 = 1 - cw; b2 = (1 - cw) / 2
    a0 = 1 + alpha;     a1 = -2 * cw;  a2 = 1 - alpha
    return [b0/a0, b1/a0, b2/a0], [1.0, a1/a0, a2/a0]


def _rbj_hp(fc: float, q: float = 0.707, sr: int = SR):
    w0 = 2 * math.pi * fc / sr
    cw = math.cos(w0); sw = math.sin(w0)
    alpha = sw / (2 * q)
    b0 = (1 + cw) / 2; b1 = -(1 + cw); b2 = (1 + cw) / 2
    a0 = 1 + alpha;     a1 = -2 * cw;  a2 = 1 - alpha
    return [b0/a0, b1/a0, b2/a0], [1.0, a1/a0, a2/a0]


def _rbj_bp(fc: float, q: float = 1.0, sr: int = SR):
    """constant-skirt-gain bandpass (RBJ)."""
    w0 = 2 * math.pi * fc / sr
    cw = math.cos(w0); sw = math.sin(w0)
    alpha = sw / (2 * q)
    b0 = sw / 2; b1 = 0.0; b2 = -sw / 2
    a0 = 1 + alpha; a1 = -2 * cw; a2 = 1 - alpha
    return [b0/a0, b1/a0, b2/a0], [1.0, a1/a0, a2/a0]


def hpf(x: np.ndarray, fc: float = 80.0, order: int = 2) -> np.ndarray:
    b, a = _rbj_hp(fc, q=0.707)
    y = x.astype(np.float64)
    for _ in range(max(1, order // 2)):
        y = _biquad_apply(y, b, a)
    return y


def lpf(x: np.ndarray, fc: float, order: int = 2) -> np.ndarray:
    b, a = _rbj_lp(fc, q=0.707)
    y = x.astype(np.float64)
    for _ in range(max(1, order // 2)):
        y = _biquad_apply(y, b, a)
    return y


def bpf(x: np.ndarray, lo: float, hi: float) -> np.ndarray:
    """Cascade HPF→LPF — we don't need true Butterworth band, just a usable shape."""
    y = hpf(x, lo, order=2)
    y = lpf(y, hi, order=2)
    return y


def normalize(x: np.ndarray, peak_db: float = -3.0) -> np.ndarray:
    peak = float(np.max(np.abs(x))) + 1e-12
    target = 10 ** (peak_db / 20)
    return (x * (target / peak)).astype(np.float64)


# ----------------------------------------------------------------------
# Family 1 — Newspaper rustle
# ----------------------------------------------------------------------
def make_newspaper(seed: int = 1, dur_s: float = 0.7) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = int(dur_s * SR)
    noise = rng.normal(0, 1, n)
    pink = lpf(noise, 1000)
    pink = bpf(pink, 800, 6000)
    t = np.arange(n) / SR
    arc = np.minimum(1.0, np.exp(-((t - 0.32) ** 2) / (2 * 0.18 ** 2)))
    grain = np.zeros(n)
    nbursts = int(rng.integers(35, 55))
    for _ in range(nbursts):
        ctr = rng.uniform(0.05, dur_s - 0.05)
        wid = rng.uniform(0.005, 0.025)
        i0 = int((ctr - wid / 2) * SR)
        i1 = int((ctr + wid / 2) * SR)
        if i0 < 0 or i1 > n or i1 - i0 < 2:
            continue
        grain[i0:i1] += float(rng.uniform(0.5, 1.0)) * np.hanning(i1 - i0)
    x = pink * grain * arc
    x = hpf(x, 200)
    return normalize(x, -6.0)


# ----------------------------------------------------------------------
# Family 2 — Ledger pen scratch
# ----------------------------------------------------------------------
def make_pen_scratch(seed: int = 2, dur_s: float = 0.35) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = int(dur_s * SR)
    noise = rng.normal(0, 1, n)
    nb = bpf(noise, 2500, 9000)
    t = np.arange(n) / SR
    e = np.exp(-((t - dur_s * 0.55) ** 2) / (2 * (dur_s * 0.18) ** 2))
    flutter = 1.0 + 0.4 * np.sin(2 * math.pi * float(rng.uniform(40, 80)) * t)
    x = nb * e * flutter
    x = hpf(x, 1500)
    return normalize(x, -8.0)


# ----------------------------------------------------------------------
# Family 3 — Telegraph dot-dash chatter
# ----------------------------------------------------------------------
def make_telegraph(seed: int = 3, dur_s: float = 1.6) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = int(dur_s * SR)
    out = np.zeros(n)
    DOT_MS = 90.0
    dot_n = int(DOT_MS * SR / 1000)
    dash_n = 3 * dot_n
    gap_n = dot_n
    inter_letter_n = 3 * dot_n
    letters = [
        [1], [3, 1, 1, 1], [3, 1, 3, 1], [3, 1, 1], [1],
        [1, 1, 3, 1], [3, 3, 1], [1, 1, 1, 1], [1, 1], [1, 3, 3, 3],
        [3, 1, 3], [1, 3, 1, 1], [3, 3], [3, 1], [3, 3, 3],
    ]
    word = [letters[int(rng.integers(0, len(letters)))]
            for _ in range(int(rng.integers(3, 5)))]
    cursor = int(0.05 * SR)
    freq = 800.0
    for letter in word:
        for mark in letter:
            length = dot_n if mark == 1 else dash_n
            if cursor + length >= n:
                break
            t = np.arange(length) / SR
            tone = np.sin(2 * math.pi * freq * t)
            a = max(1, int(0.005 * SR))
            env = np.ones(length)
            env[:a] = np.linspace(0, 1, a)
            env[-a:] = np.linspace(1, 0, a)
            out[cursor:cursor + length] += tone * env * 0.6
            cursor += length + gap_n
        cursor += inter_letter_n - gap_n
    hiss = rng.normal(0, 0.02, n)
    hiss = bpf(hiss, 300, 4000)
    out = out + hiss * 0.3
    out = bpf(out, 350, 4000)
    return normalize(out, -7.0)


# ----------------------------------------------------------------------
# Family 4 — Snare drum hit
# ----------------------------------------------------------------------
def make_snare(seed: int = 4, dur_s: float = 0.30) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = int(dur_s * SR)
    t = np.arange(n) / SR
    noise = rng.normal(0, 1, n)
    body = bpf(noise, 300, 6500)
    body_env = np.exp(-t / 0.06)
    body = body * body_env
    tone = (np.sin(2 * math.pi * 220 * t) * np.exp(-t / 0.05)
            + 0.6 * np.sin(2 * math.pi * 380 * t) * np.exp(-t / 0.04))
    snare_noise = bpf(rng.normal(0, 1, n), 4000, 9000)
    snare_noise = snare_noise * np.exp(-t / 0.10)
    x = 0.55 * body + 0.30 * tone + 0.40 * snare_noise
    x = hpf(x, 80)
    return normalize(x, -2.0)


# ----------------------------------------------------------------------
# Family 5 — Hammer on iron
# ----------------------------------------------------------------------
def make_hammer_iron(seed: int = 5, dur_s: float = 0.9) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = int(dur_s * SR)
    t = np.arange(n) / SR
    ratios = [1.00, 1.78, 2.43, 3.16, 4.27, 5.34, 6.81]
    decays = [0.35, 0.55, 0.45, 0.30, 0.25, 0.20, 0.15]
    f0 = 240.0
    out = np.zeros(n)
    for r, d in zip(ratios, decays):
        out += np.sin(2 * math.pi * f0 * r * t) * np.exp(-t / d) / r
    cn = int(0.005 * SR)
    click = bpf(rng.normal(0, 1, cn), 2000, 9000)
    out[:cn] += click * 0.7
    body_noise = bpf(rng.normal(0, 1, n), 200, 5000) * np.exp(-t / 0.05) * 0.4
    out = out + body_noise
    out = hpf(out, 80)
    return normalize(out, -3.0)


# ----------------------------------------------------------------------
# Family 6a — Distant carriage on cobblestone
# ----------------------------------------------------------------------
def make_carriage(seed: int = 6, dur_s: float = 7.0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = int(dur_s * SR)
    t = np.arange(n) / SR
    out = np.zeros(n)
    cur = 0.2
    while cur < dur_s - 0.2:
        i = int(cur * SR)
        h_n = int(0.08 * SR)
        if i + h_n > n:
            break
        ht = np.arange(h_n) / SR
        thud = np.sin(2 * math.pi * 110 * ht) * np.exp(-ht / 0.025) * 0.7
        thud += bpf(rng.normal(0, 1, h_n), 200, 1200) * np.exp(-ht / 0.020) * 0.5
        out[i:i + h_n] += thud * float(rng.uniform(0.6, 1.0))
        gap = float(rng.choice([0.22, 0.24, 0.42, 0.20]))
        cur += gap
    rumble = bpf(rng.normal(0, 1, n), 60, 250) * 0.20
    out = lpf(out + rumble, 1800)
    bell = np.exp(-((t - dur_s / 2) ** 2) / (2 * (dur_s / 3) ** 2))
    out = out * bell
    out = hpf(out, 80)
    return normalize(out, -10.0)


# ----------------------------------------------------------------------
# Family 6b — Distant rail (steam locomotive bed)
# ----------------------------------------------------------------------
def make_rail_distant(seed: int = 7, dur_s: float = 12.0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = int(dur_s * SR)
    t = np.arange(n) / SR
    chuff_rate = 3.2
    chuff_env = 0.5 + 0.5 * np.sign(np.sin(2 * math.pi * chuff_rate * t))
    chuff_env = lpf(chuff_env, 30)
    rumble = bpf(rng.normal(0, 1, n), 40, 200) * chuff_env * 0.6
    whistle_freq = 320 + 40 * np.sin(2 * math.pi * 0.05 * t)
    phase = 2 * math.pi * np.cumsum(whistle_freq) / SR
    whistle_env = np.exp(-((t - dur_s * 0.55) ** 2) / (2 * 0.6 ** 2))
    whistle = np.sin(phase) * whistle_env * 0.10
    out = rumble + whistle
    out = lpf(out, 1500)
    out = hpf(out, 60)
    fade = np.minimum(np.minimum(t / 1.5, 1.0), (dur_s - t) / 1.5)
    out = out * np.clip(fade, 0, 1)
    return normalize(out, -14.0)


# ----------------------------------------------------------------------
# Family 7 — Muted cornet single note
# ----------------------------------------------------------------------
def make_cornet(seed: int = 8, dur_s: float = 1.6) -> np.ndarray:
    n = int(dur_s * SR)
    t = np.arange(n) / SR
    f0 = 466.16
    harmonics = [1, 2, 3, 4, 5, 6, 7]
    levels = [1.0, 0.55, 0.18, 0.08, 0.05, 0.03, 0.02]
    out = np.zeros(n)
    for h, lv in zip(harmonics, levels):
        out += lv * np.sin(2 * math.pi * f0 * h * t)
    vib = 1.0 + 0.005 * np.sin(2 * math.pi * 5.0 * t)
    out = out * vib
    env = np.zeros(n)
    swell_n = int(0.12 * SR)
    hold_n = int(0.7 * SR)
    decay_n = n - swell_n - hold_n
    env[:swell_n] = np.linspace(0, 1, swell_n)
    env[swell_n:swell_n + hold_n] = 1.0
    env[swell_n + hold_n:] = np.exp(-np.linspace(0, 5, decay_n))
    out = out * env
    out = hpf(out, 200)
    return normalize(out, -8.0)


# ----------------------------------------------------------------------
# Family 8 — Mechanical clock tick
# ----------------------------------------------------------------------
def make_clock_tick(seed: int = 9, dur_s: float = 0.30) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = int(dur_s * SR)
    t = np.arange(n) / SR
    click = bpf(rng.normal(0, 1, n), 1000, 6000) * np.exp(-t / 0.008) * 0.8
    res = (0.4 * np.sin(2 * math.pi * 540 * t) * np.exp(-t / 0.020)
           + 0.2 * np.sin(2 * math.pi * 1800 * t) * np.exp(-t / 0.012))
    out = click + res
    out = hpf(out, 250)
    return normalize(out, -10.0)


INVENTORY = {
    "newspaper-01": (make_newspaper, {"seed": 11, "dur_s": 0.7}),
    "newspaper-02": (make_newspaper, {"seed": 12, "dur_s": 0.6}),
    "newspaper-03": (make_newspaper, {"seed": 13, "dur_s": 0.65}),
    "ledger-01":    (make_pen_scratch, {"seed": 21, "dur_s": 0.32}),
    "ledger-02":    (make_pen_scratch, {"seed": 22, "dur_s": 0.40}),
    "telegraph-01": (make_telegraph, {"seed": 31, "dur_s": 1.6}),
    "telegraph-02": (make_telegraph, {"seed": 32, "dur_s": 1.4}),
    "telegraph-03": (make_telegraph, {"seed": 33, "dur_s": 1.5}),
    "snare-01":     (make_snare, {"seed": 41, "dur_s": 0.30}),
    "snare-02":     (make_snare, {"seed": 42, "dur_s": 0.30}),
    "snare-03":     (make_snare, {"seed": 43, "dur_s": 0.30}),
    "hammer-01":    (make_hammer_iron, {"seed": 51, "dur_s": 1.2}),
    "carriage-01":  (make_carriage, {"seed": 61, "dur_s": 7.0}),
    "rail-01":      (make_rail_distant, {"seed": 71, "dur_s": 12.0}),
    "rail-02":      (make_rail_distant, {"seed": 72, "dur_s": 16.0}),
    "cornet-01":    (make_cornet, {"seed": 81, "dur_s": 1.6}),
    "clock-01":     (make_clock_tick, {"seed": 91, "dur_s": 0.30}),
}


def main() -> None:
    for name, (fn, kw) in INVENTORY.items():
        path = OUT / f"{name}.wav"
        x = fn(**kw)
        write_wav(path, x)
        print(f"wrote {path.relative_to(PROJ)} ({len(x)/SR:.3f}s, peak={float(np.max(np.abs(x))):.3f})")


if __name__ == "__main__":
    main()
