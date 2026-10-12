// Fast preview loop (SKILL §2b): contact sheet of a time range.
//   node scripts/preview.mjs <from> <to> [--fps 8] [--scale 0.25] [--cols 6] [--mp4]
// → renders/previews/sheet_<from>-<to>.jpg (every frame, timestamped)
// → with --mp4: renders/previews/clip_<from>-<to>.mp4 (low-res, with audio mix if cache/mix.wav exists)
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const a = process.argv.slice(2);
const from = parseFloat(a[0] ?? 0), to = parseFloat(a[1] ?? 5);
const opt = (k, d) => { const i = a.indexOf(k); return i >= 0 ? a[i + 1] : d; };
const fps = opt("--fps", "8"), scale = opt("--scale", "0.25"), cols = parseInt(opt("--cols", "6"));
const tag = `${from}-${to}`;
const run = (cmd, args) => execFileSync(cmd, args, { cwd: ROOT, stdio: "inherit" });

if (a.includes("--mp4")) {
  const audio = fs.existsSync(path.join(ROOT, "cache/mix.wav")) ? ["--audio", "cache/mix.wav"] : [];
  run("node", ["src/render.js", "--from", String(from), "--to", String(to), "--fps", "15", "--scale", "0.5", "--out", "renders/previews", "--name", `clip_${tag}`, ...audio]);
} else {
  const dir = path.join(ROOT, "cache/preview_frames", tag);
  fs.rmSync(dir, { recursive: true, force: true });
  run("node", ["src/render.js", "--from", String(from), "--to", String(to), "--fps", fps, "--scale", scale, "--out", "cache/preview_frames", "--name", tag, "--frames-only", "--stamp"]);
  const files = fs.readdirSync(dir).filter((f) => f.endsWith(".jpg")).sort();
  const rows = Math.ceil(files.length / cols);
  fs.mkdirSync(path.join(ROOT, "renders/previews"), { recursive: true });
  run("ffmpeg", ["-y", "-loglevel", "error", "-framerate", "1", "-pattern_type", "glob", "-i", path.join(dir, "f_*.jpg"),
    "-vf", `tile=${cols}x${rows}:padding=6:color=0x333333`, "-frames:v", "1", "-q:v", "3", path.join(ROOT, `renders/previews/sheet_${tag}.jpg`)]);
  console.log(`sheet: renders/previews/sheet_${tag}.jpg (${files.length} frames)`);
}
