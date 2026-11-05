// node render.js <url>: loads the page in headless Chromium, waits for network idle, prints
// {"status", "final_url", "idle", "html", "requests"} as JSON. Called by render.py; nothing else.
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage();
    const requests = [];
    page.on('request', (r) => requests.push(r.url()));
    let idle = true;
    const res = await page.goto(process.argv[2], { waitUntil: 'networkidle', timeout: 45000 }).catch((e) => {
      if (!/Timeout/i.test(e.message)) throw e;
      idle = false;
      return null;
    });
    const html = await page.content();
    process.stdout.write(JSON.stringify({ status: res && res.status(), final_url: page.url(), idle, html, requests }));
  } finally {
    await browser.close();
  }
})().catch((e) => {
  process.stderr.write(String((e && e.message) || e));
  process.exit(1);
});
