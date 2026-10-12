// S8 · (22.65–26.60) "Gjej çfarë duan vërtet dhe ktheje në një premtim që s'e bën askush."
// The highlighted phrases peel off the tapes and fly into one point on the line, where they compress into a
// single gold square (the gold square of the logo). On "askush" the camera pulls back: everyone else's lines are
// crooked and grey; only this one is straight.
import { C, SERIF, SANS, W, H, text, clamp, lerp, rng } from "../lib.js";
import { spring, paperBg, fromLine, goldLine, marker } from "../fx.js";
import { tapes, lexo } from "./s07_reviews.js";

const SQ = 140, SQX = 540, SQY = 894 - SQ / 2;
let HL = null;

export default {
  id: "s08_one", start: 22.65, end: 26.6,
  draw(ctx, t) {
    paperBg(ctx, C.marble, 6);
    const zb = spring(t - 25.22, 80, 16);
    const zin = spring(t - 23.5, 6, 4.9);                  // slow push while the promise forms
    const Z = lerp(lerp(1, 1.16, zin), 0.34, zb);
    ctx.save(); ctx.translate(540, 900); ctx.scale(Z, Z); ctx.translate(-540, -900);
    // everyone else's lines: crooked, grey, scribbled in as we pull back
    if (t > 25.2) {
      for (let k = -13; k <= 13; k++) {
        if (k === 0) continue;
        const r = rng(900 + k * 17), y0 = 900 + k * 150 + (r() - 0.5) * 40, tilt = (r() - 0.5) * 0.12;
        const pts = []; for (let i = 0; i <= 16; i++) { const x = -1300 + i * 230; pts.push([x, y0 + (x - 540) * tilt + (r() - 0.5) * 70]); }
        const d = Math.abs(k) * 0.025 + r() * 0.08;
        marker(ctx, pts, clamp((t - 25.26 - d) / 0.35), "#7D756A", 18, 300 + k);
        // their square: grey, all the same
        const q = clamp((t - 25.5 - d) / 0.2);
        if (q > 0) { const sx = -900 + r() * 2900, sy = y0 + (sx - 540) * tilt - 60; ctx.fillStyle = "#B9B1A3"; ctx.fillRect(sx - 30, sy - 30 * q, 60, 60 * q); }
      }
    }
    lexo(ctx, 1 - spring(t - 22.66, 260, 26));
    if (t < 24) tapes(ctx, t, { exit: 22.92 });
    // "një premtim" drops out of the line
    fromLine(ctx, spring(t - 24.6, 240, 21), 1, () => text(ctx, "një premtim", 540, 1050, { family: SERIF, size: 124, weight: 700, italic: true, color: C.charcoal, align: "center" }), 220);
    ctx.restore();
    goldLine(ctx);

    // phrases fly into one point and compress into the gold square
    if (!HL) HL = tapes(ctx, 22.66, { dry: true }).slice(0, 9);
    let arrived = 0;
    HL.forEach((h, i) => {
      const k = spring(t - (22.72 + i * 0.05), 120, 17);
      if (k >= 0.97) { arrived++; return; }
      const sx = h.x + h.w / 2, sy = h.y;
      const x = lerp(sx, SQX, k), y = lerp(sy, SQY, k) - Math.sin(Math.PI * clamp(k)) * 260;
      const w = lerp(h.w + 12, SQ * 0.5, clamp(k)), hh = lerp(24, SQ * 0.5, clamp(k));
      ctx.save(); ctx.translate(x, y); ctx.rotate((1 - k) * (i % 2 ? 0.5 : -0.5) * Math.sin(Math.PI * k));
      ctx.fillStyle = C.gold; ctx.fillRect(-w / 2, -hh / 2, w, hh);
      ctx.restore();
    });
    if (arrived > 0) {
      const pop = spring(t - 23.46, 380, 11);
      const grow = Math.sqrt(arrived / HL.length);
      const s = SQ * grow * (t > 23.46 ? lerp(1.35, 1, clamp(pop, 0, 1.3)) : 1) * Z;
      ctx.save(); ctx.translate(SQX, 894 - s / 2 + 6 * (1 - Z));
      ctx.fillStyle = C.gold; ctx.fillRect(-s / 2, -s / 2, s, s);
      ctx.restore();
    }
  },
};
