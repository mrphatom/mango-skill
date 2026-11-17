# 05 - Technique: Cohesive custom style

**Cures:** Generic / template / AI-looking / default-component look.

## Core idea
Pick **one** distinctive motif and push it through image crops, lettering, and controls.

## Motif examples from the source
- Scalloped (wavy) circular crop on artwork
- Curved / arched display lettering
- Buttons and scrubber that echo the same language and palette extracted from the artwork

## Rules
- One motif, many places > three different flourishes
- Extract 3–5 colours from the hero artwork as tokens
- Keep hit targets ≥ 44/48 and visible pressed/focus states
- Generate vectors with `scripts/scalloped_mask.py` and `scripts/curved_text_svg.py`

See `assets/templates/cohesive-style.html`.
