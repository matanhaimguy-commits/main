// HyperFrames mode of safezone (our own tool): no text may sit in the platform's UI zones.
//   node tools/safezone.mjs --hf [--top 269 --bottom 672 --right 227 --left 65] [--samples 21]   (from the project folder)
// A HyperFrames page needs the CLI's compiler, so this asks HyperFrames itself: one `hyperframes check
// --caption-zone` run per forbidden band (top, bottom, left, right, and the right strip of the lower half), sampled
// at every tween boundary. Any text in a band is a caption_zone_collision. Elements marked
// data-layout-allow-caption-zone (our captions) are skipped by HyperFrames; the kit's rules check them instead.
import { spawnSync } from 'node:child_process';

const raw = (k) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : undefined; };
const num = (k, d) => (raw(k) !== undefined ? Number(raw(k)) : d);
const W = 1080, H = 1920;
const TOP = num('top', 269) / H, BOT = 1 - num('bottom', 672) / H, LEFT = num('left', 65) / W;
const RIGHT = 1 - num('left', 65) / W, RIGHT_LOW = 1 - num('right', 227) / W, SAMPLES = num('samples', 21);
const f = (x) => x.toFixed(4);
const bands = {
  top: `x0=0;y0=0;x1=1;y1=${f(TOP)}`,
  bottom: `x0=0;y0=${f(BOT)};x1=1;y1=1`,
  left: `x0=0;y0=0;x1=${f(LEFT)};y1=1`,
  right: `x0=${f(RIGHT)};y0=0;x1=1;y1=1`,
  'right of the lower half': `x0=${f(RIGHT_LOW)};y0=0.5;x1=1;y1=1`,
};
const env = { ...process.env, HYPERFRAMES_NO_TELEMETRY: '1', DO_NOT_TRACK: '1', HYPERFRAMES_SKIP_SKILLS: '1',
  HYPERFRAMES_BROWSER_PATH: process.env.HYPERFRAMES_BROWSER_PATH || '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell' };

let issues = 0;
for (const [name, band] of Object.entries(bands)) {
  const r = spawnSync('npx', ['-y', 'hyperframes@0.8.150', 'check', '.', '--json', '--no-contrast', '--at-transitions',
    '--samples', String(SAMPLES), '--caption-zone', `${band};severity=error`, '--max-issues', '400'],
    { env, encoding: 'utf8', maxBuffer: 64 << 20 });
  let out;
  try { out = JSON.parse(r.stdout.slice(r.stdout.indexOf('{'))); } catch { console.log(`FAIL  ${name}: check printed no JSON\n${(r.stdout + r.stderr).slice(-600)}`); process.exit(1); }
  const hits = (out.layout?.findings || []).filter((x) => x.code === 'caption_zone_collision');
  for (const h of hits) {
    issues++;
    console.log(`t=${(h.firstSeen ?? h.time).toFixed(2)}  ${name}  "${(h.text || h.selector).slice(0, 40)}"  ` +
      `[${Math.round(h.rect.left)}, ${Math.round(h.rect.top)}, ${Math.round(h.rect.right)}, ${Math.round(h.rect.bottom)}]  ${h.sourceFile || ''}`);
  }
}
console.log(issues ? `FAIL  ${issues} text box(es) in the UI zones` : 'PASS  safe zones: no text in the UI zones');
process.exit(issues ? 1 : 0);
