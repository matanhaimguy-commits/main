// Shared drawing helpers. Pure functions of their inputs (deterministic).
export const W = 1080, H = 1920;
export const C = {
  gold: "#D4AF37", crimson: "#B31217", ivory: "#F8F6EF", charcoal: "#1F1F1F", marble: "#EDE4D6",
  ink: "#2A2723", stone: "#8E867B", charcoal2: "#2A2A2A", goldSoft: "rgba(212,175,55,0.18)",
};
export const SERIF = "Playfair", SANS = "Montserrat";
export const SAFE = { top: 220, bottom: 1500, left: 60, right: 940 }; // 9:16 reel safe area

export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lerp = (a, b, t) => a + (b - a) * t;
export const prog = (t, a, b) => clamp((t - a) / (b - a));
export const E = {
  outCubic: (x) => 1 - Math.pow(1 - x, 3),
  inCubic: (x) => x * x * x,
  inOutCubic: (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2),
  outExpo: (x) => (x === 1 ? 1 : 1 - Math.pow(2, -10 * x)),
  outBack: (x) => { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); },
  outQuart: (x) => 1 - Math.pow(1 - x, 4),
};
// eased 0..1 between a and b
export const ep = (t, a, b, f = E.outCubic) => f(prog(t, a, b));

export function rng(seed) { // mulberry32
  let s = seed >>> 0;
  return () => { s += 0x6d2b79f5; let t = s; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
}

export function rr(ctx, x, y, w, h, r) {
  const q = Math.min(r, w / 2, h / 2);
  ctx.beginPath();
  ctx.moveTo(x + q, y); ctx.arcTo(x + w, y, x + w, y + h, q); ctx.arcTo(x + w, y + h, x, y + h, q);
  ctx.arcTo(x, y + h, x, y, q); ctx.arcTo(x, y, x + w, y, q); ctx.closePath();
}

export function font(ctx, family, size, weight = 400, italic = false) {
  ctx.font = `${italic ? "italic " : ""}${weight} ${size}px ${family}`;
}

// Text with optional letter spacing. Returns width.
export function text(ctx, s, x, y, o = {}) {
  const { family = SANS, size = 40, weight = 600, color = C.ivory, align = "left", ls = 0, alpha = 1, italic = false, baseline = "alphabetic" } = o;
  ctx.save();
  ctx.globalAlpha *= alpha;
  font(ctx, family, size, weight, italic);
  ctx.fillStyle = color; ctx.textBaseline = baseline;
  ctx.letterSpacing = `${ls}px`;
  const w = ctx.measureText(s).width;
  const dx = align === "center" ? -w / 2 : align === "right" ? -w : 0;
  ctx.textAlign = "left";
  ctx.fillText(s, x + dx, y);
  ctx.restore();
  return w;
}
export function measure(ctx, s, o = {}) {
  const { family = SANS, size = 40, weight = 600, ls = 0, italic = false } = o;
  ctx.save(); font(ctx, family, size, weight, italic); ctx.letterSpacing = `${ls}px`;
  const w = ctx.measureText(s).width; ctx.restore(); return w;
}

export function shadow(ctx, blur = 30, y = 12, color = "rgba(0,0,0,0.35)") {
  ctx.shadowColor = color; ctx.shadowBlur = blur; ctx.shadowOffsetY = y; ctx.shadowOffsetX = 0;
}
export function noShadow(ctx) { ctx.shadowColor = "transparent"; ctx.shadowBlur = 0; ctx.shadowOffsetY = 0; }

// Scale-in "pop" factor with small overshoot.
export const popIn = (t, at, dur = 0.35) => E.outBack(prog(t, at, at + dur));

// StraightScale logo: red rounded square, white S cut-out, small gold square top-right (+ wordmark).
export function logo(ctx, cx, cy, size, { wordmark = true, wordColor = C.charcoal, alpha = 1 } = {}) {
  ctx.save(); ctx.globalAlpha *= alpha;
  const x = cx - size / 2, y = cy - size / 2;
  ctx.fillStyle = C.crimson; rr(ctx, x, y, size, size, size * 0.22); ctx.fill();
  text(ctx, "S", cx, cy + size * 0.27, { family: SANS, size: size * 0.78, weight: 900, color: C.ivory, align: "center" });
  const g = size * 0.2;
  ctx.fillStyle = C.gold; rr(ctx, x + size - g * 1.25, y + g * 0.25, g, g, g * 0.18); ctx.fill();
  if (wordmark) text(ctx, "StraightScale", cx, cy + size * 0.5 + size * 0.42, { family: SANS, size: size * 0.3, weight: 800, color: wordColor, align: "center", ls: -0.5 });
  ctx.restore();
}

// Cached procedural marble texture (light) + charcoal background with vignette.
let marbleCache = null;
export function marble(ctx) {
  if (!marbleCache) {
    const c = new OffscreenCanvas(W, H), g = c.getContext("2d");
    g.fillStyle = C.marble; g.fillRect(0, 0, W, H);
    const r = rng(7);
    for (let v = 0; v < 14; v++) {
      g.beginPath();
      let x = r() * W, y = -50, a = (r() - 0.5) * 0.8 + Math.PI / 2;
      g.moveTo(x, y);
      for (let i = 0; i < 80; i++) { a += (r() - 0.5) * 0.35; x += Math.cos(a) * 30; y += Math.sin(a) * 30; g.lineTo(x, y); }
      g.strokeStyle = `rgba(140,125,105,${0.05 + r() * 0.09})`; g.lineWidth = 0.8 + r() * 2.2; g.stroke();
    }
    const vg = g.createRadialGradient(W / 2, H * 0.45, 200, W / 2, H / 2, 1300);
    vg.addColorStop(0, "rgba(255,255,255,0.25)"); vg.addColorStop(1, "rgba(120,100,80,0.12)");
    g.fillStyle = vg; g.fillRect(0, 0, W, H);
    marbleCache = c;
  }
  ctx.drawImage(marbleCache, 0, 0);
}
export function charcoalBg(ctx, glow = 0) {
  ctx.fillStyle = C.charcoal; ctx.fillRect(0, 0, W, H);
  const vg = ctx.createRadialGradient(W / 2, H * 0.42, 100, W / 2, H / 2, 1250);
  vg.addColorStop(0, `rgba(60,55,48,${0.55 + glow * 0.3})`); vg.addColorStop(1, "rgba(0,0,0,0.55)");
  ctx.fillStyle = vg; ctx.fillRect(0, 0, W, H);
}

// Dashed "stitch" line between two points.
export function stitch(ctx, x1, y1, x2, y2, color = C.ivory, p = 1, width = 4) {
  ctx.save(); ctx.strokeStyle = color; ctx.lineWidth = width; ctx.setLineDash([16, 12]); ctx.lineCap = "round";
  ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(lerp(x1, x2, p), lerp(y1, y2, p)); ctx.stroke(); ctx.restore();
}
