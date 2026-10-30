// Reading-time and safe-zone check for this HyperFrames page (our own tool; same reading rule as Lemo-Opuscar's
// readcheck, DIRECTOR.md section 7: every text block stays fully visible for max(1.5 s, non-space chars / 15 + 1.5 s)).
//   node tools/textcheck.mjs film/index.html [--w 1080 --h 1920] [--step 0.04]
// Safe zones on 9:16 (Instagram Reels UI): no text or logo in the top 14 %, the bottom 20 % or the right 140 px.
// On 4:5 (feed): everything inside a 60 px margin. Also reports the smallest font size of reading text.
import { chromium } from 'playwright';
import { resolve } from 'node:path';
const arg = (k, d) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : d; };
const W = Number(arg('w', 1080)), H = Number(arg('h', 1920)), STEP = Number(arg('step', 0.04));
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: W, height: H } });
page.on('pageerror', (e) => console.log('PAGEERROR', e.message));
await page.goto('file://' + resolve(process.argv[2]));
await page.waitForFunction(() => window.__hfReady === true);
const res = await page.evaluate(({ STEP, W, H }) => {
  const seen = {}, zone = [], small = {};
  const tall = H / W > 1.5;
  const Z = tall ? { x0: 0, y0: 0.14 * H, x1: W - 140, y1: 0.8 * H } : { x0: 60, y0: 60, x1: W - 60, y1: H - 60 };
  for (let t = 0; t <= window.DURATION - 1e-3; t += STEP) {
    const vis = new Set();
    for (const b of window.TEXTS(t)) {
      const key = b.id + '|' + b.text; vis.add(key);
      const s = seen[key] ??= { id: b.id, text: b.text, t0: t, run: 0, done: false };
      if (!s.done) s.run = t - s.t0 + STEP;
    }
    for (const k in seen) if (!vis.has(k)) seen[k].done = true;
    for (const b of window.BOXES(t)) {
      const out = b.x0 < Z.x0 - 0.5 || b.y0 < Z.y0 - 0.5 || b.x1 > Z.x1 + 0.5 || b.y1 > Z.y1 + 0.5;
      if (out) zone.push({ t: Math.round(t * 100) / 100, id: b.id, text: b.text.slice(0, 30), box: [b.x0, b.y0, b.x1, b.y1].map(Math.round) });
      if (b.fs && !['axis', 'day', 'label', 'flyer'].includes(b.id)) small[b.id] = Math.min(small[b.id] ?? 999, b.fs);
    }
  }
  return { seen: Object.values(seen), zone, small, Z };
}, { STEP, W, H });
await browser.close();
let bad = 0;
for (const s of res.seen) {
  const need = Math.max(1.5, [...s.text].filter((c) => !/\s/.test(c)).length / 15 + 1.5), ok = s.run >= need - 1e-6;
  if (!ok) bad++;
  console.log(`${ok ? 'OK ' : 'BAD'} read ${s.id.padEnd(8)} from ${s.t0.toFixed(2)} s  need ${need.toFixed(2)} s  got ${s.run.toFixed(2)} s  "${s.text}"`);
}
const zk = {}; for (const z of res.zone) { const k = z.id + '|' + z.text; (zk[k] ??= []).push(z.t); }
for (const k in zk) console.log(`BAD zone ${k}  at ${zk[k].length} samples, first ${zk[k][0]} s, last ${zk[k].at(-1)} s  e.g. ${JSON.stringify(res.zone.find((z) => z.id + '|' + z.text === k).box)}`);
console.log(`zone ${JSON.stringify(res.Z)}: ${res.zone.length ? 'FAIL' : 'PASS'} (${res.zone.length} box-samples outside)`);
console.log('smallest font per block (px):', JSON.stringify(res.small));
process.exitCode = bad || res.zone.length ? 1 : 0;
