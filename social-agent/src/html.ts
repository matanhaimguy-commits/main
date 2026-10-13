/** Minimal escaping template for server-rendered pages. */
export class Raw {
  constructor(readonly value: string) {}
  toString() {
    return this.value;
  }
}

export const raw = (s: string) => new Raw(s);

function esc(v: unknown): string {
  if (v instanceof Raw) return v.value;
  if (Array.isArray(v)) return v.map(esc).join('');
  if (v === null || v === undefined || v === false) return '';
  if (v instanceof Date) return v.toISOString().replace('T', ' ').slice(0, 16);
  return String(v).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]!);
}

export function html(strings: TemplateStringsArray, ...values: unknown[]): Raw {
  let out = '';
  strings.forEach((s, i) => {
    out += s + (i < values.length ? esc(values[i]) : '');
  });
  return new Raw(out);
}

const STYLE = `
:root{--bg:#f7f7f5;--card:#fff;--ink:#1b1b1a;--muted:#6b6b66;--line:#e6e5e0;--accent:#4f46e5;--good:#15803d;--warn:#b45309;--bad:#b91c1c;--bubble:#eef0ff}
@media (prefers-color-scheme:dark){:root{--bg:#121212;--card:#1c1c1c;--ink:#ececec;--muted:#9a9a95;--line:#2c2c2c;--accent:#8b85ff;--good:#4ade80;--warn:#fbbf24;--bad:#f87171;--bubble:#25264a}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
header{display:flex;gap:16px;align-items:center;flex-wrap:wrap;padding:12px 16px;border-bottom:1px solid var(--line);background:var(--card)}
header b{margin-right:8px}header a{color:var(--ink);text-decoration:none;opacity:.8}header a:hover{opacity:1;text-decoration:underline}
main{max-width:1100px;margin:0 auto;padding:16px}
h1{font-size:20px;margin:8px 0 16px}h2{font-size:16px;margin:0 0 12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px;margin-bottom:16px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:10px}
.kpi{border:1px solid var(--line);border-radius:8px;padding:10px}.kpi .n{font-size:22px;font-weight:600;font-variant-numeric:tabular-nums}.kpi .l{color:var(--muted);font-size:12px}
.pill{display:inline-block;padding:2px 8px;border-radius:99px;font-size:12px;border:1px solid var(--line)}
.live{color:var(--good);border-color:var(--good)}.dry{color:var(--warn);border-color:var(--warn)}.bad{color:var(--bad)}
.table{overflow-x:auto}table{width:100%;border-collapse:collapse;font-size:14px}th,td{text-align:left;padding:8px 6px;border-bottom:1px solid var(--line);vertical-align:top}th{color:var(--muted);font-weight:500;font-size:12px}
a{color:var(--accent)}.muted{color:var(--muted)}
.msgs{display:flex;flex-direction:column;gap:8px}.msg{max-width:80%;padding:8px 12px;border-radius:12px;white-space:pre-wrap;word-break:break-word}
.in{align-self:flex-start;background:var(--card);border:1px solid var(--line)}.out{align-self:flex-end;background:var(--bubble)}
.meta{font-size:11px;color:var(--muted);margin-top:2px}
form.inline{display:inline}button,select,input{font:inherit;padding:6px 10px;border-radius:6px;border:1px solid var(--line);background:var(--card);color:var(--ink)}button{cursor:pointer}button:disabled{opacity:.5;cursor:not-allowed}
.row{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}.row input{flex:1;min-width:140px}
a.button{display:inline-block;padding:10px 16px;border-radius:8px;background:var(--accent);color:#fff;text-decoration:none;font-weight:600}
code{font:13px ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--bg);border:1px solid var(--line);border-radius:4px;padding:1px 5px;word-break:break-all}
.step{display:flex;gap:12px;padding:10px 0;border-bottom:1px solid var(--line)}.step:last-child{border-bottom:0}.step .mark{width:18px;flex:none;font-weight:700}
table.kv td{border:0;padding:4px 8px 4px 0}.ok{color:var(--good)}
`;

export function page(title: string, body: Raw): string {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(title)}</title><style>${STYLE}</style></head><body>${body.value}</body></html>`;
}
