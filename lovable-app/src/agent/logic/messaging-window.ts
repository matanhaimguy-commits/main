/**
 * Meta lets a business message a person freely for 24 hours after the person's last message
 * (a typed message or a button tap). Comments do not open it. The last few minutes are kept
 * back so a send never races the edge of the window.
 */

export const MESSAGING_WINDOW_MS = 24 * 60 * 60 * 1000;
export const WINDOW_SAFETY_MS = 5 * 60 * 1000;

/** True while `now` is inside the window that started at the person's last message. */
export function windowOpen(lastInboundAt: Date | null | undefined, now: Date): boolean {
  if (!lastInboundAt) return false;
  return now.getTime() - lastInboundAt.getTime() < MESSAGING_WINDOW_MS - WINDOW_SAFETY_MS;
}
