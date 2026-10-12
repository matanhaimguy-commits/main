// node render.mjs --fps 60 --dur 15 --sub 4 [--from 0] [--w 1080 --h 1920] [--out out/silent.mp4]
// --from renders a segment starting at that time, e.g. to re-render one shot or split a long film across processes.
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { mkdirSync } from 'node:fs';

const raw = (k) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : undefined; };
const arg = (k, d) => (raw(k) !== undefined ? Number(raw(k)) : d);
const FPS = arg('fps', 60), DUR = arg('dur', 15), SUB = arg('sub', 4), FROM = arg('from', 0);
const W = arg('w', 1080), H = arg('h', 1920);
const OUT = raw('out') || 'out/silent.mp4';
mkdirSync('out', { recursive: true });

// file:// pages may import lib/motion.js as an ES module; Chromium blocks that without this flag
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
await page.goto('file://' + process.cwd() + '/index.html');
await page.waitForFunction(() => typeof window.seek === 'function');
await page.evaluate(() => document.fonts.ready);

// A <canvas id="c"> lets the page average its own subframes and hand back one PNG per frame,
// which is several times faster than screenshotting every subframe.
const inPage = await page.evaluate(() => document.getElementById('c') instanceof HTMLCanvasElement);
if (inPage) {
  await page.evaluate(() => {
    const c = document.getElementById('c');
    const out = document.createElement('canvas'); out.width = c.width; out.height = c.height;
    const ox = out.getContext('2d');
    window.__frame = (times) => {
      const x = c.getContext('2d');
      let acc = null;
      for (const t of times) {
        window.seek(t);
        const d = x.getImageData(0, 0, c.width, c.height).data;
        if (!acc) acc = new Float32Array(d.length);
        for (let i = 0; i < d.length; i++) acc[i] += d[i];
      }
      const img = ox.createImageData(c.width, c.height), n = times.length;
      for (let i = 0; i < acc.length; i++) img.data[i] = acc[i] / n + 0.5;
      ox.putImageData(img, 0, 0);
      return out.toDataURL('image/png');
    };
  });
}

const ff = spawn('ffmpeg', ['-loglevel', 'error', '-y', '-f', 'image2pipe', '-framerate', String(inPage ? FPS : FPS * SUB), '-i', '-',
  ...(inPage ? [] : ['-vf', `tmix=frames=${SUB},select='eq(mod(n\\,${SUB})\\,${SUB - 1})',setpts=N/${FPS}/TB`]),
  '-r', String(FPS), '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', OUT],
  { stdio: ['pipe', 'inherit', 'inherit'] });
const write = async (buf) => { if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once('drain', r)); };

const f0 = Math.round(FROM * FPS), f1 = f0 + Math.round(DUR * FPS);
for (let f = f0; f < f1; f++) {
  const times = Array.from({ length: SUB }, (_, j) => (f * SUB + j) / (FPS * SUB));
  if (inPage) {
    const url = await page.evaluate((ts) => window.__frame(ts), times);
    await write(Buffer.from(url.slice(url.indexOf(',') + 1), 'base64'));
  } else {
    for (const t of times) {
      await page.evaluate((t) => window.seek(t), t);
      await write(await page.locator('#c').screenshot({ type: 'png' }));
    }
  }
  if (f % FPS === 0) console.log(`rendered ${f / FPS}s (${FROM}s to ${FROM + DUR}s)`);
}
ff.stdin.end();
await new Promise((r) => ff.on('close', r));
await browser.close();
