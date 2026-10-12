// S7 · (18.50–22.65) "Lexo komentet dhe vlerësimet e klientëve, për ty dhe për konkurrentët."
// Clean world. "Lexo" rises out of the gold line; under it, receipt-paper tapes of reviews scroll past and get
// read: the key phrase in each one is highlighted as it crosses the frame. Tabs split them: TI / KONKURRENTËT.
// Reviews are abstract (stars + grey text bars): no invented quotes.
import { C, SERIF, SANS, W, H, text, measure, rr, clamp, lerp, rng } from "../lib.js";
import { spring, paperBg, fromLine, goldLine } from "../fx.js";

const TAPES = [
  { y: 1012, speed: 250, enter: 18.86, seed: 3, tab: ["TI", 20.94] },
  { y: 1176, speed: 330, enter: 19.42, seed: 7, tab: ["KONKURRENTËT", 21.66] },
];
const TH = 104, ITEM = 600, S = 1.32, LW = W / S;          // tape content is drawn at 1.32×

function star(ctx, x, y, r, fill) {
  ctx.beginPath();
  for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + (i * Math.PI) / 5, rr2 = i % 2 ? r * 0.45 : r; ctx.lineTo(x + Math.cos(a) * rr2, y + Math.sin(a) * rr2); }
  ctx.closePath();
  if (fill) { ctx.fillStyle = C.charcoal; ctx.fill(); } else { ctx.strokeStyle = "#B9B1A3"; ctx.lineWidth = 2.5; ctx.stroke(); }
}

export function lexo(ctx, k) {
  fromLine(ctx, k, -1, () => text(ctx, "Lexo", 34, 862, { family: SERIF, size: 420, weight: 900, italic: true, color: C.charcoal }), 560);
}

// draws the tapes; returns highlighted phrases (screen rects) that have been "read"
export function tapes(ctx, t, { exit = null, dry = false } = {}) {
  const hl = [];
  TAPES.forEach((tp, ti) => {
    const ent = spring(t - tp.enter, 210, 23);
    if (ent <= 0.001) return;
    let ox = (1 - ent) * 1250;
    if (exit != null) ox -= spring(t - exit - ti * 0.07, 150, 20) * 1500;
    const scroll = (t - 18.5) * tp.speed / S;
    ctx.save(); ctx.translate(0, tp.y); ctx.scale(S, S);
    const L = ox / S, yc = 0;
    if (!dry) {
      ctx.fillStyle = "rgba(60,45,30,0.13)"; ctx.fillRect(L - 40, yc - TH / 2 + 7, LW + 80, TH);
      ctx.fillStyle = C.ivory; ctx.fillRect(L - 40, yc - TH / 2, LW + 80, TH);
    }
    const first = Math.floor(scroll / ITEM) - 1;
    for (let n = first; n < first + 3; n++) {
      const x0 = n * ITEM - scroll + L;
      if (x0 > LW + 20 || x0 + ITEM < -20) continue;
      const r = rng(tp.seed * 1000 + n + 500);
      const rating = [5, 4, 2, 5, 3, 5, 4, 1][Math.floor(r() * 8)];
      const w1 = 220 + r() * 200, w2 = 140 + r() * 180;
      const row = r() < 0.5 ? 0 : 1, rw = row ? w2 : w1;
      const ha = 20 + r() * (rw * 0.4), hw = Math.min(rw - ha, 100 + r() * 90);
      const tx = x0 + 104, ry = [yc + 12, yc + 34][row];
      const p = clamp((LW * 0.72 - (tx + ha)) / 140);       // read as it crosses
      if (p > 0.9) hl.push({ x: (tx + ha) * S, y: tp.y + ry * S, w: hw * S, h: 24 * S, tape: ti });
      if (dry) continue;
      // avatar
      ctx.fillStyle = ["#8E867B", "#B9B1A3", "#1F1F1F", "#CFC6B6"][n & 3]; ctx.beginPath(); ctx.arc(x0 + 52, yc, 32, 0, 7); ctx.fill();
      ctx.fillStyle = C.ivory; ctx.beginPath(); ctx.arc(x0 + 52, yc - 8, 11, 0, 7); ctx.fill();
      ctx.beginPath(); ctx.arc(x0 + 52, yc + 22, 19, Math.PI, 0); ctx.fill();
      for (let s2 = 0; s2 < 5; s2++) star(ctx, tx + 12 + s2 * 30, yc - 24, 12, s2 < rating);
      // highlighter behind the key phrase
      if (p > 0) { ctx.fillStyle = C.gold; ctx.fillRect(tx + ha - 6, ry - 12, (hw + 12) * p, 24); }
      ctx.fillStyle = "#CFC6B6"; rr(ctx, tx, yc + 7, w1, 10, 5); ctx.fill(); rr(ctx, tx, yc + 29, w2, 10, 5); ctx.fill();
      if (p > 0) { ctx.fillStyle = C.charcoal; rr(ctx, tx + ha, ry - 5, hw * p, 10, 5); ctx.fill(); }
      ctx.fillStyle = "#E4DCCD"; ctx.fillRect(x0 + ITEM - 22, yc - 34, 3, 68);
    }
    // tab: TI / KONKURRENTËT
    const tk = spring(t - tp.tab[1], 300, 24);
    if (!dry && tk > 0.01) {
      const tw = measure(ctx, tp.tab[0], { size: 30, weight: 800, ls: 3 }) + 44;
      ctx.save(); ctx.translate(L - (1 - clamp(tk)) * tw, 0);
      ctx.fillStyle = C.charcoal; ctx.fillRect(0, yc - TH / 2, tw, TH);
      text(ctx, tp.tab[0], 22, yc + 11, { size: 30, weight: 800, color: C.ivory, ls: 3 });
      ctx.restore();
    }
    ctx.restore();
  });
  return hl;
}

export default {
  id: "s07_reviews", start: 18.5, end: 22.65,
  draw(ctx, t) {
    paperBg(ctx, C.marble, 6);
    lexo(ctx, spring(t - 18.46, 210, 21));
    tapes(ctx, t);
    goldLine(ctx);
  },
};
