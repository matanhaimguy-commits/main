// node build/build.mjs  ->  checks WORDS.md, then writes WORDS.html and WORDS.pdf next to it.
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { check } from './check.mjs';
import { render } from './markdown.mjs';
import { fontFaces, page } from './page.mjs';
import { printPdf } from './print.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const res = join(here, '..');
const project = join(res, '..');
const md = readFileSync(join(res, 'WORDS.md'), 'utf8');

const result = check(md);
console.log(`WORDS.md: ${result.words} words, ${result.minutes} timed minutes`);
if (!result.ok) {
  console.error(result.problems.map((p) => `FAIL ${p}`).join('\n'));
  process.exit(1);
}
const html = page({
  body: render(md),
  css: readFileSync(join(here, 'style.css'), 'utf8'),
  fonts: fontFaces(join(project, 'assets/fonts')),
  wordmarkPath: join(project, 'assets/brand/wordmark-white.png'),
  title: 'The WORDS Sheet',
});
writeFileSync(join(res, 'WORDS.html'), html);
await printPdf(html, join(res, 'WORDS.pdf'));
console.log('wrote WORDS.html, WORDS.pdf');
