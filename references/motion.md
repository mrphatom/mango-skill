# mango — Motion: scroll is the timeline, not a decoration channel

## Principles
1. **One metaphor runs the whole page.** In the AURELIA build the camera objective rotates, dollies, and the iris contracts as scroll advances — the user is walking through the story, not watching scattered effects.
2. **Scroll-scrub, not autoplay.** `gsap.to(..., { scrollTrigger: { scrub: 0.6 } })`. Scrub values 0.5–1.0 feel mechanical; lower = cheaper, higher = sluggish.
3. **Animate one property per beat.** Rotate the object while fading the collage layer; never scale X/Y together with rotate and blur.
4. **Hover is a question, not a fireworks show.** Tilt 3–6°, translate 4–8px, shadow lift one step. Anything larger reads as a different site.
5. **Intro under 1.2s total.** Stagger 0.1–0.15s; ease `power3/4.out`. If the hero is not readable by 1s, it's too slow.
6. **Reduced motion is a feature branch, not a global off switch.** Keep functional state changes (counters, iris) but remove parallax and scrub rotation.

## Layer recipes that worked
- **Hero parallax:** 3 SVG illustration layers (diagram, reticle, badge) driven by one rAF loop with per-layer coefficients; lerp 0.07–0.1. No GSAP needed there.
- **Scroll-linked rotation:** `gsap.to(layer, { rotate, y, ease:'none', scrollTrigger: { scrub: 0.7 }})` — scrub ties motion to reading speed.
- **Sticky horizontal strip:** pin a container, translate its track by `x: -distance()`, `end: '+=' + (distance() + innerHeight*0.3)`. On <760px replace with `overflow-x: auto` + `scroll-snap`; NEVER `overflow: hidden` a mobile horizontal strip.
- **Stacked-sheet plate:** pseudo-elements at ±6px offsets, rotate 0.5–0.8deg; main plate tilts with pointer (max 6°).
- **Zero-JS fallback:** if GSAP/ScrollTrigger missing, skip registration and reveal sections statically; no console errors.

## Performance guardrails
- `will-change` only on elements actively animated; remove after intro if possible.
- `pointermove` handlers: passive, lerp in rAF, never set style synchronously per event.
- Dust/particle counts ≤ 700 desktop; sprite canvas 64px; `Points` with `sizeAttenuation: true`.
- `gsap.ticker.lagSmoothing(0)` when syncing Lenis; `lenis.on('scroll', ScrollTrigger.update)`.
- Screenshot the page after each motion PR and compare top/bottom contrast — motion must not muddy the gradient budget.

## Interaction checklist per page
- [ ] At least one persistent interactive affordance (drag, hover, tap) — not only scroll.
- [ ] One section where activation changes a readout (spec/figure/price).
- [ ] All animations respect `prefers-reduced-motion`.
- [ ] No element traps scroll (Lenis `duration ≤ 1.2`, `wheelMultiplier ≤ 1`).
- [ ] Mobile: horizontal strips scrollable by finger; no `cursor: none` below 760px.
