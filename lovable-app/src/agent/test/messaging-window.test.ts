// @vitest-environment node
import { describe, expect, it } from 'vitest';
import { MESSAGING_WINDOW_MS, WINDOW_SAFETY_MS, windowOpen } from '../logic/messaging-window';

const LAST = new Date('2026-10-28T10:00:00Z');
const after = (ms: number) => new Date(LAST.getTime() + ms);
const HOUR = 3_600_000;

describe('windowOpen', () => {
  it('is open soon after the person wrote', () => {
    expect(windowOpen(LAST, after(0))).toBe(true);
    expect(windowOpen(LAST, after(HOUR))).toBe(true);
    expect(windowOpen(LAST, after(23 * HOUR))).toBe(true);
  });

  it('closes at 24 hours, a few minutes early so a send never races the edge', () => {
    expect(windowOpen(LAST, after(MESSAGING_WINDOW_MS - WINDOW_SAFETY_MS - 1))).toBe(true);
    expect(windowOpen(LAST, after(MESSAGING_WINDOW_MS - WINDOW_SAFETY_MS))).toBe(false);
    expect(windowOpen(LAST, after(MESSAGING_WINDOW_MS))).toBe(false);
    expect(windowOpen(LAST, after(25 * HOUR))).toBe(false);
  });

  it('is closed when the person never wrote (a comment alone does not open it)', () => {
    expect(windowOpen(null, LAST)).toBe(false);
    expect(windowOpen(undefined, LAST)).toBe(false);
  });
});
