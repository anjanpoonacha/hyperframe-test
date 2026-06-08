#!/usr/bin/env bun
/**
 * extract-v4-narration.ts — split FULL_SCRIPT.v4.md into per-section .txt files for TTS.
 *
 * Reads `research/script/FULL_SCRIPT.v4.md`, walks `## SectionTitle [00:00–00:00]` headers,
 * strips HTML comments, italics, noqa tags, and writes one .txt per section under
 * `assets/narration/v4/sections/`.
 */

import { readFileSync, writeFileSync, mkdirSync, rmSync, existsSync } from "node:fs";
import { join, resolve } from "node:path";

const PROJECT_ROOT = resolve(import.meta.dir, "..");
const SCRIPT = join(PROJECT_ROOT, "research/script/FULL_SCRIPT.v4.md");
const OUT = join(PROJECT_ROOT, "assets/narration/v4");

if (existsSync(OUT)) rmSync(OUT, { recursive: true });
mkdirSync(join(OUT, "sections"), { recursive: true });

const text = readFileSync(SCRIPT, "utf8");
const lines = text.split("\n");

interface Section {
  num: number;
  slug: string;
  header: string;
  prose: string[];
}

const sections: Section[] = [];
let current: Section | null = null;
let inFrontmatter = false;
let inProse = false;
let n = 0;

const SECTION_HEADER = /^##\s+([^\[]+?)(?:\s+\[[^\]]+\])?\s*$/;
const FRONTMATTER = /^---\s*$/;

for (const raw of lines) {
  if (FRONTMATTER.test(raw)) {
    inFrontmatter = !inFrontmatter;
    continue;
  }
  if (inFrontmatter) continue;
  if (raw.startsWith("# ")) continue; // top-level title

  const m = raw.match(SECTION_HEADER);
  if (m) {
    n++;
    const title = m[1].trim();
    const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
    current = { num: n, slug, header: title, prose: [] };
    sections.push(current);
    inProse = true;
    continue;
  }

  if (!inProse || !current) continue;
  // Skip HTML comments (composition tags, noqa)
  let line = raw.replace(/<!--[\s\S]*?-->/g, "");
  // Strip italic/bold markers but keep text
  line = line.replace(/\*\*([^*]+)\*\*/g, "$1");
  line = line.replace(/\*([^*]+)\*/g, "$1");
  // Strip leading/trailing whitespace
  line = line.trim();
  // Skip ellipsis-only beat lines (they're directorial silence cues)
  if (line === "..." || line === "…") {
    current.prose.push(""); // create paragraph break
    continue;
  }
  if (line === "") {
    current.prose.push("");
    continue;
  }
  current.prose.push(line);
}

// Collapse consecutive empty paragraphs and write
function buildText(s: Section): string {
  // join lines with newlines, then collapse multiple blanks to single blank
  const joined = s.prose.join("\n");
  return joined.replace(/\n{3,}/g, "\n\n").trim() + "\n";
}

let totalWords = 0;
const manifest: Array<{ section: string; file: string; words: number }> = [];
for (const s of sections) {
  const txt = buildText(s);
  if (!txt.trim()) continue; // skip Title Card (no narration) and outro tag
  const fname = `${String(s.num).padStart(2, "0")}-${s.slug}.txt`;
  writeFileSync(join(OUT, "sections", fname), txt);
  const words = txt.split(/\s+/).filter(Boolean).length;
  totalWords += words;
  manifest.push({ section: s.header, file: fname, words });
}

writeFileSync(join(OUT, "sections-manifest.json"), JSON.stringify(manifest, null, 2) + "\n");

console.log(`✓ ${sections.length} sections parsed, ${manifest.length} with narration`);
console.log(`✓ Total spoken words: ${totalWords}`);
console.log(`✓ Output: ${OUT}/sections/`);
console.log("");
console.log("Per-section word counts:");
for (const m of manifest) {
  console.log(`  ${m.file.padEnd(38)} ${m.words.toString().padStart(5)} words`);
}
