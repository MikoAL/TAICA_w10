// Browser check: open the deck at 1280x720, visit every slide, screenshot it, and report
// content that overflows the slide or runs into the source footer, plus console errors.
// Usage: node scripts/check_browser.mjs [url] [outDir]
import { chromium } from 'playwright-core';
import { mkdirSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';

const url = process.argv[2] || 'file://' + resolve('index.html');
const outDir = process.argv[3] || 'logs/run-1';
const shots = `${outDir}/shots`;
mkdirSync(shots, { recursive: true });

const browser = await chromium.launch({ executablePath: process.env.CHROME || '/usr/bin/chromium' });
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
const consoleErrors = [];
page.on('console', m => { if (m.type() === 'error') consoleErrors.push(m.text()); });
page.on('pageerror', e => consoleErrors.push(String(e)));

await page.goto(url, { waitUntil: 'networkidle' });
await page.waitForFunction(() => window.Reveal && Reveal.isReady());
await page.evaluate(() => document.fonts.ready);
const total = await page.evaluate(() => Reveal.getTotalSlides());

const lines = [];
let errors = 0;
for (let i = 0; i < total; i++) {
  await page.evaluate(n => { Reveal.slide(n); Reveal.getCurrentSlide().querySelectorAll('.fragment').forEach(f => f.classList.add('visible')); }, i);
  await page.waitForTimeout(1000);
  // Measure in slide coordinates (reveal scales the 1280x720 slide to the viewport).
  const r = await page.evaluate(() => {
    const s = Reveal.getCurrentSlide();
    const scale = Reveal.getScale();
    const top = s.getBoundingClientRect().top;
    const footer = s.querySelector('footer.src');
    const footerTop = footer ? (footer.getBoundingClientRect().top - top) / scale : 720;
    let maxBottom = 0, culprit = '';
    s.querySelectorAll('*').forEach(el => {
      if (el.closest('footer.src') || el.closest('aside.notes')) return;
      const b = el.getBoundingClientRect();
      if (b.height === 0) return;
      const bottom = (b.bottom - top) / scale;
      if (bottom > maxBottom) { maxBottom = bottom; culprit = el.tagName.toLowerCase() + (el.className ? '.' + el.className : ''); }
    });
    return { title: (s.querySelector('h1,h2')?.innerText || '').replace(/\s+/g, ' '), maxBottom, footerTop, culprit };
  });
  const n = String(i + 1).padStart(2, '0');
  await page.screenshot({ path: `${shots}/slide-${n}.png` });
  const limit = Math.min(r.footerTop - 6, 720);
  if (r.maxBottom > limit) {
    errors++;
    lines.push(`OVERFLOW slide${i + 1} "${r.title}" content bottom ${r.maxBottom.toFixed(0)}px > limit ${limit.toFixed(0)}px (${r.culprit})`);
  } else {
    lines.push(`OK slide${i + 1} "${r.title}" content bottom ${r.maxBottom.toFixed(0)}px <= ${limit.toFixed(0)}px`);
  }
}
for (const e of consoleErrors) { errors++; lines.push(`CONSOLE_ERROR ${e}`); }
lines.push(`SUMMARY slides=${total} errors=${errors}`);
writeFileSync(`${outDir}/browser.txt`, lines.join('\n') + '\n');
console.log(lines.join('\n'));
await browser.close();
process.exit(errors ? 1 : 0);
