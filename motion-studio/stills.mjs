// Contact sheet straight from index.html, no full render needed.
// node stills.mjs --from 0.25 --step 0.5 --dur 15 [--cols 8] [--scale 0.25] [--w 1080 --h 1920] [--out out/beats.png]
// node stills.mjs --at 1.2,3.4,7 --scale 0.5 --out out/moments.png
import { chromium } from 'playwright';
import { spawnSync } from 'node:child_process';
import { mkdirSync, rmSync } from 'node:fs';

const raw = (k) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : undefined; };
const num = (k, d) => (raw(k) !== undefined ? Number(raw(k)) : d);
const W = num('w', 1080), H = num('h', 1920), SCALE = num('scale', 0.25), COLS = num('cols', 8);
const OUT = raw('out') || 'out/beats.png';

let times;
if (raw('at')) times = raw('at').split(',').map(Number);
else {
  const from = num('from', 0.25), step = num('step', 0.5), dur = num('dur', 15);
  times = [];
  for (let t = from; t < dur; t += step) times.push(Math.round(t * 1000) / 1000);
}

const dir = 'out/stills';
rmSync(dir, { recursive: true, force: true });
mkdirSync(dir, { recursive: true });

const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
// --page index.html?lang=en renders a variant of the same page (default index.html)
await page.goto('file://' + process.cwd() + '/' + (process.argv.includes('--page') ? process.argv[process.argv.indexOf('--page') + 1] : 'index.html'));
await page.waitForFunction(() => typeof window.seek === 'function');
await page.evaluate(() => document.fonts.ready);
for (const [i, t] of times.entries()) {
  await page.evaluate((t) => window.seek(t), t);
  await page.locator('#c').screenshot({ path: `${dir}/${String(i).padStart(4, '0')}.png` });
}
await browser.close();

const rows = Math.ceil(times.length / COLS);
const cols = Math.min(COLS, times.length);
const r = spawnSync('ffmpeg', ['-loglevel', 'error', '-y', '-i', `${dir}/%04d.png`,
  '-vf', `scale=${Math.round(W * SCALE)}:-1,pad=iw+6:ih+6:3:3:white,tile=${cols}x${rows}`, '-frames:v', '1', OUT], { stdio: 'inherit' });
if (r.status !== 0) process.exit(r.status);
console.log(`${OUT}: ${times.length} frames at t = ${times.join(', ')}`);
