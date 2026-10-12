// S3 · Patchwork (4.70–9.55) "Problemi është që flet njësoj si të gjithë: 'cilësi', 'çmimet më të mira'."
import { C, SERIF, SANS, text, rr, ep, popIn, prog, E, shadow, noShadow, charcoalBg, stitch, lerp, measure } from "../lib.js";

const PATCHES = [
  { label: "Faqja: një freelancer", fill: "#8FB3B0", icon: "web", rot: -2.2, from: [-700, 0] },
  { label: "Reklamat: një agjenci", fill: "#E3A48F", icon: "ad", rot: 1.6, from: [700, 0] },
  { label: "Instagrami: nipi", fill: "#B9AED6", icon: "ig", rot: 1.1, from: [-700, 300] },
  { label: "Telefoni: kush është afër", fill: "#A9BF8E", icon: "phone", rot: -1.4, from: [700, 300] },
];

function icon(ctx, kind, cx, cy) {
  ctx.save(); ctx.strokeStyle = "rgba(31,31,31,0.75)"; ctx.fillStyle = "rgba(31,31,31,0.75)"; ctx.lineWidth = 7; ctx.lineCap = "round"; ctx.lineJoin = "round";
  if (kind === "web") {
    rr(ctx, cx - 120, cy - 80, 240, 160, 16); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(cx - 120, cy - 40); ctx.lineTo(cx + 120, cy - 40); ctx.stroke();
    for (let i = 0; i < 3; i++) { ctx.beginPath(); ctx.arc(cx - 96 + i * 22, cy - 60, 6, 0, Math.PI * 2); ctx.fill(); }
    ctx.fillRect(cx - 90, cy - 15, 120, 16); ctx.fillRect(cx - 90, cy + 15, 170, 12); ctx.fillRect(cx - 90, cy + 40, 140, 12);
  } else if (kind === "ad") {
    rr(ctx, cx - 110, cy - 90, 220, 180, 16); ctx.stroke();
    text(ctx, "Sponsorizuar", cx - 90, cy - 50, { size: 22, weight: 700, color: "rgba(31,31,31,0.75)" });
    ctx.fillRect(cx - 90, cy - 30, 180, 80);
  } else if (kind === "ig") {
    rr(ctx, cx - 90, cy - 90, 180, 180, 46); ctx.stroke();
    ctx.beginPath(); ctx.arc(cx, cy, 42, 0, Math.PI * 2); ctx.stroke();
    ctx.beginPath(); ctx.arc(cx + 52, cy - 52, 9, 0, Math.PI * 2); ctx.fill();
  } else {
    ctx.beginPath();
    ctx.moveTo(cx - 70, cy - 80); ctx.quadraticCurveTo(cx - 110, cy - 10, cx - 30, cy + 60); ctx.quadraticCurveTo(cx + 40, cy + 120, cx + 90, cy + 70);
    ctx.lineWidth = 34; ctx.stroke();
    text(ctx, "Alo?", cx + 40, cy - 40, { size: 40, weight: 800, color: "rgba(31,31,31,0.75)" });
  }
  ctx.restore();
}

function stamp(ctx, s, cx, cy, k, size, rot) {
  if (k <= 0) return;
  const sc = lerp(1.9, 1, E.outCubic(Math.min(1, k * 1.4)));
  ctx.save(); ctx.translate(cx, cy); ctx.rotate(rot); ctx.scale(sc, sc); ctx.globalAlpha = Math.min(1, k * 2.5);
  const w = measure(ctx, s, { size, weight: 900, ls: 3 }) + 44;
  ctx.strokeStyle = C.crimson; ctx.lineWidth = 6; rr(ctx, -w / 2, -size * 0.85, w, size * 1.3, 10); ctx.stroke();
  text(ctx, s, 0, size * 0.32, { size, weight: 900, color: C.crimson, align: "center", ls: 3 });
  ctx.restore();
}

export default {
  id: "s03_patchwork", start: 4.7, end: 9.55,
  draw(ctx, t) {
    charcoalBg(ctx);
    // shake on stamp impacts
    const hit = (a) => { const p = prog(t, a, a + 0.25); return p > 0 && p < 1 ? Math.sin(p * 40) * (1 - p) * 10 : 0; };
    ctx.translate(hit(7.25) + hit(8.1) * 0.7, hit(7.25) * 0.5);
    // title
    const tt = ep(t, 4.75, 5.2);
    text(ctx, "Marketing copë-copë", 540, 285 + (1 - tt) * 20, { family: SERIF, size: 74, weight: 700, italic: true, color: C.ivory, align: "center", alpha: tt });
    ctx.fillStyle = C.gold; ctx.fillRect(540 - 180 * tt, 312, 360 * tt, 5);
    const gx = 95, gy = 380, pw = 437, ph = 400, gap = 16;
    PATCHES.forEach((p, i) => {
      const col = i % 2, row = Math.floor(i / 2);
      const x = gx + col * (pw + gap), y = gy + row * (ph + gap);
      const k = ep(t, 4.8 + i * 0.16, 5.35 + i * 0.16, E.outBack);
      const ox = (1 - k) * p.from[0], oy = (1 - k) * p.from[1];
      ctx.save();
      ctx.translate(x + pw / 2 + ox, y + ph / 2 + oy); ctx.rotate(((p.rot + (1 - k) * 12) * Math.PI) / 180);
      shadow(ctx, 24, 10, "rgba(0,0,0,0.45)");
      ctx.fillStyle = p.fill; rr(ctx, -pw / 2, -ph / 2, pw, ph, 14); ctx.fill(); noShadow(ctx);
      // fabric texture lines
      ctx.strokeStyle = "rgba(255,255,255,0.08)"; ctx.lineWidth = 2;
      for (let j = -ph / 2 + 12; j < ph / 2; j += 14) { ctx.beginPath(); ctx.moveTo(-pw / 2, j); ctx.lineTo(pw / 2, j + (i % 2 ? 6 : -6)); ctx.stroke(); }
      icon(ctx, p.icon, 0, -40);
      text(ctx, p.label, 0, ph / 2 - 40, { size: 27, weight: 700, color: C.ink, align: "center" });
      // uneven stitching around the patch
      const sp = ep(t, 5.6 + i * 0.1, 6.5 + i * 0.1, E.inOutCubic);
      const m = 14;
      stitch(ctx, -pw / 2 + m, -ph / 2 + m, pw / 2 - m, -ph / 2 + m + (i - 1.5) * 3, C.ivory, sp, 4);
      stitch(ctx, pw / 2 - m, ph / 2 - m, -pw / 2 + m, ph / 2 - m - (i - 1.5) * 4, C.ivory, sp, 4);
      // stamps: "CILËSI" (7.2) then "ÇMIMET MË TË MIRA" (8.05)
      stamp(ctx, "CILËSI", 10, -60, prog(t, 7.2 + i * 0.06, 7.5 + i * 0.06), 64, (-8 + i * 5) * Math.PI / 180);
      stamp(ctx, "ÇMIMET MË TË MIRA", 0, 60, prog(t, 8.05 + i * 0.06, 8.35 + i * 0.06), 30, (6 - i * 4) * Math.PI / 180);
      ctx.restore();
    });
  },
};
