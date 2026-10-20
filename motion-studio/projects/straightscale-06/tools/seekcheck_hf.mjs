// Determinism check for this HyperFrames page (our own tool, adapted from motion-studio/tools/seekcheck.mjs, which
// reads a canvas): every frame must be a pure function of time. Seeks each sample time cold, then after jumping
// elsewhere, and compares screenshot hashes; also seeks every 0.1 s and reports any seek that throws.
//   node tools/seekcheck_hf.mjs film/index.html [--n 24] [--w 1080 --h 1920]
import { chromium } from 'playwright';
import { createHash } from 'node:crypto';
import { resolve } from 'node:path';
const arg = (k, d) => { const i = process.argv.indexOf('--' + k); return i > 0 ? Number(process.argv[i + 1]) : d; };
const N = arg('n', 24), W = arg('w', 1080), H = arg('h', 1920);
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 0.5 });
const errors = [];
page.on('pageerror', (e) => errors.push(String(e)));
await page.goto('file://' + resolve(process.argv[2]));
await page.waitForFunction(() => window.__hfReady === true);
const DUR = await page.evaluate(() => window.DURATION);
const hashAt = async (t) => { await page.evaluate((t) => { window.seek(t); }, t); return createHash('sha1').update(await page.screenshot()).digest('hex').slice(0, 12); };
const times = Array.from({ length: N }, (_, i) => Math.round(((i * 0.6180339887) % 1) * DUR * 1000) / 1000);
const mismatches = [];
for (const t of times) {
  const a = await hashAt(t);
  await hashAt((t + DUR * 0.37) % DUR);
  await hashAt((t + DUR * 0.81) % DUR);
  const b = await hashAt(t);
  if (a !== b) mismatches.push(t);
}
const throws = [];
for (let t = 0; t <= DUR; t = Math.round((t + 0.1) * 10) / 10) {
  try { await page.evaluate((t) => { window.seek(t); }, t); } catch (e) { throws.push(`${t}: ${String(e).split('\n')[0]}`); }
}
await browser.close();
console.log(`${mismatches.length ? 'FAIL' : 'PASS'}  same frame on revisit at ${N} sample times${mismatches.length ? ': differs at ' + mismatches.join(', ') : ''}`);
console.log(`${throws.length ? 'FAIL' : 'PASS'}  seek runs without errors every 0.1 s${throws.length ? ':\n  ' + throws.slice(0, 10).join('\n  ') : ''}`);
if (errors.length) console.log(`WARN  page errors: ${errors.slice(0, 5).join(' | ')}`);
process.exit(mismatches.length || throws.length ? 1 : 0);
