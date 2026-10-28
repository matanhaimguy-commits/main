// Checks WORDS.md against the brief before it is built: every source section has its searches,
// a filled example, "What to copy" and "Sort it"; no em dashes or hype words; short enough for 20 minutes.

export const SOURCES = [
  "Competitors' Google reviews", 'Review sites', 'Reddit', 'Newsletter and Substack comments',
  'YouTube comments', 'Public Facebook groups',
];
const HYPE = ['ultimate', 'secret', 'hack', 'game-changer', 'game changer', 'insane', 'proven', 'guaranteed', 'skyrocket', 'explode', 'crush'];
// About 1,600 words reads in about 7 minutes; the rest of the 20 is searching.
export const MAX_WORDS = 1600;

export function sections(md) {
  const out = {};
  let name = null;
  for (const line of md.split('\n')) {
    const m = line.match(/^## (?:\d+\. )?(.+?)(?: \(\d+ minutes\))?$/);
    if (m) { name = m[1]; out[name] = ''; } else if (name) out[name] += line + '\n';
  }
  return out;
}

export function check(md) {
  const problems = [];
  const secs = sections(md);
  for (const src of SOURCES) {
    const body = secs[src];
    if (body === undefined) { problems.push(`missing section: ${src}`); continue; }
    if (!/\*\*Search \d+\.\*\*/.test(body)) problems.push(`${src}: no numbered search`);
    if (!body.includes('```')) problems.push(`${src}: no copy-paste box`);
    if (!/Filled example|filled example|Filled in/.test(body) && !/https:\/\//.test(body)) problems.push(`${src}: no filled example`);
    if (!body.includes('**What to copy:**')) problems.push(`${src}: no "What to copy"`);
    if (!body.includes('**Sort it:**')) problems.push(`${src}: no "Sort it"`);
  }
  for (const col of ['FEAR', 'DESIRE', 'IDENTITY']) if (!md.includes(col)) problems.push(`no ${col} column`);
  if (/—/.test(md)) problems.push('em dash found');
  const lower = md.toLowerCase();
  for (const w of HYPE) if (new RegExp(`\\b${w}\\b`).test(lower)) problems.push(`hype word: ${w}`);
  const words = md.split(/\s+/).filter(Boolean).length;
  if (words > MAX_WORDS) problems.push(`too long: ${words} words (max ${MAX_WORDS})`);
  const minutes = [...md.matchAll(/^## .*\((\d+) minutes\)$/gm)].reduce((a, m) => a + Number(m[1]), 0);
  if (minutes > 20) problems.push(`timed sections add up to ${minutes} minutes (max 20)`);
  return { ok: problems.length === 0, problems, words, minutes };
}
