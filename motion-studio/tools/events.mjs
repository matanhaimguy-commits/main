// Dump a canvas-engine page's sound events (window.EVENTS), named cues (window.CUES) and duration (window.DURATION) to JSON,
// so the score and effects use the composition's own times. node tools/events.mjs <project dir> > audio/events.json
import { chromium } from 'playwright';
const dir = process.argv[2];
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
// --page index.html?lang=en checks a variant of the same page (default index.html)
await page.goto('file://' + dir + '/' + (process.argv.includes('--page') ? process.argv[process.argv.indexOf('--page') + 1] : 'index.html'));
await page.waitForFunction(() => typeof window.seek === 'function');
const out = await page.evaluate(() => ({ duration: window.DURATION, cues: window.CUES || {}, events: (window.EVENTS || []).map((e) => ({ ...e, t: Math.round(e.t * 1000) / 1000 })) }));
await browser.close();
console.log(JSON.stringify(out, null, 0).replace(/},{/g, '},\n{'));
