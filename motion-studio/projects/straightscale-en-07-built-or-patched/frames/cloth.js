// Paper, cloth and scraps for the EN 07 hook frames. Every shape is a pure function of its arguments (no time yet).
export const C = {
  char: '#1F1F1F', ivory: '#F8F6EF', marble: '#EDE4D6', gold: '#DD9A10', red: '#BE0F18',
  grey: '#6E685F', dim: '#B9B2A5', card: '#2A2826', edge: '#4A4540',
};

function rng(seed) { let s = seed >>> 0; return () => { s = (s + 0x6D2B79F5) >>> 0; let x = s; x = Math.imul(x ^ (x >>> 15), x | 1); x ^= x + Math.imul(x ^ (x >>> 7), x | 61); return ((x ^ (x >>> 14)) >>> 0) / 4294967296; }; }

export function paper(ctx, W, H) {
  ctx.fillStyle = C.ivory; ctx.fillRect(0, 0, W, H);
  const r = rng(7);
  for (let i = 0; i < 9000; i++) {
    ctx.fillStyle = r() < 0.5 ? 'rgba(110,104,95,0.05)' : 'rgba(255,255,255,0.35)';
    ctx.fillRect(r() * W, r() * H, 2, 2);
  }
}

function weave(ctx, x, y, w, h, base, line, step) {
  ctx.fillStyle = base; ctx.fillRect(x, y, w, h);
  ctx.strokeStyle = line; ctx.lineWidth = 2;
  for (let i = step / 2; i < w; i += step) { ctx.beginPath(); ctx.moveTo(x + i, y); ctx.lineTo(x + i, y + h); ctx.stroke(); }
  for (let j = step / 2; j < h; j += step) { ctx.beginPath(); ctx.moveTo(x, y + j); ctx.lineTo(x + w, y + j); ctx.stroke(); }
}

// The big cloth: charcoal weave with a soft shadow on the paper.
export function cloth(ctx, x, y, w, h) {
  ctx.save();
  ctx.shadowColor = 'rgba(31,31,31,0.28)'; ctx.shadowBlur = 40; ctx.shadowOffsetY = 18;
  ctx.fillStyle = C.card; ctx.fillRect(x, y, w, h);
  ctx.restore();
  weave(ctx, x, y, w, h, C.card, 'rgba(248,246,239,0.06)', 9);
  ctx.setLineDash([22, 14]); ctx.strokeStyle = 'rgba(248,246,239,0.28)'; ctx.lineWidth = 4;
  ctx.strokeRect(x + 26, y + 26, w - 52, h - 52); ctx.setLineDash([]);
}

const PATTERNS = {
  gingham: (ctx, w, h) => {
    ctx.fillStyle = C.gold; ctx.fillRect(0, 0, w, h);
    ctx.fillStyle = 'rgba(248,246,239,0.38)';
    for (let i = 0; i < w; i += 44) ctx.fillRect(i, 0, 22, h);
    for (let j = 0; j < h; j += 44) ctx.fillRect(0, j, w, 22);
  },
  stripes: (ctx, w, h) => {
    ctx.fillStyle = C.marble; ctx.fillRect(0, 0, w, h);
    ctx.fillStyle = C.grey;
    for (let i = -h; i < w; i += 40) { ctx.beginPath(); ctx.moveTo(i, h); ctx.lineTo(i + 14, h); ctx.lineTo(i + 14 + h, 0); ctx.lineTo(i + h, 0); ctx.fill(); }
  },
  dots: (ctx, w, h) => {
    ctx.fillStyle = C.dim; ctx.fillRect(0, 0, w, h);
    ctx.fillStyle = C.ivory;
    for (let j = 18; j < h; j += 36) for (let i = 18 + ((j / 36) % 2) * 18; i < w; i += 36) { ctx.beginPath(); ctx.arc(i, j, 7, 0, 7); ctx.fill(); }
  },
};

