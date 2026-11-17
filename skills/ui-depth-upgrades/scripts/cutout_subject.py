#!/usr/bin/env python3
"""Simple subject cutout helper (colorkey / basic).

Example:
  python cutout_subject.py photo.png cutout.webp --method colorkey --shadow
"""
from __future__ import annotations
import argparse
import sys

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input")
    p.add_argument("output")
    p.add_argument("--method", choices=["colorkey", "manual"], default="colorkey")
    p.add_argument("--key", default="#00ff00", help="chroma key colour")
    p.add_argument("--tolerance", type=int, default=40)
    p.add_argument("--shadow", action="store_true")
    a = p.parse_args(argv)

    try:
        from PIL import Image, ImageFilter, ImageOps
    except ImportError:
        sys.exit("Pillow required: pip install pillow")

    img = Image.open(a.input).convert("RGBA")
    # Very basic colorkey for demo; real use should use rembg or similar
    if a.method == "colorkey":
        key = tuple(int(a.key.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
        datas = img.getdata()
        new = []
        for item in datas:
            if abs(item[0]-key[0]) < a.tolerance and abs(item[1]-key[1]) < a.tolerance and abs(item[2]-key[2]) < a.tolerance:
                new.append((0, 0, 0, 0))
            else:
                new.append(item)
        img.putdata(new)

    if a.shadow:
        # Simple drop shadow
        shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
        # placeholder – full version expands bounds and blurs alpha
        pass

    img.save(a.output)
    print(f"wrote {a.output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
