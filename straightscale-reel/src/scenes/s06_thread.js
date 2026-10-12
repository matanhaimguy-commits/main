// S6 · (17.40–18.50) "Ja çfarë bën."  One straight gold line slices the collage; both halves fall away,
// revealing clean marble. The line swings level and becomes the baseline of everything that follows.
import { C, W, H, clamp, lerp } from "../lib.js";
import { spring, track, paperBg } from "../fx.js";
import { redactedBoard, s5Zoom } from "./s05_compare.js";

export default {
  id: "s06_thread", start: 17.4, end: 18.5,
  draw(ctx, t) {
    paperBg(ctx, C.marble, 6);
    const draw = clamp((t - 17.44) / 0.16);              // line slices in ~5 frames
    const fall = clamp((t - 17.66) / 0.7);                // halves drop with gravity
    const g = fall * fall;
    const A = [-60, 560], B = [W + 60, 1240];               // cut line (diagonal)
    const half = (above, dx, dy, rot) => {
      ctx.save();
      ctx.translate(W / 2 + dx, 900 + dy); ctx.rotate(rot); ctx.translate(-W / 2, -900);
      ctx.beginPath();
      if (above) { ctx.moveTo(-200, -200); ctx.lineTo(W + 200, -200); ctx.lineTo(B[0], B[1]); ctx.lineTo(A[0], A[1]); }
      else { ctx.moveTo(A[0], A[1]); ctx.lineTo(B[0], B[1]); ctx.lineTo(W + 200, H + 200); ctx.lineTo(-200, H + 200); }
      ctx.closePath(); ctx.clip();
      paperBg(ctx, "#232220", 11);
      const z = s5Zoom(17.4);
      ctx.translate(W / 2, 820); ctx.scale(z, z); ctx.translate(-540, -820);
      redactedBoard(ctx, 17.4);
      ctx.restore();
    };
    if (fall < 1) {
      half(true, -g * 260, -g * 1400, -g * 0.25);
      half(false, g * 200, g * 1700, g * 0.3);
    }
    // the gold line: slices diagonally, then swings level at y=900 and stays
    const lev = spring(t - 18.05, 160, 20);
    const ay = lerp(A[1], 900, clamp(lev)), by = lerp(B[1], 900, clamp(lev));
    ctx.save(); ctx.strokeStyle = C.gold; ctx.lineWidth = 12; ctx.lineCap = "butt";
    ctx.beginPath(); ctx.moveTo(A[0], ay); ctx.lineTo(lerp(A[0], B[0], draw), lerp(ay, by, draw)); ctx.stroke();
    ctx.restore();
  },
};
