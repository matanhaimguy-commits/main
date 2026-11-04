import { existsSync, readFileSync } from 'node:fs';
import path from 'node:path';
import { Hono } from 'hono';
import { PROJECT_ROOT } from './config/load.js';
import { OrganicHandoffSchema } from './integrations/organic.js';

type Guide = { title: string; description: string; steps: [string, string, string]; labels: string[] };
const GUIDES: Record<string, Guide> = {
  'V24-01': {
    title: 'מה להגיד לכל לקוח כדי שיקשיב למודעה שלך',
    description: 'הפרומפט יראה לך את חמש רמות המודעות של הקהל שלך ויכין מודעה לכל רמה.',
    steps: ['העתק את הפרומפט', 'כתוב מה העסק מוכר ולמי', 'קבל חמש מודעות ובחר מה לבדוק'],
    labels: ['הפרומפט שלך'],
  },
  'V24-02': {
    title: 'הפוך הקלטות של לקוחות למודעות טובות יותר',
    description: 'הלקוחות שלך כבר אומרים את המילים. הכלי הזה עוזר לך למצוא אותן.',
    steps: ['בחר הקלטות או הודעות', 'הדבק את המילים שלהם בפרומפט', 'קבל כותרות והוקים בשפת הלקוח'],
    labels: ['פרומפט לניתוח שיחות'],
  },
  'V24-03': {
    title: 'בנה הצעה חדשה בלי להוריד מחיר',
    description: 'קבל שלוש הצעות שייתנו ללקוח סיבה לבחור בך, בלי להתחיל מהנחה.',
    steps: ['העתק את הפרומפט', 'כתוב מה אתה מוכר וכמה זה עולה', 'קבל שלוש הצעות ובחר את המתאימה'],
    labels: ['פרומפט להצעה חדשה'],
  },
  'V24-04': {
    title: '8 רעיונות שונים למודעות שלך',
    description: 'לא עוד שמונה תמונות של אותו מסר. שמונה סיבות שונות לקנות.',
    steps: ['תאר את המוצר שלך', 'קבל שמונה זוויות שונות', 'בחר ארבעה רעיונות שונים לבדיקה'],
    labels: ['הפרומפט לשמונה זוויות'],
  },
  'V24-05': {
    title: 'כמה כסף באמת נשאר מהפרסום?',
    description: 'מחשבון קצר ופרומפט שיראו כמה כסף נשאר אחרי הוצאות ופרסום.',
    steps: ['מלא את המספרים במחשבון', 'העתק את הפרומפט והכנס נתונים', 'בדוק כמה הרווחת ומה כדאי לשנות'],
    labels: ['מחשבון קצר', 'פרומפט לחישוב הרווח'],
  },
  'V24-06': {
    title: 'איך להגיב כשמישהו מנסה להקטין אותך',
    description: 'שבע תגובות קצרות ופרומפט שיעזור לך לענות כמו שאתה רוצה.',
    steps: ['בחר תגובה שמתאימה לך', 'העתק את הפרומפט', 'תאר מה אמרו לך וקבל תשובות משלך'],
    labels: ['פרומפט לתשובה אישית'],
  },
};

