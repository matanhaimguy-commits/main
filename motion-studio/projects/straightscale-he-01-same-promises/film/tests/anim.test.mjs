import test from 'node:test';
import assert from 'node:assert/strict';
import { load } from './load.mjs';

const SS = load(['src/lib/anim.js']);
const near = (a, b, eps = 1e-3) => assert.ok(Math.abs(a - b) < eps, `${a} != ${b}`);

test('spring starts at 0 and settles at 1', () => {
  near(SS.anim.spring(0), 0);
  near(SS.anim.spring(3), 1);
});

test('a path holds its start value before the first step and lands on the target', () => {
  const f = SS.anim.path(5, [{ t: 1, to: 10 }]);
  near(f(0), 5);
  near(f(0.999), 5);
  near(f(5), 10);
});

test('a later step starts from wherever the value is, so there is no jump', () => {
  const f = SS.anim.path(0, [{ t: 0, to: 100, k: 50, d: 14 }, { t: 0.3, to: -20 }]);
  near(f(0.3), f(0.2999), 2);
});

test('bounce never passes through the target (the desk) and settles on it', () => {
  const f = SS.anim.path(0, [{ t: 0, to: 1, how: 'bounce', k: 230, d: 14 }]);
  for (let t = 0; t < 2; t += 0.01) assert.ok(f(t) <= 1 + 1e-9);
  near(f(3), 1);
});

test('fall is gravity: slow first, all the way down at its duration', () => {
  const f = SS.anim.path(1, [{ t: 0, to: 0, how: 'fall', dur: 0.12 }]);
  assert.ok(f(0.06) > 0.5);
  near(f(0.12), 0);
});

test('same time, same value, whatever was evaluated before (pure function of time)', () => {
  const f = SS.anim.paths({ x: 0, y: 0 }, [{ t: 0.5, to: { x: 10 } }, { t: 1, to: { y: 4 } }]);
  const a = f(1.37);
  f(0.1); f(9);
  assert.deepEqual(f(1.37), a);
});
