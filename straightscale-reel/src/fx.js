// Collage toolkit: paper, torn scraps, tape, label-maker tape, ransom letters, marker, stamp.
// All seeded and pure functions of their inputs.
import { C, SERIF, SANS, W, H, rng, rr, text, measure, clamp, lerp } from "./lib.js";

// spring from motion-studio/lib/motion.js (closed form, pure)
export function spring(t, k = 170, d = 26) {
  if (t <= 0) return 0;
  const w0 = Math.sqrt(k), z = d / (2 * w0);
  if (z < 1) { const wd = w0 * Math.sqrt(1 - z * z); return 1 - Math.exp(-z * w0 * t) * (Math.cos(wd * t) + (z * w0 / wd) * Math.sin(wd * t)); }
  return 1 - Math.exp(-w0 * t) * (1 + w0 * t);
}
export function track(t, keys, k = 170, d = 26) {
  let v = keys[0][1];
  for (let i = 1; i < keys.length; i++) v += (keys[i][1] - keys[i - 1][1]) * spring(t - keys[i][0], k, d);
  return v;
}

// --- paper textures (cached per colour) ---
const paperCache = new Map();
export function paperTex(color, seed = 1, fibers = 1) {
  const key = color + seed;
  if (paperCache.has(key)) return paperCache.get(key);
  const c = new OffscreenCanvas(W, H), g = c.getContext("2d"), r = rng(seed);
  g.fillStyle = color; g.fillRect(0, 0, W, H);
  for (let i = 0; i < 9000 * fibers; i++) {
    const x = r() * W, y = r() * H, a = r() * Math.PI, l = 2 + r() * 10;
    g.strokeStyle = r() < 0.5 ? `rgba(0,0,0,${0.03 + r() * 0.05})` : `rgba(255,255,255,${0.05 + r() * 0.08})`;
    g.lineWidth = 0.6 + r(); g.beginPath(); g.moveTo(x, y); g.lineTo(x + Math.cos(a) * l, y + Math.sin(a) * l); g.stroke();
  }
  for (let i = 0; i < 2500; i++) { g.fillStyle = `rgba(0,0,0,${r() * 0.06})`; g.fillRect(r() * W, r() * H, 1.5, 1.5); }
  paperCache.set(key, c); return c;
}
export function paperBg(ctx, color, seed = 1) { ctx.drawImage(paperTex(color, seed), 0, 0); }

// --- torn scrap polygon (local coords, centred) ---
export function tornPath(ctx, w, h, seed, rough = 7) {
  const r = rng(seed), pts = [];
  const edge = (x1, y1, x2, y2, n) => { for (let i = 0; i < n; i++) { const k = i / n; const j = (r() - 0.5) * rough * 2; pts.push([lerp(x1, x2, k) + (y1 === y2 ? 0 : j), lerp(y1, y2, k) + (y1 === y2 ? j : 0)]); } };
  const nx = Math.max(6, Math.round(w / 22)), ny = Math.max(6, Math.round(h / 22));
  edge(-w / 2, -h / 2, w / 2, -h / 2, nx); edge(w / 2, -h / 2, w / 2, h / 2, ny);
  edge(w / 2, h / 2, -w / 2, h / 2, nx); edge(-w / 2, h / 2, -w / 2, -h / 2, ny);
  ctx.beginPath(); pts.forEach(([x, y], i) => (i ? ctx.lineTo(x, y) : ctx.moveTo(x, y))); ctx.closePath();
}
// draw a torn scrap with paper texture + drop shadow, then run inner(ctx) clipped to it
export function scrap(ctx, x, y, w, h, rot, color, seed, inner, { shadowA = 0.35, rough = 7, lift = 1 } = {}) {
  ctx.save(); ctx.translate(x, y); ctx.rotate(rot);
  ctx.save(); ctx.translate(6 * lift, 10 * lift); tornPath(ctx, w, h, seed, rough); ctx.fillStyle = `rgba(0,0,0,${shadowA})`; ctx.filter = "blur(8px)"; ctx.fill(); ctx.restore();
  tornPath(ctx, w, h, seed, rough); ctx.save(); ctx.clip();
  ctx.drawImage(paperTex(color, seed % 5 + 1), -w / 2 - (seed % 300), -h / 2 - (seed % 500));
  if (inner) inner(ctx);
  ctx.restore(); ctx.restore();
}

// --- halftone dots inside a rect (local) ---
export function halftone(ctx, x, y, w, h, color, step = 14, angle = 0.4, falloff = 1) {
  ctx.save(); ctx.fillStyle = color;
  for (let yy = 0; yy < h; yy += step) for (let xx = 0; xx < w; xx += step) {
    const k = falloff ? 1 - (xx / w) * 0.8 : 1; const rad = step * 0.42 * k;
    const ox = (yy / step) % 2 ? step / 2 : 0;
    ctx.beginPath(); ctx.arc(x + xx + ox, y + yy, Math.max(0.5, rad), 0, Math.PI * 2); ctx.fill();
  }
  ctx.restore();
}

