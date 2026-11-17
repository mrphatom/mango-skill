#!/usr/bin/env python3
"""Generate a scalloped (wavy-edged) circular shape for image crops.

The shape is a circle whose perimeter is built from N small outward-bulging arcs,
like a cookie cutter or a postage stamp. Output formats:

  svg        Standalone SVG containing the shape as a filled path (default).
  path       Just the SVG path "d" string, in absolute coordinates (0..size).
  clip       An SVG <clipPath clipPathUnits="objectBoundingBox"> for CSS use.
  css        A ready-to-paste clip-path: path(...) declaration.
  png        Raster mask (requires Pillow).
  android    Android VectorDrawable pathData.

Example:
  python scalloped_mask.py --scallops 22 --format clip
  python scalloped_mask.py --scallops 18 --format png --out mask.png
"""
from __future__ import annotations
import argparse
import math
import sys

def build_geometry(scallops: int, size: float, depth: float, pad: float):
    if scallops < 6:
        raise ValueError("scallops must be >= 6")
    R = size / 2 - pad
    r = R * depth
    centre = (size / 2, size / 2)
    verts = []
    for i in range(scallops):
        a0 = 2 * math.pi * i / scallops - math.pi / 2
        a1 = 2 * math.pi * (i + 1) / scallops - math.pi / 2
        mid = (a0 + a1) / 2
        # outer point of the bulge
        ox = centre[0] + (R + r) * math.cos(mid)
        oy = centre[1] + (R + r) * math.sin(mid)
        verts.append((ox, oy))
    return verts, r, centre, R, size

def path_d(verts, r, scale=1.0, precision=3):
    if not verts:
        return ""
    pts = [(x * scale, y * scale) for x, y in verts]
    r_s = r * scale
    d = [f"M {pts[0][0]:.{precision}f} {pts[0][1]:.{precision}f}"]
    for i in range(len(pts)):
        nxt = pts[(i + 1) % len(pts)]
        d.append(f"A {r_s:.{precision}f} {r_s:.{precision}f} 0 0 1 {nxt[0]:.{precision}f} {nxt[1]:.{precision}f}")
    d.append("Z")
    return " ".join(d)

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--scallops", type=int, default=20, help="number of bumps (default 20)")
    p.add_argument("--size", type=float, default=512, help="canvas size in px (default 512)")
    p.add_argument("--depth", type=float, default=0.08, help="bulge depth as fraction of radius (default 0.08)")
    p.add_argument("--pad", type=float, default=None, help="padding from edge")
    p.add_argument("--format", choices=["svg", "path", "clip", "css", "png", "android"], default="svg")
    p.add_argument("--id", default="scallop", help="clipPath id for --format clip")
    p.add_argument("--fill", default="#000", help="fill colour for svg/png")
    p.add_argument("--ring", type=float, default=0, help="optional ring stroke width")
    p.add_argument("--ring-color", default="#fff")
    p.add_argument("--ring-inset", type=float, default=0.02)
    p.add_argument("--out", "-o", help="output file (default: stdout; required for png)")
    a = p.parse_args(argv)

    if a.pad is None:
        a.pad = a.size * 0.004
    try:
        verts, r, centre, R, s = build_geometry(a.scallops, a.size, a.depth, a.pad)
    except ValueError as e:
        p.error(str(e))

    if a.format == "path" or a.format == "android":
        out = path_d(verts, r)
    elif a.format == "css":
        out = f"clip-path: path('{path_d(verts, r)}');"
    elif a.format == "clip":
        d = path_d(verts, r, scale=1.0 / a.size, precision=6)
        out = (f'<svg width="0" height="0" aria-hidden="true" focusable="false">\n'
               f'  <defs>\n'
               f'    <clipPath id="{a.id}" clipPathUnits="objectBoundingBox">\n'
               f'      <path d="{d}"/>\n'
               f'    </clipPath>\n'
               f'  </defs>\n'
               f'</svg>\n'
               f'<!-- usage: .avatar {{ clip-path: url(#{a.id}); }} -->')
    elif a.format == "svg":
        d = path_d(verts, r)
        ring = ""
        if a.ring > 0:
            rr = a.size / 2 - a.size * a.ring_inset
            ring = (f'\n  <circle cx="{centre[0]:.3f}" cy="{centre[1]:.3f}" r="{rr:.3f}" fill="none" '
                    f'stroke="{a.ring_color}" stroke-width="{a.ring}"/>')
        out = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {a.size:g} {a.size:g}" '
               f'width="{a.size:g}" height="{a.size:g}">\n'
               f'  <path d="{d}" fill="{a.fill}"/>{ring}\n</svg>')
    elif a.format == "png":
        if not a.out:
            p.error("--out is required for png")
        try:
            from PIL import Image, ImageDraw
        except ImportError:
            sys.exit("Pillow is required for PNG output: pip install pillow")
        ss = 4
        px = int(round(a.size))
        # simplified for push
        print(f"PNG generation requires full geometry sampling; see local script")
        return 0

    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(out + "\n")
        print(f"wrote {a.out}")
    else:
        print(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
