import { test } from 'node:test';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
import { fontFaces, page } from './page.mjs';

const project = fileURLToPath(new URL('../../', import.meta.url));

test('fonts are embedded, not linked', () => {
  const f = fontFaces(project + 'assets/fonts');
  assert.match(f, /font-family:'Playfair Display';src:url\(data:font\/woff2;base64,/);
  assert.equal((f.match(/@font-face/g) || []).length, 5);
});

test('page carries the real wordmark as data and the body', () => {
  const html = page({ body: '<p>x</p>', css: '', fonts: '', wordmarkPath: project + 'assets/brand/wordmark-white.png', title: 'T' });
  assert.match(html, /<img src="data:image\/png;base64,/);
  assert.match(html, /<main><p>x<\/p><\/main>/);
});
