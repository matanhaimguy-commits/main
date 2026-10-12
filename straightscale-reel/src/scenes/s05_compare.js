// S5 · (13.60–17.40) "Kur të gjithë thonë të njëjtën gjë, klienti krahason vetëm çmimin."
// Dive back into one board. Every scrap re-slaps the exact same cut-out word; then black marker redacts
// everything the customer stops reading. Only the red € stickers survive.
import { C, SERIF, SANS, W, H, text, measure, clamp, lerp, rng } from "../lib.js";
import { spring, track, paperBg, marker } from "../fx.js";
import { drawBoard, BOARD } from "./s03_patchwork.js";
import { drawWall, cilesiSticker, slab, WALL_C, Z_START, Z_END } from "./s04_wall.js";
import { ransomWord, dymo } from "../fx.js";

const INK = "#121212";
// camera on the board after the dive (push on "çmimin")
export const s5Zoom = (t) => track(t, [[0, 1.04], [16.56, 1.12]], 150, 22);

// the board with redactions and € stickers (also used, frozen, by S6)
export function redactedBoard(ctx, t) {
  drawBoard(ctx, t, { still: true, sameAt: 14.46 });
  BOARD.forEach((s, i) => {
    const [x, y, rot] = s._pos;
    const at = 15.3 + i * 0.13;
    ctx.save(); ctx.translate(x, y); ctx.rotate(rot);
    const hw = s.w / 2 - 30, wy = s.kind === "web" ? 40 : 60;
    marker(ctx, [[-hw, wy + 4], [0, wy - 6], [hw, wy + 2]], clamp((t - at) / 0.13), INK, 92, 20 + i);
    marker(ctx, [[-hw, -112], [hw * 0.2, -118], [hw, -108]], clamp((t - at - 0.1) / 0.13), INK, 100, 30 + i);
    ctx.restore();
    // over the label-maker strip
    const lx = Math.min(x, 650), ly = y + s.h / 2 - 34;
    const lw = measure(ctx, s.label, { size: 28, weight: 800, ls: 3 }) / 2 + 30;
    marker(ctx, [[lx - lw, ly + 3], [lx + lw, ly - 3]], clamp((t - at - 0.2) / 0.12), INK, 62, 40 + i);
  });
  // over the stamp
  marker(ctx, [[60, 925], [540, 970], [1020, 1012]], clamp((t - 15.95) / 0.16), INK, 130, 51);
  // € stickers: the only thing still readable
  BOARD.forEach((s, i) => {
    const k = spring(t - (16.26 + i * 0.07), 420, 20);
    if (k <= 0.01) return;
    const [x, y, rot] = s._pos;
    const sc = lerp(1.9, 1, clamp(k));
    ctx.save(); ctx.translate(x, y); ctx.rotate(rot); ctx.translate(s.w / 2 - 100, -s.h / 2 + 100); ctx.rotate(-0.12 + i * 0.08); ctx.scale(sc, sc);
    ctx.save(); ctx.translate(6, 10); ctx.fillStyle = "rgba(0,0,0,0.35)"; ctx.filter = "blur(6px)"; ctx.beginPath(); ctx.arc(0, 0, 78, 0, 7); ctx.fill(); ctx.restore();
    ctx.fillStyle = C.crimson; ctx.beginPath(); ctx.arc(0, 0, 78, 0, 7); ctx.fill();
    text(ctx, "€", 0, 36, { size: 104, weight: 900, color: C.ivory, align: "center" });
    ctx.restore();
  });
}

export default {
  id: "s05_compare", start: 13.6, end: 17.4,
  draw(ctx, t) {
    paperBg(ctx, "#232220", 11);
    // dive back in through the wall (reverse of S4)
    const e = spring(t - 13.6, 55, 14.8);
    const Zs = Z_END * 0.95;
    const Z = Zs * Math.pow(Z_START / Zs, e) * (s5Zoom(t) / 1.04);
    drawWall(ctx, t, Z, lerp(WALL_C[0], 540, e), lerp(WALL_C[1], 820, e), 540, lerp(960, 820, e), {
      center: (c) => redactedBoard(c, t),
      sticker: t < 14.0 ? cilesiSticker(ctx, t, 0, 13.6) : null,
    });
    // the slab and the word fly off
    if (t < 14.2) {
      const fly = spring(t - 13.62, 120, 16);
      slab(ctx, t, fly);
      ransomWord(ctx, "CILËSI", 600, 1310 + fly * 1400, 128, 47, t, () => 0);
      dymo(ctx, "THONË", 205 - fly * 400, 1205 + fly * 900, -0.05 - fly, 36, 78, 1);
    }
  },
};