// --- translucent tape strip ---
export function tape(ctx, x, y, w, h, rot, seed, alpha = 0.78) {
  const r = rng(seed);
  ctx.save(); ctx.translate(x, y); ctx.rotate(rot);
  ctx.beginPath(); ctx.moveTo(-w / 2, -h / 2);
  for (let i = 0; i <= 6; i++) ctx.lineTo(w / 2 + (r() - 0.5) * 8, -h / 2 + (h * i) / 6);
  for (let i = 6; i >= 0; i--) ctx.lineTo(-w / 2 + (r() - 0.5) * 8, -h / 2 + (h * i) / 6);
  ctx.closePath(); ctx.fillStyle = `rgba(236,226,200,${alpha})`; ctx.fill();
  ctx.fillStyle = "rgba(255,255,255,0.18)"; ctx.fillRect(-w / 2, -h / 2 + 3, w, h * 0.25);
  ctx.restore();
}

// --- label-maker tape (black embossed) ---
export function dymo(ctx, s, x, y, rot, size = 30, seed = 1, k = 1) {
  const w = measure(ctx, s, { size, weight: 800, ls: 3 }) + size * 1.1, h = size * 1.55;
  ctx.save(); ctx.translate(x, y); ctx.rotate(rot); ctx.scale(k, k);
  ctx.fillStyle = "rgba(0,0,0,0.35)"; ctx.fillRect(-w / 2 + 4, -h / 2 + 6, w, h);
  ctx.fillStyle = "#151515"; ctx.fillRect(-w / 2, -h / 2, w, h);
  const r = rng(seed); ctx.fillStyle = "#262626"; for (let i = 0; i < 40; i++) ctx.fillRect(-w / 2 + r() * w, -h / 2 + r() * h, 2, 1);
  text(ctx, s, 0, size * 0.36, { size, weight: 800, color: "#EDEDED", align: "center", ls: 3 });
  ctx.restore();
}

// --- ransom letter styles (brand fonts only: contrast by weight/italic/colour/scrap) ---
export const RANSOM = [
  { bg: "#EFE8D8", fg: C.charcoal, family: SERIF, weight: 900, italic: false, ht: true },  // newsprint
  { bg: C.crimson, fg: C.ivory, family: SANS, weight: 900, italic: false },                // red sticker
  { bg: C.charcoal, fg: C.ivory, family: SERIF, weight: 700, italic: true },               // black magazine
  { bg: "#D9D2C5", fg: C.charcoal, family: SANS, weight: 300, italic: false },             // thin grey
  { bg: C.ivory, fg: C.crimson, family: SERIF, weight: 900, italic: true },                // ivory/red italic
  { bg: "#B9B1A3", fg: "#111", family: SANS, weight: 800, italic: false },                 // stone block
];
// Draws one ransom letter centred at (x,y). k = landing spring (0..1+), returns width
export function ransomLetter(ctx, ch, x, y, size, styleIdx, seed, k = 1) {
  const st = RANSOM[styleIdx % RANSOM.length], r = rng(seed);
  const sz = size * (0.86 + r() * 0.28);
  const gw = measure(ctx, ch, { family: st.family, size: sz, weight: st.weight, italic: st.italic });
  const w = gw + sz * 0.32, h = sz * 1.12, rot = (r() - 0.5) * 0.22, dy = (r() - 0.5) * size * 0.12;
  if (k <= 0) return w;
  const s = lerp(1.6, 1, clamp(k, 0, 1.2)) ;
  ctx.save(); ctx.translate(x, y + dy); ctx.rotate(rot + (1 - clamp(k)) * 0.5); ctx.scale(s, s);
  ctx.save(); ctx.translate(5, 9); tornPath(ctx, w, h, seed, 4); ctx.fillStyle = "rgba(0,0,0,0.35)"; ctx.fill(); ctx.restore();
  tornPath(ctx, w, h, seed, 4); ctx.fillStyle = st.bg; ctx.fill();
  if (st.ht) { ctx.save(); tornPath(ctx, w, h, seed, 4); ctx.clip(); halftone(ctx, -w / 2, -h / 2, w, h, "rgba(0,0,0,0.12)", 10); ctx.restore(); }
  text(ctx, ch, 0, sz * 0.36, { family: st.family, size: sz, weight: st.weight, italic: st.italic, color: st.fg, align: "center" });
  ctx.restore();
  return w * 0.92;
}
export function ransomWidth(ctx, word, size, seed0) {
  let tot = 0;
  for (let i = 0; i < word.length; i++) {
    if (word[i] === " ") { tot += size * 0.35; continue; }
    const st = RANSOM[(seed0 + i * 7) % RANSOM.length], r = rng(seed0 * 31 + i);
    const sz = size * (0.86 + r() * 0.28);
    tot += (measure(ctx, word[i], { family: st.family, size: sz, weight: st.weight, italic: st.italic }) + sz * 0.32) * 0.92;
  }
  return tot;
}
// word laid out centred; landAt(i) -> time of letter i; returns nothing
export function ransomWord(ctx, word, cx, y, size, seed0, t, landAt, flyOut = null) {
  const total = ransomWidth(ctx, word, size, seed0);
  let x = cx - total / 2;
  for (let i = 0; i < word.length; i++) {
    const ch = word[i];
    if (ch === " ") { x += size * 0.35; continue; }
    const st = (seed0 + i * 7) % RANSOM.length, sd = seed0 * 31 + i;
    const r = rng(sd); const sz = size * (0.86 + r() * 0.28);
    const sti = RANSOM[st];
    const w = (measure(ctx, ch, { family: sti.family, size: sz, weight: sti.weight, italic: sti.italic }) + sz * 0.32) * 0.92;
    const k = spring(t - landAt(i), 260, 18);
    ctx.save();
    if (flyOut) { const f = flyOut(i); if (f) { ctx.translate(x + w / 2 + f.dx, y + f.dy); ctx.rotate(f.rot); ctx.translate(-(x + w / 2), -y); } }
    ransomLetter(ctx, ch, x + w / 2, y, size, st, sd, k);
    ctx.restore();
    x += w;
  }
}

