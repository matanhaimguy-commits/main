// S10 · (31.10–35.05) "Pastaj thuaje kudo: në reklama, në faqe, në telefon."
// Frame-in-frame: the promise from S9 turns out to be on a phone screen (an ad). The camera pulls back along the
// gold line to two more screens (website, phone call), all saying the same thing on the same straight line.
// The opposite of S3: same channels, but straight edges, aligned, one message.
import { C, SERIF, SANS, W, H, text, measure, rr, clamp, lerp } from "../lib.js";
import { spring, track, paperBg, goldLine, rubberStamp } from "../fx.js";
import { promise } from "./s09_promise.js";

const GAP = 1260, LABELS = [["NË REKLAMA", 32.5], ["NË FAQE", 33.36], ["NË TELEFON", 34.08]];
export const camS10 = (t) => ({
  Z: track(t, [[0, 1], [31.2, 0.5], [34.5, 0.27]], 120, 21),
  cx: track(t, [[0, 540], [33.28, 540 + GAP], [34.0, 540 + GAP * 2], [34.5, 540 + GAP]], 130, 22),
});

function chrome(ctx, k, t, a) {
  const top = 1 - clamp(a), bot = 1 - clamp(a);
  ctx.save(); ctx.translate(0, -top * 300);
  if (k === 0) {
    ctx.fillStyle = "#B9B1A3"; ctx.beginPath(); ctx.arc(120, 250, 50, 0, 7); ctx.fill();
    text(ctx, "Biznesi yt", 196, 242, { size: 46, weight: 800, color: C.charcoal });
    text(ctx, "Sponsorizuar", 196, 292, { size: 34, weight: 500, color: "#8E867B" });
  } else if (k === 1) {
    ctx.fillStyle = "#E2D9C9"; rr(ctx, 60, 180, 960, 116, 58); ctx.fill();
    text(ctx, "faqja jote", 540, 252, { size: 40, weight: 600, color: "#7A7266", align: "center" });
  } else {
    text(ctx, "Telefonatë", 540, 230, { size: 40, weight: 600, color: "#8E867B", align: "center" });
    text(ctx, "Klient i ri", 540, 304, { size: 60, weight: 800, color: C.charcoal, align: "center" });
  }
  ctx.restore();
  ctx.save(); ctx.translate(0, bot * 400);
  if (k === 2) {
    ctx.fillStyle = C.crimson; ctx.beginPath(); ctx.arc(540, 1640, 92, 0, 7); ctx.fill();
    ctx.save(); ctx.translate(540, 1640); ctx.rotate(2.35); ctx.strokeStyle = C.ivory; ctx.lineWidth = 26; ctx.lineCap = "round";
    ctx.beginPath(); ctx.arc(0, 0, 34, -0.9, 0.9); ctx.stroke(); ctx.restore();
  } else {
    ctx.fillStyle = k === 0 ? C.crimson : C.charcoal; rr(ctx, 60, 1560, 960, 140, k === 0 ? 20 : 70); ctx.fill();
    text(ctx, k === 0 ? "Na shkruaj" : "Na kontakto", 540, 1648, { size: 50, weight: 800, color: C.ivory, align: "center" });
  }
  ctx.restore();
}

// the three screens in world space (screen k spans x ∈ [k·GAP, k·GAP+1080], y ∈ [0, 1920])
export function screens(ctx, t, { drop = 0 } = {}) {
  for (let k = 0; k < 3; k++) {
    const r = drop > 0 ? (k - 1) * 0.15 * drop : 0;
    ctx.save(); ctx.translate(k * GAP + 540, 960 + drop * drop * (2600 + k * 500)); ctx.rotate(r); ctx.translate(-540, -960);
    // device frame + shadow (fades in only as we pull back)
    const fr = clamp((t - 31.2) / 0.25);
    if (fr > 0 || k > 0) {
      ctx.save(); ctx.filter = "blur(24px)"; ctx.fillStyle = "rgba(60,45,30,0.25)"; rr(ctx, 10, 40, 1080, 1920, 110); ctx.fill(); ctx.restore();
      ctx.fillStyle = C.charcoal; rr(ctx, -34, -34, 1148, 1988, 130); ctx.fill();
    }
    ctx.fillStyle = C.marble; rr(ctx, 0, 0, 1080, 1920, 100); ctx.fill();
    promise(ctx, 99);
    if (k === 0) rubberStamp(ctx, "SHEMBULL", 820, 560, 0.14, 40, 1, 12);
    chrome(ctx, k, t, k === 0 ? spring(t - 31.2, 220, 22) : 1);
    ctx.restore();
  }
}

export default {
  id: "s10_everywhere", start: 31.1, end: 35.05,
  draw(ctx, t) {
    paperBg(ctx, C.marble, 6);
    const { Z, cx } = camS10(t);
    ctx.save(); ctx.translate(540, 900); ctx.scale(Z, Z); ctx.translate(-cx, -900);
    screens(ctx, t);
    // labels above each screen, on their words
    LABELS.forEach(([s, at], k) => {
      const q = spring(t - at, 320, 22);
      if (q <= 0.01) return;
      ctx.save(); ctx.translate(k * GAP + 540, -150); ctx.scale(1, clamp(q, 0, 1.2));
      text(ctx, s, 0, 0, { size: 150, weight: 900, color: C.charcoal, align: "center", ls: 4 });
      ctx.restore();
    });
    ctx.restore();
    goldLine(ctx);
    // "Thuaje kudo." heading before the labels take over
    const hk = spring(t - 31.5, 260, 22) - spring(t - 32.3, 260, 24);
    if (hk > 0.01) {
      ctx.save(); ctx.beginPath(); ctx.rect(0, 160, W, 200); ctx.clip();
      text(ctx, "Thuaje kudo.", 540, 330 + (1 - clamp(hk, 0, 1.2)) * 190, { family: SERIF, size: 120, weight: 900, italic: true, color: C.charcoal, align: "center" });
      ctx.restore();
    }
  },
};
