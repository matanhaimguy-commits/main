// Load the page, print page errors and the solved path (contacts, plate angles, pegs). node tools/report.mjs [page]
import { chromium } from '/home/user/main/motion-studio/node_modules/playwright/index.mjs';
const pageArg = process.argv[2] || 'index.html';
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
page.on('pageerror', (e) => console.log('PAGEERROR', e.message));
page.on('console', (m) => console.log('console:', m.text()));
await page.goto('file://' + process.cwd() + '/' + pageArg);
await page.waitForFunction(() => typeof window.seek === 'function', null, { timeout: 20000 }).catch((e) => console.log('no seek', e.message));
const r = await page.evaluate(() => window.__pathReport && window.__pathReport());
console.log(JSON.stringify(r, null, 0));
const t0 = Date.now(); await page.evaluate(() => { for (let i = 0; i < 20; i++) window.seek(10 + i * 0.1); }); console.log('seek ms', (Date.now() - t0) / 20);
await browser.close();
