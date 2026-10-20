// Stills straight from the composition page (no HyperFrames compile), for fast styleframes and contact sheets.
//   node tools/shots.mjs <page.html> <outdir> t1,t2,... [--w 1080 --h 1920] [--scale 0.5]
// Seeks through the page's own paused timeline (window.seek -> tl.totalTime), so it is the same path HyperFrames uses.
import { chromium } from 'playwright';
import { mkdirSync } from 'node:fs';
import { resolve } from 'node:path';
const [pagePath, outDir, tsArg] = process.argv.slice(2);
const arg = (k, d) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : d; };
const W = Number(arg('w', 1080)), H = Number(arg('h', 1920)), SCALE = Number(arg('scale', 1));
mkdirSync(outDir, { recursive: true });
const t0 = Date.now(); const log = (...a) => process.env.DEBUG && console.log(((Date.now() - t0) / 1000).toFixed(1), ...a);
log('start');
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
log('browser');
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: SCALE });
const errors = [];
page.on('pageerror', (e) => errors.push(String(e)));
page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') errors.push('console: ' + m.text()); });
log('launched'); await page.goto('file://' + resolve(pagePath)); log('loaded');
await page.waitForFunction(() => window.__hfReady === true, null, { timeout: 20000 });
for (const t of tsArg.split(',').map(Number)) {
  await page.evaluate((t) => { window.seek(t); }, t);
  log('seek', t); await page.screenshot({ path: `${outDir}/f_${t.toFixed(2).padStart(6, '0')}.png` }); log('shot');
}
await browser.close();
if (errors.length) console.log('ERRORS:\n' + errors.join('\n'));
console.log('done', tsArg.split(',').length, 'frames');
