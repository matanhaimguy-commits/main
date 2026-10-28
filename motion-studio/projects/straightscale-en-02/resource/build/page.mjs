// Wraps the rendered resource in the EN 02 brand page: fonts embedded, wordmark on the cover band.
import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const b64 = (p) => readFileSync(p).toString('base64');

export function fontFaces(fontsDir) {
  const faces = [
    ['Playfair Display', 'PlayfairDisplay/playfair-display-latin-700-normal.woff2', 700, 'normal'],
    ['Playfair Display', 'PlayfairDisplay/playfair-display-latin-400-italic.woff2', 400, 'italic'],
    ['Montserrat', 'Montserrat/montserrat-latin-400-normal.woff2', 400, 'normal'],
    ['Montserrat', 'Montserrat/montserrat-latin-600-normal.woff2', 600, 'normal'],
    ['Montserrat', 'Montserrat/montserrat-latin-700-normal.woff2', 700, 'normal'],
  ];
  return faces
    .map(([family, file, weight, style]) =>
      `@font-face{font-family:'${family}';src:url(data:font/woff2;base64,${b64(join(fontsDir, file))}) format('woff2');font-weight:${weight};font-style:${style};}`)
    .join('\n');
}

export function page({ body, css, fonts, wordmarkPath, title }) {
  const mark = `data:image/png;base64,${b64(wordmarkPath)}`;
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>${title}</title>
<style>${fonts}\n${css}</style></head><body>
<header class="band"><img src="${mark}" alt="StraightScale"></header>
<main>${body}</main></body></html>`;
}
