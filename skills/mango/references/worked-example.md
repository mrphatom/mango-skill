# mango — Worked example: the AURELIA build (case study of method only)

> **Critical:** This is a case study of *process*, not a style guide.  
> Reference the screenshots in `assets/reference-shots/` only for density and layering calibration.  
> **Never copy this site's tokens, palette, type system, layout patterns, FIG. language, or visual DNA into the next build.**  
> The artifact, constraints, object, and accent all differ by brief. If the next brief is real-estate, logistics, restaurant, SaaS, or anything else, the finished page must look native to *that* domain.

## Direction card (as built for AURELIA only)
1. Artifact: printed technical monograph / specification plate for a fictitious lens manufactory ("AURELIA OPTICS AG, Baar, CH").
2. Constraints: hairline rules; numbered `FIG.` sections with reg keys; one dark interferometric readout plate on paper; one vermilion spot accent; expanded grotesque display with variable width; optical serif body; technical mono labels; no pure black/white.
3. Hero object: procedural 40 mm f/0.95 "Nocturne" objective (brass ring, machined barrel, 9-blade iris, vermilion ember).
4. Type system: Archivo Expanded 850–900 for display (measured fit), Newsreader 400–600 for body/italic caption style, Spline Sans Mono for HUD labels.
5. Accent: vermilion (#e8442e) on paper (#f2efe6) and ink (#131310).

## What generalized (keep the method)
- Direction card written before any code.
- Verify.sh harness and geometry probes.
- R6 headline-fit rule.
- Collage coefficients and drag-inspect pattern (when the artifact supports them).
- Mobile sticky-strip overflow rule.
- One scroll metaphor, scrubbed.
- Domain-native artifact selection.

## What is brand-specific (must be discarded on every other brief)
- The monograph constraints
- The vermilion / paper / ink palette
- The camera / lens object
- Archivo Expanded specifically
- "BAAR", "FIG. n", "SECTION A–A", technical plate language
- Any layout that still reads as a printed instrument monograph

If the next brief is a real-estate developer, a logistics company, a restaurant, or a SaaS product, **none** of the visual decisions above should appear. Choose a new artifact that belongs to that industry and derive a new direction card from scratch.

## Calibration images (density only)
- `assets/reference-shots/calibration-hero-desktop.png` — hero with collage overlap (type/illustration layering intent).
- `assets/reference-shots/calibration-hero-mobile.png` — mobile collapse of collage (diagram top, badge beside lede, no overflow).
- `assets/reference-shots/calibration-reserve.png` — order-slip (persistent CTA as artifact, not newsletter signup).

Use them to calibrate density and layering — never as layout blueprints or color references.
