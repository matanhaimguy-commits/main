// The text hook: charcoal Montserrat in the top third, wrapped to fit, below the 250 px platform band.
import { C } from './cloth.js';

export function hookText(ctx, lines, { top = 290, size = 104, lead = 1.12, maxW = 960, accent = [] } = {}) {
  ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
  lines.forEach((line, i) => {
    let s = size;
    ctx.font = `800 ${s}px Montserrat`;
    while (ctx.measureText(line).width > maxW) { s -= 2; ctx.font = `800 ${s}px Montserrat`; }
    const words = line.split(' ');
    const total = ctx.measureText(line).width;
    let x = 540 - total / 2;
    const y = top + size * 0.8 + i * size * lead;
    words.forEach((w, k) => {
      const piece = k < words.length - 1 ? w + ' ' : w;
      ctx.fillStyle = accent.includes(w.replace(/[^A-Za-z']/g, '').toLowerCase()) ? C.gold : C.char;
      ctx.fillText(piece, x, y);
      x += ctx.measureText(piece).width;
    });
  });
}
