// S4 · (9.55–13.60) "Rreth një mijë e tetëqind reklama aktive në Shqipëri thonë 'cilësi'."
// Droste pull-back: the collage is one of 1,800 identical boards on a wall. A charcoal slab slams in with an
// odometer 1.000 → 1.800; on "cilësi" a red sticker ripples across every board at once.
import { C, SERIF, SANS, W, H, text, measure, rr, clamp, lerp, rng } from "../lib.js";
import { spring, paperBg, scrap, dymo, ransomWord } from "../fx.js";
import { drawBoard } from "./s03_patchwork.js";

const COLS = 36, ROWS = 50, PX = 1150, PY = 1500;           // 36 × 50 = 1,800 boards
const BX = -20, BY = 300, BW = 1120, BH = 1060;            // board region (world coords)
export const WALL_C = [540 - PX / 2, 820 - PY / 2];        // wall centre
export const Z_START = 1.04, Z_END = 0.0282;
const LEVELS = [0.5, 0.15, 0.05];
let sprites = null;

export function initWall() {
  if (sprites) return;
  sprites = [];
  let prev = null;
  for (const lv of LEVELS) {
    const c = document.createElement("canvas");
    c.width = Math.ceil(BW * lv); c.height = Math.ceil(BH * lv);
    const g = c.getContext("2d");
    g.imageSmoothingQuality = "high";
    if (!prev) { g.scale(lv, lv); g.translate(-BX, -BY); drawBoard(g, 99, { still: true }); }
    else g.drawImage(prev, 0, 0, c.width, c.height);
    sprites.push(c); prev = c;
  }
}

// world -> screen: s = a + Z (p - f).  center(ctx) replaces the board of the middle tile; sticker(...) per tile.
export function drawWall(ctx, t, Z, fx, fy, ax, ay, { center = null, sticker = null } = {}) {
  const vec = Z > 0.5;
  let lvl = 0; while (lvl < LEVELS.length - 1 && LEVELS[lvl + 1] >= Z) lvl++;
  ctx.save(); ctx.imageSmoothingQuality = "high";
  for (let j = -ROWS / 2; j < ROWS / 2; j++) for (let i = -COLS / 2; i < COLS / 2; i++) {
    const isC = i === 0 && j === 0;
    const r = rng(5000 + (j + 40) * 97 + i + 40);
    const jx = isC ? 0 : (r() - 0.5) * 60, jy = isC ? 0 : (r() - 0.5) * 60, rot = isC ? 0 : (r() - 0.5) * 0.07;
    const cx = 540 + i * PX + jx, cy = 820 + j * PY + jy;
    const sx = ax + Z * (cx - fx), sy = ay + Z * (cy - fy);
    const hw = Z * 640, hh = Z * 580;
    if (sx + hw < 0 || sx - hw > W || sy + hh < 0 || sy - hh > H) continue;
    ctx.save(); ctx.translate(sx, sy); ctx.scale(Z, Z); ctx.rotate(rot); ctx.translate(-540, -820);
    if (isC && center) center(ctx);
    else if (vec) drawBoard(ctx, t, { still: true });
    else ctx.drawImage(sprites[lvl], BX, BY, BW, BH);
    ctx.restore();
    if (sticker) sticker(sx, sy, Z, rot, r, i, j);
  }
  ctx.restore();
}

export function wallZoom(t) {
  const e = spring(t - 9.58, 40, 12.65);
  const Z = Z_START * Math.pow(Z_END / Z_START, e) * (1 - 0.05 * clamp((t - 10.4) / 3.2));
  return { e, Z, fx: lerp(540, WALL_C[0], e), fy: lerp(820, WALL_C[1], e), ay: lerp(820, 960, e) };
}

// red "CILËSI" sticker on every board, rippling out from the centre
export function cilesiSticker(ctx, t, at, off = null) {
  return (sx, sy, Z, rot, r) => {
    const d = Math.hypot(sx - 540, sy - 900) / 2600;
    let k = spring(t - at - d, 420, 22);
    if (off != null) k *= 1 - clamp(spring(t - off - d * 0.3, 400, 30));
    if (k <= 0.01) return;
    const w = Z * 760, h = Z * 300, s = lerp(1.9, 1, clamp(k));
    ctx.save(); ctx.translate(sx + Z * 20, sy - Z * 40); ctx.rotate(rot + (r() - 0.5) * 0.3); ctx.scale(s, s);
    ctx.fillStyle = C.crimson; ctx.fillRect(-w / 2, -h / 2, w, h);
    if (Z * 100 > 4) text(ctx, "CILËSI", 0, h * 0.24, { size: h * 0.62, weight: 900, color: C.ivory, align: "center", ls: h * 0.05 });
    else { ctx.fillStyle = C.ivory; ctx.fillRect(-w * 0.34, -h * 0.08, w * 0.68, h * 0.16); }
    ctx.restore();
  };
}

