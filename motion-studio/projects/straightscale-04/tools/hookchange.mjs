// Quick estimate of frames_metrics' hook_change_0_2s straight from the page (no render): share of a 120 px wide grey
// frame changing > 10 levels between samples, bottom 6 % masked. node tools/hookchange.mjs [--step 1.5] [--page ...]
import { chromium } from '/home/user/main/motion-studio/node_modules/playwright/index.mjs';
const raw = (k) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : undefined; };
const STEP = Number(raw('step') || 1.5), PAGE = raw('page') || 'index.html', H = PAGE.includes('fmt=45') ? 1350 : 1920;
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1080, height: H } });
await page.goto('file://' + process.cwd() + '/' + PAGE);
await page.waitForFunction(() => typeof window.seek === 'function');
const grab = (t) => page.evaluate((t) => {
  window.seek(t); const c = document.getElementById('c'), s = document.createElement('canvas'); s.width = 120; s.height = Math.round(c.height * 120 / c.width);
  const x = s.getContext('2d'); x.imageSmoothingQuality = 'medium'; x.drawImage(c, 0, 0, s.width, s.height);
  const d = x.getImageData(0, 0, s.width, s.height).data, g = []; for (let i = 0; i < d.length; i += 4) g.push((d[i] + d[i + 1] + d[i + 2]) / 3); return { g, w: s.width, h: s.height };
}, t);
const ts = []; for (let t = 0; t <= 2 + 1e-9; t += STEP) ts.push(t);
const fr = []; for (const t of ts) fr.push(await grab(t));
await browser.close();
const hh = Math.floor(fr[0].h * 0.94), ch = [];
for (let i = 1; i < fr.length; i++) { let n = 0; for (let k = 0; k < hh * fr[i].w; k++) if (Math.abs(fr[i].g[k] - fr[i - 1].g[k]) > 10) n++; ch.push(n / (hh * fr[i].w)); }
console.log(`hook change (step ${STEP} s, samples ${ts.join(', ')}): ${ch.map((v) => v.toFixed(3)).join(' ')}  mean ${(ch.reduce((a, b) => a + b, 0) / ch.length).toFixed(3)}`);
