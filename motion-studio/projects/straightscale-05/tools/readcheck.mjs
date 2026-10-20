// Reading-time check for this canvas page, same rule as Lemo-Opuscar core/render/readcheck.mjs (DIRECTOR.md §7):
// every text block must stay fully visible (all words in, not leaving, inside the frame) for at least
// max(1.5 s, non-space chars / 15 + 1.5 s), counted from the first frame it is fully visible.
//   node tools/readcheck.mjs [--page index.html?fmt=4x5] [--w 1080 --h 1920] [--step 0.04]
import { createRequire } from 'node:module';
const require = createRequire(new URL('../../../package.json', import.meta.url));
const { chromium } = require('playwright');
const raw = (k) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : undefined; };
const W = Number(raw('w') || 1080), H = Number(raw('h') || 1920), STEP = Number(raw('step') || 0.04);
const page0 = raw('page') || 'index.html';
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: W, height: H } });
page.on('pageerror', (e) => console.log('PAGEERROR', e.message));
await page.goto('file://' + process.cwd() + '/' + page0);
await page.waitForFunction(() => typeof window.seek === 'function');
const res = await page.evaluate(({ STEP, W, H }) => {
  const seen = {};
  for (let t = 0; t <= window.DURATION; t += STEP) {
    const vis = new Set();
    const groups = {};
    for (const b of window.TEXTS(t)) {   // lines that share an id are one block (e.g. a two-line question)
      const g = groups[b.id] ??= { id: b.id, text: '', full: true, x0: 1e9, y0: 1e9, x1: -1e9, y1: -1e9 };
      g.text += (g.text ? ' ' : '') + b.text; g.full = g.full && b.full;
      g.x0 = Math.min(g.x0, b.x0); g.y0 = Math.min(g.y0, b.y0); g.x1 = Math.max(g.x1, b.x1); g.y1 = Math.max(g.y1, b.y1);
    }
    for (const b of Object.values(groups)) {
      const key = b.id + '|' + b.text;
      const inside = b.x0 >= 0 && b.y0 >= 0 && b.x1 <= W && b.y1 <= H;
      if (!b.full || !inside) continue;
      vis.add(key);
      const s = seen[key] ??= { id: b.id, text: b.text, t0: t, run: 0, done: false };
      if (!s.done) s.run = t - s.t0 + STEP;
    }
    for (const k in seen) if (!vis.has(k)) seen[k].done = true;
  }
  return Object.values(seen);
}, { STEP, W, H });
await browser.close();
let bad = 0;
for (const s of res) {
  const n = Math.max(1.5, [...s.text].filter((c) => !/\s/.test(c)).length / 15 + 1.5), ok = s.run >= n - 1e-6;
  if (!ok) bad++;
  console.log(`${ok ? 'OK ' : 'BAD'} ${s.id.padEnd(12)} full at ${s.t0.toFixed(2)} s  need ${n.toFixed(2)} s  got ${s.run.toFixed(2)} s  "${s.text}"`);
}
if (!res.length) { console.log('NOT CHECKED: no text reported'); process.exit(2); }
process.exitCode = bad ? 1 : 0;
