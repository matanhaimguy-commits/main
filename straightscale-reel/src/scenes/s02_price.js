// S2 · (3.00–4.70) "Problemi nuk është çmimi."  Crimson hit, giant cropped ÇMIMI, black marker strike.
import { C, SERIF, SANS, W, H, text, measure, clamp, lerp } from "../lib.js";
import { spring, track, paperBg, marker } from "../fx.js";

export default {
  id: "s02_price", start: 3.0, end: 4.7,
  draw(ctx, t) {
    paperBg(ctx, C.crimson, 8);
    // kicker words snap in on their syllables (left aligned, no fades)
    const words = [["PROBLEMI", 3.04, 72, 540], ["NUK", 3.52, 72, 650], ["ËSHTË", 3.68, null, 650]];
    let lastX = 72;
    for (const [w, at, x0, y] of words) {
      const x = x0 ?? lastX;
      const k = spring(t - at, 320, 22);
      if (k > 0.001) {
        ctx.save(); ctx.translate(x, y + (1 - k) * 60); ctx.scale(1, k);
        text(ctx, w, 0, 0, { size: 96, weight: 900, color: C.ivory, ls: 3 });
        ctx.restore();
      }
      lastX = x + measure(ctx, w, { size: 96, weight: 900, ls: 3 }) + 30;
    }
    // giant ÇMIMI, wider than the frame, panning left
    const k = spring(t - 3.86, 260, 20);
    if (k > 0.001) {
      const pan = lerp(140, -110, clamp((t - 3.86) / 0.84));
      ctx.save(); ctx.translate(W / 2 + pan, 1010); ctx.scale(lerp(1.35, 1, clamp(k)), lerp(1.35, 1, clamp(k)));
      text(ctx, "ÇMIMI", 0, 140, { size: 420, weight: 900, color: C.ivory, align: "center", ls: -12 });
      ctx.restore();
      // black marker strike, drawn fast after the word lands
      const p = clamp((t - 4.06) / 0.22);
      marker(ctx, [[-40, 1040], [300, 990], [620, 1010], [1120, 950]], p, C.charcoal, 54, 3);
    }
  },
};
