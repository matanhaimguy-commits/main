// Reading-time check for this page's caption table (window.CAPTIONS) and an SRT of the on-screen lines.
// Gate (v2, the house rule the independent reviewer applies): on screen, fully in to the start of its exit,
// >= 0.25 s per word + 0.5 s. Advisory: Lemo-Opuscar DIRECTOR.md section 7 ("roughly" letters/15 + 1.5 s), printed for
// reference; v1 held the ask 5.6 s to meet it, which the review found too long for a beat-sync loop.
// node tools/readcheck.mjs [--srt deliver/v1/captions.srt]
import { chromium } from '/home/user/main/motion-studio/node_modules/playwright/index.mjs';
import { writeFileSync } from 'node:fs';
const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto('file://' + process.cwd() + '/index.html');
await page.waitForFunction(() => typeof window.seek === 'function');
const { cues, end } = await page.evaluate(() => ({ cues: window.CAPTIONS, end: window.DURATION }));
await browser.close();
let fail = 0;
for (const c of cues) {
  const words = c.text.split(/\s+/).filter(Boolean).length, need = 0.25 * words + 0.5, hold = c.tout - c.readFrom;
  const letters = c.text.replace(/[^A-Za-z]/g, '').length, lemo = letters / 15 + 1.5;
  const ok = hold >= need - 1e-6; if (!ok) fail++;
  console.log(`${ok ? 'PASS' : 'FAIL'}  ${c.tin.toFixed(2)}-${c.tout.toFixed(2)}  hold ${hold.toFixed(2)} s >= ${need.toFixed(2)} s (${words} words)  [lemo advisory ${lemo.toFixed(2)} s: ${hold >= lemo ? 'met' : 'short ' + (lemo - hold).toFixed(2) + ' s'}]  "${c.text}"`);
}
const i = process.argv.indexOf('--srt');
if (i > 0) {
  const ts = (x) => { x = Math.max(0, x); const h = Math.floor(x / 3600), m = Math.floor(x / 60) % 60, s = Math.floor(x) % 60, ms = Math.round((x % 1) * 1000);
    return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')},${String(ms).padStart(3, '0')}`; };
  // lines that share the screen become one subtitle (start of the first, end of the last)
  const groups = [];
  for (const c of [...cues].sort((a, b) => a.tin - b.tin)) {
    const g = groups[groups.length - 1];
    if (g && c.tin < g.tout - 0.05) { g.lines.push(...c.lines); g.tout = Math.max(g.tout, c.tout); }
    else groups.push({ tin: c.tin, tout: c.tout, lines: [...c.lines] });
  }
  const srt = groups.map((c, k) => `${k + 1}\n${ts(c.tin)} --> ${ts(Math.min(c.tout + 0.25, end, k + 1 < groups.length ? groups[k + 1].tin : end))}\n${c.lines.join('\n')}\n`).join('\n');
  writeFileSync(process.argv[i + 1], srt); console.log('wrote', process.argv[i + 1]);
}
process.exit(fail ? 1 : 0);