// the odometer slab, in screen space
export function slab(ctx, t, fly = 0) {
  const k = spring(t - 9.92, 320, 20);
  if (k <= 0.001) return;
  const s = lerp(1.5, 1, clamp(k));
  ctx.save();
  ctx.translate(540 + fly * 300, 850 - fly * 1700); ctx.rotate(-0.025 + fly * 0.5); ctx.scale(s, s);
  scrap(ctx, 0, 0, 980, 640, 0, "#1A1A1A", 61, (c) => {
    // 1.000 → 1.800 (hundreds digit rolls on "tetëqind")
    const size = 300, o = { size, weight: 900, ls: 0 };
    const dw = measure(c, "0", o), w1 = measure(c, "1", o), wd = measure(c, ".", o);
    const show000 = t >= 10.06;
    const total = w1 + (show000 ? wd + dw * 3 : 0);
    let x = -total / 2; const y = 70;
    text(c, "1", x, y, { ...o, color: C.ivory }); x += w1;
    if (show000) {
      const kk = spring(t - 10.06, 420, 24);
      c.save(); c.translate(0, (1 - clamp(kk)) * -40);
      text(c, ".", x, y, { ...o, color: C.ivory }); x += wd;
      // rolling digit
      const roll = 8 * spring(t - 10.44, 110, 18);
      c.save(); c.beginPath(); c.rect(x - 6, y - size * 0.82, dw + 12, size * 0.98); c.clip();
      for (let n = Math.max(0, Math.floor(roll) - 1); n <= Math.min(9, Math.ceil(roll) + 1); n++)
        text(c, String(n), x + dw / 2, y + (n - roll) * size * 0.95, { ...o, color: C.ivory, align: "center" });
      c.restore(); x += dw;
      text(c, "0", x + dw / 2, y, { ...o, color: C.ivory, align: "center" }); x += dw;
      text(c, "0", x + dw / 2, y, { ...o, color: C.ivory, align: "center" });
      c.restore();
    }
    // REKLAMA AKTIVE NË SHQIPËRI, word by word
    const words = [["REKLAMA", 10.8], ["AKTIVE", 11.2], ["NË", 11.6], ["SHQIPËRI", 11.68]];
    const lo = { size: 44, weight: 800, ls: 5 };
    const lw = words.reduce((a, [w]) => a + measure(c, w, lo) + 22, -22);
    let lx = -lw / 2;
    for (const [w, at] of words) {
      const q = spring(t - at, 380, 24);
      if (q > 0.01) { c.save(); c.translate(lx, 178); c.scale(1, clamp(q, 0, 1.2)); text(c, w, 0, 0, { ...lo, color: C.ivory }); c.restore(); }
      lx += measure(c, w, lo) + 22;
    }
    if (t > 11.0) text(c, "Burimi: Meta Ad Library, 11.10.2026", 0, 252, { size: 28, weight: 600, color: "#A39B8F", align: "center", ls: 1 });
  }, { shadowA: 0.6, lift: 2 });
  ctx.restore();
  // "RRETH" (about) label-maker strip
  const rk = spring(t - 9.6, 320, 20);
  if (rk > 0.01) dymo(ctx, "RRETH", 250 + fly * 300, 560 - fly * 1700, -0.06, 40, 77, lerp(1.6, 1, clamp(rk)));
}

export default {
  id: "s04_wall", start: 9.55, end: 13.6,
  init: initWall,
  draw(ctx, t) {
    paperBg(ctx, "#232220", 11);
    const z = wallZoom(t);
    drawWall(ctx, t, z.Z, z.fx, z.fy, 540, z.ay, { sticker: cilesiSticker(ctx, t, 12.62) });
    slab(ctx, t);
    // "thonë" + the same cut-out word everyone uses
    const tk = spring(t - 12.16, 320, 20);
    if (tk > 0.01) dymo(ctx, "THONË", 205, 1205, -0.05, 36, 78, lerp(1.6, 1, clamp(tk)));
    ransomWord(ctx, "CILËSI", 600, 1310, 128, 47, t, (j) => 12.62 + j * 0.035);
  },
};
