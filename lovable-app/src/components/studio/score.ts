const fmt = (n: number) => (Number.isInteger(n) ? String(n) : n.toFixed(1));

/** "86/100", or null without a score. */
export function scoreText(score: number | undefined, max: number | undefined): string | null {
  return score == null ? null : `${fmt(score)}/${fmt(max ?? 100)}`;
}
