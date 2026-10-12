// S13 · CTA (42.66–47.60) "Shkruaj ANALIZA në komente. Të shkruajmë në privat."
// Macro comment field fills the frame; ANALIZA is typed in huge type and sent; the gold line underlines the ask;
// a StraightScale DM drops in.
import { C, SERIF, SANS, W, H, text, rr, measure, clamp, lerp } from "../lib.js";
import { spring, paperBg } from "../fx.js";
import { logo } from "../lib.js";

export default {
  id: "s13_cta", start: 42.66, end: 47.6,
  draw(ctx, t) {
    paperBg(ctx, "#232220", 11);
    // SHKRUAJ (big italic, left)
    const a = spring(t - 42.7, 260, 20);
    ctx.save(); ctx.translate(64 - (1 - a) * 300, 470);
    text(ctx, "Shkruaj", 0, 0, { family: SERIF, size: 168, weight: 900, italic: true, color: C.ivory });
    ctx.restore();
    // giant comment field
    const f = spring(t - 42.78, 220, 22);
    const sent = spring(t - 43.95, 240, 22);
    const fy = 560 + (1 - f) * 500;
    ctx.save();
    ctx.fillStyle = C.ivory; rr(ctx, 44, fy, W - 88, 290, 145); ctx.fill();
    const typed = Math.round(lerp(0, 7, clamp((t - 43.28) / 0.48)));
    const word = "ANALIZA".slice(0, typed);
    ctx.save(); ctx.beginPath(); rr(ctx, 44, fy, W - 88, 290, 145); ctx.clip();
    if (typed === 0 || sent > 0.6) text(ctx, "Shto një koment…", 120, fy + 165, { size: 54, weight: 500, color: "#A39B8F" });
    else {
      ctx.save(); ctx.translate(0, -sent * 400);
      text(ctx, word, 110, fy + 198, { size: 158, weight: 900, color: C.charcoal, ls: -4 });
      const cw = measure(ctx, word, { size: 158, weight: 900, ls: -4 });
      if (Math.floor(t * 4) % 2 === 0 && sent < 0.05) { ctx.fillStyle = C.charcoal; ctx.fillRect(122 + cw, fy + 70, 9, 160); }
      ctx.restore();
    }
    ctx.restore();
    // send button presses on 43.85
    const press = t > 43.85 && t < 44.02 ? 0.86 : 1;
    ctx.save(); ctx.translate(W - 150, fy + 145); ctx.scale(press, press);
    ctx.fillStyle = typed > 0 ? C.crimson : "#C9C1B4"; ctx.beginPath(); ctx.arc(0, 0, 96, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = C.ivory; ctx.beginPath(); ctx.moveTo(-34, -44); ctx.lineTo(46, 0); ctx.lineTo(-34, 44); ctx.lineTo(-18, 0); ctx.closePath(); ctx.fill();
    ctx.restore();
    ctx.restore();
    // NË KOMENTE + the gold line underlining the ask
    const b = spring(t - 43.9, 260, 20);
    ctx.save(); ctx.translate(64 + (1 - b) * 300, 1010);
    text(ctx, "NË KOMENTE", 0, 0, { size: 104, weight: 900, color: C.ivory, ls: 2 });
    ctx.restore();
    const ln = clamp((t - 44.2) / 0.25);
    ctx.fillStyle = C.gold; ctx.fillRect(0, 1046, W * ln, 12);
    // DM from StraightScale
    const d = spring(t - 44.72, 220, 20);
    if (d > 0.001) {
      const dy = 1110 + (1 - d) * 260;
      ctx.save(); ctx.fillStyle = C.ivory; rr(ctx, 64, dy, 860, 150, 30); ctx.fill();
      logo(ctx, 150, dy + 75, 86, { wordmark: false });
      text(ctx, "StraightScale", 220, dy + 66, { size: 38, weight: 800, color: C.charcoal });
      text(ctx, "Të shkruajmë në privat", 220, dy + 114, { size: 36, weight: 500, color: "#6d665c" });
      const bd = spring(t - 45.0, 300, 18);
      ctx.save(); ctx.translate(860, dy + 75); ctx.scale(bd, bd);
      ctx.fillStyle = C.crimson; ctx.beginPath(); ctx.arc(0, 0, 30, 0, Math.PI * 2); ctx.fill();
      text(ctx, "1", 0, 12, { size: 34, weight: 800, color: C.ivory, align: "center" });
      ctx.restore(); ctx.restore();
    }
  },
};
