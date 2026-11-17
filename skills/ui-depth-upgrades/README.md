# ui-depth-upgrades

A Claude skill that turns boring, flat, or generic app/web UI into designed UI using three techniques taught in a short design-tip video (@ayoships):

1. **Oversized subject + headline overlap** - cures a boring layout
2. **Scene background + layered content** - cures a flat screen
3. **One motif everywhere** (scalloped crops, curved lettering, matching controls) - cures a generic look

## Install
Upload the `ui-depth-upgrades/` folder (or the zip) as a skill in Claude (Settings > Capabilities > Skills), or place it in your Claude Code skills directory (`~/.claude/skills/`).

## Contents
- `SKILL.md` - triggers, workflow, the three moves, output format
- `references/` - diagnosis, deep dives per move, code recipes (Web/RN/SwiftUI/Compose), asset prompts, accessibility, QA, worked examples, video source notes
- `scripts/` - `scalloped_mask.py`, `curved_text_svg.py`, `contrast_check.py`, `cutout_subject.py`, `audit_style_tokens.py` (Python 3; Pillow + numpy for the image ones)
- `assets/templates/` - three standalone HTML demos with Before/After toggles (open in a browser)
- `evals/evals.json` - sample prompts for testing

## Quick start
```bash
python scripts/scalloped_mask.py --scallops 22 --format clip
python scripts/curved_text_svg.py --text "SLOW SUNDAY" --radius 330 --arc 56 --out title.svg
python scripts/contrast_check.py "#ffffff" "#bcd4f2" --scrim "#0b2a55@0.4" --text-alpha 0.88 --large
python scripts/cutout_subject.py photo.png cutout.webp --method colorkey --shadow
python scripts/audit_style_tokens.py ./src
```

## Notes
The source video's audio could not be transcribed here; the script was reconstructed from its burned-in captions (see `references/01-video-source-notes.md`). Example artwork is original, not copied from the video.
