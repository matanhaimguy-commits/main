// The 22:47 race: the overlay layer (captions, bubbles, chat, brand beat, end card).
// A pure function of time: draw(ctx, t) paints frame t on a transparent 1080x1920 canvas.
// Times come from the voice master (docs/edl.md). Safe zones: top 250, bottom 400, right 140.

const W = 1080, H = 1920;
const C = { red: '#BE0F18', gold: '#DD9A10', ivory: '#F8F6EF', char: '#1F1F1F', ink: '#141414', grey: '#3A3A3C', bubbleIn: '#2C2C2E' };
const FONT = 'Montserrat';

const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lin = (t, a, b) => clamp((t - a) / (b - a));
const easeOut = (x) => 1 - Math.pow(1 - x, 3);
const easeInOut = (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2);
// Critically damped-ish spring with a little overshoot, closed form.
const spring = (x) => (x <= 0 ? 0 : x >= 1.6 ? 1 : 1 - Math.exp(-7 * x) * Math.cos(9 * x));
// In/out envelope: 0 before a, ramps in over fi, holds, ramps out over fo ending at b.
const env = (t, a, b, fi = 0.18, fo = 0.18) => Math.min(lin(t, a, a + fi), 1 - lin(t, b - fo, b));

const img = {};
function loadImages() {
  return Promise.all(
    [['sym', SYM], ['wm', WM]].map(
      ([k, src]) => new Promise((res) => { const i = new Image(); i.onload = () => { img[k] = i; res(); }; i.src = src; }),
    ),
  );
}

function rr(ctx, x, y, w, h, r) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.arcTo(x + w, y, x + w, y + h, r);
  ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r);
  ctx.arcTo(x, y, x + w, y, r);
  ctx.closePath();
}

function wrap(ctx, text, maxW) {
  const words = text.split(' ');
  const lines = [];
  let cur = '';
  for (const w of words) {
    const test = cur ? cur + ' ' + w : w;
    if (ctx.measureText(test).width > maxW && cur) { lines.push(cur); cur = w; } else cur = test;
  }
  if (cur) lines.push(cur);
  return lines;
}

// A super: ivory heavy type on solid charcoal bars, one key phrase on brand red. Pops in word-group by line.
function superText(ctx, t, a, b, lines, y, opts = {}) {
  const e = env(t, a, b, 0.001, 0.2);
  if (e <= 0) return;
  const size = opts.size || 66;
  ctx.font = `800 ${size}px ${FONT}`;
  const lh = size * 1.32;
  lines.forEach((ln, i) => {
    const appear = spring(lin(t, a + i * 0.08, a + i * 0.08 + 0.45) * 1.6);
    if (appear <= 0) return;
    const parts = Array.isArray(ln) ? ln : [[ln, false]];
    let total = 0;
    for (const [s] of parts) total += ctx.measureText(s).width;
    const padX = 22, padY = 12;
    let x = (W - total) / 2 - 20; // centred, nudged left of the right UI rail
    const yy = y + i * lh;
    ctx.save();
    ctx.globalAlpha = e;
    const s = 0.86 + 0.14 * appear;
    ctx.translate(W / 2, yy);
    ctx.scale(s, s);
    ctx.translate(-W / 2, -yy);
    // one bar behind the whole line
    ctx.fillStyle = 'rgba(20,20,20,0.88)';
    rr(ctx, x - padX, yy - size * 0.86 - padY, total + padX * 2, size * 1.1 + padY * 2, 14);
    ctx.fill();
    for (const [str, hot] of parts) {
      const w = ctx.measureText(str).width;
      if (hot) {
        ctx.fillStyle = C.red;
        rr(ctx, x - 8, yy - size * 0.86 - 6, w + 16, size * 1.1 + 12, 10);
        ctx.fill();
      }
      ctx.fillStyle = C.ivory;
      ctx.fillText(str, x, yy);
      x += w;
    }
    ctx.restore();
  });
}

