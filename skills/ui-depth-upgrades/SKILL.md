---
name: ui-depth-upgrades
description: Diagnose and fix boring, flat, or generic-looking app and web UI screens by adding depth, layering, and a cohesive custom visual style. Covers three techniques - (1) pull the main subject out as a cutout, make it oversized, and overlap the headline; (2) turn a flat background into an immersive scene and layer content on top; (3) replace generic components with a custom motif (scalloped image crops, curved lettering, matching buttons and controls). Use this skill whenever the user says a screen, layout, app, landing page, or mockup looks boring, flat, plain, generic, template-like, "AI-looking", or "default", asks for depth, polish, or a custom look, or wants to upgrade UI that currently feels like a stock template.
---

# UI Depth Upgrades

Turn flat / boring / generic screens into designed UI with three concrete moves from a short design-tip video.

## When to use

- User says a screen is boring, flat, plain, generic, template-like, or "AI-looking"
- User asks for more depth, polish, custom style, or a less default look
- User provides a screenshot or description of a UI and wants visual upgrades
- Designing or redesigning app screens, landing pages, marketing sites, or mockups

## Core workflow

1. **Diagnose** the current UI (see references/02-diagnosis-framework.md)
2. **Pick the right move(s)** based on the diagnosis
3. **Implement** with concrete recipes (Web, React Native, SwiftUI, Compose)
4. **Verify** accessibility, contrast, and performance
5. **Ship** with before/after notes

## The three moves

### Move 1 — Oversized subject + headline overlap
**Cures:** Boring layout, weak hierarchy, "everything is the same size"

Pull the main subject (photo, product, illustration, person) out as a cutout, scale it large, and let the headline / key text overlap it. Instant depth and editorial energy.

See: `references/03-technique-oversized-overlap.md` + `assets/templates/oversized-overlap.html`

### Move 2 — Scene background + layered content
**Cures:** Flat screen, no atmosphere, sterile cards-on-white

Replace a solid/flat background with an immersive scene (photo, gradient mesh, illustration) and layer content on top with careful z-order, scrims, and shadows.

See: `references/04-technique-scene-background-layers.md` + `assets/templates/immersive-scene.html`

### Move 3 — One motif everywhere
**Cures:** Generic look, stock components, no brand personality

Pick one distinctive visual motif (scalloped image crops, curved lettering, a custom control shape) and apply it consistently across images, type, buttons, and details.

See: `references/05-technique-cohesive-custom-style.md` + `assets/templates/cohesive-style.html`

## Output format

When applying this skill:

1. State the diagnosis in one sentence
2. Name which move(s) you are applying and why
3. Provide concrete implementation (code, CSS, component changes, or asset prompts)
4. Call out accessibility / contrast notes
5. Optionally show a quick before → after summary

## Scripts

Useful helpers in `scripts/`:

- `scalloped_mask.py` — generate scalloped clip-path / SVG / PNG masks
- `curved_text_svg.py` — generate curved text SVGs
- `contrast_check.py` — check text contrast against backgrounds and scrims
- `cutout_subject.py` — simple subject cutout helpers
- `audit_style_tokens.py` — scan a project for style token consistency

## References

Full detail lives in `references/`. Start with the diagnosis framework, then dive into the specific technique files and implementation recipes.
