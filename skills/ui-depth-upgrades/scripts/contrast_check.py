#!/usr/bin/env python3
"""WCAG 2.x contrast checker for text on solid colours, translucent text, and scrimmed photos.

Typical uses:

  # Plain pair
  python contrast_check.py "#12234a" "#fbefc3"

  # White text over the brightest cloud colour, with a 35% black scrim on top of the photo
  python contrast_check.py "#ffffff" "#e8f1fb" --scrim "#000000@0.35"

  # Semi-transparent white numerals (85% opacity) over several sampled sky colours; report the worst case
  python contrast_check.py "#ffffff" "#bcd4f2" "#f4f8ff" "#6fa3e0" --text-alpha 0.85 --scrim "#0b2a55@0.25"

  # Frosted glass panel: background colour + white 14% panel fill, then text
  python contrast_check.py "#ffffff" "#9cc3f0" --panel "#ffffff@0.14"

  # Machine-readable
  python contrast_check.py "#fff" "#888" --json

Arguments:
  foreground       text colour (#rgb, #rrggbb)
  backgrounds      one or more sampled background colours behind the text. Sample the
                   LIGHTEST and DARKEST areas behind the text, not the average.

Layers are composited in this order: background -> scrim -> panel -> text (with --text-alpha).

Thresholds (WCAG 2.x):
  AA normal text  >= 4.5     AA large text  >= 3.0
  AAA normal text >= 7.0     AAA large text >= 4.5
  Non-text UI components and graphical objects >= 3.0
"Large" = at least 24 px regular or 18.66 px bold (about 18 pt / 14 pt bold).

Exit status: 0 if the worst case passes the selected --level, 1 otherwise.
"""
from __future__ import annotations

import argparse
import json
import sys


def parse_hex(s: str):
    s = s.strip().lstrip("#")
    if len(s) == 3:
        s = "".join(ch * 2 for ch in s)
    if len(s) != 6:
        raise ValueError(f"bad colour '{s}': use #rgb or #rrggbb")
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))


def parse_layer(spec: str):
    """'#rrggbb@0.35' -> ((r,g,b), 0.35). Alpha defaults to 1."""
    if "@" in spec:
        col, al = spec.split("@", 1)
        return parse_hex(col), float(al)
    return parse_hex(spec), 1.0


def blend(over, under, alpha):
    return tuple(over[i] * alpha + under[i] * (1 - alpha) for i in range(3))


def channel(v):
    v = v / 255.0
    return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*(int(round(c)) for c in rgb))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("foreground", help="text colour")
    p.add_argument("backgrounds", nargs="+", help="one or more background sample colours")
    p.add_argument("--scrim", help="scrim colour and opacity, e.g. '#000000@0.35'")
    p.add_argument("--panel", help="frosted/glass panel fill drawn above the scrim, e.g. '#ffffff@0.14'")
    p.add_argument("--text-alpha", type=float, default=1.0, help="opacity of the text, 0..1")
    p.add_argument("--large", action="store_true", help="treat text as large (24px / 18.66px bold or more)")
    p.add_argument("--level", choices=["AA", "AAA"], default="AA")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)

    try:
        fg = parse_hex(a.foreground)
        bgs = [parse_hex(b) for b in a.backgrounds]
        scrim = parse_layer(a.scrim) if a.scrim else None
        panel = parse_layer(a.panel) if a.panel else None
    except ValueError as e:
        p.error(str(e))

    need = {("AA", False): 4.5, ("AA", True): 3.0, ("AAA", False): 7.0, ("AAA", True): 4.5}[(a.level, a.large)]

    rows = []
    for bg0 in bgs:
        bg = bg0
        if scrim:
            bg = blend(scrim[0], bg, scrim[1])
        if panel:
            bg = blend(panel[0], bg, panel[1])
        text = blend(fg, bg, a.text_alpha) if a.text_alpha < 1 else fg
        r = ratio(text, bg)
        rows.append({
            "background_sample": to_hex(bg0),
            "effective_background": to_hex(bg),
            "effective_text": to_hex(text),
            "ratio": round(r, 2),
            "AA_normal": r >= 4.5, "AA_large": r >= 3.0,
            "AAA_normal": r >= 7.0, "AAA_large": r >= 4.5,
            "passes_selected": r >= need,
        })

    worst = min(rows, key=lambda x: x["ratio"])
    result = {"required": need, "level": a.level, "large_text": a.large,
              "worst_ratio": worst["ratio"], "passes": worst["passes_selected"], "samples": rows}

    if a.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Required: {need}:1  ({a.level}, {'large' if a.large else 'normal'} text)")
        for r in rows:
            flag = "PASS" if r["passes_selected"] else "FAIL"
            print(f"  bg {r['background_sample']} -> effective {r['effective_background']}, "
                  f"text {r['effective_text']}: {r['ratio']}:1  {flag}")
        print(f"Worst case: {worst['ratio']}:1 -> {'PASS' if worst['passes_selected'] else 'FAIL'}")
        if not worst["passes_selected"]:
            print("Fix: add or strengthen a scrim, darken/lighten the panel tint, enlarge/bolden the text, or move it to a calmer region.")
    return 0 if worst["passes_selected"] else 1


if __name__ == "__main__":
    sys.exit(main())