// --- marker stroke along a polyline, revealed by p (0..1) ---
export function marker(ctx, pts, p, color, width, seed = 1) {
  if (p <= 0) return;
  const r = rng(seed); let L = 0; const seg = [];
  for (let i = 1; i < pts.length; i++) { const d = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); seg.push(d); L += d; }
  const target = L * clamp(p);
  ctx.save(); ctx.strokeStyle = color; ctx.lineCap = "round"; ctx.lineJoin = "round";
  for (let pass = 0; pass < 3; pass++) {
    ctx.globalAlpha = pass === 0 ? 0.95 : 0.35; ctx.lineWidth = width * (pass === 0 ? 1 : 0.6);
    ctx.beginPath(); let acc = 0; ctx.moveTo(pts[0][0] + (pass ? (r() - 0.5) * 6 : 0), pts[0][1] + (pass ? (r() - 0.5) * 6 : 0));
    for (let i = 1; i < pts.length; i++) {
      const d = seg[i - 1];
      if (acc + d >= target) { const k = (target - acc) / d; ctx.lineTo(lerp(pts[i - 1][0], pts[i][0], k), lerp(pts[i - 1][1], pts[i][1], k)); break; }
      ctx.lineTo(pts[i][0] + (pass ? (r() - 0.5) * 6 : 0), pts[i][1] + (pass ? (r() - 0.5) * 6 : 0)); acc += d;
    }
    ctx.stroke();
  }
  ctx.restore();
}

// --- rubber stamp with ink texture ---
export function rubberStamp(ctx, s, x, y, rot, size, k, seed = 9, color = C.crimson) {
  if (k <= 0) return;
  const s1 = lerp(2.2, 1, clamp(k));
  ctx.save(); ctx.translate(x, y); ctx.rotate(rot); ctx.scale(s1, s1); ctx.globalAlpha = clamp(k * 3) * 0.92;
  const w = measure(ctx, s, { size, weight: 900, ls: 6 }) + size * 1.2, h = size * 1.7;
  ctx.strokeStyle = color; ctx.lineWidth = size * 0.12; ctx.strokeRect(-w / 2, -h / 2, w, h);
  ctx.lineWidth = size * 0.04; ctx.strokeRect(-w / 2 + size * 0.18, -h / 2 + size * 0.18, w - size * 0.36, h - size * 0.36);
  text(ctx, s, 0, size * 0.36, { size, weight: 900, color, align: "center", ls: 6 });
  // ink gaps
  const r = rng(seed); ctx.globalCompositeOperation = "destination-out";
  for (let i = 0; i < 90; i++) { ctx.globalAlpha = 0.5 + r() * 0.5; ctx.fillRect(-w / 2 + r() * w, -h / 2 + r() * h, 2 + r() * 10, 1 + r() * 3); }
  ctx.restore();
}

// --- caption strip: straight charcoal tape behind clean type ---
export function captionStrip(ctx, x, y, w, h) {
  ctx.save(); ctx.fillStyle = "rgba(18,18,18,0.92)";
  ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + w, y + 2); ctx.lineTo(x + w - 6, y + h); ctx.lineTo(x + 4, y + h - 2); ctx.closePath(); ctx.fill();
  ctx.restore();
}

// --- clean world: the gold line, and things that rise out of / drop out of it ---
export const LINE_Y = 894;
export function goldLine(ctx, x0 = 0, x1 = W, y = LINE_Y) { ctx.fillStyle = C.gold; ctx.fillRect(x0, y, x1 - x0, 12); }
// dir -1: content lives above the line and rises out of it; dir +1: lives below and drops out of it
export function fromLine(ctx, k, dir, draw, dist = 400, y = LINE_Y) {
  if (k <= 0.001) return;
  ctx.save(); ctx.beginPath();
  if (dir < 0) ctx.rect(-6000, -6000, 16000, y + 6000); else ctx.rect(-6000, y + 12, 16000, 12000);
  ctx.clip(); ctx.translate(0, (1 - k) * dist * (dir < 0 ? 1 : -1)); draw(); ctx.restore();
}
