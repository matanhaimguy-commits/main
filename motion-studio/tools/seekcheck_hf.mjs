// HyperFrames mode of seekcheck (our own tool): every frame must be a pure function of time.
//   node tools/seekcheck.mjs --hf [--dur 10] [--n 12]      (run from the HyperFrames project folder)
// A HyperFrames page has no window.seek and needs the CLI's compiler, so this drives `hyperframes snapshot` twice:
// once at the sample times, once with a different time seeked before each sample. Same pixels at every sample = pass.
import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdtempSync, readdirSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const raw = (k) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : undefined; };
const DUR = Number(raw('dur') ?? 10), N = Number(raw('n') ?? 12);
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
    if (m) out[r3(Number(m[1]))] = createHash('sha1').update(readFileSync(join(dir, f))).digest('hex').slice(0, 12);
  }
  rmSync(dir, { recursive: true, force: true });
  return out;
}

const a = shoot(times);
const b = shoot(times.flatMap((t, i) => [decoys[i], t]));
const missing = times.filter((t) => !a[t] || !b[t]);
const mismatches = times.filter((t) => a[t] && b[t] && a[t] !== b[t]);
console.log(`${mismatches.length ? 'FAIL' : 'PASS'}  same frame after a different seek at ${N - missing.length} sample times`
  + `${mismatches.length ? ': differs at ' + mismatches.join(', ') : ''}`);
if (missing.length) console.log(`WARN  no snapshot for ${missing.join(', ')}`);
process.exit(mismatches.length || missing.length === N ? 1 : 0);
