#!/usr/bin/env python3
"""
voicebox_tts.py — Direct CLI for the Voicebox local HTTP API.

The Voicebox desktop app runs a FastAPI server on localhost:17493. The MCP
server, the React frontend, and this script all talk to that same backend.
This script bypasses the app/MCP and goes straight to the REST API so you
can script TTS generation without touching the UI.

Generation flow (from docs.voicebox.sh/developer/tts-generation):
  1. POST /generate {profile_id, text, ...}  -> {id, status: "generating"}
  2. SSE  /generate/{id}/status              -> streams "data: {...}\\n\\n"
                                                until status in {completed, failed}
  3. GET  /audio/{id}                        -> raw WAV bytes (24 kHz mono, 16-bit PCM)

Usage:
    # List profiles (so you can pick a profile_id)
    python tools/voicebox_tts.py profiles

    # Generate (profile name OR uuid)
    python tools/voicebox_tts.py speak \\
        --profile George \\
        --text "Hello from the direct API." \\
        --out out.wav

    # Read text from stdin / file, override engine
    python tools/voicebox_tts.py speak --profile George --text-file script.txt \\
        --engine kokoro --out out.wav

Stdlib only. Compatible with Python 3.9+.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

DEFAULT_BASE_URL = "http://localhost:17493"
DEFAULT_TIMEOUT = 600  # seconds for a single long generation


# ───────────────────────────────────────────── HTTP helpers ──

def _request(
    method: str,
    url: str,
    body: dict[str, Any] | None = None,
    timeout: int = 30,
    stream: bool = False,
) -> Any:
    data = None
    headers = {"Accept": "application/json"}
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=timeout)
    except urllib.error.HTTPError as e:
        msg = e.read().decode("utf-8", "replace")
        raise SystemExit(f"HTTP {e.code} {method} {url}\n{msg}")
    except urllib.error.URLError as e:
        raise SystemExit(
            f"Cannot reach Voicebox at {url}: {e.reason}\n"
            "Is the Voicebox app running? It serves the API on localhost:17493."
        )
    if stream:
        return resp
    return json.loads(resp.read().decode())


# ────────────────────────────────────────────── operations ──

def list_profiles(base_url: str) -> list[dict]:
    return _request("GET", f"{base_url}/profiles")


def find_profile(profiles: list[dict], wanted: str) -> dict:
    """Match by exact uuid first, then by case-insensitive name."""
    for p in profiles:
        if p["id"] == wanted:
            return p
        if p["name"].lower() == wanted.lower():
            return p
    names = ", ".join(p["name"] for p in profiles)
    raise SystemExit(f"No profile matches '{wanted}'. Available: {names}")


def submit_generation(base_url: str, payload: dict) -> str:
    resp = _request("POST", f"{base_url}/generate", body=payload, timeout=30)
    if "id" not in resp:
        raise SystemExit(f"Unexpected /generate response: {resp}")
    return resp["id"]


def wait_for_completion(base_url: str, gen_id: str, timeout: int) -> dict:
    """
    Listen to the SSE status stream. Each frame is `data: {json}\\n\\n`.
    Returns the final status dict; raises if it ends in 'failed'.
    """
    url = f"{base_url}/generate/{gen_id}/status"
    resp = _request("GET", url, timeout=timeout, stream=True)
    last: dict = {}
    deadline = time.time() + timeout
    buf = b""
    while time.time() < deadline:
        chunk = resp.read1(4096) if hasattr(resp, "read1") else resp.read(4096)
        if not chunk:
            # stream closed — use whatever we last parsed
            break
        buf += chunk
        while b"\n\n" in buf:
            frame, buf = buf.split(b"\n\n", 1)
            for line in frame.splitlines():
                if line.startswith(b"data:"):
                    payload = line[5:].strip()
                    if not payload:
                        continue
                    try:
                        last = json.loads(payload)
                    except json.JSONDecodeError:
                        continue
                    status = last.get("status")
                    sys.stderr.write(f"  ↳ {status}")
                    if status in {"completed", "failed", "cancelled"}:
                        sys.stderr.write("\n")
                        if status == "failed":
                            raise SystemExit(f"Generation failed: {last.get('error')}")
                        if status == "cancelled":
                            raise SystemExit("Generation cancelled")
                        return last
                    sys.stderr.write("\n")
    raise SystemExit(f"Timed out after {timeout}s waiting for generation {gen_id}")


def download_audio(base_url: str, gen_id: str, out_path: Path) -> Path:
    url = f"{base_url}/audio/{gen_id}"
    resp = _request("GET", url, timeout=120, stream=True)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "wb") as f:
        while True:
            chunk = resp.read(65536)
            if not chunk:
                break
            f.write(chunk)
    return out_path


# ───────────────────────────────────────────────── CLI ──

def cmd_profiles(args: argparse.Namespace) -> None:
    profiles = list_profiles(args.base_url)
    if args.json:
        print(json.dumps(profiles, indent=2))
        return
    print(f"{'NAME':<24} {'ENGINE':<10} {'PRESET':<14} ID")
    print("-" * 80)
    for p in profiles:
        print(
            f"{p['name']:<24} "
            f"{(p.get('default_engine') or '-'):<10} "
            f"{(p.get('preset_voice_id') or '-'):<14} "
            f"{p['id']}"
        )


def cmd_speak(args: argparse.Namespace) -> None:
    # 1. Resolve text
    if args.text_file:
        text = Path(args.text_file).read_text(encoding="utf-8")
    elif args.text:
        text = args.text
    else:
        text = sys.stdin.read()
    text = text.strip()
    if not text:
        raise SystemExit("No text provided (use --text, --text-file, or stdin)")

    # 2. Resolve profile
    profiles = list_profiles(args.base_url)
    profile = find_profile(profiles, args.profile)
    sys.stderr.write(
        f"Profile: {profile['name']} ({profile['id']}) "
        f"engine={profile.get('default_engine')} preset={profile.get('preset_voice_id')}\n"
    )

    # 3. Build request
    payload: dict[str, Any] = {
        "profile_id": profile["id"],
        "text": text,
        "language": args.language,
        "engine": args.engine or profile.get("default_engine") or "kokoro",
        "normalize": not args.no_normalize,
        "max_chunk_chars": args.max_chunk_chars,
        "crossfade_ms": args.crossfade_ms,
    }
    if args.seed is not None:
        payload["seed"] = args.seed
    if args.instruct:
        payload["instruct"] = args.instruct
    if args.personality:
        payload["personality"] = True

    sys.stderr.write(f"Submitting {len(text)} chars to {args.base_url}/generate ...\n")
    gen_id = submit_generation(args.base_url, payload)
    sys.stderr.write(f"Generation id: {gen_id}\n")

    # 4. Wait for completion (SSE)
    final = wait_for_completion(args.base_url, gen_id, timeout=args.timeout)
    duration = final.get("duration", 0.0)

    # 5. Download
    out = Path(args.out).expanduser()
    download_audio(args.base_url, gen_id, out)
    sys.stderr.write(
        f"✔ Saved {out} ({out.stat().st_size:,} bytes, ~{duration:.2f}s audio)\n"
    )
    print(out)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base-url", default=DEFAULT_BASE_URL, help=f"default: {DEFAULT_BASE_URL}")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp_profiles = sub.add_parser("profiles", help="List voice profiles")
    sp_profiles.add_argument("--json", action="store_true")
    sp_profiles.set_defaults(func=cmd_profiles)

    sp_speak = sub.add_parser("speak", help="Generate speech and save to a WAV file")
    sp_speak.add_argument("--profile", required=True, help="Profile name or UUID")
    grp = sp_speak.add_mutually_exclusive_group()
    grp.add_argument("--text", help="Inline text")
    grp.add_argument("--text-file", help="Path to a UTF-8 text file")
    sp_speak.add_argument("--out", default="out.wav", help="Output WAV path (default: out.wav)")
    sp_speak.add_argument(
        "--engine",
        choices=["qwen", "qwen_custom_voice", "luxtts", "chatterbox", "chatterbox_turbo", "tada", "kokoro"],
        help="Override engine (defaults to profile.default_engine)",
    )
    sp_speak.add_argument("--language", default="en")
    sp_speak.add_argument("--seed", type=int)
    sp_speak.add_argument("--instruct", help="Natural-language style hint (Qwen CustomVoice only)")
    sp_speak.add_argument(
        "--personality",
        action="store_true",
        help="Rewrite text in profile's personality voice before TTS",
    )
    sp_speak.add_argument("--no-normalize", action="store_true")
    sp_speak.add_argument("--max-chunk-chars", type=int, default=800)
    sp_speak.add_argument("--crossfade-ms", type=int, default=50)
    sp_speak.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    sp_speak.set_defaults(func=cmd_speak)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
