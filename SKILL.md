---
name: mango
description: This skill should be used when the user asks to "build a landing page", "create a website", "design a homepage", "make a 3D website", "build a site with depth", "redesign this site", "make it not generic", "give it depth and 3D", "add motion", "awwwards-style site", "immersive site", or requests an artisan/premium/anti-template web presence for a product, brand, venue, or portfolio. Handles artifact-native art direction, bespoke template generation (not reuse), fixed-canvas WebGL depth, collage layering, scroll choreography, and evidence-based verification.
---

# mango — Anti-slop immersive website builder

Build one-of-one websites: artifact-native direction, measured type, depth via a fixed WebGL stage and collage layers, scroll-linked motion, and headless verification. Never ship the same layout twice; never ship the default dark/glow template.

## Non-negotiables (read first)
1. **Direction card before code.** Name the artifact, derive constraints, pick the hero object, the three role fonts, one accent. See `references/art-direction.md`.
2. **Never reuse tokens or layout across briefs.** Calibration shots in `assets/reference-shots/` calibrate density only.
3. **Measure, don't eyeball.** Headline fit, mobile shell width, console errors, failed requests — via `scripts/verify.sh` and the geometry probes in `references/verification.md`.
4. **Reduced motion and touch are first-class.** Keep functional state changes; drop parallax on `prefers-reduced-motion` / `pointer: coarse`.
5. **Report what was verified.** If you could not look at the page, say so; give the numbers you measured.

## Workflow

**0. Ground** — read the user's domain, product, existing site if any, and must-have content. If the user demands "native to the current website," inspect that site first (fetch/crawl); if nothing exists, proceed with the artifact method and state the assumption.

**1. Direction card** — write: `Artifact / Constraints(5+) / Hero object / Type roles / One accent`. If the artifact is unnamed or the constraints are "premium, dark, gold," stop — that is the slop pattern; pick the artifact instead.

**2. Tokens** — seed the OKLCH palette (`scripts/palette.py <hue> <chroma>`), hand-tune tinted neutrals; pick the three role fonts from `references/typography.md`; verify pairing by rendering one display line and one body paragraph before writing sections.

**3. Scaffold** — copy `assets/starter/` into the target repo (`index.html`, `css/main.css`, `js/main.js`, `js/scene.js`). Replace `{{PLACEHOLDERS}}`. Never add a component library unless the artifact demands it.

**4. Hero object (if the artifact has one)** — build the procedural three.js stage per `references/threejs-stage.md`; or, if the story is editorial, build the SVG collage per `references/depth-collage.md` (both may coexist). Object must be interactive or scroll-reactive — otherwise it is decoration.

**5. Sections** — compose from the artifact's region grammar (`references/composition.md`); add one activation→readout interaction (spec plate, scorecard, manifest). One dark band, one ask.

**6. Motion pass** — one scroll metaphor; scrub, not autoplay; honed to ≤3 animated properties per section; sticky horizontals convert to `overflow-x: auto` on mobile (`references/motion.md`).

**7. Anti-slop audit** — run the self-audit in `references/anti-slop.md`; delete anything that fails "could this appear on any brand?"

**8. Verify** — `scripts/verify.sh <url>`; then the geometry probes and interaction probe; then state evidence table (`references/verification.md`) or what you could not verify. Fix failures; re-run. Present the served URL, not localhost-only if a host is assigned.

## Resources
- **references/art-direction.md** — artifact-native method, direction card
- **references/composition.md** — region grammar, grid, type composition
- **references/color.md** — OKLCH ramp, tinted neutrals, accent budget
- **references/typography.md** — three roles, measured fit, loading
- **references/motion.md** — scroll choreography, performance guardrails
- **references/depth-collage.md** — SVG illustration layers, parallax coefficients
- **references/threejs-stage.md** — WebGL fixed canvas, failure modes
- **references/anti-slop.md** — reject list + replacement rule
- **references/verification.md** — headless pipeline, report format
- **references/worked-example.md** — AURELIA case study, calibration boundaries
- **assets/starter/** — minimal baseline (tokens, scripts, pins) — never shipped unmodified
- **assets/reference-shots/** — density calibration only
- **scripts/verify.sh** — headless load/error/overflow/screenshot harness (puppeteer-core + system chromium)
- **scripts/palette.py** — OKLCH 11-step seed ramp generator

## Hard stops
- Do not commit or push unless the user explicitly asks.
- Do not reuse AURELIA tokens/layout as "the mango template."
- Do not claim delivery without running at least steps 8.1–8.3 of verification.
