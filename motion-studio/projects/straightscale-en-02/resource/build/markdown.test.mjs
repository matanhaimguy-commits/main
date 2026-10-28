import { test } from 'node:test';
import assert from 'node:assert/strict';
import { inline, render } from './markdown.mjs';

test('inline: bold, italic, code, escaping', () => {
  assert.equal(inline('**a** *b* `c<d>`'), '<strong>a</strong> <em>b</em> <code>c&lt;d&gt;</code>');
  assert.equal(inline('`**x**`'), '<code>**x**</code>');
});

test('render: headings, fence, list with sub-items, table', () => {
  const html = render('# T\n\n## S\n\n```\nsite:x "a"\n```\n\n1. one\n   - sub\n2. two\n\n| a | b |\n|---|---|\n| 1 | 2 |\n');
  assert.match(html, /<h1>T<\/h1>/);
  assert.match(html, /<h2>S<\/h2>/);
  assert.match(html, /<pre><code>site:x "a"<\/code><\/pre>/);
  assert.match(html, /<ol>\n<li>one<ul><li>sub<\/li><\/ul><\/li>\n<li>two<\/li>/);
  assert.match(html, /<th>a<\/th><th>b<\/th>.*<td>1<\/td><td>2<\/td>/s);
});

test('render: wrapped list item joins its continuation line', () => {
  assert.match(render('- a\n  b\n'), /<li>a b<\/li>/);
});
