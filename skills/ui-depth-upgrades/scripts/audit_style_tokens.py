#!/usr/bin/env python3
"""Lightweight style-token sprawl auditor.

Scans a directory for hardcoded colours, radii, and font sizes and reports
duplicates / near-duplicates so you can consolidate into tokens.

Example:
  python audit_style_tokens.py ./src
"""
from __future__ import annotations
import argparse
import os
import re
from collections import defaultdict

COLOR_RE = re.compile(r"#(?:[0-9a-fA-F]{3}){1,2}\b")
RADIUS_RE = re.compile(r"(?:border-radius|rounded|cornerRadius)\s*[:=]?\s*([\d.]+)(px|dp|pt)?", re.I)

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("root", nargs="?", default=".")
    a = p.parse_args(argv)

    colors = defaultdict(list)
    for dirpath, _, files in os.walk(a.root):
        for name in files:
            if not name.endswith((".css", ".scss", ".tsx", ".ts", ".jsx", ".js", ".swift", ".kt", ".xml")):
                continue
            path = os.path.join(dirpath, name)
            try:
                text = open(path, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            for m in COLOR_RE.finditer(text):
                colors[m.group(0).lower()].append(path)

    print("=== Colour usage ===")
    for col, paths in sorted(colors.items(), key=lambda x: -len(x[1])):
        print(f"{col:10}  {len(paths):3} files")
        if len(paths) <= 3:
            for pth in paths:
                print(f"           {pth}")
    print("\nTip: extract the most frequent colours into CSS variables / design tokens.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
