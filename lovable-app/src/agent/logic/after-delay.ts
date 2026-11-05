/**
 * The optional wait between a funnel's delivery message and its last message (`after`, the
 * qualifying question). ORGANIC-OS 8.5 step 4: wait 10 to 60 minutes. 0 keeps the old
 * behaviour, the question right after the resource.
 */

export const AFTER_DELAY_MAX_MINUTES = 60;

/** Whole minutes from 0 to 60; anything that is not a number counts as 0. */
export function clampAfterDelay(raw: unknown): number {
  const n = typeof raw === 'number' ? raw : Number(raw);
  if (!Number.isFinite(n)) return 0;
  return Math.min(AFTER_DELAY_MAX_MINUTES, Math.max(0, Math.round(n)));
}

/** When a message queued at `now` with this delay becomes due. */
export function afterDueAt(now: Date, minutes: number): Date {
  return new Date(now.getTime() + minutes * 60_000);
}
