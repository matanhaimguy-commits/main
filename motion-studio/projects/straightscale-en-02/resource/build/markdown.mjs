// The small Markdown subset WORDS.md uses: # and ## headings, paragraphs, - and 1. lists,
// ``` fences, | tables, **bold**, *italic*, `code`. Anything else is a paragraph.

const escape = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

export function inline(text) {
  const parts = escape(text).split(/(`[^`]+`)/);
  return parts
    .map((p) =>
      p.startsWith('`') && p.endsWith('`') && p.length > 1
        ? `<code>${p.slice(1, -1)}</code>`
        : p.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/\*([^*]+)\*/g, '<em>$1</em>'),
    )
    .join('');
}

const cells = (row) => row.trim().replace(/^\||\|$/g, '').split('|').map((c) => c.trim());

function table(rows) {
  const [head, , ...body] = rows;
  const th = cells(head).map((c) => `<th>${inline(c)}</th>`).join('');
  const tr = body.map((r) => `<tr>${cells(r).map((c) => `<td>${inline(c)}</td>`).join('')}</tr>`).join('\n');
  return `<table><thead><tr>${th}</tr></thead><tbody>\n${tr}\n</tbody></table>`;
}

function list(lines, ordered) {
  const items = [];
  for (const line of lines) {
    const m = line.match(/^\s*(?:-|\d+\.)\s+(.*)$/);
    if (m && !/^\s{3,}/.test(line)) items.push({ text: m[1], sub: [] });
    else if (m) items.at(-1).sub.push(m[1]);
    else items.at(-1).text += ' ' + line.trim();
  }
  const tag = ordered ? 'ol' : 'ul';
  const li = items
    .map((i) => `<li>${inline(i.text)}${i.sub.length ? `<ul>${i.sub.map((s) => `<li>${inline(s)}</li>`).join('')}</ul>` : ''}</li>`)
    .join('\n');
  return `<${tag}>\n${li}\n</${tag}>`;
}

export function render(md) {
  const lines = md.replace(/\r\n/g, '\n').split('\n');
  const out = [];
  let i = 0;
  const isList = (l) => /^\s*(?:-|\d+\.)\s+/.test(l);
  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) { i++; continue; }
    if (line.startsWith('```')) {
      const body = [];
      for (i++; i < lines.length && !lines[i].startsWith('```'); i++) body.push(lines[i]);
      i++;
      out.push(`<pre><code>${escape(body.join('\n'))}</code></pre>`);
    } else if (/^#{1,3} /.test(line)) {
      const level = line.match(/^#+/)[0].length;
      out.push(`<h${level}>${inline(line.slice(level + 1))}</h${level}>`);
      i++;
    } else if (line.startsWith('|')) {
      const rows = [];
      for (; i < lines.length && lines[i].startsWith('|'); i++) rows.push(lines[i]);
      out.push(table(rows));
    } else if (isList(line)) {
      const ordered = /^\s*\d+\./.test(line);
      const block = [];
      for (; i < lines.length && lines[i].trim() && (isList(lines[i]) || /^\s+/.test(lines[i])); i++) block.push(lines[i]);
      out.push(list(block, ordered));
    } else {
      const para = [];
      for (; i < lines.length && lines[i].trim() && !/^(#|```|\|)/.test(lines[i]) && !isList(lines[i]); i++) para.push(lines[i].trim());
      out.push(`<p>${inline(para.join(' '))}</p>`);
    }
  }
  return out.join('\n');
}
