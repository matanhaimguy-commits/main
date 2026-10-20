// Seamless-loop check: the change across the seam (last frame -> first frame) must look like any other frame step.
// node tools/loopcheck.mjs [--fps 60] [--page index.html]
import { chromium } from '/home/user/main/motion-studio/node_modules/playwright/index.mjs';
const raw = (k) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : undefined; };
const FPS = Number(raw('fps') || 60), PAGE = raw('page') || 'index.html', H = PAGE.includes('fmt=45') ? 1350 : 1920;
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1080, height: H } });
await page.goto('file://' + process.cwd() + '/' + PAGE);
await page.waitForFunction(() => typeof window.seek === 'function');
const T = await page.evaluate(() => window.DURATION);
const grab = (t) => page.evaluate((t) => { window.seek(t); const c = document.getElementById('c'); const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data; const o = []; for (let i = 0; i < d.length; i += 64) o.push(d[i], d[i + 1], d[i + 2]); return o; }, t);
const diff = (a, b) => { let s = 0; for (let i = 0; i < a.length; i++) s += Math.abs(a[i] - b[i]); return s / a.length; };
const ts = [T - 3 / FPS, T - 2 / FPS, T - 1 / FPS, 0, 1 / FPS, 2 / FPS];
const fr = []; for (const t of ts) fr.push(await grab(t));
const d = []; for (let i = 1; i < fr.length; i++) d.push(diff(fr[i - 1], fr[i]));
await browser.close();
const seam = d[2], others = [d[0], d[1], d[3], d[4]], mx = Math.max(...others);
console.log(`frame steps around the loop (mean |dRGB|): ${d.map((x) => x.toFixed(2)).join('  ')}  (seam is the 3rd)`);
const ok = seam <= Math.max(mx * 1.6, 0.6);
console.log(`${ok ? 'PASS' : 'FAIL'}  seam step ${seam.toFixed(2)} vs neighbours max ${mx.toFixed(2)}`);
process.exit(ok ? 0 : 1);