function chip(ctx, t, a, b, text, x, y, opts = {}) {
  const e = env(t, a, b, 0.001, 0.18);
  if (e <= 0) return;
  const p = spring(lin(t, a, a + 0.45) * 1.6);
  const size = opts.size || 46;
  ctx.font = `800 ${size}px ${FONT}`;
  const w = ctx.measureText(text).width + 52;
  const h = size + 34;
  ctx.save();
  ctx.globalAlpha = e;
  ctx.translate(x + w / 2, y + h / 2);
  ctx.scale(0.7 + 0.3 * p, 0.7 + 0.3 * p);
  ctx.fillStyle = opts.bg || 'rgba(20,20,20,0.9)';
  rr(ctx, -w / 2, -h / 2, w, h, h / 2);
  ctx.fill();
  if (opts.ring) { ctx.strokeStyle = opts.ring; ctx.lineWidth = 4; ctx.stroke(); }
  ctx.fillStyle = opts.color || C.ivory;
  ctx.textBaseline = 'middle';
  ctx.fillText(text, -w / 2 + 26, 2);
  ctx.restore();
}

// A chat bubble. side: 'in' (grey, left) or 'out' (red, right). Returns its height.
function bubble(ctx, text, x, y, maxW, side, alpha = 1, scale = 1, size = 44) {
  ctx.font = `800 ${size}px ${FONT}`;
  const lines = wrap(ctx, text, maxW - 56);
  const lh = size * 1.25;
  const w = Math.min(maxW, Math.max(...lines.map((l) => ctx.measureText(l).width)) + 56);
  const h = lines.length * lh + 34;
  const bx = side === 'out' ? x + maxW - w : x;
  ctx.save();
  ctx.globalAlpha = alpha;
  const ox = side === 'out' ? bx + w : bx, oy = y + h;
  ctx.translate(ox, oy);
  ctx.scale(scale, scale);
  ctx.translate(-ox, -oy);
  ctx.fillStyle = side === 'out' ? C.red : C.bubbleIn;
  rr(ctx, bx, y, w, h, 34);
  ctx.fill();
  ctx.fillStyle = C.ivory;
  ctx.textBaseline = 'alphabetic';
  lines.forEach((l, i) => ctx.fillText(l, bx + 28, y + 17 + size * 0.95 + i * lh));
  ctx.restore();
  return h;
}

// Small line icons for the three businesses (drawn, not from any brand).
function icon(ctx, kind, cx, cy, r, color) {
  ctx.save();
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = r * 0.16;
  ctx.lineCap = 'round';
  ctx.lineJoin = 'round';
  if (kind === 'tooth') {
    ctx.beginPath();
    ctx.moveTo(cx - r * 0.55, cy - r * 0.35);
    ctx.bezierCurveTo(cx - r * 0.6, cy - r * 0.85, cx - r * 0.1, cy - r * 0.7, cx, cy - r * 0.5);
    ctx.bezierCurveTo(cx + r * 0.1, cy - r * 0.7, cx + r * 0.6, cy - r * 0.85, cx + r * 0.55, cy - r * 0.35);
    ctx.bezierCurveTo(cx + r * 0.5, cy + r * 0.1, cx + r * 0.35, cy + r * 0.75, cx + r * 0.22, cy + r * 0.72);
    ctx.bezierCurveTo(cx + r * 0.1, cy + r * 0.7, cx + r * 0.08, cy + r * 0.15, cx, cy + r * 0.15);
    ctx.bezierCurveTo(cx - r * 0.08, cy + r * 0.15, cx - r * 0.1, cy + r * 0.7, cx - r * 0.22, cy + r * 0.72);
    ctx.bezierCurveTo(cx - r * 0.35, cy + r * 0.75, cx - r * 0.5, cy + r * 0.1, cx - r * 0.55, cy - r * 0.35);
    ctx.stroke();
  } else if (kind === 'scissors') {
    ctx.beginPath(); ctx.arc(cx - r * 0.35, cy + r * 0.45, r * 0.22, 0, Math.PI * 2); ctx.stroke();
    ctx.beginPath(); ctx.arc(cx + r * 0.35, cy + r * 0.45, r * 0.22, 0, Math.PI * 2); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(cx - r * 0.2, cy + r * 0.28); ctx.lineTo(cx + r * 0.45, cy - r * 0.7); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(cx + r * 0.2, cy + r * 0.28); ctx.lineTo(cx - r * 0.45, cy - r * 0.7); ctx.stroke();
  } else {
    // laser: a beam with sparkles
    ctx.beginPath(); ctx.moveTo(cx - r * 0.6, cy - r * 0.6); ctx.lineTo(cx + r * 0.25, cy + r * 0.25); ctx.stroke();
    for (const [dx, dy, s] of [[0.45, 0.45, 0.22], [0.15, 0.62, 0.12], [0.62, 0.12, 0.12]]) {
      ctx.beginPath();
      ctx.moveTo(cx + r * dx, cy + r * (dy - s)); ctx.lineTo(cx + r * dx, cy + r * (dy + s));
      ctx.moveTo(cx + r * (dx - s), cy + r * dy); ctx.lineTo(cx + r * (dx + s), cy + r * dy);
      ctx.stroke();
    }
  }
  ctx.restore();
}

