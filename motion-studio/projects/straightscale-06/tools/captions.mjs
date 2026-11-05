// captions.srt from the film itself: samples every painted text line (window.BOXES) and writes one cue per block,
// from the first frame any of its lines shows to the last. The on-screen copy, word for word.
//   node tools/captions.mjs film/index.html > deliver/v1/captions.srt
import { chromium } from 'playwright';
import { resolve } from 'node:path';
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto('file://' + resolve(process.argv[2]));
await page.waitForFunction(() => window.__hfReady === true);
const seen = await page.evaluate(() => {
  const S = {};
  for (let t = 0; t <= window.DURATION - 1e-3; t += 1 / 30) {
    for (const b of window.BOXES(t)) {
      if (['chip', 'clock', 'label', 'flyer', 'axis', 'day', 'logo'].includes(b.id)) continue;
      const blk = b.id.replace(/\d$/, '');
      const s = (S[blk] ??= { t0: t, t1: t, lines: [] });
      s.t1 = t;
      if (!s.lines.includes(b.text)) s.lines.push(b.text);
    }
  }
  return S;
}, null);
await browser.close();
const order = ['head', 'note', 'math', 'sys', 'list', 'comment', 'key', 'body'];
const merged = [];
for (const k of order) {
  if (!seen[k]) continue;
  if (k === 'key' && merged.length && merged.at(-1).k === 'comment') { const m = merged.at(-1); m.lines.push(...seen[k].lines); m.t1 = Math.max(m.t1, seen[k].t1); continue; }
  merged.push({ k, ...seen[k] });
}
const ts = (t) => { const ms = Math.round(t * 1000); const h = Math.floor(ms / 3600000), m = Math.floor(ms / 60000) % 60, s = Math.floor(ms / 1000) % 60; return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')},${String(ms % 1000).padStart(3, '0')}`; };
merged.sort((a, b) => a.t0 - b.t0);
console.log(merged.map((c, i) => `${i + 1}\n${ts(c.t0)} --> ${ts(c.t1 + 1 / 30)}\n${c.lines.join(' ')}\n`).join('\n'));
