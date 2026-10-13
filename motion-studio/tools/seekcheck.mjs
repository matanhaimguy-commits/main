// Determinism check for a seek(t) page (our own tool): every frame must be a pure function of time.
//   node tools/seekcheck.mjs [--dur 50] [--n 24] [--w 1080 --h 1920]     (run from the project folder)
// Seeks each sample time cold, then after jumping elsewhere, and compares pixel hashes.
// Also seeks every 0.1 s across the film and reports any time where seek throws.
import { chromium } from 'playwright';
import { createHash } from 'node:crypto';

const raw = (k) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : undefined; };
const num = (k, d) => (raw(k) !== undefined ? Number(raw(k)) : d);
const DUR = num('dur', 15), N = num('n', 24), W = num('w', 1080), H = num('h', 1920);

const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
const errors = [];
page.on('pageerror', (e) => errors.push(String(e)));
// --page index.html?lang=en renders a variant of the same page (default index.html)
await page.goto('file://' + process.cwd() + '/' + (process.argv.includes('--page') ? process.argv[process.argv.indexOf('--page') + 1] : 'index.html'));
await page.waitForFunction(() => typeof window.seek === 'function');
await page.evaluate(() => document.fonts.ready);

const hashAt = async (t) => {
  const url = await page.evaluate((t) => { window.seek(t); return document.getElementById('c').toDataURL('image/png'); }, t);
  return createHash('sha1').update(url).digest('hex').slice(0, 12);
};

// golden-ratio stepping gives well spread, repeatable sample times
const times = Array.from({ length: N }, (_, i) => Math.round(((i * 0.6180339887) % 1) * DUR * 1000) / 1000);
const mismatches = [];
for (const t of times) {
  const a = await hashAt(t);
  await hashAt((t + DUR * 0.37) % DUR);        // jump somewhere else
  const b = await hashAt(t);
  if (a !== b) mismatches.push(t);
}
const throws = [];
for (let t = 0; t <= DUR; t = Math.round((t + 0.1) * 10) / 10) {
  try { await page.evaluate((t) => window.seek(t), t); } catch (e) { throws.push(`${t}: ${String(e).split('\n')[0]}`); }
}
await browser.close();

console.log(`${mismatches.length ? 'FAIL' : 'PASS'}  same frame on revisit at ${N} sample times${mismatches.length ? ': differs at ' + mismatches.join(', ') : ''}`);
console.log(`${throws.length ? 'FAIL' : 'PASS'}  seek runs without errors every 0.1 s${throws.length ? ':\n  ' + throws.slice(0, 10).join('\n  ') : ''}`);
if (errors.length) console.log(`WARN  page errors: ${errors.slice(0, 5).join(' | ')}`);
process.exit(mismatches.length || throws.length ? 1 : 0);
