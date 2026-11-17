#!/usr/bin/env python3
"""Generate curved / arched text as SVG.

Example:
  python curved_text_svg.py --text "SLOW SUNDAY" --radius 330 --arc 56 --out title.svg
"""
from __future__ import annotations
import argparse
import math
import sys

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--text", required=True)
    p.add_argument("--radius", type=float, default=300)
    p.add_argument("--arc", type=float, default=60, help="arc angle in degrees")
    p.add_argument("--font-size", type=float, default=48)
    p.add_argument("--font-family", default="system-ui, sans-serif")
    p.add_argument("--fill", default="#0a1628")
    p.add_argument("--out", "-o")
    a = p.parse_args(argv)

    # Simple path-based arc text approximation
    r = a.radius
    arc_rad = math.radians(a.arc)
    start = -arc_rad / 2
    # SVG path for the arc
    x1 = r * math.sin(start)
    y1 = r * (1 - math.cos(start))
    x2 = r * math.sin(start + arc_rad)
    y2 = r * (1 - math.cos(start + arc_rad))
    large = 1 if a.arc > 180 else 0
    path_d = f"M {x1:.2f} {y1:.2f} A {r:.2f} {r:.2f} 0 {large} 1 {x2:.2f} {y2:.2f}"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-r-20} {-20} {2*r+40} {r+40}" width="{2*r+40}" height="{r+40}">
  <defs>
    <path id="curve" d="{path_d}" fill="none"/>
  </defs>
  <text font-family="{a.font_family}" font-size="{a.font_size}" fill="{a.fill}" text-anchor="middle">
    <textPath href="#curve" startOffset="50%">{a.text}</textPath>
  </text>
</svg>'''

    if a.out:
        with open(a.out, "w") as f:
            f.write(svg)
        print(f"wrote {a.out}")
    else:
        print(svg)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
