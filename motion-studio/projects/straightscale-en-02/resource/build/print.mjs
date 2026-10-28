// Prints an HTML string to an A4 PDF with the pre-installed Chromium.
// require() finds the globally installed Playwright; an ESM import does not.
import { createRequire } from 'node:module';

const { chromium } = createRequire(import.meta.url)('playwright');

export async function printPdf(html, outPath) {
  const browser = await chromium.launch();
  try {
    const p = await browser.newPage();
    await p.setContent(html, { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: outPath, format: 'A4', printBackground: true, margin: { top: '16mm', bottom: '16mm', left: '16mm', right: '16mm' } });
  } finally {
    await browser.close();
  }
}
