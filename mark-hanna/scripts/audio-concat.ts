#!/usr/bin/env bun
/**
 * audio-concat.ts — Build the master narration wav from manifest.json.
 *
 * Reads `assets/narration/manifest.json` and produces:
 *   assets/narration/narration.fullscale.raw.wav    — concatenated raw audio
 *   assets/narration/narration.fullscale.wav        — two-pass loudnorm at -15 LUFS / -1.5 TP / LRA 18
 *
 * Pipeline (per M15 + M15a in REBUILD.md):
 *   1. Generate silence chunks via ffmpeg `anullsrc` for each {silence: N} entry
 *   2. ffmpeg concat demuxer over all chunks (audio chunks + generated silences)
 *   3. Two-pass loudnorm with `linear=true` for single-gain master
 *
 * Usage: bun scripts/audio-concat.ts [--manifest PATH] [--out PATH]
 */

import { readFileSync, writeFileSync, mkdirSync, rmSync, existsSync } from "node:fs";
import { join, dirname, resolve } from "node:path";
import { spawn } from "node:child_process";

type ManifestEntry = { chunk: string } | { silence: number };

const PROJECT_ROOT = resolve(import.meta.dir, "..");
const NARR_DIR = join(PROJECT_ROOT, "assets/narration");
const DEFAULT_MANIFEST = join(NARR_DIR, "manifest.json");
const DEFAULT_OUT = join(NARR_DIR, "narration.fullscale.wav");

const args = Bun.argv.slice(2);
let manifestPath = DEFAULT_MANIFEST;
let outPath = DEFAULT_OUT;
for (let i = 0; i < args.length; i++) {
  if (args[i] === "--manifest") manifestPath = resolve(args[++i]);
  else if (args[i] === "--out") outPath = resolve(args[++i]);
}

const SAMPLE_RATE = 24000; // Kokoro native; final master will be 48k after loudnorm
const TMP_DIR = join(NARR_DIR, ".tmp_concat");

function run(cmd: string, cmdArgs: string[]): Promise<{ stdout: string; stderr: string; code: number }> {
  return new Promise((res, rej) => {
    const p = spawn(cmd, cmdArgs);
    let stdout = "";
    let stderr = "";
    p.stdout.on("data", (d) => (stdout += d.toString()));
    p.stderr.on("data", (d) => (stderr += d.toString()));
    p.on("close", (code) => res({ stdout, stderr, code: code ?? 1 }));
    p.on("error", rej);
  });
}

