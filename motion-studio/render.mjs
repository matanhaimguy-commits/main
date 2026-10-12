// node render.mjs --fps 60 --dur 15 --sub 4 [--w 1080 --h 1920]
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { mkdirSync } from 'node:fs';

const arg = (k, d) => { const i = process.argv.indexOf('--' + k); return i > 0 ? Number(process.argv[i + 1]) : d; };
const FPS = arg('fps', 60), DUR = arg('dur', 15), SUB = arg('sub', 4);
const W = arg('w', 1080), H = arg('h', 1920);
mkdirSync('out', { recursive: true });

// file:// pages may import lib/motion.js as an ES module; Chromium blocks that without this flag
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
await page.goto('file://' + process.cwd() + '/index.html');
await page.waitForFunction(() => typeof window.seek === 'function');
await page.evaluate(() => document.fonts.ready);

const vf = `tmix=frames=${SUB},select='eq(mod(n\\,${SUB})\\,${SUB - 1})',setpts=N/${FPS}/TB`;
const ff = spawn('ffmpeg', ['-y', '-f', 'image2pipe', '-framerate', String(FPS * SUB), '-i', '-',
  '-vf', vf, '-r', String(FPS), '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', 'out/silent.mp4'],
  { stdio: ['pipe', 'inherit', 'inherit'] });

const total = Math.round(DUR * FPS * SUB);
for (let i = 0; i < total; i++) {
  await page.evaluate((t) => window.seek(t), i / (FPS * SUB));
  const png = await page.locator('#c').screenshot({ type: 'png' });
  if (!ff.stdin.write(png)) await new Promise((r) => ff.stdin.once('drain', r));
  if (i % (FPS * SUB) === 0) console.log(`rendered ${i / (FPS * SUB)}s / ${DUR}s`);
}
ff.stdin.end();
await new Promise((r) => ff.on('close', r));
await browser.close();
