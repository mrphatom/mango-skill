---
name: mango
description: This skill should be used when the user asks to "build a landing page", "create a website", "design a homepage", "make a 3D website", "build a site with depth", "redesign this site", "make it not generic", "give it depth and 3D", "add motion", "awwwards-style site", "immersive site", or requests an artisan/premium/anti-template web presence for a product, brand, venue, or portfolio. Handles artifact-native art direction, bespoke template generation (not reuse), fixed-canvas WebGL depth, collage layering, scroll choreography, and evidence-based verification.
---

# mango — Anti-slop immersive website builder

Build one-of-one websites that look native to the actual domain first. The skill supplies method, density discipline, and anti-slop rules — never a visual template. Never ship the same layout twice; never ship the default dark/glow template; never ship the AURELIA visual system on a non-AURELIA brief.

## Non-negotiables (read first)
1. **Domain-native first.** A real-estate site must look like a serious real-estate site. A logistics site must look like a logistics operator. The artifact is chosen *from the domain*, not forced onto it. If the finished page could be mistaken for a camera monograph, a film program, or any previous mango output, it has failed.
2. **Direction card before code.** Name the artifact that actually belongs to this domain, derive constraints, pick the hero object, the three role fonts, one accent. See `references/art-direction.md`.
3. **Never reuse tokens or layout across briefs.** Calibration shots in `assets/reference-shots/` calibrate density and layering only. They are not layout blueprints and not a color system.
4. **Measure, don't eyeball.** Headline fit, mobile shell width, console errors, failed requests — via `scripts/verify.sh` and the geometry probes in `references/verification.md`.
5. **Reduced motion and touch are first-class.** Keep functional state changes; drop parallax on `prefers-reduced-motion` / `pointer: coarse`.
6. **Report what was verified.** If you could not look at the page, say so; give the numbers you measured.

## Workflow

**0. Ground** — read the user's domain, product, existing site if any, and must-have content. If the user demands "native to the current website," inspect that site first (fetch/crawl); if nothing exists, proceed with the artifact method and state the assumption. Ask: what physical or editorial object does this industry already produce?

**1. Direction card** — write: `Artifact / Constraints(5+) / Hero object / Type roles / One accent`.  
   - If the artifact is unnamed or the constraints are "premium, dark, gold," stop — that is the slop pattern.  
   - If the artifact is still "printed technical monograph" or the accent is still vermilion on paper when the domain is real-estate / logistics / restaurant / SaaS, stop and re-derive from the actual domain.

**2. Tokens** — seed the OKLCH palette (`scripts/palette.py <hue> <chroma>`), hand-tune tinted neutrals *for this domain*; pick the three role fonts from `references/typography.md` that fit the industry, not the previous brief; verify pairing by rendering one display line and one body paragraph before writing sections.

**3. Scaffold** — copy `assets/starter/` into the target repo (`index.html`, `css/main.css`, `js/main.js`, `js/scene.js`). Immediately replace every token, font, and color. The starter is a neutral shell, not a look.

**4. Hero object (if the artifact has one)** — build the procedural three.js stage per `references/threejs-stage.md`; or, if the story is editorial, build the SVG collage per `references/depth-collage.md` (both may coexist). Object must be interactive or scroll-reactive — otherwise it is decoration. The object must belong to the domain (house model, route map, warehouse volume, menu plate, etc.), never a default camera lens or abstract icosahedron.

**5. Sections** — compose from the artifact's region grammar (`references/composition.md`); add one activation→readout interaction that makes sense for the industry. One dark band, one ask.

**6. Motion pass** — one scroll metaphor that fits the domain story; scrub, not autoplay; honed to ≤3 animated properties per section; sticky horizontals convert to `overflow-x: auto` on mobile (`references/motion.md`).

**7. Anti-slop audit** — run the self-audit in `references/anti-slop.md`; delete anything that fails "could this appear on any brand?" and the stronger test "would a professional in this industry immediately recognize this as their world?"

**8. Verify** — `scripts/verify.sh <url>`; then the geometry probes and interaction probe; then state evidence table (`references/verification.md`) or what you could not verify. Fix failures; re-run. Present the served URL, not localhost-only if a host is assigned.

## Resources
- **references/art-direction.md** — artifact-native method, direction card, domain examples
- **references/composition.md** — region grammar, grid, type composition
- **references/color.md** — OKLCH ramp, tinted neutrals, accent budget
- **references/typography.md** — three roles, measured fit, loading
- **references/motion.md** — scroll choreography, performance guardrails
- **references/depth-collage.md** — SVG illustration layers, parallax coefficients
- **references/threejs-stage.md** — WebGL fixed canvas, failure modes
- **references/anti-slop.md** — reject list + replacement rule
- **references/verification.md** — headless pipeline, report format
- **references/worked-example.md** — AURELIA case study only (discard the look)
- **assets/starter/** — minimal baseline (tokens, scripts, pins) — never shipped unmodified
- **assets/reference-shots/** — density calibration only
- **scripts/verify.sh** — headless load/error/overflow/screenshot harness (puppeteer-core + system chromium)
- **scripts/palette.py** — OKLCH 11-step seed ramp generator

## Hard stops
- Do not commit or push unless the user explicitly asks.
- **Do not reuse AURELIA tokens, palette, type system, layout patterns, FIG. language, monograph grammar, or any visual DNA from the worked example.** That build is a case study of *method*, not a style guide.
- Do not force editorial/print aesthetics onto industrial, commercial, real-estate, logistics, restaurant, or SaaS briefs.
- Do not claim delivery without running at least steps 8.1–8.3 of verification.
