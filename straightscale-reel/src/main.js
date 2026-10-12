// Entry: loads fonts + timing, exposes window.drawFrame(t) (pure function of t).
import { W, H, C, SANS, text, measure, rr, prog, E, clamp } from "./lib.js";
import { scenes } from "./scenes/index.js";
import { captionStrip, spring } from "./fx.js";

const q = new URLSearchParams(location.search);
const SCALE = parseFloat(q.get("scale") || "1");
const STAMP = q.get("stamp") === "1";
const canvas = document.getElementById("c");
canvas.width = Math.round(W * SCALE); canvas.height = Math.round(H * SCALE);
const ctx = canvas.getContext("2d");
window.__canvas = canvas;

let WORDS = [], GROUPS = [];
export const DURATION = 47.6;
window.DURATION = DURATION;

// Caption hidden where the same words are already big on screen.
const NO_CAPTION = [[3.0, 4.7], [9.55, 13.62], [28.2, 31.15], [31.1, 35.05], [37.0, 42.66], [42.66, 99]];

function buildGroups(words) {
  const g = []; let cur = [];
  for (const w of words) {
    cur.push(w);
    if (/[.,:?!…]["“”]?\.{0,3}$/.test(w.w) || cur.length >= 4) { g.push(cur); cur = []; }
  }
  if (cur.length) g.push(cur);
  return g;
}
const clean = (w) => w.replace(/["“”]/g, "").replace(/\.\.\.$/, "…");

function drawCaptions(t) {
  if (NO_CAPTION.some(([a, b]) => t >= a && t < b)) return;
  const grp = GROUPS.find((g) => t >= g[0].s - 0.08 && t < g[g.length - 1].e + 0.18);
  if (!grp) return;
  let size = 54, gap = 16; const y = 1355;
  const parts = grp.map((w) => clean(w.w));
  let widths = parts.map((p) => measure(ctx, p, { size, weight: 800 }));
  let total = widths.reduce((a, b) => a + b, 0) + gap * (parts.length - 1);
  if (total > 780) { const f = 780 / total; size *= f; gap *= f; widths = widths.map((w) => w * f); total = 780; }
  const CX = 500;
  // strip snaps open from its left edge (spring, no fade)
  const k = clamp(spring(t - (grp[0].s - 0.1), 420, 30), 0, 1.1);
  if (k < 0.01) return;
  ctx.save();
  ctx.save(); ctx.translate(CX - total / 2 - 26, 0); ctx.scale(k, 1); ctx.translate(-(CX - total / 2 - 26), 0);
  captionStrip(ctx, CX - total / 2 - 26, y - 60, total + 52, 84);
  ctx.restore();
  if (k < 0.6) { ctx.restore(); return; }
  let x = CX - total / 2;
  grp.forEach((w, i) => {
    const on = t >= w.s - 0.04;
    const active = t >= w.s - 0.04 && t < w.e + 0.05;
    const pop = on ? E.outBack(prog(t, w.s - 0.04, w.s + 0.14)) : 0;
    ctx.save();
    ctx.translate(x + widths[i] / 2, y);
    ctx.scale(0.85 + 0.15 * pop, 0.85 + 0.15 * pop);
    text(ctx, parts[i], 0, 0, { size, weight: 800, color: active ? C.gold : C.ivory, align: "center", alpha: on ? 1 : 0.35 });
    ctx.restore();
    x += widths[i] + gap;
  });
  ctx.restore();
}

window.drawFrame = (t) => {
  ctx.setTransform(SCALE, 0, 0, SCALE, 0, 0);
  ctx.globalAlpha = 1;
  ctx.fillStyle = C.charcoal; ctx.fillRect(0, 0, W, H);
  const sc = scenes.find((s) => t >= s.start && t < s.end) || scenes[scenes.length - 1];
  ctx.save(); sc.draw(ctx, t, { words: WORDS }); ctx.restore();
  drawCaptions(t);
  if (STAMP) {
    ctx.fillStyle = "rgba(0,0,0,0.7)"; ctx.fillRect(0, H - 90, 330, 90);
    text(ctx, `${t.toFixed(2)}s ${sc.id}`, 20, H - 28, { size: 46, weight: 700, color: "#fff" });
  }
};

(async () => {
  const b = await (await fetch("../plan/beats.json")).json();
  WORDS = b.words; GROUPS = buildGroups(WORDS);
  window.WORDS = WORDS;
  const faces = ["400 20px Playfair", "700 20px Playfair", "900 20px Playfair", "italic 400 20px Playfair", "italic 700 20px Playfair", "italic 900 20px Playfair",
    "300 20px Montserrat", "500 20px Montserrat", "600 20px Montserrat", "700 20px Montserrat", "800 20px Montserrat", "900 20px Montserrat"];
  await Promise.all(faces.map((f) => document.fonts.load(f, "ëçËÇ€→ABC")));
  await document.fonts.ready;
  for (const s of scenes) if (s.init) await s.init();
  window.__ready = true;
})();
