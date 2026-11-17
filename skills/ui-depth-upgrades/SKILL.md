---
name: ui-depth-upgrades
description: Diagnose and fix boring, flat, or generic-looking app and web UI screens by adding depth, layering, and a cohesive custom visual style. Covers three techniques - (1) pull the main subject out as a cutout, make it oversized, and overlap the headline; (2) turn a flat background into an immersive scene and layer content on top; (3) replace generic components with a custom motif (scalloped image crops, curved lettering, matching buttons and controls). Use this skill whenever the user says a screen, layout, app, landing page, or mockup looks boring, flat, plain, generic, template-like, "AI-looking", or "default", asks how to make a UI more premium, editorial, expressive, or distinctive, wants to polish a vibe-coded or AI-generated interface, or asks for before/after UI redesign prompts for plant, weather, music, fitness, food, finance or any other app - even if they never name these techniques.
---

# UI Depth Upgrades

Turn a screen that "works but feels boring" into one that feels designed. The method comes from a short design-tip video (creator handle @ayoships) that showed three before/after app screens - a plant-care detail page, a weather app, and a music player - and boiled the fix down to three moves, each matched to a symptom. See `references/01-video-source-notes.md` for the full breakdown of the source.

The core idea: boring UI is usually **flat** (everything sits on one plane), **timid** (every element is the same size and politely inside its box), or **generic** (stock components with no shared personality). Each symptom has a specific remedy.

## The three moves at a glance

| Symptom the user describes | Move | One-line recipe |
|---|---|---|
| "The layout feels boring" | **1. Oversized subject + headline overlap** | Cut the main subject out of its photo box, scale it up past the layout grid, and let it overlap the headline. |
| "The screen feels flat" | **2. Scene background + layers** | Make the background a full-bleed scene (not a flat colour), then stack content on top in clear layers. |
| "It feels generic" | **3. Cohesive custom style** | Pick one motif and push it through image crops, lettering, and controls so they all match. |

These can be combined, but apply them in order of the diagnosis, not all at once. Stacking all three on every screen produces visual noise. Usually one primary move plus light support from another is right.

## Workflow

1. **Capture the screen.** Get the screenshot, code, Figma description, or written description. Identify the screen's *job* (what the user must do or learn here), its *hero* (the single most emotionally or informationally important thing), and its *content* (text, data, controls that must stay readable). If the user supplies only a vague request, make reasonable assumptions, state them in one line, and proceed. Ask at most one clarifying question.
2. **Diagnose.** Use `references/02-diagnosis-framework.md` to map symptoms to moves. Name the symptom out loud in your answer ("This is flat because the background is a single blue fill and everything sits on one plane").
3. **Pick the primary move** (and at most one supporting move). Read the matching reference:
   - Move 1 → `references/03-technique-oversized-overlap.md`
   - Move 2 → `references/04-technique-scene-background-layers.md`
   - Move 3 → `references/05-technique-cohesive-custom-style.md`
4. **Produce the deliverable the user needs.** Depending on the request, that is one or more of:
   - A redesign spec (what changes, why, exact values: sizes, offsets, z-order, blur, radii, colours).
   - Working code. See `references/06-implementation-recipes.md` for HTML/CSS, React Native, SwiftUI, and Jetpack Compose. Start from `assets/templates/` when building web mockups.
   - Image-generation prompts for the cutout, scene, or artwork. See `references/07-asset-generation-prompts.md`.
   - A before/after description or mockup.
5. **Protect usability.** Depth must never cost legibility or accessibility. Run through `references/08-accessibility-and-performance.md` and `references/09-qa-checklist.md` before finalising. Use `scripts/contrast_check.py` for any text sitting on imagery.
6. **Explain the why.** For every change, give a one-sentence reason tied to the symptom. Users learn the principle, not just the patch.

## Move 1 - Oversized subject + headline overlap (cures "boring layout")

What the video showed: a plant-care page had a small rectangular photo of a fiddle-leaf fig, a centred title, and rows of info. The upgrade removed the photo's box, cut the plant out, blew it up so leaves bleed off the right edge, set the title "Fiddle-leaf fig" in a large condensed serif, and let the plant's leaves overlap the headline.

