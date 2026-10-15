// Renders the overlay page to transparent PNG frames (24 fps).
// node render.mjs --from 0 --to 20 --out frames     (run 3 ranges in parallel for the full 60 s)
// node render.mjs --times 0.5,2,9.5 --out test       (single test frames)
import { chromium } from 'playwright';
import fs from 'fs';
const args = process.argv.slice(2);
const opt = {}; for (let i=0;i<args.length;i+=2) opt[args[i].replace(/^--/,'')]=args[i+1];
const out = opt.out || 'frames'; fs.mkdirSync(out,{recursive:true});
const fps = 24;
let times = [];
if (opt.times) times = opt.times.split(',').map(Number).map(t=>({t,name:`t_${t.toFixed(2)}`}));
else { const a=+(opt.from||0), b=+(opt.to||60); for (let i=Math.round(a*fps); i<Math.round(b*fps); i++) times.push({t:i/fps,name:`f${String(i).padStart(5,'0')}`}); }
const browser = await chromium.launch();
const page = await browser.newPage({ viewport:{width:1080,height:1920} });
page.on('console', m => console.log('console:', m.text()));
page.on('pageerror', e => console.log('pageerror:', e.message));
await page.goto('file://' + process.cwd() + '/index.html');
await page.evaluate(() => window.ready);
let n=0;
for (const {t,name} of times) {
  const d = await page.evaluate(t => window.render(t), t);
  fs.writeFileSync(`${out}/${name}.png`, Buffer.from(d.split(',')[1], 'base64'));
  if (++n % 120 === 0) console.log('done', n, '/', times.length);
}
await browser.close(); console.log('ok', n);
