#!/usr/bin/env bash
# mango verification harness — checks a built site headlessly via system chromium + puppeteer-core.
# Usage: scripts/verify.sh <url> [workdir]
# Requires: node >= 18, /usr/bin/chromium (or $CHROMIUM), npm registry reachable for puppeteer-core.
set -u
URL="${1:-http://127.0.0.1:8137/}"
WORK="${2:-/tmp/mango-verify}"
CHROMIUM_BIN="${CHROMIUM:-/usr/bin/chromium}"

mkdir -p "$WORK" && cd "$WORK" || exit 2

# 1) Install puppeteer-core into the workdir if absent (never into the target repo)
if [ ! -d node_modules/puppeteer-core ]; then
  echo "[mango] installing puppeteer-core@23 into $WORK ..."
  npm init -y >/dev/null 2>&1
  npm install puppeteer-core@23 --no-audit --no-fund --loglevel=error || exit 3
fi

# 2) Write the harness once
cat > check.mjs <<'MJS'
import puppeteer from 'puppeteer-core';
const url = process.argv[2];
const browser = await puppeteer.launch({
  executablePath: process.env.CHROMIUM_BIN || '/usr/bin/chromium',
  headless: 'new',
  args: ['--no-sandbox', '--disable-dev-shm-usage', '--window-size=1440,900', '--ignore-gpu-blocklist']
});
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 1 });
const errors = [], failed = [];
page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
page.on('pageerror', e => errors.push('pageerror: ' + e.message));
page.on('requestfailed', r => failed.push('reqfail: ' + r.url().slice(0, 110) + ' :: ' + (r.failure()?.errorText || '')));
page.on('response', r => { if (r.status() >= 400) failed.push(r.status() + ' ' + r.url().slice(0, 110)); });

// NOTE: use domcontentloaded, never 'load'/'networkidle2' — rAF/WebGL pages hang those waits forever.
await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
await new Promise(r => setTimeout(r, 3500));
const info = await page.evaluate(() => ({
  title: document.title,
  h: document.documentElement.scrollHeight,
  webgl: !!document.querySelector('canvas#webgl, canvas')
}));
console.log('PAGE', JSON.stringify(info));

// Section sweep: screenshot anything with an ID or common section classes
const ids = await page.evaluate(() => Array.from(document.querySelectorAll('section[id], main [id]')).map(e => e.id).filter(Boolean));
for (const id of ids.slice(0, 8)) {
  await page.evaluate(id => document.getElementById(id)?.scrollIntoView(), id);
  await new Promise(r => setTimeout(r, 1200));
  await page.screenshot({ path: `${process.env.WORK}/shot-${id.replace(/[^a-z0-9_-]/gi, '-')}.png` });
}
await page.screenshot({ path: `${process.env.WORK}/shot-full.png`, fullPage: false });

// Mobile shell overflow check
const mob = await browser.newPage();
await mob.setViewport({ width: 390, height: 844, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });
mob.on('pageerror', e => errors.push('mobile pageerror: ' + e.message));
await mob.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
await new Promise(r => setTimeout(r, 2500));
const ov = await mob.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth }));
console.log('MOBILE_OVERFLOW', JSON.stringify(ov));
await mob.close();

// Headline/inner-text fit: any .line__inner wider than its parent is a clipped headline
const fit = await page.evaluate(() => {
  const bad = [];
  document.querySelectorAll('.line__inner, .headline-fit').forEach(el => {
    if (el.scrollWidth > el.parentElement.clientWidth + 1) bad.push({ text: el.textContent.slice(0, 30), need: el.scrollWidth, have: el.parentElement.clientWidth });
  });
  return bad;
});
if (fit.length) console.log('FIT_WARN', JSON.stringify(fit));

console.log('ERRORS', JSON.stringify(errors, null, 2));
console.log('FAILED', JSON.stringify(failed, null, 2));
await browser.close();
process.exit(errors.length || failed.length ? 1 : 0);
MJS

CHROMIUM_BIN="$CHROMIUM_BIN" WORK="$WORK" node check.mjs "$URL"
code=$?
echo "[mango] exit=$code  (shots in $WORK)"
exit $code
