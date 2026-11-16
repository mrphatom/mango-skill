# mango — Worked example: the AURELIA build (case study, not template)

> Reference the screenshots in `assets/reference-shots/` as calibrated output — never copy this site's tokens or layout into the next build. The artifact, constraints, object, and accent all differ by brief.

## Direction card (as built)
1. Artifact: printed technical monograph / specification plate for a fictitious lens manufactory ("AURELIA OPTICS AG, Baar, CH").
2. Constraints: hairline rules; numbered `FIG.` sections with reg keys; one dark interferometric readout plate on paper; one vermilion spot accent; expanded grotesque display with variable width; optical serif body; technical mono labels; no pure black/white.
3. Hero object: procedural 40 mm f/0.95 "Nocturne" objective (brass ring, machined barrel, 9-blade iris, vermilion ember).
4. Type system: Archivo Expanded 850–900 for display (measured fit), Newsreader 400–600 for body/italic caption style, Spline Sans Mono for HUD labels.
5. Accent: vermilion (#e8442e) on paper (#f2efe6) and ink (#131310).

## Build sequence mapped to phases
- Phase 0 – brief: user demanded "anti-slop, native, depth, 3D, scroll choreography." Rejected the first pass (generic dark+gold) precisely because it fit the default-luxury AI pattern.
- Phase 1 – artifact + constraints: chose the monograph; derived the constraint list; wrote direction card before code.
- Phase 2 – color/type: `scripts/palette.py` seed → hand-tuned tinted neutrals; Archivo Expanded adopted for `font-stretch` control.
- Phase 3 – scaffold: `assets/starter/` extended (GSAP/ScrollTrigger/Lenis/three CDN pins), not a UI kit.
- Phase 4 – 3D stage: cylinder barrel + brass ring + knurled focus ring + emissive index line + 3-layer glass + 9-blade iris group + emissive core/halo + 650-point dust + `FogExp2(0xf2efe6, 0.055)`.
- Phase 5 – collage: cross-section SVG ("SECTION A–A / 124 mm"), aperture reticle rotor, EST-2011 circular textPath badge; pointer-parallax coefficients −14/+22/−26px; badge scroll-rotation via scrub.
- Phase 6 – motion pass: sticky horizontal "film contact sheet," spec-plate tilt, ghost numerals, ledger counters, vermilion spec-bar sweep.
- Phase 7 – verification: `scripts/verify.sh`; fixed real failures: mobile overflow (`scrollWidth 2265→390`), clipped headline (measured 1473px needed vs 1318 available → per-line clamps), dead drag-inspect (canvas `pointer-events:none` vs scene bound to canvas events → moved to window-level cover-scoped handler).
- Phase 8 – close: public host confirmed 200 via headless browser; uncommitted files; user told explicitly what was and was not verified.

## What generalized (keep)
- Verify.sh harness, R6 headline-fit rule, direction card, collage coefficients, drag-inspect pattern, mobile sticky-strip overflow rule.

## What is brand-specific (discard on the next brief)
- The monograph constraints, the vermilion/paper palette, the camera object, Archivo Expanded specifically, "BAAR" references, `FIG. n` labels — all belong to AURELIA, the artifact.

## Calibration images
- `assets/reference-shots/calibration-hero-desktop.png` — hero with collage overlap (type/illustration layering intent).
- `assets/reference-shots/calibration-hero-mobile.png` — mobile collapse of collage (diagram top, badge beside lede, no overflow).
- `assets/reference-shots/calibration-reserve.png` — order-slip (persistent CTA as artifact, not newsletter signup).
Use them to calibrate density and layering — never as layout blueprints.
