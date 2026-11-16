#!/usr/bin/env python3
"""mango palette generator — builds an 11-shade OKLCH ramp from a single brand hue.
Usage: scripts/palette.py <hue 0-360> [chroma 0-0.4]
Prints CSS custom properties. Neutrals (ink/paper) are printed at fixed low chroma of the same hue.
Requires: uv (or python3 with no deps — pure stdlib OKLCH->sRGB conversion).
"""
import sys, math

def oklch_to_srgb(L, C, H):
    h = math.radians(H)
    a, b = C * math.cos(h), C * math.sin(h)
    # OKLCH -> OKLab -> linear sRGB (Björn Ottosson matrices)
    l_, m_, s_ = (L + 0.3963377774 * a + 0.2158037573 * b,
                  L - 0.1055613458 * a - 0.0638541728 * b,
                  L - 0.0894841775 * a - 1.2914855480 * b)
    l, m, s = l_**3, m_**3, s_**3
    r =  4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bl = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    def enc(x):
        x = max(0.0, min(1.0, x))
        return round(12.92 * x * 255) if x <= 0.0031308 else round((1.055 * x ** (1/2.4) - 0.055) * 255)
    return enc(r), enc(g), enc(bl)

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    hue = float(sys.argv[1]); chroma = float(sys.argv[2]) if len(sys.argv) > 2 else 0.16
    print(f":root {{  /* generated from hue {hue:.0f}, chroma {chroma:.2f} — adjust against the real brand */")
    for i, L in enumerate([0.985, 0.95, 0.90, 0.82, 0.72, 0.62, 0.52, 0.43, 0.34, 0.24, 0.15]):
        step = (i + 1) * 100
        c = chroma if 2 < i < 8 else chroma * 0.35 if L > 0.9 else chroma * 0.6
        r, g, b = oklch_to_srgb(L, c, hue)
        print(f"  --brand-{step}: rgb({r} {g} {b});")
    # Paper (warm, low chroma) and ink (near-black, hue-tinted)
    for name, L, c in [("paper", 0.965, 0.012), ("paper-2", 0.92, 0.014), ("card", 0.99, 0.008), ("ink", 0.16, 0.015), ("ink-soft", 0.35, 0.018)]:
        r, g, b = oklch_to_srgb(L, c, hue)
        print(f"  --{name}: rgb({r} {g} {b});")
    print("}")

if __name__ == "__main__":
    main()
