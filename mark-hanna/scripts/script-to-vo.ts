#!/usr/bin/env bun
/**
 * script-to-vo.ts — Extract per-scene voiceover text + audio manifest from FULL_SCRIPT.v2.md.
 *
 * Reads `research/script/FULL_SCRIPT.v2.md`, walks scene-by-scene, and emits:
 *   assets/narration/scenes/scene-NN.txt      — clean prose for `hyperframes tts` input
 *   assets/narration/manifest.json            — ordered list of {chunk: path} | {silence: seconds}
 *
 * Stripping rules (per M2 / M14 / M15 in REBUILD.md):
 *   - `[BEAT — 0.6 s]` / `[4 s silence — push-in]` lines  → silence chunk in manifest, NOT in text
 *   - `**(verbatim)** / **(spoken; …)**`                  → strip annotation tags
 *   - `<!-- noqa: ... -->`                                → strip HTML comment
 *   - `*"…"*`                                             → unwrap italics around primary-source quotes (TTS reads flat)
 *   - leading `> ` blockquote markers                     → strip (markdown rendering only)
 *   - everything outside `### SCENE N` blocks             → ignored
 *   - lines outside `*Narration:*` block within a scene   → ignored (visuals/setting/characters)
 *
 * Usage: bun scripts/script-to-vo.ts [--script PATH] [--out DIR]
 */

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join, dirname, resolve } from "node:path";

type ManifestEntry = { chunk: string } | { silence: number };

const PROJECT_ROOT = resolve(import.meta.dir, "..");
const DEFAULT_SCRIPT = join(PROJECT_ROOT, "research/script/FULL_SCRIPT.v2.md");
const DEFAULT_OUT = join(PROJECT_ROOT, "assets/narration");

// Parse CLI args
const args = Bun.argv.slice(2);
let scriptPath = DEFAULT_SCRIPT;
let outDir = DEFAULT_OUT;
for (let i = 0; i < args.length; i++) {
  if (args[i] === "--script") scriptPath = resolve(args[++i]);
  else if (args[i] === "--out") outDir = resolve(args[++i]);
}

const SCENE_HEADER = /^### SCENE (\d+)\s+—/;
const NARRATION_MARK = /^\*Narration[^*]*\*\s*$/;
const HORIZONTAL_RULE = /^---\s*$/;
const BEAT_PATTERN = /\[(?:BEAT[^\]]*|(\d+(?:\.\d+)?)\s*s\s+silence[^\]]*)\]/i;
// matches `[BEAT — 0.6 s]`, `[BEAT — 0.6 s — held black]`, `[4 s silence — push-in]`, `[BEAT — silence 1.5 s — typography plate alone]`

function extractSilenceSeconds(line: string): number | null {
  const m = line.match(BEAT_PATTERN);
  if (!m) return null;
  // pull out a number followed by 's' from the matched bracket content
  const numMatch = m[0].match(/(\d+(?:\.\d+)?)\s*s/);
  if (!numMatch) return null;
  return parseFloat(numMatch[1]);
}

function cleanProseLine(line: string): string {
  // remove leading "> " blockquote
  let s = line.replace(/^>\s?/, "");
  // strip annotation tags **(verbatim)**, **(spoken; ...)**, **(comma-merge per ...)**, etc.
  s = s.replace(/\s*\*\*\([^)]*\)\*\*/g, "");
  // strip <!-- noqa: ... --> HTML comments
  s = s.replace(/<!--[\s\S]*?-->/g, "");
  // unwrap *"..."* italics (primary-source quotes — TTS reads flat anyway)
  s = s.replace(/\*"([^"]+)"\*/g, '"$1"');
  s = s.replace(/\*([^*]+)\*/g, "$1");
  // collapse whitespace
  s = s.replace(/\s+/g, " ").trim();
  return s;
}

interface Scene {
  num: number;
  header: string;
  prose: string[]; // sequential paragraphs of clean narration text
  silences: Array<{ afterParagraph: number; seconds: number }>;
  // silences[k].afterParagraph = N means "this silence comes after prose paragraph index N"
  // afterParagraph = -1 means "before the first paragraph" (e.g. opening "[4 s silence — push-in]")
}

