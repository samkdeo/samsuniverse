#!/usr/bin/env python3
"""WCAG 2.x contrast ratios for a brand palette.

    contrast.py "#1F3D2B" "#F4EDE0" "#E8845C"     pair matrix for every combination
    contrast.py ink=#1F3D2B ground=#F4EDE0        same, with the rows labelled
    contrast.py "#7BA05B"                          one colour against white and black
    contrast.py --darken BRAND GROUND              derive a text colour from a brand colour

The matrix is the deliverable: every foreground against every ground, with a
verdict per pair. --darken answers the follow-up question, holding the brand
hue and walking lightness down until the pairing clears each threshold, so the
text colour is derived from the brand rather than picked by eye.

Thresholds (WCAG 2.1 AA):
    4.5:1  body text
    3.0:1  large text (>=24px regular, or >=18.66px bold) and
           meaningful non-text (UI components, informative icons)
Logotypes and purely decorative art carry no requirement.

These ratios are defined for sRGB on screen. Treat them as a proxy for print,
not as the governing standard: see the SKILL.md note on regulated panels.
"""

import sys


def parse_hex(value):
    h = value.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6 or any(c not in "0123456789abcdefABCDEF" for c in h):
        raise ValueError(f"not a hex colour: {value!r}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def luminance(rgb):
    channels = []
    for raw in rgb:
        c = raw / 255
        channels.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = channels
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = luminance(a), luminance(b)
    lighter, darker = max(la, lb), min(la, lb)
    return (lighter + 0.05) / (darker + 0.05)



def to_hsl(rgb):
    r, g, b = (c / 255 for c in rgb)
    hi, lo = max(r, g, b), min(r, g, b)
    l = (hi + lo) / 2
    if hi == lo:
        return 0.0, 0.0, l
    d = hi - lo
    s = d / (2 - hi - lo) if l > 0.5 else d / (hi + lo)
    if hi == r:
        h = ((g - b) / d) % 6
    elif hi == g:
        h = (b - r) / d + 2
    else:
        h = (r - g) / d + 4
    return h * 60, s, l


def from_hsl(h, s, l):
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2
    quad = [(c, x, 0), (x, c, 0), (0, c, x), (0, x, c), (x, 0, c), (c, 0, x)]
    r, g, b = quad[int(h // 60) % 6]
    return tuple(round((v + m) * 255) for v in (r, g, b))


def to_hex(rgb):
    return "#" + "".join(f"{c:02X}" for c in rgb)


def darken(brand, ground):
    """Walk lightness down, holding hue and saturation, to clear each threshold."""
    h, s, _ = to_hsl(brand)
    out = {}
    for target in (3.0, 4.5, 7.0):
        for step in range(100, -1, -1):
            cand = from_hsl(h, s, step / 100)
            if ratio(cand, ground) >= target:
                out[target] = (cand, ratio(cand, ground))
                break
    return out


def verdict(r):
    if r >= 7:
        return "AAA body, AA everything"
    if r >= 4.5:
        return "AA body text"
    if r >= 3:
        return "AA large text + UI only"
    return "decorative / logotype only"


def main(argv):
    if any(a in ("-h", "--help") for a in argv) or not argv:
        print(__doc__)
        return 0

    if argv[0] == "--darken":
        if len(argv) != 3:
            print("usage: contrast.py --darken BRAND GROUND", file=sys.stderr)
            return 2
        try:
            brand, ground = parse_hex(argv[1]), parse_hex(argv[2])
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        base = ratio(brand, ground)
        print(f"{to_hex(brand)} on {to_hex(ground)}  {base:.2f}:1  {verdict(base)}")
        print("nearest same-hue colour clearing each threshold:")
        for target, (cand, r) in sorted(darken(brand, ground).items()):
            print(f"  >= {target:>3}:1   {to_hex(cand)}  {r:6.2f}:1")
        print("Keep the brand colour for what carries no obligation;")
        print("use the derived colour for text and meaningful marks only.")
        return 0

    args = [a for a in argv if a != "--pairs"]
    if not args:
        print(__doc__)
        return 1

    colours = []
    for arg in args:
        label, _, value = arg.rpartition("=")
        try:
            rgb = parse_hex(value)
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        colours.append((label or value.strip(), value.strip(), rgb))

    if len(colours) == 1:
        name, hexval, rgb = colours[0]
        print(f"{name} {hexval}  relative luminance {luminance(rgb):.4f}")
        for other, label in ((255, 255, 255), "white"), ((0, 0, 0), "black"):
            print(f"  vs {label:<5} {ratio(rgb, other):6.2f}:1  {verdict(ratio(rgb, other))}")
        return 0

    width = max(len(c[0]) for c in colours)
    print(f"{'pair':<{width * 2 + 5}} {'ratio':>7}  verdict")
    print("-" * (width * 2 + 40))
    seen = set()
    for i, (n1, _, rgb1) in enumerate(colours):
        for j, (n2, _, rgb2) in enumerate(colours):
            if i == j or (j, i) in seen:
                continue
            seen.add((i, j))
            r = ratio(rgb1, rgb2)
            print(f"{n1:<{width}} on {n2:<{width}} {r:6.2f}:1  {verdict(r)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
