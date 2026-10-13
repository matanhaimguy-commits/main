// Safe-zone and size check for canvas-engine pages whose text helper pushes boxes into window.__boxes
// ({x, y, w, h, text}, y = top of the cap height, h = font size).
// node tools/safezone.mjs <project dir> [--dur 41] [--step 0.1] [--top 250 --bottom 400 --right 140 --left 96 --min 44]
import { chromium } from 'playwright';
const dir = process.argv[2];
const raw = (k) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : undefined; };
const num = (k, d) => (raw(k) !== undefined ? Number(raw(k)) : d);
const W = 1080, H = 1920, TOP = num('top', 250), BOT = H - num('bottom', 400), RIGHT = W - num('right', 140), LEFT = num('left', 96), MIN = num('min', 44);
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: W, height: H } });
page.on('pageerror', (e) => console.log('PAGEERROR', e.message));
await page.goto('file://' + dir + '/index.html');
await page.waitForFunction(() => typeof window.seek === 'function');
const dur = num('dur', await page.evaluate(() => window.DURATION || 15)), step = num('step', 0.1);
const issues = new Map();
for (let t = 0; t < dur; t += step) {
  const boxes = await page.evaluate((t) => { window.__boxes = []; window.seek(t); const b = window.__boxes; window.__boxes = null; return b; }, t);
  for (const b of boxes) {
    const bottom = b.y + b.h * 1.05, why = [];
    if (b.x < LEFT - 1) why.push(`left ${Math.round(b.x)}`);
    if (b.x + b.w > RIGHT) why.push(`right edge ${Math.round(b.x + b.w)} > ${RIGHT}`);
    if (b.y < TOP) why.push(`top ${Math.round(b.y)} < ${TOP}`);
    if (bottom > BOT) why.push(`bottom ${Math.round(bottom)} > ${BOT}`);
    if (b.h < MIN) why.push(`size ${b.h} < ${MIN}`);
    if (why.length) { const k = b.text + ' | ' + why.join(', '); if (!issues.has(k)) issues.set(k, t.toFixed(1)); }
  }
}
await browser.close();
if (!issues.size) console.log('safe zones: ok');
for (const [k, t] of issues) console.log(`t=${t}  ${k}`);
process.exitCode = issues.size ? 1 : 0;
