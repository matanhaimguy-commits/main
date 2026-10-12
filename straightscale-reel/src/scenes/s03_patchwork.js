// S3 · Patchwork (4.70–9.55) "Problemi është që flet njësoj si të gjithë: 'cilësi', 'çmimet më të mira'."
// A real collage: torn scraps, tape, label-maker strips. On "cilësi" every scrap spells the same word in a
// different cut-out font; one rubber stamp slams across the whole board on "çmimet më të mira".
import { C, SERIF, SANS, W, H, text, rr, clamp, lerp, rng } from "../lib.js";
import { spring, track, paperBg, scrap, halftone, tape, dymo, ransomWord, rubberStamp } from "../fx.js";

export const BOARD = [
  { x: 330, y: 560, w: 600, h: 430, rot: -0.09, color: C.ivory, seed: 21, kind: "web", label: "FAQJA: NJË FREELANCER", land: 4.72, word: 31 },
  { x: 745, y: 650, w: 500, h: 470, rot: 0.08, color: "#EFE8D8", seed: 22, kind: "ad", label: "REKLAMAT: NJË AGJENCI", land: 5.12, word: 47 },
  { x: 300, y: 1030, w: 540, h: 430, rot: 0.06, color: C.marble, seed: 23, kind: "ig", label: "INSTAGRAMI: NIPI", land: 5.5, word: 13 },
  { x: 735, y: 1065, w: 520, h: 410, rot: -0.07, color: "#CFC6B6", seed: 24, kind: "phone", label: "TELEFONI: KUSH ËSHTË AFËR", land: 5.86, word: 58 },
];

function content(ctx, s, t) {
  ctx.strokeStyle = "rgba(31,31,31,0.7)"; ctx.fillStyle = "rgba(31,31,31,0.7)"; ctx.lineWidth = 6; ctx.lineCap = "round";
  if (s.kind === "web") {
    ctx.strokeRect(-250, -170, 500, 300); ctx.beginPath(); ctx.moveTo(-250, -125); ctx.lineTo(250, -125); ctx.stroke();
    for (let i = 0; i < 3; i++) { ctx.beginPath(); ctx.arc(-222 + i * 24, -148, 7, 0, 7); ctx.fill(); }
  } else if (s.kind === "ad") {
    halftone(ctx, -260, -235, 520, 470, "rgba(31,31,31,0.10)", 14);
    text(ctx, "Sponsorizuar", -210, -150, { size: 30, weight: 700, color: "rgba(31,31,31,0.75)" });
  } else if (s.kind === "ig") {
    rr(ctx, -150, -170, 300, 300, 80); ctx.stroke(); ctx.beginPath(); ctx.arc(0, -20, 70, 0, 7); ctx.stroke();
    ctx.beginPath(); ctx.arc(90, -110, 14, 0, 7); ctx.fill();
  } else {
    ctx.save(); ctx.lineWidth = 46; ctx.beginPath(); ctx.moveTo(-170, -150); ctx.quadraticCurveTo(-230, -40, -120, 40); ctx.quadraticCurveTo(-30, 110, 40, 60); ctx.stroke(); ctx.restore();
    text(ctx, "Alo?", 80, -90, { family: SERIF, size: 70, weight: 900, italic: true, color: "rgba(31,31,31,0.8)" });
  }
}

export function drawBoard(ctx, t, { stampAt = 8.05, wordAt = 7.2, still = false, sameAt = null } = {}) {
  BOARD.forEach((s, i) => {
    const k = still ? 1 : spring(t - s.land, 240, 19);
    if (k < 0.001) return;
    const from = [[-900, -300], [900, -200], [-900, 300], [900, 400]][i];
    const x = s.x + (1 - k) * from[0], y = s.y + (1 - k) * from[1];
    const rot = s.rot + (1 - clamp(k)) * (i % 2 ? 0.6 : -0.6);
    scrap(ctx, x, y, s.w, s.h, rot, s.color, s.seed, (c) => {
      content(c, s, t);
      // the same word, different cut-out letters, on every scrap at once
      // sameAt: every scrap re-slaps the exact same cut-out word ("të njëjtën gjë")
      const same = sameAt != null && t >= sameAt + i * 0.07;
      if (same) ransomWord(c, "CILËSI", 0, s.kind === "web" ? 40 : 60, 76, 47, t, (j) => sameAt + i * 0.07 + j * 0.02);
      else ransomWord(c, "CILËSI", 0, s.kind === "web" ? 40 : 60, s.kind === "ad" ? 74 : 76, s.word, t, (j) => (still ? -9 : wordAt + i * 0.03 + j * 0.03));
    }, { lift: 1 + (1 - clamp(k)) * 2 });
    // tape at corners (slapped right after landing)
    const tk = still ? 1 : spring(t - s.land - 0.18, 300, 22);
    if (tk > 0.01) {
      ctx.save(); ctx.globalAlpha = clamp(tk);
      tape(ctx, x - s.w * 0.42, y - s.h * 0.46, 150, 44, -0.6 + i * 0.1, s.seed + 5);
      tape(ctx, x + s.w * 0.4, y + s.h * 0.45, 150, 44, -0.5 - i * 0.1, s.seed + 6);
      ctx.restore();
    }
    s._pos = [x, y, rot];
  });
  // label-maker strips on top of everything, naming who made each piece
  BOARD.forEach((s, i) => {
    if (!s._pos) return;
    const lk = still ? 1 : spring(t - (6.0 + i * 0.22), 300, 20);
    const [x, y, rot] = s._pos;
    if (lk > 0.01 && (still || t > s.land)) dymo(ctx, s.label, Math.min(x, 650), y + s.h / 2 - 34, rot * 0.6 + (i % 2 ? 0.03 : -0.03), 28, s.seed, lerp(1.4, 1, clamp(lk)));
  });
  // one big stamp across the whole board
  rubberStamp(ctx, "ÇMIMET MË TË MIRA", W / 2, 965, 0.1, 62, still ? 1 : spring(t - stampAt, 380, 24), 9);
}

export default {
  id: "s03_patchwork", start: 4.7, end: 9.55,
  draw(ctx, t) {
    paperBg(ctx, "#232220", 11);
    // camera: starts tight on the first scrap, pulls out as the others land; punch on the word and on the stamp
    const z = track(t, [[4.7, 1.75], [4.95, 1.0], [7.2, 1.07], [7.55, 1.02], [8.05, 1.1], [8.4, 1.04]], 140, 20);
    const cx = track(t, [[4.7, 330], [4.95, 540]], 140, 22), cy = track(t, [[4.7, 560], [4.95, 820]], 140, 22);
    const sh = (a) => { const p = clamp((t - a) / 0.3); return p > 0 && p < 1 ? Math.sin(p * 46) * (1 - p) * 14 : 0; };
    ctx.translate(W / 2 + sh(8.05), 820 + sh(8.05) * 0.6); ctx.scale(z, z); ctx.translate(-cx, -cy);
    drawBoard(ctx, t);
  },
};
