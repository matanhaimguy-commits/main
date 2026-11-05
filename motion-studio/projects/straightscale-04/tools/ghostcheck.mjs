// Ghost check (independent review r1, finding 1): nothing on the moving wall may show through a caption.
// For every frame where a band caption is drawn, render the same frame without the type and without grain
// (index.html?nocap=1&nograin=1) and measure how far the pixels inside each line's rectangle stray from the band's flat
// colour. A logo or plate ghost at 6 % on ivory is ~13 levels; a clean band is 0-1. Also checks that the logo, when it
// shows, sits fully below the band's fade.
// node tools/ghostcheck.mjs [--page index.html?fmt=45] [--step 0.05] [--from 0 --to 25]
import { chromium } from '/home/user/main/motion-studio/node_modules/playwright/index.mjs';
const raw = (k) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : undefined; };
const PAGE = raw('page') || 'index.html', H = PAGE.includes('fmt=45') ? 1350 : 1920, STEP = Number(raw('step') || 0.05);
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const open = async (q) => {
  const p = await browser.newPage({ viewport: { width: 1080, height: H } });
  p.on('pageerror', (e) => console.log('PAGEERROR', e.message));
  await p.goto('file://' + process.cwd() + '/' + q);
  await p.waitForFunction(() => typeof window.seek === 'function');
  return p;
};
const A = await open(PAGE), B = await open(PAGE + (PAGE.includes('?') ? '&' : '?') + 'nocap=1&nograin=1');
const T = await A.evaluate(() => window.DURATION), band = await A.evaluate(() => window.BAND);
const from = Number(raw('from') || 0), to = Number(raw('to') || T);
const DARK = new Set(['No reply.', 'Gone.']);
let worst = { dev: 0 }, frames = 0, logoMin = Infinity, logoFrames = 0, fails = [];
for (let t = from; t <= to + 1e-9; t += STEP) {
  const info = await A.evaluate((t) => { window.__capboxes = []; window.seek(t); const b = window.__capboxes; window.__capboxes = null; return { boxes: b, logo: window.__logo, band: window.__band }; }, t);
  if (info.logo && info.band) { logoFrames++; logoMin = Math.min(logoMin, info.logo.y0 - band.fadeEnd); }
  const boxes = info.boxes.filter((b) => b.a > 0.02 && !DARK.has(b.text));
  if (!boxes.length) continue;
  frames++;
  const res = await B.evaluate(({ t, boxes }) => {
    window.seek(t);
    const c = document.getElementById('c'), x = c.getContext('2d'), col = window.__band ? window.__band.col.split(',').map(Number) : null;
    return boxes.map((b) => {
      const x0 = Math.max(0, Math.floor(b.x)), y0 = Math.max(0, Math.floor(b.y)), w = Math.min(c.width - x0, Math.ceil(b.w)), h = Math.min(c.height - y0, Math.ceil(b.h));
      const d = x.getImageData(x0, y0, w, h).data;
      if (!col) return { text: b.text, dev: 255, share: 1, noband: true };
      let mx = 0, n = 0;
      for (let i = 0; i < d.length; i += 4) { const e = Math.max(Math.abs(d[i] - col[0]), Math.abs(d[i + 1] - col[1]), Math.abs(d[i + 2] - col[2])); if (e > mx) mx = e; if (e > 3) n++; }
      return { text: b.text, dev: mx, share: n / (d.length / 4) };
    });
  }, { t, boxes });
  for (const r of res) {
    if (r.dev > worst.dev) worst = { ...r, t };
    if (r.dev > 3) fails.push(`t=${t.toFixed(2)} "${r.text}" max ${r.dev} levels, ${(r.share * 100).toFixed(1)} % of its box${r.noband ? ' (no band)' : ''}`);
  }
}
await browser.close();
console.log(`${PAGE}: ${frames} frames with band captions checked (step ${STEP} s), band opaque to y ${band.opaque}, fade ends ${band.fadeEnd}`);
console.log(`worst deviation under a caption: ${worst.dev} levels${worst.t != null ? ` at ${worst.t.toFixed(2)} s ("${worst.text}")` : ''}`);
console.log(`logo shown with the band on in ${logoFrames} frames; smallest gap below the fade: ${logoFrames ? logoMin.toFixed(0) + ' px' : 'n/a'}`);
for (const f of fails.slice(0, 20)) console.log('  ' + f);
const ok = !fails.length && (!logoFrames || logoMin >= 0);
console.log(ok ? 'PASS  no ghost under any caption; the logo never enters the band' : `FAIL  ${fails.length} ghosted line-frames${logoFrames && logoMin < 0 ? ', logo inside the band fade' : ''}`);
process.exit(ok ? 0 : 1);
