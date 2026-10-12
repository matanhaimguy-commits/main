// S12 · (37.60–42.66) "Analizë falas, dyzet e pesë minuta, pa detyrim. Të tregojmë edhe reklamat e konkurrentëve."
// The offer, set like an editorial page on the line. A crimson clock fills 45 of 60 minutes; out of its empty
// quarter slide your competitors' ads (the cut-out collage again), labelled with the label maker.
import { C, SERIF, SANS, W, H, text, measure, rr, clamp, lerp, rng } from "../lib.js";
import { spring, paperBg, goldLine, fromLine, scrap, halftone, ransomWord, dymo } from "../fx.js";
import { lockup, proofChart } from "./s11_logo.js";

const CK = { x: 300, y: 1160, r: 225 };
const ADS = [ // competitor ads fanning out of the clock's empty quarter
  { x: 320, y: 470, rot: -0.12, color: "#EFE8D8", seed: 81, word: 13, at: 40.4 },
  { x: 730, y: 420, rot: 0.1, color: C.ivory, seed: 82, word: 58, at: 40.55 },
  { x: 540, y: 660, rot: -0.03, color: "#D9D2C5", seed: 83, word: 31, at: 40.7 },
];

export default {
  id: "s12_offer", start: 37.6, end: 42.66,
  draw(ctx, t) {
    paperBg(ctx, C.marble, 6);
    // lockup + chart leave upward
    const out = spring(t - 37.6, 170, 20);
    if (out < 1.2 && t < 38.3) { ctx.save(); ctx.translate(0, -out * 1300); lockup(ctx, 99, 1); ctx.restore(); proofChart(ctx, 99, out); }
    // Analizë / falas. rise out of the line as one block
    const hb = spring(t - 37.62, 200, 21) - spring(t - 40.28, 220, 24);   // sinks back to make room
    fromLine(ctx, hb, -1, () => {
      text(ctx, "Analizë", 66, 668, { family: SERIF, size: 168, weight: 900, color: C.charcoal });
      text(ctx, "falas.", 70, 846, { family: SERIF, size: 168, weight: 900, italic: true, color: C.crimson });
    }, 640);

    // competitor ads come out from behind the clock
    ADS.forEach((a, i) => {
      const k = spring(t - a.at, 150, 18);
      if (k <= 0.001) return;
      const x = lerp(CK.x - 60, a.x, k), y = lerp(CK.y - 80, a.y, k), s = lerp(0.35, 1, clamp(k));
      ctx.save(); ctx.translate(x, y); ctx.scale(s, s);
      scrap(ctx, 0, 0, 470, 380, a.rot + (1 - clamp(k)) * 0.6, a.color, a.seed, (c) => {
        halftone(c, -235, -190, 470, 380, "rgba(31,31,31,0.08)", 14);
        text(c, "Sponsorizuar", -190, -120, { size: 28, weight: 700, color: "rgba(31,31,31,0.7)" });
        ransomWord(c, "CILËSI", 0, 40, 74, a.word, t, () => -9);
      }, { shadowA: 0.4 });
      ctx.restore();
    });
    const lk = spring(t - 41.1, 320, 20);
    if (lk > 0.01) dymo(ctx, "REKLAMAT E KONKURRENTËVE", 540, 846, -0.03, 36, 90, lerp(1.6, 1, clamp(lk)));

    goldLine(ctx);
    // the clock: 45 of 60 minutes
    const ck = spring(t - 38.1, 300, 22);
    if (ck > 0.01) {
      const p = clamp(spring(t - 38.18, 50, 14.2));
      ctx.save(); ctx.translate(CK.x, CK.y); ctx.scale(clamp(ck, 0, 1.1), clamp(ck, 0, 1.1));
      ctx.strokeStyle = "#B9B1A3"; ctx.lineWidth = 6; ctx.setLineDash([4, 22]); ctx.beginPath(); ctx.arc(0, 0, CK.r, 0, 7); ctx.stroke(); ctx.setLineDash([]);
      if (p > 0.001) { ctx.fillStyle = C.crimson; ctx.beginPath(); ctx.moveTo(0, 0); ctx.arc(0, 0, CK.r, -Math.PI / 2, -Math.PI / 2 + Math.PI * 1.5 * p); ctx.closePath(); ctx.fill(); }
      const n = Math.round(45 * p);
      text(ctx, String(n), 52, 92, { size: 150, weight: 900, color: C.ivory, align: "center", ls: -4 });
      text(ctx, "MIN", 52, 146, { size: 40, weight: 800, color: C.ivory, align: "center", ls: 6 });
      ctx.restore();
    }
    // PA DETYRIM + where
    const words = [["PA", 39.38, 1090], ["DETYRIM", 39.5, 1168]];
    for (const [w, at, y] of words) {
      const q = spring(t - at, 380, 22);
      if (q > 0.01) { ctx.save(); ctx.translate(586, y); ctx.scale(1, clamp(q, 0, 1.2)); text(ctx, w, 0, 0, { size: 74, weight: 900, color: C.charcoal, ls: 1 }); ctx.restore(); }
    }
    const wk = spring(t - 39.8, 300, 22);
    if (wk > 0.01) {
      ctx.save(); ctx.translate((1 - clamp(wk)) * 60, 0);
      text(ctx, "Në zyrën tonë në Tiranë", 588, 1236, { size: 27, weight: 600, color: "#6D665C" });
      text(ctx, "ose te biznesi yt.", 588, 1278, { size: 27, weight: 600, color: "#6D665C" });
      ctx.restore();
    }
  },
};
