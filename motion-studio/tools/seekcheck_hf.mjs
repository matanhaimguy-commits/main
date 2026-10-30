// HyperFrames mode of seekcheck (our own tool): every frame must be a pure function of time.
//   node tools/seekcheck.mjs --hf [--dur 10] [--n 12]      (run from the HyperFrames project folder)
// A HyperFrames page has no window.seek and needs the CLI's compiler, so this drives `hyperframes snapshot` twice:
// once at the sample times, once with a different time seeked before each sample. Same pixels at every sample = pass.
// Chrome can re-raster a glyph's antialiased edge after a layer is rebuilt (seen 30 Oct: one "S", 400 px, nothing
// moved). That is not animation state, so a frame whose changed pixels stay under --tol of the frame (default 0.1%,
// about 2,000 px at 1080x1920) passes as "glyph jitter" and is reported; a word, card or move out of place changes
// tens of thousands of pixels and fails. --tol 0 restores the exact-hash check.
import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdtempSync, readdirSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const raw = (k) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : undefined; };
const DUR = Number(raw('dur') ?? 10), N = Number(raw('n') ?? 12), TOL = Number(raw('tol') ?? 0.001);
const env = { ...process.env, HYPERFRAMES_NO_TELEMETRY: '1', DO_NOT_TRACK: '1', HYPERFRAMES_SKIP_SKILLS: '1',
  HYPERFRAMES_BROWSER_PATH: process.env.HYPERFRAMES_BROWSER_PATH || '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell' };

const r3 = (x) => Math.round(x * 1000) / 1000;
// golden-ratio stepping, kept off the very ends of the film
const times = Array.from({ length: N }, (_, i) => r3(0.05 + ((i * 0.6180339887) % 1) * (DUR - 0.1)));
const decoys = times.map((t) => r3(0.05 + ((t / DUR + 0.37) % 1) * (DUR - 0.1)));

function shoot(list) {
  const dir = mkdtempSync(join(tmpdir(), 'seekcheck-hf-'));
  const r = spawnSync('npx', ['-y', 'hyperframes@0.8.150', 'snapshot', '.', '--at', list.join(','), '--output', dir],
    { env, encoding: 'utf8' });
  if (r.status) { console.log(`FAIL  hyperframes snapshot exited ${r.status}\n${(r.stdout + r.stderr).slice(-800)}`); process.exit(1); }
  const out = {};
  for (const f of readdirSync(dir)) {
    const m = f.match(/^frame-\d+-at-([\d.]+)s\.png$/);
    if (m) out[r3(Number(m[1]))] = { file: join(dir, f), hash: createHash('sha1').update(readFileSync(join(dir, f))).digest('hex').slice(0, 12) };
  }
  return { dir, out };
}

// share of pixels that changed visibly (summed RGB delta over 30) between two PNGs, measured with Python/PIL
function changed(a, b) {
  const py = 'import sys\nfrom PIL import Image, ImageChops\nd = ImageChops.difference(Image.open(sys.argv[1]).convert("RGB"), Image.open(sys.argv[2]).convert("RGB"))\n' +
    'px = [r + g + b for r, g, b in d.getdata()]\nprint(sum(1 for v in px if v > 30) / len(px))';
  const r = spawnSync('python3', ['-c', py, a, b], { encoding: 'utf8' });
  return r.status ? 1 : Number(r.stdout.trim());
}

const A = shoot(times);
const B = shoot(times.flatMap((t, i) => [decoys[i], t]));
const a = A.out, b = B.out;
const missing = times.filter((t) => !a[t] || !b[t]);
const mismatches = [], jitter = [];
for (const t of times) {
  if (!a[t] || !b[t] || a[t].hash === b[t].hash) continue;
  const share = changed(a[t].file, b[t].file);
  (share <= TOL ? jitter : mismatches).push(`${t} (${(share * 100).toFixed(3)}%)`);
}
rmSync(A.dir, { recursive: true, force: true });
rmSync(B.dir, { recursive: true, force: true });
console.log(`${mismatches.length ? 'FAIL' : 'PASS'}  same frame after a different seek at ${N - missing.length} sample times`
  + `${mismatches.length ? ': differs at ' + mismatches.join(', ') : ''}`);
if (jitter.length) console.log(`NOTE  glyph antialiasing jitter under ${(TOL * 100).toFixed(2)}% of the frame at ${jitter.join(', ')}`);
if (missing.length) console.log(`WARN  no snapshot for ${missing.join(', ')}`);
process.exit(mismatches.length || missing.length === N ? 1 : 0);
