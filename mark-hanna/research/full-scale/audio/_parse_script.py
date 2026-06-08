#!/usr/bin/env python3
"""Parse FULL_SCRIPT.md into per-scene TTS chunks + silence beats."""
import re, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
src = (ROOT / "research/script/FULL_SCRIPT.md").read_text()

scene_re = re.compile(
    r"### SCENE (\d+) — ([\d:]+)–([\d:]+) \((.*?)\) — (.*?)\n(.*?)(?=\n### |\n## |\Z)",
    re.DOTALL,
)

def parse_beat_seconds(line):
    m = re.search(r"\[(?:BEAT\s*—\s*)?([\d.]+)\s*s", line)
    return float(m.group(1)) if m else None

def clean_for_tts(line):
    line = re.sub(r"\*\*\([^)]*\)\*\*", "", line).strip()
    return line or None

scenes = []
for m in scene_re.finditer(src):
    num = int(m.group(1))
    start_s, end_s, dur, title, body = m.groups()[1:]
    narr_m = re.search(r"\*Narration:\*\s*\n(.*)", body, re.DOTALL)
    narr_block = narr_m.group(1) if narr_m else ""
    vis_m = re.search(r"\*Visuals:\*\s*(.*?)\n\*", body, re.DOTALL)
    visuals = vis_m.group(1).strip() if vis_m else ""
    emo_m = re.search(r"\*Intended emotion:\*\s*(.*?)\n", body, re.DOTALL)
    emotion = emo_m.group(1).strip() if emo_m else ""
    lines = []
    for raw in narr_block.split("\n"):
        s = raw.strip()
        if s.startswith(">"):
            s = s[1:].strip()
        if not s:
            continue
        if s.startswith("```") or s == "---":
            continue
        lines.append(s)
    scenes.append(dict(num=num, start=start_s, end=end_s, duration=dur,
                       title=title.strip(), visuals=visuals, emotion=emotion,
                       narration_lines=lines))

out_dir = ROOT / "research/full-scale/audio/scenes"
out_dir.mkdir(parents=True, exist_ok=True)

manifest = []
for sc in scenes:
    tts_chunks = []
    current_text = []
    for raw in sc["narration_lines"]:
        if raw.startswith("[BEAT") or re.match(r"^\[[\d.]", raw):
            if current_text:
                tts_chunks.append(("text", " ".join(current_text)))
                current_text = []
            secs = parse_beat_seconds(raw)
            if secs is not None:
                tts_chunks.append(("silence", secs))
        else:
            cleaned = clean_for_tts(raw)
            if cleaned:
                current_text.append(cleaned)
    if current_text:
        tts_chunks.append(("text", " ".join(current_text)))

    scene_path = out_dir / f"scene-{sc['num']:02d}-narration.md"
    lines_md = [
        f"# Scene {sc['num']:02d} — {sc['title']}",
        f"**Window:** {sc['start']}–{sc['end']} ({sc['duration']})",
        f"**Emotion:** {sc['emotion']}",
        "",
        "## TTS render plan",
        "",
        "Render each `text` chunk as its own wav (Voicebox George + atempo 1.18, loudnorm I=-16:TP=-1.5).",
        "Concat in order with `anullsrc` silence chunks between them via ffmpeg `-f concat`.",
        "Final per-scene wav: `assets/scenes/scene-NN-narration.wav`.",
        "",
    ]
    for i, (kind, val) in enumerate(tts_chunks, 1):
        if kind == "text":
            lines_md += [f"### chunk {i:02d} — text", "```", val, "```", ""]
        else:
            lines_md += [f"### chunk {i:02d} — silence {val} s (anullsrc -t {val})", ""]
    scene_path.write_text("\n".join(lines_md))

    flat_path = out_dir / f"scene-{sc['num']:02d}-narration.txt"
    text_only = [v for k, v in tts_chunks if k == "text"]
    flat_path.write_text("\n\n".join(text_only) + "\n")

    silence_total = sum(v for k, v in tts_chunks if k == "silence")
    word_count = sum(len(v.split()) for k, v in tts_chunks if k == "text")
    manifest.append(dict(
        scene=sc["num"], title=sc["title"],
        window=f"{sc['start']}-{sc['end']}", duration=sc["duration"],
        chunks=len(tts_chunks), silence_seconds=silence_total,
        word_count=word_count, emotion=sc["emotion"],
        files={"plan": scene_path.name, "tts_text": flat_path.name},
    ))

print(f"scenes parsed: {len(scenes)}")
for m in manifest:
    print(f"  s{m['scene']:02d} {m['window']:>11} ({m['duration']:>5}) — "
          f"{m['word_count']:>4}w, {m['silence_seconds']:>4.1f}s sil — {m['title']}")

(out_dir.parent / "VO_MANIFEST.json").write_text(json.dumps(manifest, indent=2))
print("\nVO_MANIFEST.json written")
