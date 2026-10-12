// Deterministic frame renderer (render CLI contract, SKILL §2).
//   node src/render.js --from 0 --to 50 --fps 30 --scale 1 --out renders/final [--jpg]
//        [--name reel_v1] [--audio cache/mix.wav] [--frames-only] [--stamp]
// Every frame depends only on t: page.drawFrame(t) paints the canvas, we grab it
// and pipe it into ffmpeg. Preview frames are identical to final frames, just smaller.
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

function args() {
  const a = process.argv.slice(2);
  const o = { from: 0, to: null, fps: 30, scale: 1, out: "renders/final", jpg: false, name: null, audio: null, framesOnly: false, stamp: false };
  for (let i = 0; i < a.length; i++) {
    const k = a[i];
    if (k === "--from") o.from = parseFloat(a[++i]);
    else if (k === "--to") o.to = parseFloat(a[++i]);
    else if (k === "--fps") o.fps = parseFloat(a[++i]);
    else if (k === "--scale") o.scale = parseFloat(a[++i]);
    else if (k === "--out") o.out = a[++i];
    else if (k === "--name") o.name = a[++i];
    else if (k === "--audio") o.audio = a[++i];
    else if (k === "--jpg") o.jpg = true;
    else if (k === "--frames-only") o.framesOnly = true;
    else if (k === "--stamp") o.stamp = true;
  }
  return o;
}

const MIME = { ".html": "text/html", ".js": "text/javascript", ".mjs": "text/javascript", ".json": "application/json", ".woff2": "font/woff2", ".png": "image/png", ".jpg": "image/jpeg", ".svg": "image/svg+xml" };
function serve() {
  return new Promise((resolve) => {
    const srv = http.createServer((req, res) => {
      const p = path.join(ROOT, decodeURIComponent(new URL(req.url, "http://x").pathname));
      if (!p.startsWith(ROOT) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { res.writeHead(404); return res.end(); }
      res.writeHead(200, { "Content-Type": MIME[path.extname(p)] || "application/octet-stream" });
      fs.createReadStream(p).pipe(res);
    });
    srv.listen(0, "127.0.0.1", () => resolve(srv));
  });
}

async function main() {
  const o = args();
  const srv = await serve();
  const port = srv.address().port;
  const W = Math.round(1080 * o.scale), H = Math.round(1920 * o.scale);
  const browser = await chromium.launch({ args: ["--force-color-profile=srgb", "--font-render-hinting=none"] });
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  page.on("pageerror", (e) => console.error("PAGE ERROR:", e.message));
  page.on("console", (m) => { if (m.type() === "error") console.error("console:", m.text()); });
  await page.goto(`http://127.0.0.1:${port}/src/index.html?scale=${o.scale}&stamp=${o.stamp ? 1 : 0}`);
  await page.waitForFunction(() => window.__ready === true, null, { timeout: 60000 });
  const duration = await page.evaluate(() => window.DURATION);
  const to = o.to == null ? duration : Math.min(o.to, duration);
  const n = Math.max(1, Math.round((to - o.from) * o.fps));
  fs.mkdirSync(path.join(ROOT, o.out), { recursive: true });
  const name = o.name || `render_${o.from}-${to}`;
  const t0 = Date.now();

  let ff = null, framesDir = null;
  if (o.framesOnly) {
    framesDir = path.join(ROOT, o.out, name);
    fs.mkdirSync(framesDir, { recursive: true });
  } else {
    const outFile = path.join(ROOT, o.out, `${name}${o.audio ? "_noaudio" : ""}.mp4`);
    ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(o.fps), "-i", "-",
      "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", outFile], { stdio: ["pipe", "inherit", "inherit"] });
  }

  for (let i = 0; i < n; i++) {
    const t = o.from + i / o.fps;
    const b64 = await page.evaluate(([t, jpg]) => { window.drawFrame(t); return window.__canvas.toDataURL(jpg ? "image/jpeg" : "image/png", 0.92).split(",")[1]; }, [t, o.jpg || !!framesDir]);
    const buf = Buffer.from(b64, "base64");
    if (framesDir) fs.writeFileSync(path.join(framesDir, `f_${String(i).padStart(5, "0")}_${t.toFixed(2)}.jpg`), buf);
    else if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once("drain", r));
    if (i % 60 === 0) process.stdout.write(`frame ${i}/${n} t=${t.toFixed(2)}s\n`);
  }
  if (ff) {
    ff.stdin.end();
    await new Promise((r) => ff.on("close", r));
    if (o.audio) {
      const v = path.join(ROOT, o.out, `${name}_noaudio.mp4`), f = path.join(ROOT, o.out, `${name}.mp4`);
      await new Promise((r, j) => {
        const m = spawn("ffmpeg", ["-y", "-loglevel", "error", "-i", v, "-ss", String(o.from), "-t", String(to - o.from), "-i", path.join(ROOT, o.audio),
          "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", "-movflags", "+faststart", f], { stdio: "inherit" });
        m.on("close", (c) => (c === 0 ? r() : j(new Error("mux failed"))));
      });
      fs.unlinkSync(v);
    }
  }
  console.log(`done: ${n} frames in ${((Date.now() - t0) / 1000).toFixed(1)} s → ${o.out}/${name}${framesDir ? "/" : ".mp4"}`);
  await browser.close();
  srv.close();
}
main().catch((e) => { console.error(e); process.exit(1); });