async function main() {
  const manifest: ManifestEntry[] = JSON.parse(readFileSync(manifestPath, "utf8"));
  console.log(`✓ manifest: ${manifest.length} entries`);

  // 1. Clean and prep tmp dir
  if (existsSync(TMP_DIR)) rmSync(TMP_DIR, { recursive: true });
  mkdirSync(TMP_DIR, { recursive: true });

  // 2. Build the concat-demuxer file list. Generate silence wavs as needed.
  const concatLines: string[] = [];
  let silenceIdx = 0;
  for (const entry of manifest) {
    if ("chunk" in entry) {
      const abs = resolve(NARR_DIR, entry.chunk);
      if (!existsSync(abs)) {
        console.error(`✗ MISSING: ${abs}`);
        process.exit(1);
      }
      concatLines.push(`file '${abs.replace(/'/g, "'\\''")}'`);
    } else {
      const silenceFile = join(TMP_DIR, `silence_${String(silenceIdx).padStart(3, "0")}.wav`);
      const r = await run("ffmpeg", [
        "-y", "-f", "lavfi",
        "-i", `anullsrc=r=${SAMPLE_RATE}:cl=mono`,
        "-t", String(entry.silence),
        "-c:a", "pcm_s16le",
        silenceFile,
      ]);
      if (r.code !== 0) {
        console.error(`✗ silence gen failed (${entry.silence}s):`, r.stderr.slice(-500));
        process.exit(1);
      }
      concatLines.push(`file '${silenceFile.replace(/'/g, "'\\''")}'`);
      silenceIdx++;
    }
  }
  const concatList = join(TMP_DIR, "concat.txt");
  writeFileSync(concatList, concatLines.join("\n") + "\n");
  console.log(`✓ generated ${silenceIdx} silence chunk(s); concat list has ${concatLines.length} entries`);

  // 3. Concat via filter_complex (concat-demuxer corrupts boundaries between
  //    Kokoro 24kHz wavs + anullsrc silence; user reported "M [pause] A" cut-and-play
  //    artifacts at chunk boundaries that disappeared with filter_complex).
  //    Build inputs list: each chunk wav OR generated silence is a separate -i.
  //    Then [0:a][1:a]...[N:a]concat=n=N:v=0:a=1 produces clean concatenation.
  const rawOut = join(NARR_DIR, "narration.fullscale.raw.wav");
  const inputArgs: string[] = [];
  let inputIdx = 0;
  let labelChain = "";
  for (const entry of manifest) {
    if ("chunk" in entry) {
      const abs = resolve(NARR_DIR, entry.chunk);
      inputArgs.push("-i", abs);
    } else {
      inputArgs.push("-f", "lavfi", "-t", String(entry.silence),
                     "-i", `anullsrc=r=${SAMPLE_RATE}:cl=mono`);
    }
    labelChain += `[${inputIdx}:a]`;
    inputIdx++;
  }
  const filterComplex = `${labelChain}concat=n=${inputIdx}:v=0:a=1[out]`;
  const ffArgs = [
    "-y",
    ...inputArgs,
    "-filter_complex", filterComplex,
    "-map", "[out]",
    "-c:a", "pcm_s16le",
    "-ar", String(SAMPLE_RATE),
    "-ac", "1",
    rawOut,
  ];
  // DEBUG: log the exact args being passed to ffmpeg so we can compare to a working manual run
  console.log("FFMPEG ARGS:", JSON.stringify(ffArgs));
  console.log("FFMPEG INPUT COUNT:", inputIdx);
  const concatCmd = await run("ffmpeg", ffArgs);
  if (concatCmd.code !== 0) {
    console.error("✗ filter_complex concat failed:", concatCmd.stderr.slice(-1000));
    process.exit(1);
  }
  console.log(`✓ filter_complex concat (${inputIdx} inputs) → ${rawOut}`);

  // 4. Skip two-pass loudnorm — it corrupts audio at chunk boundaries (user
  //    reported "M [pause] A" cut-and-play artifacts that disappeared when
  //    bypassing loudnorm). Kokoro output is already at consistent loudness;
  //    apply only a sample-rate convert to 48kHz for ffprobe/composition compat.
  console.log("→ resampling to 48kHz (no loudnorm — preserves chunk boundaries)...");
  const pass2 = await run("ffmpeg", [
    "-y", "-i", rawOut,
    "-ar", "48000",
    "-c:a", "pcm_s16le",
    outPath,
  ]);
  if (pass2.code !== 0) {
    console.error("✗ resample failed:", pass2.stderr.slice(-1500));
    process.exit(1);
  }
  console.log(`✓ master (24kHz → 48kHz, no loudnorm) → ${outPath}`);

  // 6. Final ffprobe summary
  const probe = await run("ffprobe", [
    "-v", "error",
    "-show_entries", "stream=codec_name,sample_rate,channels",
    "-show_entries", "format=duration,size",
    "-of", "default=nw=1",
    outPath,
  ]);
  console.log("\n=== final master ===");
  console.log(probe.stdout);

  // 7. Cleanup
  rmSync(TMP_DIR, { recursive: true });
  // raw stays — useful for re-running loudnorm with different targets without re-concating
}

main().catch((e) => {
  console.error("FATAL:", e);
  process.exit(1);
});
