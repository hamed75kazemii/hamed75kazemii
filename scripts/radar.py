"""Radar charts from profile/skills.json and profile/langmix.json -> 4 SVGs."""
from __future__ import annotations

import json
import math

from common import MONO, OUT, SANS, THEMES, esc, write_svg

W, H = 460, 400
CX, CY = W / 2, H / 2
R = 120          # outer ring radius
RINGS = 5        # 2,4,6,8,10
LABEL_PAD = 22


def polar(i: int, n: int, r: float) -> tuple[float, float]:
    ang = -math.pi / 2 + 2 * math.pi * i / n
    return CX + r * math.cos(ang), CY + r * math.sin(ang)


def render(spec: dict, theme: str) -> str:
    t = THEMES[theme]
    axes = spec["axes"]
    n = len(axes)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'role="img" aria-label="{esc(spec["title"])} radar chart">',
        f'<rect width="{W}" height="{H}" rx="14" fill="{t["bg"]}" stroke="{t["border"]}"/>',
        f'<style>.lab{{font:600 12px {SANS};fill:{t["text"]}}}.val{{font:500 10px {MONO};fill:{t["muted"]}}}'
        f'.tick{{font:500 9px {MONO};fill:{t["muted"]};paint-order:stroke;stroke:{t["bg"]};stroke-width:3px}}'
        f'.shape{{animation:grow 1.1s cubic-bezier(.2,.8,.2,1) both;transform-origin:{CX}px {CY}px}}'
        f'@keyframes grow{{from{{transform:scale(.15);opacity:0}}to{{transform:scale(1);opacity:1}}}}'
        f'@media (prefers-reduced-motion:reduce){{.shape{{animation:none}}}}</style>',
    ]
    # grid rings (recessive)
    for k in range(1, RINGS + 1):
        rr = R * k / RINGS
        pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in (polar(i, n, rr) for i in range(n)))
        parts.append(f'<polygon points="{pts}" fill="none" stroke="{t["grid"]}" stroke-width="1"/>')
        if k in (2, 4):
            x, y = polar(0, n, rr)
            parts.append(f'<text class="tick" x="{x+5:.1f}" y="{y-3:.1f}">{k*2}</text>')
    # spokes
    for i in range(n):
        x, y = polar(i, n, R)
        parts.append(f'<line x1="{CX}" y1="{CY}" x2="{x:.1f}" y2="{y:.1f}" stroke="{t["grid"]}" stroke-width="1"/>')
    # data polygon (thin stroke, soft fill, >=8px markers with a surface ring)
    pts = []
    for i, a in enumerate(axes):
        v = max(0, min(10, float(a["value"])))
        pts.append(polar(i, n, R * v / 10))
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    parts.append('<g class="shape">')
    parts.append(f'<polygon points="{poly}" fill="{t["accent_soft"]}" stroke="{t["accent"]}" stroke-width="2" stroke-linejoin="round"/>')
    for x, y in pts:
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{t["accent"]}" stroke="{t["bg"]}" stroke-width="2"/>')
    parts.append("</g>")
    # labels: name + value, anchored by side
    for i, a in enumerate(axes):
        x, y = polar(i, n, R + LABEL_PAD)
        ang = -math.pi / 2 + 2 * math.pi * i / n
        c = math.cos(ang)
        anchor = "middle" if abs(c) < 0.25 else ("start" if c > 0 else "end")
        dy = 4 if abs(math.sin(ang)) < 0.25 else (12 if math.sin(ang) > 0 else -2)
        parts.append(f'<text class="lab" x="{x:.1f}" y="{y+dy:.1f}" text-anchor="{anchor}">{esc(a["label"])}</text>')
        parts.append(f'<text class="val" x="{x:.1f}" y="{y+dy+13:.1f}" text-anchor="{anchor}">{a["value"]}/10</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    for src, prefix in (("skills.json", "radar"), ("langmix.json", "radar-langs")):
        spec = json.loads((OUT / src).read_text())
        for theme in THEMES:
            write_svg(f"{prefix}-{theme}.svg", render(spec, theme))


if __name__ == "__main__":
    main()
