// S11 · (35.05–37.60) "Këtë bëjmë ne te StraightScale."
// The screens drop away. The logo is built on the gold line: the crimson square rises out of it, the S is cut,
// the gold square drops into its corner. Then the lockup moves up and the line tilts up three times:
// the three client results from the brief as a before/after slope chart.
import { C, SERIF, SANS, W, H, text, measure, rr, clamp, lerp } from "../lib.js";
import { spring, paperBg, goldLine, fromLine } from "../fx.js";
import { screens, camS10 } from "./s10_everywhere.js";

const PROOF = [ // only the numbers given in the brief
  { a: 15, b: 55, aL: "€15K", bL: "€55K", what: "firmë konsulence" },
  { a: 30, b: 100, aL: "€30K", bL: "€100K", what: "biznes kursesh" },
  { a: 0, b: 140, aL: "€0", bL: "€140K", what: "biznes i ri konsulence" },
];
const AX = 110, BX2 = 640, vy = (v) => 894 - v * 3.05;

export function lockup(ctx, t, m) {
  // m: 0 = big on the line, 1 = small at the top
  const size = lerp(280, 116, m), cx = lerp(540, 132, m), cy = lerp(894 - 140, 300, m);
  const rise = spring(t - 35.1, 230, 21);
  const x = cx - size / 2, y = cy - size / 2;
  const sq = () => {
    ctx.fillStyle = C.crimson; rr(ctx, x, y, size, size, size * 0.22); ctx.fill();
    const sk = spring(t - 35.34, 380, 20);
    if (sk > 0.01) { ctx.save(); ctx.translate(cx, cy); const s = lerp(1.6, 1, clamp(sk)); ctx.scale(s, s); text(ctx, "S", 0, size * 0.27, { size: size * 0.78, weight: 900, color: C.ivory, align: "center" }); ctx.restore(); }
  };
  if (m > 0.001) sq(); else fromLine(ctx, rise, -1, sq, 320);
  // gold square drops into the corner
  const gk = spring(t - 35.58, 300, 15);
  if (gk > 0.001) {
    const g = size * 0.2;
    ctx.fillStyle = C.gold; rr(ctx, x + size - g * 1.25, y + g * 0.25 - (1 - gk) * 420, g, g, g * 0.18); ctx.fill();
  }
  // wordmark drops out of the line, then slides beside the mark
  const wk = spring(t - 35.88, 260, 22);
  const ws = lerp(92, 54, m);
  const wo = { size: ws, weight: 800, color: C.charcoal, ls: -0.5 };
  const ww = measure(ctx, "StraightScale", wo);
  const wx = lerp(540 - ww / 2, 214, m), wy = lerp(1012, 320, m);
  if (m > 0.001) text(ctx, "StraightScale", wx, wy, wo);
  else fromLine(ctx, wk, 1, () => text(ctx, "StraightScale", wx, wy, wo), 160);
}

export function proofChart(ctx, t, out = 0) {
  ctx.save(); ctx.translate(0, -out * 1300);
  const hk = spring(t - 36.32, 300, 24);
  if (hk > 0.01) text(ctx, "Të ardhurat mujore të klientëve", 72, 408, { size: 32, weight: 700, color: "#7A7266", alpha: clamp(hk) });
  if (hk > 0.01) {
    text(ctx, "PARA", AX, 958, { size: 32, weight: 800, color: "#7A7266", align: "center", ls: 3 });
    text(ctx, "PAS", BX2, 958, { size: 32, weight: 800, color: "#7A7266", align: "center", ls: 3 });
  }
  PROOF.forEach((p, i) => {
    const k = clamp(spring(t - (36.4 + i * 0.16), 140, 22));
    if (k <= 0.001) return;
    const x1 = AX, y1 = vy(p.a), x2 = lerp(AX, BX2, k), y2 = lerp(vy(p.a), vy(p.b), k);
    ctx.strokeStyle = C.gold; ctx.lineWidth = 11; ctx.lineCap = "round";
    ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
    ctx.fillStyle = C.charcoal; ctx.beginPath(); ctx.arc(x1, y1, 11, 0, 7); ctx.fill();
    ctx.beginPath(); ctx.arc(x2, y2, 15, 0, 7); ctx.fill();
    text(ctx, p.aL, x1 - 26, y1 + 11, { size: 30, weight: 800, color: C.charcoal, align: "right" });
    const lk = spring(t - (36.4 + i * 0.16 + 0.32), 360, 22);
    if (lk > 0.01) {
      ctx.save(); ctx.translate(BX2 + 34, vy(p.b) + 16); ctx.scale(clamp(lk, 0, 1.15), clamp(lk, 0, 1.15));
      const vw = text(ctx, p.bL, 0, 0, { size: 60, weight: 900, color: C.charcoal, ls: -1 });
      text(ctx, "/muaj", vw + 6, 0, { size: 30, weight: 700, color: "#7A7266" });
      text(ctx, p.what, 2, 40, { size: 28, weight: 600, color: "#7A7266" });
      ctx.restore();
    }
  });
  ctx.restore();
}

export default {
  id: "s11_logo", start: 35.05, end: 37.6,
  draw(ctx, t) {
    paperBg(ctx, C.marble, 6);
    // the three screens fall away
    if (t < 35.7) {
      const { Z, cx } = camS10(35.05);
      ctx.save(); ctx.translate(540, 900); ctx.scale(Z, Z); ctx.translate(-cx, -900);
      screens(ctx, 99, { drop: clamp((t - 35.05) / 0.6) });
      ctx.restore();
    }
    goldLine(ctx);
    const m = spring(t - 36.22, 200, 22);
    lockup(ctx, t, clamp(m, 0, 1.05));
    proofChart(ctx, t);
  },
};