// One scrap. lift: 0 flat and sewn, 1 the top-right corner peels up; float: the whole scrap hovers (a bigger shadow).
export function scrap(ctx, { x, y, w, h, rot = 0, pattern = 'gingham', lift = 0, float = 0, stitch = true, thread = true }) {
  ctx.save();
  ctx.translate(x + w / 2, y + h / 2); ctx.rotate(rot * Math.PI / 180); ctx.translate(-w / 2, -h / 2);
  const peel = lift * Math.min(w, h) * 0.42;
  const outline = () => { ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(w - peel, 0); ctx.lineTo(w, peel); ctx.lineTo(w, h); ctx.lineTo(0, h); ctx.closePath(); };
  ctx.save();
  ctx.shadowColor = `rgba(0,0,0,${0.35 + float * 0.15})`; ctx.shadowBlur = 10 + float * 40; ctx.shadowOffsetY = 4 + float * 34; ctx.shadowOffsetX = float * 10;
  outline(); ctx.fillStyle = C.gold; ctx.fill();
  ctx.restore();
  ctx.save(); outline(); ctx.clip(); PATTERNS[pattern](ctx, w, h); ctx.restore();
  if (stitch) {
    ctx.setLineDash([18, 12]); ctx.strokeStyle = C.char; ctx.lineWidth = 5;
    const m = 16;
    ctx.beginPath(); ctx.moveTo(m, m); ctx.lineTo(w - peel - m * 0.4, m);
    ctx.moveTo(w - m, peel + m * 0.4); ctx.lineTo(w - m, h - m); ctx.lineTo(m, h - m); ctx.lineTo(m, m); ctx.stroke();
    ctx.setLineDash([]);
  }
  if (lift > 0 && thread) {
    // the peeled corner: its back side, and a loose thread hanging from the last stitch
    ctx.beginPath(); ctx.moveTo(w - peel, 0); ctx.lineTo(w, peel); ctx.lineTo(w - peel * 0.15, peel * 0.15); ctx.closePath();
    ctx.fillStyle = '#B8770A'; ctx.fill();
  }
  if (lift > 0 && !thread) {
    ctx.beginPath(); ctx.moveTo(w - peel, 0); ctx.lineTo(w, peel); ctx.lineTo(w - peel * 0.15, peel * 0.15); ctx.closePath();
    ctx.fillStyle = '#8C8578'; ctx.fill();
  }
  if (lift > 0 && thread) {
    ctx.strokeStyle = C.char; ctx.lineWidth = 4;
    ctx.beginPath(); ctx.moveTo(w - peel - 6, 16); ctx.bezierCurveTo(w - peel + 30, -40, w + 30, -10, w + 50, -70); ctx.stroke();
  }
  ctx.restore();
}

// A short label sewn onto a scrap, struck through in red when strike is true (red only for strikes).
export function label(ctx, s, cx, cy, size, strike = false) {
  ctx.font = `800 ${size}px Montserrat`; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
  const w = ctx.measureText(s).width + 36, h = size + 26;
  ctx.fillStyle = C.ivory; ctx.fillRect(cx - w / 2, cy - h / 2, w, h);
  ctx.fillStyle = C.char; ctx.fillText(s, cx, cy + 2);
  if (strike) { ctx.strokeStyle = C.red; ctx.lineWidth = 10; ctx.beginPath(); ctx.moveTo(cx - w / 2 - 10, cy + 4); ctx.lineTo(cx + w / 2 + 10, cy - 2); ctx.stroke(); }
}

// A scrap torn half off: only its left edge is still sewn; it hangs off the cloth with a deep shadow,
// and the empty stitch holes where its right side used to be stay on the cloth.
export function tornScrap(ctx, { x, y, w, h, rot = 24 }) {
  ctx.save();
  ctx.fillStyle = 'rgba(0,0,0,0.25)'; ctx.fillRect(x, y, w, h);
  ctx.setLineDash([18, 12]); ctx.strokeStyle = 'rgba(248,246,239,0.8)'; ctx.lineWidth = 6;
  ctx.beginPath(); ctx.moveTo(x + 16, y + 16); ctx.lineTo(x + w - 16, y + 16); ctx.lineTo(x + w - 16, y + h - 16); ctx.lineTo(x + 16, y + h - 16); ctx.stroke();
  ctx.setLineDash([]);
  ctx.translate(x, y + h); ctx.rotate(rot * Math.PI / 180);
  ctx.shadowColor = 'rgba(0,0,0,0.5)'; ctx.shadowBlur = 50; ctx.shadowOffsetX = 24; ctx.shadowOffsetY = 40;
  ctx.fillStyle = C.gold; ctx.fillRect(0, -h, w, h);
  ctx.shadowColor = 'transparent';
  ctx.save(); ctx.beginPath(); ctx.rect(0, -h, w, h); ctx.clip(); ctx.translate(0, -h); PATTERNS.gingham(ctx, w, h); ctx.restore();
  ctx.setLineDash([18, 12]); ctx.strokeStyle = C.char; ctx.lineWidth = 5;
  ctx.beginPath(); ctx.moveTo(16, -h + 16); ctx.lineTo(16, -16); ctx.stroke(); ctx.setLineDash([]);
  ctx.restore();
}
