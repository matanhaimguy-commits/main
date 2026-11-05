import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { load } from './load.mjs';

const SS = load(['src/lib/timing.js']);
const data = JSON.parse(readFileSync(new URL('../timing.json', import.meta.url), 'utf8'));
const T = SS.timing.make(data);

test('every cue resolves to a time inside the film', () => {
  for (const name of Object.keys(data.cues)) {
    const t = T.cue(name);
    assert.ok(Number.isFinite(t) && t > -1 && t < T.duration, `${name} = ${t}`);
  }
});

test('word cues follow the words: moving a word moves its cue (retiming is a data change)', () => {
  const moved = structuredClone(data);
  moved.lines.find((l) => l.id === 1).words[3].s += 0.5;
  assert.ok(Math.abs(SS.timing.make(moved).cue('hit.hook') - (T.cue('hit.hook') + 0.5)) < 1e-9);
});

test('the film lasts until the last line ends plus the end-card tail', () => {
  const last = data.lines[data.lines.length - 1];
  assert.equal(T.duration, +(last.end + data.tail).toFixed(3));
});

test('words are in order inside each line', () => {
  for (const l of data.lines) {
    for (let i = 1; i < l.words.length; i++) assert.ok(l.words[i].s > l.words[i - 1].s, `line ${l.id} word ${i}`);
  }
});

test('an unknown cue fails loudly', () => {
  assert.throws(() => T.cue('nope'));
});
