#!/usr/bin/env python
"""Single-call Kokoro synthesizer for the punctuation spike.

usage: python synth.py "<text>" <out.wav> [voice]
"""
import sys
import json
import time
from pathlib import Path

import kokoro_onnx
import soundfile as sf

MODEL = "/Users/I548399/.cache/hyperframes/tts/models/kokoro-v1.0.onnx"
VOICES = "/Users/I548399/.cache/hyperframes/tts/voices/voices-v1.0.bin"

_model = None

def get_model():
    global _model
    if _model is None:
        _model = kokoro_onnx.Kokoro(MODEL, VOICES)
    return _model

def synth(text: str, out_path: str, voice: str = "bm_george", speed: float = 1.0):
    model = get_model()
    t0 = time.time()
    samples, sr = model.create(text, voice=voice, speed=speed)
    sf.write(out_path, samples, sr)
    return {
        "out": out_path,
        "sample_rate": sr,
        "duration": round(len(samples) / sr, 3),
        "synth_time": round(time.time() - t0, 2),
    }

if __name__ == "__main__":
    text = sys.argv[1]
    out = sys.argv[2]
    voice = sys.argv[3] if len(sys.argv) > 3 else "bm_george"
    print(json.dumps(synth(text, out, voice)))
