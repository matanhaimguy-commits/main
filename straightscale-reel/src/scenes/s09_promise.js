// S9 · The promise (26.60–31.10) "Jo 'cilësi', por: 'Instalim për dhjetë ditë, me datë në kontratë.'"
import { C, SERIF, SANS, text, rr, ep, popIn, prog, E, shadow, noShadow, marble, measure, lerp } from "../lib.js";

const LINE1 = [["Instalim", 28.24], ["për", 28.72], ["10", 28.96], ["ditë,", 29.2]];
const LINE2 = [["me", 29.68], ["datë", 29.84], ["në", 30.08], ["kontratë.", 30.24]];

function words(ctx, list, cx, y, t, size) {
  const gap = size * 0.28;
  const f = (w) => (/^\d/.test(w) ? { family: SANS, size: size * 0.92, weight: 800 } : { family: SERIF, size, weight: 700 });
  const ws = list.map(([w]) => measure(ctx, w, f(w)));
  let x = cx - (ws.reduce((a, b) => a + b, 0) + gap * (list.length - 1)) / 2;
  list.forEach(([w, at], i) => {
    const k = ep(t, at - 0.06, at + 0.22);
    text(ctx, w, x, y + (1 - k) * 26, { ...f(w), color: C.charcoal, alpha: k });
    x += ws[i] + gap;
  });
}

export default {
  id: "s09_promise", start: 26.6, end: 31.1,
  draw(ctx, t) {
    marble(ctx);
    // "cilësi" crossed out
    const a = popIn(t, 26.7, 0.3);
    const up = ep(t, 27.75, 28.2, E.inOutCubic);
    ctx.save();
    ctx.translate(540, lerp(470, 360, up)); ctx.scale(lerp(a, 0.7, up), lerp(a, 0.7, up));
    text(ctx, "“cilësi”", 0, 0, { family: SERIF, size: 150, weight: 700, italic: true, color: "#9C9284", align: "center" });
    const s = ep(t, 27.0, 27.32, E.outQuart);
    ctx.strokeStyle = C.crimson; ctx.lineWidth = 14; ctx.lineCap = "round";
    ctx.beginPath(); ctx.moveTo(-250, -40); ctx.lineTo(-250 + 500 * s, -60 - 10 * s); ctx.stroke();
    ctx.restore();
    // promise card
    const c = ep(t, 27.75, 28.2, E.outBack);
    if (c > 0) {
      const cw = 900, ch = 470, cx = 540 - cw / 2, cy = 560 + (1 - c) * 60;
      ctx.save(); ctx.globalAlpha = Math.min(1, c * 1.5);
      shadow(ctx, 50, 22, "rgba(60,45,30,0.28)");
      ctx.fillStyle = C.ivory; rr(ctx, cx, cy, cw, ch, 30); ctx.fill(); noShadow(ctx);
      ctx.fillStyle = C.gold; rr(ctx, cx, cy, 14, ch, 7); ctx.fill();
      // "SHEMBULL" chip (ivory on crimson)
      const chip = measure(ctx, "SHEMBULL", { size: 26, weight: 800, ls: 4 }) + 40;
      ctx.fillStyle = C.crimson; rr(ctx, cx + 60, cy + 50, chip, 52, 26); ctx.fill();
      text(ctx, "SHEMBULL", cx + 60 + chip / 2, cy + 86, { size: 26, weight: 800, color: C.ivory, align: "center", ls: 4 });
      text(ctx, "Një premtim i qartë", cx + 60 + chip + 22, cy + 86, { size: 26, weight: 600, color: C.stone });
      words(ctx, LINE1, 540, cy + 250, t, 78);
      words(ctx, LINE2, 540, cy + 360, t, 78);
      ctx.restore();
    }
    // contract with date stamp
    const d = ep(t, 30.2, 30.55, E.outBack);
    if (d > 0) {
      ctx.save(); ctx.translate(540, 1240); ctx.rotate(-0.05); ctx.scale(d, d);
      shadow(ctx, 30, 12, "rgba(60,45,30,0.25)");
      ctx.fillStyle = "#FFFDF8"; rr(ctx, -150, -110, 300, 220, 14); ctx.fill(); noShadow(ctx);
      text(ctx, "KONTRATË", -120, -62, { size: 24, weight: 800, color: C.ink, ls: 3 });
      ctx.fillStyle = "#D9D1C3"; for (let i = 0; i < 4; i++) ctx.fillRect(-120, -36 + i * 26, 170 - (i % 2) * 50, 10);
      const st = popIn(t, 30.55, 0.3);
      ctx.save(); ctx.translate(80, 40); ctx.rotate(-0.25); ctx.scale(lerp(1.8, 1, st), lerp(1.8, 1, st)); ctx.globalAlpha = Math.min(1, st * 2);
      ctx.strokeStyle = C.crimson; ctx.lineWidth = 6; ctx.beginPath(); ctx.arc(0, 0, 62, 0, Math.PI * 2); ctx.stroke();
      text(ctx, "DATA", 0, -10, { size: 22, weight: 900, color: C.crimson, align: "center", ls: 2 });
      text(ctx, "✓", 0, 32, { size: 40, weight: 900, color: C.crimson, align: "center" });
      ctx.restore();
      ctx.restore();
    }
  },
};