const KINDS = ['tooth', 'scissors', 'laser'];

// 0.0-4.05: the hook. Three "Sa kushton?" bubbles leave her phone for three businesses.
function hook(ctx, t) {
  if (t > 4.3) return;
  const src = { x: 600, y: 1010 };
  const chips = [{ x: 868, y: 640 }, { x: 868, y: 790 }, { x: 868, y: 940 }];
  const send = [0.3, 0.9, 1.5];
  // business chips
  chips.forEach((c, i) => {
    const a = env(t, 0.15 + i * 0.12, 4.05, 0.3, 0.25);
    if (a <= 0) return;
    const hit = lin(t, send[i] + 0.5, send[i] + 0.62) - lin(t, send[i] + 0.62, send[i] + 0.95);
    const s = (0.7 + 0.3 * spring(lin(t, 0.15 + i * 0.12, 0.65 + i * 0.12) * 1.6)) * (1 + 0.12 * hit);
    ctx.save();
    ctx.globalAlpha = a;
    ctx.translate(c.x, c.y);
    ctx.scale(s, s);
    ctx.fillStyle = 'rgba(20,20,20,0.9)';
    ctx.beginPath(); ctx.arc(0, 0, 58, 0, Math.PI * 2); ctx.fill();
    ctx.strokeStyle = t > send[i] + 0.55 ? C.ivory : 'rgba(248,246,239,0.35)';
    ctx.lineWidth = 5; ctx.stroke();
    ctx.restore();
    if (a > 0) { ctx.save(); ctx.globalAlpha = a; icon(ctx, KINDS[i], c.x, c.y, 34 * s, C.ivory); ctx.restore(); }
  });
  // flying bubbles
  send.forEach((s0, i) => {
    const p = lin(t, s0, s0 + 0.6);
    if (t < s0 || t > 4.05) return;
    const e = easeInOut(p);
    const tx = chips[i].x - 78 - 360, ty = chips[i].y - 44;
    const x = src.x - 150 + (tx - (src.x - 150)) * e;
    const y = src.y + (ty - src.y) * e - Math.sin(e * Math.PI) * 140;
    const sc = p < 1 ? 0.6 + 0.4 * spring(lin(t, s0, s0 + 0.35) * 1.6) : 1;
    const fade = 1 - lin(t, 3.7, 4.05);
    bubble(ctx, 'Sa kushton?', x, y, 420, 'in', fade, sc, 46);
  });
  superText(ctx, t, 0.0, 3.75, [[['Ajo nuk pyeti ', false], ['vetëm ty', true]], 'për çmimin.'], 400, { size: 70 });
}