function parseScript(text: string): Scene[] {
  const lines = text.split("\n");
  const scenes: Scene[] = [];
  let current: Scene | null = null;
  let inNarration = false;
  let pendingParagraph: string[] = [];

  function flushParagraph() {
    if (!current) return;
    const joined = pendingParagraph.join(" ").trim();
    if (joined) current.prose.push(joined);
    pendingParagraph = [];
  }

  for (const raw of lines) {
    const line = raw;
    const m = line.match(SCENE_HEADER);
    if (m) {
      // close previous scene
      if (current) flushParagraph();
      current = { num: parseInt(m[1], 10), header: line.trim(), prose: [], silences: [] };
      scenes.push(current);
      inNarration = false;
      pendingParagraph = [];
      continue;
    }
    if (!current) continue;
    if (NARRATION_MARK.test(line)) {
      inNarration = true;
      continue;
    }
    if (HORIZONTAL_RULE.test(line.trim())) {
      // scene divider — close out
      flushParagraph();
      inNarration = false;
      continue;
    }
    if (!inNarration) continue;

    // We're inside a Narration block. Lines start with "> " or are blank between paragraphs.
    const stripped = line.replace(/^>\s?/, "").trim();
    if (stripped === "") {
      // paragraph break inside the narration block
      flushParagraph();
      continue;
    }

    // Check for BEAT/silence marker
    if (BEAT_PATTERN.test(stripped)) {
      flushParagraph(); // close the current paragraph if any
      const seconds = extractSilenceSeconds(stripped) ?? 0;
      if (seconds > 0) {
        current.silences.push({ afterParagraph: current.prose.length - 1, seconds });
      }
      continue;
    }

    // Regular narration text (may need cleaning)
    const cleaned = cleanProseLine(line);
    if (cleaned) pendingParagraph.push(cleaned);
  }
  if (current) flushParagraph();

  return scenes;
}

function buildSceneText(scene: Scene): string {
  // Concatenate paragraphs with double-newline separation. Silences between paragraphs are
  // NOT embedded in the text (that's a manifest concern). Within a single TTS call,
  // paragraph breaks act as sentence/clause boundaries to Kokoro's segmenter.
  return scene.prose.join("\n\n").trim() + "\n";
}

function buildManifest(scenes: Scene[]): ManifestEntry[] {
  const entries: ManifestEntry[] = [];
  for (const scene of scenes) {
    const sceneFile = `scenes/scene-${String(scene.num).padStart(2, "0")}.wav`;

    // Pre-scene silences (afterParagraph === -1 — e.g. opening "[4 s silence — push-in]")
    const preSilences = scene.silences.filter((s) => s.afterParagraph === -1);
    for (const s of preSilences) entries.push({ silence: s.seconds });

    entries.push({ chunk: sceneFile });

    // Post-scene padding silence (the *next* scene's pre-silence covers transitions, but
    // we also model intra-scene silences here since we render the scene as ONE wav and
    // can't split mid-scene without a separate sub-manifest. We document them in the
    // scene_silences sidecar for future use; the main manifest just chains scene wavs.)
  }
  return entries;
}

// Build a sidecar with per-scene intra-paragraph silences (informational; will inform
// future mid-scene chunk splits if a scene needs surgical re-rendering).
function buildSidecar(scenes: Scene[]) {
  return scenes.map((s) => ({
    scene: s.num,
    header: s.header,
    paragraphs: s.prose,
    silences: s.silences,
  }));
}

// MAIN
const scriptText = readFileSync(scriptPath, "utf8");
const scenes = parseScript(scriptText);

mkdirSync(join(outDir, "scenes"), { recursive: true });

let totalChars = 0;
let totalParas = 0;
for (const scene of scenes) {
  const filename = join(outDir, "scenes", `scene-${String(scene.num).padStart(2, "0")}.txt`);
  const txt = buildSceneText(scene);
  writeFileSync(filename, txt);
  totalChars += txt.length;
  totalParas += scene.prose.length;
}

const manifest = buildManifest(scenes);
writeFileSync(join(outDir, "manifest.json"), JSON.stringify(manifest, null, 2) + "\n");

const sidecar = buildSidecar(scenes);
writeFileSync(join(outDir, "scenes-sidecar.json"), JSON.stringify(sidecar, null, 2) + "\n");

// Report
console.log(`✓ Parsed ${scenes.length} scenes from ${scriptPath}`);
console.log(`✓ Wrote ${scenes.length} scene .txt files → ${join(outDir, "scenes")}`);
console.log(`✓ manifest.json (${manifest.length} entries) → ${join(outDir, "manifest.json")}`);
console.log(`✓ scenes-sidecar.json (per-scene silence map) → ${join(outDir, "scenes-sidecar.json")}`);
console.log(`Total prose: ${totalParas} paragraphs, ${totalChars} chars across ${scenes.length} scenes`);
console.log("");
console.log("Per-scene summary:");
for (const s of scenes) {
  const sec = s.silences.reduce((a, b) => a + b.seconds, 0);
  console.log(`  scene-${String(s.num).padStart(2, "0")}: ${s.prose.length} paragraphs, ${s.silences.length} beats (${sec.toFixed(1)}s silence)`);
}