Essentials:
- **Cut out** the subject (transparent PNG/WebP). A subject in a rectangle reads as a thumbnail; a subject with no box reads as a poster.
- **Scale past the grid.** The subject should be larger than its original slot, often 1.4–2×, and intentionally break the margin or bleed off an edge.
- **Overlap the type.** Place the headline so the subject intersects it (leaves over letters, product over title). Use a high-contrast fill or text-shadow / outline so the type stays readable where it crosses the subject.
- **Anchor the rest.** Keep secondary content (stats, buttons, body copy) in a stable lower region so the composition does not feel chaotic.

Use `scripts/cutout_subject.py` for simple keying / shadow, and `references/03-technique-oversized-overlap.md` for layout recipes and platform code.

## Move 2 - Scene background + layered content (cures "flat screen")

What the video showed: a weather app with a solid blue fill and white cards. The upgrade replaced the fill with a full-bleed scene (sky + landscape), added a soft gradient scrim, and stacked the temperature, location, and forecast cards so they float above the scene with clear depth.

Essentials:
- **Full-bleed scene.** The background is an image, illustration, or rich gradient that fills the entire viewport, not a solid colour or a small hero image.
- **Scrim / gradient for legibility.** Darken or lighten the region behind text so contrast holds. Prefer a soft multi-stop gradient over a hard black overlay.
- **Clear layer stack.** Background scene → scrim → primary content → secondary cards / controls. Use z-index, elevation, or shadow to make the stack readable at a glance.
- **Atmosphere over decoration.** The scene should support the content's mood (stormy for weather, calm for meditation) rather than just looking pretty.

See `references/04-technique-scene-background-layers.md` and `assets/templates/immersive-scene.html`.

## Move 3 - Cohesive custom style (cures "generic look")

What the video showed: a music player with stock circular album art, standard buttons, and plain type. The upgrade applied scalloped (wavy) crops to the album art, curved the track title, and matched the play button and progress indicator to the same visual language.

Essentials:
- **One motif, many places.** Pick a single distinctive treatment (scalloped edge, curved lettering, a custom corner radius language, a repeated geometric accent) and apply it to images, type, and controls.
- **Consistency beats novelty.** The same motif on the avatar, the title, and the primary button reads as intentional design; three different flourishes read as decoration.
- **Generate the motif assets.** Use `scripts/scalloped_mask.py` for clip-paths and masks, `scripts/curved_text_svg.py` for arc text. Keep the motif vector where possible so it scales cleanly.
- **Match interactive states.** Hover, pressed, and disabled states should still feel like they belong to the same family.

See `references/05-technique-cohesive-custom-style.md` and `assets/templates/cohesive-style.html`.

## Combining moves

- Boring + flat → Move 1 primary, light Move 2 support (scene behind the oversized subject).
- Flat + generic → Move 2 primary, Move 3 on the controls and type.
- All three symptoms → prioritise the strongest symptom; do not force all three on one screen.

## Accessibility and performance non-negotiables

- Text contrast must pass WCAG AA (4.5:1 normal, 3:1 large) even when overlaid on imagery. Use `scripts/contrast_check.py`.
- Decorative depth (shadows, blurs, parallax) must not hide focus indicators or reduce hit targets below 44×44 pt.
- Prefer CSS/SVG solutions over large raster assets when the motif can be vector. Lazy-load heavy scene images.
- Respect `prefers-reduced-motion` for any animated depth effects.

Full checklist: `references/08-accessibility-and-performance.md` and `references/09-qa-checklist.md`.

## Scripts quick reference

```bash
# Scalloped mask / clip-path
python scripts/scalloped_mask.py --scallops 22 --format clip

# Curved text SVG
python scripts/curved_text_svg.py --text "SLOW SUNDAY" --radius 330 --arc 56 --out title.svg

# Contrast check (text on colour + optional scrim)
python scripts/contrast_check.py "#ffffff" "#bcd4f2" --scrim "#0b2a55@0.4" --text-alpha 0.88 --large

# Subject cutout helper
python scripts/cutout_subject.py photo.png cutout.webp --method colorkey --shadow

# Token audit
python scripts/audit_style_tokens.py ./src
```

## Worked examples and further reading

- `references/10-worked-examples.md` — plant, weather, music, and additional app types
- `references/06-implementation-recipes.md` — HTML/CSS, RN, SwiftUI, Compose
- `references/07-asset-generation-prompts.md` — prompts for cutouts and scenes
- `evals/evals.json` — sample evaluation prompts

When in doubt, diagnose first, pick one primary move, ship a clear before → after, and protect legibility.