// The race graphic (15.25-18.9): three businesses, one reply time each; the third wins.
function race(ctx, t) {
  const a = 15.25, b = 18.95;
  const e = env(t, a, b, 0.2, 0.2);
  if (e <= 0) return;
  ctx.save();
  ctx.globalAlpha = e;
  ctx.fillStyle = 'rgba(15,15,15,0.72)';
  ctx.fillRect(0, 0, W, H);
  const rows = [
    { kind: 'tooth', time: '07:10', win: false },
    { kind: 'scissors', time: '08:30', win: false },
    { kind: 'laser', time: '22:47', win: true },
  ];
  const win = spring(lin(t, 17.1, 17.6) * 1.6);
  rows.forEach((r, i) => {
    const appear = spring(lin(t, a + 0.1 + i * 0.22, a + 0.6 + i * 0.22) * 1.6);
    if (appear <= 0) return;
    const y = 640 + i * 230;
    const x = 140, w = 760, h = 190;
    const grow = r.win ? 1 + 0.08 * win : 1 - 0.04 * win;
    ctx.save();
    ctx.translate(x + w / 2, y + h / 2);
    ctx.scale(grow * (0.85 + 0.15 * appear), grow * (0.85 + 0.15 * appear));
    ctx.globalAlpha = e * (r.win ? 1 : 1 - 0.5 * win);
    ctx.fillStyle = r.win && win > 0.05 ? C.red : '#2A2A2C';
    rr(ctx, -w / 2, -h / 2, w, h, 34);
    ctx.fill();
    icon(ctx, r.kind, -w / 2 + 100, 0, 46, C.ivory);
    ctx.fillStyle = C.ivory;
    ctx.font = `800 84px ${FONT}`;
    ctx.textBaseline = 'middle';
    ctx.fillText(r.time, -w / 2 + 190, 4);
    if (r.win) {
      ctx.font = `800 54px ${FONT}`;
      const lbl = '✓ Rezervuar';
      ctx.globalAlpha = e * win;
      ctx.fillText(lbl, w / 2 - 40 - ctx.measureText(lbl).width, 4);
    }
    ctx.restore();
  });
  ctx.restore();
  superText(ctx, t, 17.05, 18.95, [[['Fiton ', false], ['përgjigja e parë', true]], 'e mirë.'], 1460, { size: 66 });
}

