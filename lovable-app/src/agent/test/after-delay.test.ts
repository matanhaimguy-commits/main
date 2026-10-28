// @vitest-environment node
import { describe, expect, it } from 'vitest';
import { AFTER_DELAY_MAX_MINUTES, afterDueAt, clampAfterDelay } from '../logic/after-delay';

describe('clampAfterDelay', () => {
  it('keeps whole minutes from 0 to 60', () => {
    expect(clampAfterDelay(0)).toBe(0);
    expect(clampAfterDelay(15)).toBe(15);
    expect(clampAfterDelay(AFTER_DELAY_MAX_MINUTES)).toBe(60);
  });

  it('rounds, and holds the ends', () => {
    expect(clampAfterDelay(12.6)).toBe(13);
    expect(clampAfterDelay(-5)).toBe(0);
    expect(clampAfterDelay(500)).toBe(60);
  });

  it('turns anything that is not a number into 0', () => {
    expect(clampAfterDelay('')).toBe(0);
    expect(clampAfterDelay('abc')).toBe(0);
    expect(clampAfterDelay(undefined)).toBe(0);
    expect(clampAfterDelay(Number.NaN)).toBe(0);
    expect(clampAfterDelay('25')).toBe(25);
  });
});

describe('afterDueAt', () => {
  it('is the queue time plus the delay', () => {
    const now = new Date('2026-10-28T10:00:00Z');
    expect(afterDueAt(now, 15).toISOString()).toBe('2026-10-28T10:15:00.000Z');
    expect(afterDueAt(now, 60).toISOString()).toBe('2026-10-28T11:00:00.000Z');
    expect(afterDueAt(now, 0).getTime()).toBe(now.getTime());
  });
});
