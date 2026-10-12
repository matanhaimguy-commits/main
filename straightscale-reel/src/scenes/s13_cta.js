// S13 · CTA (42.66–47.60) "Shkruaj ANALIZA në komente. Të shkruajmë në privat."
import { C, SERIF, SANS, text, rr, ep, popIn, prog, E, shadow, noShadow, charcoalBg, measure, logo, lerp, rng } from "../lib.js";

export default {
  id: "s13_cta", start: 42.66, end: 47.6,
  draw(ctx, t) {
    charcoalBg(ctx, 0.3);
    // headline
    const h1 = ep(t, 42.7, 43.05);
    text(ctx, "Shkruaj", 540, 330 + (1 - h1) * 24, { family: SERIF, size: 84, weight: 700, color: C.ivory, align: "center", alpha: h1 });
    const word = "ANALIZA";
    const sz = 150, ls = 10;
    const tot = measure(ctx, word, { family: SERIF, size: sz, weight: 900, ls });
    let x = 540 - tot / 2;
    for (let i = 0; i < word.length; i++) {
      const at = 43.22 + i * 0.065;
      const k = ep(t, at, at + 0.3, E.outBack);
      const w = measure(ctx, word[i], { family: SERIF, size: sz, weight: 900, ls });
      ctx.save(); ctx.translate(x + w / 2, 490 + (1 - k) * -60); ctx.globalAlpha = Math.min(1, k * 1.4);
      text(ctx, word[i], 0, 0, { family: SERIF, size: sz, weight: 900, color: C.gold, align: "center", ls });
      ctx.restore();
      x += w;
    }
    const h3 = ep(t, 43.9, 44.25);
    text(ctx, "në komente", 540, 580 + (1 - h3) * 20, { size: 50, weight: 700, color: C.ivory, align: "center", alpha: h3 });
    // comment sheet
    const sh = ep(t, 42.75, 43.2, E.outQuart);
    const px = 90, pw = 900, py = 690 + (1 - sh) * 120, ph = 520;
    ctx.save(); ctx.globalAlpha = sh;
    shadow(ctx, 50, 20, "rgba(0,0,0,0.5)");
    ctx.fillStyle = C.ivory; rr(ctx, px, py, pw, ph, 38); ctx.fill(); noShadow(ctx);
    ctx.fillStyle = "#D6CFC3"; rr(ctx, 540 - 40, py + 18, 80, 8, 4); ctx.fill();
    text(ctx, "Komente", 540, py + 74, { size: 32, weight: 700, color: C.ink, align: "center" });
    // existing (abstract) comment rows
    const posted = ep(t, 44.05, 44.4, E.outCubic);
    const shift = posted * 104;
    ctx.save(); ctx.beginPath(); ctx.rect(px, py + 100, pw, 300); ctx.clip();
    const r = rng(11);
    for (let i = 0; i < 3; i++) {
      const yy = py + 130 + i * 104 - shift;
      ctx.fillStyle = ["#C9BFAF", "#B8C7C2", "#D4C2B8"][i]; ctx.beginPath(); ctx.arc(px + 70, yy + 28, 28, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#DDD6CA"; rr(ctx, px + 120, yy + 6, 160 + r() * 80, 18, 9); ctx.fill();
      ctx.fillStyle = "#E8E2D7"; rr(ctx, px + 120, yy + 36, 380 + r() * 200, 18, 9); ctx.fill();
    }
    // the new comment "ANALIZA"
    if (posted > 0) {
      const yy = py + 130 + 3 * 104 - shift;
      ctx.fillStyle = C.charcoal; ctx.beginPath(); ctx.arc(px + 70, yy + 28, 28, 0, Math.PI * 2); ctx.fill();
      text(ctx, "Ti", px + 70, yy + 38, { size: 24, weight: 800, color: C.ivory, align: "center" });
      text(ctx, "ANALIZA", px + 120, yy + 40, { size: 38, weight: 800, color: C.ink, ls: 2 });
      const hp = popIn(t, 44.35, 0.3);
      ctx.save(); ctx.translate(px + pw - 70, yy + 28); ctx.scale(hp, hp);
      text(ctx, "♥", 0, 14, { size: 44, weight: 700, color: C.crimson, align: "center" });
      ctx.restore();
    }
    ctx.restore();
    // input row
    const iy = py + ph - 110;
    ctx.fillStyle = "#EFEAE0"; rr(ctx, px + 30, iy, pw - 60, 84, 42); ctx.fill();
    const typed = Math.floor(lerp(0, 7, prog(t, 43.3, 43.8)));
    const inputTxt = posted > 0.3 ? "" : word.slice(0, typed);
    if (inputTxt) text(ctx, inputTxt, px + 70, iy + 56, { size: 38, weight: 800, color: C.ink, ls: 2 });
    else text(ctx, "Shto një koment...", px + 70, iy + 54, { size: 32, weight: 500, color: "#A39B8F" });
    if (!inputTxt || Math.floor(t * 3) % 2 === 0) {
      const cw = inputTxt ? measure(ctx, inputTxt, { size: 38, weight: 800, ls: 2 }) : 0;
      if (inputTxt) { ctx.fillStyle = C.ink; ctx.fillRect(px + 74 + cw, iy + 20, 4, 46); }
    }
    const press = popIn(t, 43.85, 0.25);
    ctx.save(); ctx.translate(px + pw - 80, iy + 42); ctx.scale(t > 43.85 && t < 44.05 ? 0.88 : 1, t > 43.85 && t < 44.05 ? 0.88 : 1);
    ctx.fillStyle = typed > 0 ? C.crimson : "#C9C1B4"; ctx.beginPath(); ctx.arc(0, 0, 34, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = C.ivory; ctx.beginPath(); ctx.moveTo(-12, -16); ctx.lineTo(16, 0); ctx.lineTo(-12, 16); ctx.lineTo(-6, 0); ctx.closePath(); ctx.fill();
    ctx.restore();
    ctx.restore();
    // DM notification
    const dm = ep(t, 44.7, 45.05, E.outBack);
    if (dm > 0) {
      const dw = 760, dx = 540 - dw / 2, dy = 1250 + (1 - dm) * 80;
      ctx.save(); ctx.globalAlpha = Math.min(1, dm * 1.4);
      shadow(ctx, 40, 16, "rgba(0,0,0,0.5)");
      ctx.fillStyle = C.charcoal2; rr(ctx, dx, dy, dw, 130, 34); ctx.fill(); noShadow(ctx);
      ctx.strokeStyle = "rgba(212,175,55,0.6)"; ctx.lineWidth = 2; rr(ctx, dx, dy, dw, 130, 34); ctx.stroke();
      logo(ctx, dx + 75, dy + 65, 70, { wordmark: false });
      text(ctx, "StraightScale", dx + 135, dy + 55, { size: 30, weight: 800, color: C.ivory });
      text(ctx, "Të shkruajmë në privat", dx + 135, dy + 97, { size: 30, weight: 500, color: C.gold });
      const b = popIn(t, 45.0, 0.3);
      ctx.save(); ctx.translate(dx + dw - 60, dy + 65); ctx.scale(b, b);
      ctx.fillStyle = C.crimson; ctx.beginPath(); ctx.arc(0, 0, 24, 0, Math.PI * 2); ctx.fill();
      text(ctx, "1", 0, 10, { size: 28, weight: 800, color: C.ivory, align: "center" });
      ctx.restore();
      ctx.restore();
    }
  },
};