// The inside of the third owner's phone (31.4-40.05): an example chat.
function phoneChat(ctx, t) {
  const a = 31.4, b = 40.05;
  const e = env(t, a, b, 0.25, 0.22);
  if (e <= 0) return;
  ctx.save();
  ctx.globalAlpha = e;
  ctx.fillStyle = 'rgba(10,10,10,0.55)';
  ctx.fillRect(0, 0, W, H);
  const px = 150, py = 270, pw = 760, ph = 1240;
  const s = 0.9 + 0.1 * spring(lin(t, a, a + 0.5) * 1.6);
  ctx.translate(px + pw / 2, py + ph / 2);
  ctx.scale(s, s);
  ctx.translate(-(px + pw / 2), -(py + ph / 2));
  ctx.fillStyle = '#0E0E0F';
  rr(ctx, px, py, pw, ph, 64);
  ctx.fill();
  ctx.strokeStyle = '#3A3A3C';
  ctx.lineWidth = 6;
  ctx.stroke();
  // header
  const second = t > 35.75;
  const name = second ? 'Arbër' : 'Elira';
  ctx.fillStyle = C.ivory;
  ctx.font = `800 50px ${FONT}`;
  ctx.textBaseline = 'alphabetic';
  ctx.fillText(name, px + 56, py + 110);
  ctx.font = `800 30px ${FONT}`;
  ctx.fillStyle = C.gold;
  ctx.fillText('SHEMBULL', px + pw - 56 - ctx.measureText('SHEMBULL').width, py + 104);
  ctx.fillStyle = '#2A2A2C';
  ctx.fillRect(px + 30, py + 150, pw - 60, 3);
  ctx.save();
  rr(ctx, px + 8, py + 160, pw - 16, ph - 170, 56);
  ctx.clip();
  const cx = px + 40, cw = pw - 80;
  if (!second) {
    const y0 = py + 210;
    const h1 = bubble(ctx, 'Sa kushton?', cx, y0, cw * 0.7, 'in', 1, 1, 50);
    // typing dots then the answer
    const typing = env(t, 31.55, 32.05, 0.05, 0.05);
    if (typing > 0) {
      ctx.fillStyle = C.red;
      rr(ctx, cx + cw - 170, y0 + h1 + 30, 170, 86, 43);
      ctx.fill();
      for (let i = 0; i < 3; i++) {
        const j = 0.5 + 0.5 * Math.sin((t - 31.55) * 12 - i * 0.9);
        ctx.fillStyle = `rgba(248,246,239,${0.4 + 0.6 * j})`;
        ctx.beginPath(); ctx.arc(cx + cw - 125 + i * 40, y0 + h1 + 73, 10, 0, Math.PI * 2); ctx.fill();
      }
    }
    let y = y0 + h1 + 30;
    if (t >= 32.05) {
      const p = spring(lin(t, 32.05, 32.5) * 1.6);
      const hh = bubble(ctx, 'Përshëndetje, Elira! Ja çmimi dhe 2 orare të lira: e enjte 18:00 · e shtunë 11:00', cx, y, cw * 0.92, 'out', 1, 0.8 + 0.2 * p, 48);
      ctx.font = `800 36px ${FONT}`;
      ctx.fillStyle = '#A1A1A6';
      ctx.fillText('22:47 · brenda 1 minute', cx + cw - ctx.measureText('22:47 · brenda 1 minute').width - 10, y + hh + 50);
      y += hh + 90;
    }
    if (t >= 33.95) {
      const p = spring(lin(t, 33.95, 34.4) * 1.6);
      const hh = bubble(ctx, 'E enjte 18:00 👍', cx, y, cw * 0.8, 'in', 1, 0.8 + 0.2 * p, 50);
      y += hh + 40;
    }
    if (t >= 34.6) {
      const p = spring(lin(t, 34.6, 35.05) * 1.6);
      ctx.save();
      ctx.translate(px + pw / 2, y + 60);
      ctx.scale(0.7 + 0.3 * p, 0.7 + 0.3 * p);
      ctx.font = `800 46px ${FONT}`;
      const s2 = '✓ E enjte 18:00 · rezervuar';
      const bw2 = ctx.measureText(s2).width + 80;
      ctx.fillStyle = 'rgba(221,154,16,0.16)';
      rr(ctx, -bw2 / 2, -58, bw2, 116, 58);
      ctx.fill();
      ctx.strokeStyle = C.gold; ctx.lineWidth = 4; ctx.stroke();
      ctx.fillStyle = C.ivory;
      ctx.textBaseline = 'middle';
      ctx.fillText(s2, -ctx.measureText(s2).width / 2, 3);
      ctx.restore();
    }
  } else {
    const y0 = py + 210;
    const h1 = bubble(ctx, 'Sa kushton?', cx, y0, cw * 0.7, 'in', 1, 1, 50);
    let y = y0 + h1 + 26;
    const h2 = bubble(ctx, 'Përshëndetje, Arbër! Ja çmimi dhe 2 orare të lira 👇', cx, y, cw * 0.92, 'out', 1, 1, 48);
    y += h2 + 60;
    // she went quiet
    const q = spring(lin(t, 36.3, 36.75) * 1.6);
    if (q > 0) {
      ctx.save();
      ctx.globalAlpha = Math.min(1, q);
      ctx.fillStyle = '#2A2A2C';
      ctx.font = `800 44px ${FONT}`;
      const lbl = 'Heshti · 1 orë';
      const w = ctx.measureText(lbl).width + 64;
      rr(ctx, px + (pw - w) / 2, y, w, 76, 38);
      ctx.fill();
      ctx.fillStyle = '#AEAEB2';
      ctx.textBaseline = 'middle';
      ctx.fillText(lbl, px + (pw - w) / 2 + 32, y + 40);
      ctx.restore();
    }
    y += 110;
    // the follow-up: another client's review
    if (t >= 37.2) {
      const p = spring(lin(t, 37.2, 37.65) * 1.6);
      const bw = cw, bx = cx, bh = 300;
      ctx.save();
      ctx.translate(bx + bw, y + bh);
      ctx.scale(0.8 + 0.2 * p, 0.8 + 0.2 * p);
      ctx.translate(-(bx + bw), -(y + bh));
      ctx.fillStyle = C.red;
      rr(ctx, bx, y, bw, bh, 34);
      ctx.fill();
      ctx.fillStyle = C.ivory;
      ctx.font = `800 44px ${FONT}`;
      ctx.textBaseline = 'alphabetic';
      ctx.fillText('Vlerësim nga një', bx + 32, y + 66);
      ctx.fillText('klient tjetër', bx + 32, y + 120);
      ctx.fillStyle = C.gold;
      ctx.font = `800 52px ${FONT}`;
      ctx.fillText('★★★★★', bx + 32, y + 190);
      ctx.fillStyle = 'rgba(248,246,239,0.45)';
      rr(ctx, bx + 32, y + 220, bw - 100, 22, 11); ctx.fill();
      rr(ctx, bx + 32, y + 256, bw - 240, 22, 11); ctx.fill();
      ctx.restore();
      y += bh + 50;
    }
    // never a discount
    if (t >= 38.85) {
      const p = spring(lin(t, 38.85, 39.25) * 1.6);
      const cross = lin(t, 39.15, 39.45);
      ctx.save();
      ctx.translate(px + pw / 2 + 160, y + 70);
      ctx.rotate(-0.12);
      ctx.scale(0.6 + 0.4 * p, 0.6 + 0.4 * p);
      ctx.fillStyle = '#F2F2F2';
      rr(ctx, -120, -62, 240, 124, 26);
      ctx.fill();
      ctx.fillStyle = '#1F1F1F';
      ctx.font = `800 70px ${FONT}`;
      ctx.textBaseline = 'middle';
      ctx.fillText('−20%', -ctx.measureText('−20%').width / 2, 4);
      if (cross > 0) {
        ctx.strokeStyle = C.red; ctx.lineWidth = 12; ctx.lineCap = 'round';
        ctx.beginPath(); ctx.moveTo(-150, 20); ctx.lineTo(-150 + 300 * cross, 20 - 40 * cross); ctx.stroke();
      }
      ctx.restore();
    }
  }
  ctx.restore();
  ctx.restore();
}