function esc(s: string): string {
  return s.replace(/[&<>"']/g, (c) =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]!);
}

function load(client: string, video: string): { guide: Guide; asset: string } | undefined {
  if (client !== 'emperium' || !GUIDES[video]) return undefined;
  const file = path.join(PROJECT_ROOT, 'imports', 'emperium-v24.json');
  if (!existsSync(file)) return undefined;
  const parsed = OrganicHandoffSchema.parse(JSON.parse(readFileSync(file, 'utf8')));
  const flow = parsed.flows.find((f) => f.source_video_id === video);
  if (!flow) return undefined;
  return { guide: GUIDES[video]!, asset: flow.delivery.asset_content };
}

const CSS = [
  ':root{--bg:#f5f6f2;--ink:#142129;--muted:#586c70;--accent:#007b6c;--mint:#d6eee7;--white:#fff;--line:#dde6e1}',
  '*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 Arial,system-ui,sans-serif}',
  '.top{background:#fff;border-bottom:1px solid var(--line);padding:19px 5%}.brand{max-width:820px;margin:auto;font-size:14px;letter-spacing:2px;font-weight:900}',
  'main{max-width:820px;margin:auto;padding:32px 20px 70px}.eyebrow{color:var(--accent);font-weight:700;font-size:14px}',
  'h1{font-size:clamp(32px,5vw,47px);line-height:1.15;margin:11px 0 18px;letter-spacing:-.5px}h2{font-size:22px;margin:0 0 15px}',
  '.lead{font-size:19px;color:#42535b;max-width:640px;margin-bottom:30px}',
  '.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:20px 0}.step{background:#e7f2ee;border-radius:12px;padding:17px}',
  '.step b{display:grid;place-items:center;background:var(--ink);color:#fff;width:30px;height:30px;border-radius:50%;margin-bottom:10px;font-size:14px}',
  '.panel{border:1px solid var(--line);background:#fff;border-radius:17px;padding:24px;margin:22px 0}',
  '.head{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}',
  '.copy{border:0;background:var(--accent);color:#fff;font:700 15px Arial,sans-serif;border-radius:9px;padding:12px 23px;cursor:pointer}',
  '.copy:hover{filter:brightness(.93)}.copy:focus-visible{outline:3px solid #80d1bf;outline-offset:3px}',
  '.tool{white-space:pre-wrap;overflow-wrap:anywhere;unicode-bidi:plaintext;background:#f1f5f3;border:1px solid #e5eae8;',
  'border-radius:12px;padding:18px;font-size:14px;line-height:1.85;max-height:650px;overflow:auto;margin:14px 0 0}',
  '.extra{white-space:pre-wrap;font-size:15px;color:#3c4d55}.hint{background:var(--mint);padding:20px;border-radius:12px;border-right:4px solid var(--accent)}',
  '.bottom{text-align:center;margin-top:27px}.bottom a{color:var(--accent);font-weight:700;text-decoration:none}',
  '.muted{color:var(--muted);font-size:13px}a:focus-visible{outline:3px solid #80d1bf}',
  '@media(max-width:670px){.steps{grid-template-columns:1fr}.step{display:flex;align-items:center;gap:14px;padding:12px}.step b{margin:0;flex:none}',
  '.panel{padding:18px}main{padding:24px 14px 70px}.lead{font-size:17px}.copy{width:100%}}',
].join('');

function sections(content: string): { codes: string[]; extra: string } {
  const ticks = String.fromCharCode(96).repeat(3);
  const pattern = new RegExp(ticks + '(?:text|json|markdown)?\\r?\\n([\\s\\S]*?)' + ticks, 'g');
  const codes = [...content.matchAll(pattern)].map((m) => m[1]!.trim());
  let extra = content.replace(pattern, '').replace(/^״[^\n]+״\s*/, '').replace(/\*\*/g, '');
  extra = extra.replace(/^(?:הפרומפט לשליחה|הפרומפט להתאמה אישית|מחשבון קצר לשליחה מיד|מדריך קצר לשליחה יחד עם הפרומפט|שבע תגובות מוכנות):\s*$/gm, '');
  return { codes, extra: extra.trim() };
}

export function renderResourcePage(client: string, video: string): string | undefined {
  const resource = load(client, video);
  if (!resource) return undefined;
  const { guide, asset } = resource;
  const { codes, extra } = sections(asset);
  const steps = guide.steps.map((s, i) => '<div class="step"><b>' + (i + 1) +
    '</b><span>' + esc(s) + '</span></div>').join('');
  const cards = codes.map((block, i) => {
    const id = 'prompt-' + i;
    return [
      '<section class="panel"><div class="head"><h2>', esc(guide.labels[i] ?? 'הכלי שלך'), '</h2>',
      '<button class="copy" type="button" data-target="', id, '">העתק</button></div>',
      '<pre class="tool" id="', id, '" dir="auto">', esc(block), '</pre></section>',
    ].join('');
  }).join('');
  const extraBlock = extra ? '<section class="panel"><h2>עוד משהו שיעזור לך</h2><div class="extra">' +
    esc(extra) + '</div></section>' : '';
  const copyScript = [
    'document.querySelectorAll("[data-target]").forEach(function(b){',
    'b.addEventListener("click",async function(){var p=document.getElementById(b.getAttribute("data-target"));if(!p)return;',
    'try{await navigator.clipboard.writeText(p.textContent||"");b.textContent="הועתק!";',
    'setTimeout(function(){b.textContent="העתק";},2000);}catch(e){',
    'var r=document.createRange();r.selectNodeContents(p);var s=window.getSelection();',
    'if(s){s.removeAllRanges();s.addRange(r);}b.textContent="סומן להעתקה";',
    '}});});',
  ].join('');
  return [
    '<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1">',
    '<meta name="description" content="', esc(guide.description), '">',
    '<meta name="theme-color" content="#142129"><title>', esc(guide.title), ' | Emperium</title>',
    '<style>', CSS, '</style></head><body><header class="top"><div class="brand">EMPERIUM</div></header>',
    '<main><p class="eyebrow">המדריך שביקשת בסרטון</p><h1>', esc(guide.title), '</h1>',
    '<p class="lead">', esc(guide.description), '</p>',
    '<h2>איך משתמשים בזה?</h2><div class="steps">', steps, '</div>',
    cards, extraBlock,
    '<div class="hint"><b>הצעד הבא:</b> העתק את הפרומפט, פתח את ChatGPT,',
    ' הדבק אותו ומלא את הפרטים שלך.</div>',
    '<div class="bottom"><a href="https://chatgpt.com/" target="_blank" rel="noopener noreferrer">פתח ChatGPT</a>',
    '<p class="muted">הכלי פתוח לשימוש. אין צורך להירשם.</p></div>',
    '</main><script>', copyScript, '</script></body></html>',
  ].join('');
}

export function resourceRoutes(): Hono {
  const app = new Hono();
  app.get('/:client/:video', (c) => {
    const body = renderResourcePage(c.req.param('client'), c.req.param('video'));
    if (!body) return c.text('Resource not found', 404);
    c.header('Cache-Control', 'public, max-age=300');
    c.header('X-Content-Type-Options', 'nosniff');
    return c.html(body);
  });
  return app;
}
