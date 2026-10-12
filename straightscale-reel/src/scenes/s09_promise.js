// S9 · The promise (26.60–31.10) "Jo 'cilësi', por: 'Instalim për dhjetë ditë, me datë në kontratë.'"
// Ransom-note CILËSI gets struck and drops out of frame; the promise lands, word by word, ON the gold line.
import { C, SERIF, SANS, W, H, text, measure, clamp, lerp, rng } from "../lib.js";
import { spring, paperBg, ransomWord, marker, rubberStamp } from "../fx.js";

function land(ctx, w, x, y, at, t, o) {
  const k = spring(t - at, 260, 20);
  if (k < 0.001) return measure(ctx, w, o);
  ctx.save(); ctx.translate(x, y - (1 - k) * 120);
  text(ctx, w, 0, 0, { ...o, alpha: 1 });
  ctx.restore();
  return measure(ctx, w, o);
}

export default {
  id: "s09_promise", start: 26.6, end: 31.1,
  draw(ctx, t) {
    paperBg(ctx, C.marble, 6);
    // the straight line from S6 stays as the baseline
    ctx.fillStyle = C.gold; ctx.fillRect(0, 894, W, 12);
    // CILËSI (ransom) → struck → letters drop away
    const drop = (i) => { const p = clamp((t - (27.5 + i * 0.04)) / 0.6); if (p <= 0) return null; const r = rng(70 + i); return { dx: (r() - 0.5) * 200 * p, dy: 1900 * p * p, rot: (r() - 0.5) * 3 * p }; };
    ransomWord(ctx, "CILËSI", W / 2, 420, 150, 31, t, (j) => 26.7 + j * 0.035, drop);
    if (t < 27.6) marker(ctx, [[150, 410], [520, 380], [940, 398]], clamp((t - 27.0) / 0.25), C.crimson, 34, 5);
    promise(ctx, t);
    // stamp: it's an example, not a client claim
    rubberStamp(ctx, "SHEMBULL", 820, 560, 0.14, 40, spring(t - 28.35, 380, 24), 12);
  },
};

// the promise, left aligned, sitting on the line (also shown on the three screens in S10)
export function promise(ctx, t) {
    const ser = { family: SERIF, size: 122, weight: 700, color: C.charcoal };
    let x = 72;
    x += land(ctx, "Instalim", x, 700, 28.24, t, ser) + 34;
    land(ctx, "për", x, 700, 28.72, t, ser);
    x = 72;
    x += land(ctx, "10", x, 870, 28.96, t, { family: SANS, size: 172, weight: 900, color: C.charcoal, ls: -6 }) + 30;
    land(ctx, "ditë,", x, 870, 29.2, t, ser);
    const it = { family: SERIF, size: 86, weight: 700, italic: true, color: C.charcoal };
    x = 76;
    for (const [w, at] of [["me", 29.68], ["datë", 29.84], ["në", 30.08], ["kontratë.", 30.24]]) x += land(ctx, w, x, 1035, at, t, it) + 24;
}