function brandBeat(ctx, t) {
  const a = 42.6, b = 45.6;
  const e = env(t, a, b, 0.14, 0.16);
  if (e <= 0 || !img.sym) return;
  ctx.save();
  ctx.globalAlpha = e;
  ctx.fillStyle = C.char;
  ctx.fillRect(0, 0, W, H);
  const p = spring(lin(t, a + 0.05, a + 0.6) * 1.6);
  const ww = 820 * (0.82 + 0.18 * p), wh = (ww * img.wm.height) / img.wm.width;
  ctx.drawImage(img.wm, (W - ww) / 2 - 20, 860 - wh / 2, ww, wh);
  // red rule sweeps under the wordmark
  ctx.fillStyle = C.red;
  const rw = 460 * easeOut(lin(t, a + 0.45, a + 0.95));
  ctx.fillRect((W - 460) / 2 - 20, 860 + 820 * img.wm.height / img.wm.width / 2 + 60, rw, 12);
  ctx.restore();
}

function ctaBlock(ctx, t) {
  // comment box typing ANALIZA, then a stopwatch, then our real reply arriving
  const a = 46.75, b = 50.7;
  const e = env(t, a, b, 0.15, 0.2);
  if (e > 0) {
    ctx.save();
    ctx.globalAlpha = e;
    const y = 1180, x = 110, w = 820, h = 120;
    const p = spring(lin(t, a, a + 0.4) * 1.6);
    ctx.translate(x + w / 2, y + h / 2);
    ctx.scale(0.85 + 0.15 * p, 0.85 + 0.15 * p);
    ctx.translate(-(x + w / 2), -(y + h / 2));
    ctx.fillStyle = 'rgba(248,246,239,0.96)';
    rr(ctx, x, y, w, h, 60);
    ctx.fill();
    const word = 'ANALIZA';
    const n = Math.floor(clamp((t - (a + 0.15)) / 0.6) * word.length);
    ctx.fillStyle = C.char;
    ctx.font = `800 58px ${FONT}`;
    ctx.textBaseline = 'middle';
    ctx.fillText(word.slice(0, n), x + 50, y + h / 2 + 3);
    const cw = ctx.measureText(word.slice(0, n)).width;
    if (Math.floor(t * 3) % 2 === 0 && n < word.length) ctx.fillRect(x + 54 + cw, y + 30, 5, 62);
    // send arrow
    ctx.fillStyle = C.red;
    ctx.beginPath(); ctx.arc(x + w - 70, y + h / 2, 42, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = C.ivory;
    ctx.beginPath();
    ctx.moveTo(x + w - 88, y + h / 2 - 22); ctx.lineTo(x + w - 46, y + h / 2); ctx.lineTo(x + w - 88, y + h / 2 + 22); ctx.closePath();
    ctx.fill();
    ctx.restore();
    // stopwatch
    const sw = env(t, 47.95, b, 0.15, 0.2);
    if (sw > 0) {
      const secs = Math.min(5, Math.floor((t - 48.0) / 0.34));
      chip(ctx, t, 47.95, b, `⏱ 0:0${Math.max(0, secs)}`, 380, 1340, { size: 54 });
    }
  }
  // our real opener arriving as a DM banner
  const d = env(t, 49.65, 52.9, 0.001, 0.25);
  if (d > 0) {
    const p = spring(lin(t, 49.65, 50.1) * 1.6);
    const y = 270 - (1 - p) * 220;
    ctx.save();
    ctx.globalAlpha = d;
    ctx.fillStyle = 'rgba(28,28,30,0.96)';
    rr(ctx, 60, y, 880, 236, 40);
    ctx.fill();
    if (img.sym) ctx.drawImage(img.sym, 92, y + 30, 76, 76);
    ctx.fillStyle = C.ivory;
    ctx.font = `800 44px ${FONT}`;
    ctx.textBaseline = 'alphabetic';
    ctx.fillText('StraightScale', 190, y + 82);
    ctx.font = `800 44px ${FONT}`;
    ctx.fillStyle = '#D1D1D6';
    ctx.fillText('Faleminderit! 🙌 Analiza falas', 92, y + 154);
    ctx.fillText('zgjat 45 minuta, pa detyrim…', 92, y + 208);
    ctx.restore();
  }
}

function endCard(ctx, t) {
  const a = 58.35;
  const e = lin(t, a, a + 0.3);
  if (e <= 0 || !img.sym) return;
  ctx.save();
  ctx.globalAlpha = e;
  ctx.fillStyle = C.char;
  ctx.fillRect(0, 0, W, H);
  const p = spring(lin(t, a + 0.05, a + 0.55) * 1.6);
  const sz = 200 * (0.7 + 0.3 * p);
  ctx.drawImage(img.sym, (W - sz) / 2 - 20, 520 - sz / 2, sz, sz);
  ctx.restore();
  superText(ctx, t, a + 0.15, 61, [[['Komento ', false], ['ANALIZA', true], [' 👇', false]]], 860, { size: 82 });
  superText(ctx, t, a + 0.3, 61, ['Analizë falas · 45 min', 'pa detyrim'], 1010, { size: 56 });
}

function draw(ctx, t) {
  ctx.clearRect(0, 0, W, H);
  ctx.textBaseline = 'alphabetic';
  hook(ctx, t);
  // the night clock
  chip(ctx, t, 4.05, 11.5, '22:47', 70, 270, { size: 50, color: C.ivory });
  // the third owner's phone answers
  if (t >= 8.15 && t < 11.6) {
    const p = spring(lin(t, 8.15, 8.6) * 1.6);
    const fade = 1 - lin(t, 11.3, 11.6);
    bubble(ctx, 'Përshëndetje! Ja çmimi dhe oraret e lira 👇', 150, 1330, 760, 'out', fade, 0.75 + 0.25 * p, 50);
  }
  superText(ctx, t, 9.2, 11.5, [[['Përgjigje ', false], ['brenda 1 minute', true]]], 420, { size: 64 });
  chip(ctx, t, 12.0, 13.4, '✓ Rezervuar', 330, 1100, { size: 58, bg: C.red });
  chip(ctx, t, 13.45, 15.2, '07:10', 70, 270, { size: 50 });
  race(ctx, t);
  // the useless auto-reply, struck out
  if (t >= 24.05 && t < 25.95) {
    const p = spring(lin(t, 24.05, 24.5) * 1.6);
    const fade = 1 - lin(t, 25.7, 25.95);
    const h = bubble(ctx, "Faleminderit për mesazhin! Do t'ju përgjigjemi së shpejti.", 130, 1080, 790, 'in', fade, 0.75 + 0.25 * p, 50);
    const s = lin(t, 24.9, 25.2);
    if (s > 0) {
      ctx.save();
      ctx.globalAlpha = fade;
      ctx.strokeStyle = C.red; ctx.lineWidth = 14; ctx.lineCap = 'round';
      ctx.beginPath(); ctx.moveTo(110, 1080 + h / 2); ctx.lineTo(110 + 820 * s, 1080 + h / 2 - 20 * s); ctx.stroke();
      ctx.restore();
    }
  }
  superText(ctx, t, 29.15, 31.45, [[['Asistent ', false], ['AI', true], [' në Instagram', false]]], 420, { size: 70 });
  phoneChat(ctx, t);
  // the alert on the third owner's phone
  const al = env(t, 40.35, 42.55, 0.001, 0.2);
  if (al > 0) {
    const p = spring(lin(t, 40.35, 40.8) * 1.6);
    const y = 270 - (1 - p) * 200;
    ctx.save();
    ctx.globalAlpha = al;
    ctx.fillStyle = 'rgba(28,28,30,0.95)';
    rr(ctx, 90, y, 820, 130, 40);
    ctx.fill();
    ctx.fillStyle = C.ivory;
    ctx.font = `800 48px ${FONT}`;
    ctx.textBaseline = 'middle';
    ctx.fillText('🔔  Klient i ri · rezervoi', 130, y + 67);
    ctx.restore();
  }
  brandBeat(ctx, t);
  superText(ctx, t, 46.8, 49.65, [[['Komento ', false], ['ANALIZA', true]]], 420, { size: 74 });
  ctaBlock(ctx, t);
  superText(ctx, t, 51.35, 54.6, ['Analizë falas · 45 min', [['pa detyrim', true]]], 1260, { size: 64 });
  superText(ctx, t, 55.0, 58.3, [[['Bëhu ', false], ['përgjigja e parë', true], ['.', false]]], 420, { size: 64 });
  endCard(ctx, t);
}
