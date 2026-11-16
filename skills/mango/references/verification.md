# mango — Verification: evidence, not adjectives

Forbidden close: "it should be live now." Required close: a table of what was run, what it printed, and what is unverified.

## The pipeline (run in order)
1. **Static** — `node --check js/*.js` (ESM scene files: `cp scene.js /tmp/x.mjs && node --check /tmp/x.mjs; rm /tmp/x.mjs`). CSS: open once, look for stray `@media` nesting and unmatched braces; optionally `npx stylelint "css/**/*.css"` if the repo has it — do not install it into the user's repo without asking.
2. **Headless load + errors** — `scripts/verify.sh <url>`. Read the output; do not skim it. Required: `ERRORS []`, `FAILED []`.
3. **Geometry probes** — in `page.evaluate`, measure: `documentElement.scrollWidth` vs `clientWidth`; every `.headline-fit` / `.line__inner` `scrollWidth` vs its parent's `clientWidth`. Fail the build if any overflows.
4. **Section sweep** — scroll to each `section[id]`, wait ~1.2s, screenshot. Compare pixel stats of new vs old if iterating (Pillow `resize((120,75)).getdata()` → average + max/min). "Average brightness moved" is not success; "errors are 0 and mobile sw == cw" is.
5. **Interaction probe** — drive the primary affordance headlessly: `dispatchEvent(new PointerEvent('pointerdown' …))` → check `body.classList.contains('is-inspecting')`; click the optics radio group; scroll to `.ledger` and assert counters are non-zero.
6. **Reduce risk of lying tools** — `waitUntil: 'domcontentloaded'`, never `'load'`/`'networkidle2'`. If your browser tool times out with "no close frame", fall back to `verify.sh`; do not conclude the site is broken.
7. **Manual gate** — report what was *looked at* vs *measured*. If you cannot view images (agent limitation), say so; geometry + stats are the evidence.

## HTTP / deployment checks
- `curl -s -o /dev/null -w '%{http_code}' <local>` for each asset (HTML, css, js, hero video/images).
- For the public host: `curl` from the sandbox may return `000` while `verify.sh` from the same machine returns `200` — trust the headless browser result; report both.
- If the site is served by `python3 -m http.server`, note the PID and document that stopping the conversation's shell will stop the server.
- Never commit/push unless the user asks. If asked: `git status --short`, `git add` explicitly-named paths, commit with `Co-authored-by: openhands <openhands@all-hands.dev>`, then push.

## Anti-patterns observed in the field
- Claiming "desktop is fine" after checking mobile only.
- Checking `scrollH` (content height) as a proxy for "no overflow" — use `scrollWidth`.
- Treating console *warnings* as errors and rewriting the page; treat 404s as failures, warnings as notes.
- Using `page.goto(..., waitUntil: 'load')` then declaring victory on timeout — the page may be fine; the wait was wrong.
