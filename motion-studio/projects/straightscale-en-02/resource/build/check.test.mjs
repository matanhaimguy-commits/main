import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { check, sections, SOURCES } from './check.mjs';

const good = SOURCES.map((s, i) => `## ${i + 1}. ${s} (3 minutes)\n\n**Search ${i + 1}.** x\n\n\`\`\`\nq\n\`\`\`\n\nFilled example: y\n\n- **What to copy:** a\n- **Sort it:** b\n`).join('\n') + '\nFEAR DESIRE IDENTITY\n';

test('a complete sheet passes', () => assert.deepEqual(check(good).problems, []));

test('sections strips the number and the minutes', () => assert.ok('Reddit' in sections(good)));

test('flags missing parts, em dashes, hype and overtime', () => {
  const bad = good.replace('## 3. Reddit (3 minutes)', '## 3. Reddit (9 minutes)').replace(/\*\*Sort it:\*\* b\n$/m, '') + ' — the ultimate';
  const p = check(bad).problems.join('\n');
  assert.match(p, /em dash/);
  assert.match(p, /hype word: ultimate/);
  assert.match(p, /add up to 24 minutes/);
});

test('the real WORDS.md passes', () => {
  const r = check(readFileSync(new URL('../WORDS.md', import.meta.url), 'utf8'));
  assert.deepEqual(r.problems, []);
});
