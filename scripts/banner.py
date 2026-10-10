"""Terminal-style animated banner (`profile.sh --live`) -> profile/banner-{dark,light}.svg.
Reads live numbers from profile/stats.json (written by cards.py); falls back to config only."""
from __future__ import annotations

import json

from common import CONFIG, MONO, OUT, THEMES, esc, fmt, write_svg

W, LINE_H, PAD_X, TOP = 880, 26, 28, 76
CHAR_W = 8.4          # approx advance of 14px monospace; used for the type-on clip width
TYPE_SPEED = 0.032    # seconds per character


def lines(stats: dict | None) -> list[tuple[str, str, str]]:
    """(kind, key, value). kind: prompt | row | status"""
    rows = [
        ("prompt", "", "./profile.sh --live"),
        ("row", "name", CONFIG["display_name"]),
        ("row", "role", CONFIG["role"]),
        ("row", "stack", CONFIG["stack_line"]),
        ("row", "building", CONFIG["building_line"]),
    ]
    if stats:
        rows.append(("row", "github", f"{stats['public_repos']} repos · {fmt(stats['stars'])} stars · {fmt(stats['followers'])} followers"))
        rows.append(("status", "status", f"online · last push {stats['last_push']}"))
    else:
        rows.append(("status", "status", "online"))
    rows.append(("cursor", "", ""))
    return rows


def render(stats: dict | None, theme: str) -> str:
    t = THEMES[theme]
    rows = lines(stats)
    h = TOP + LINE_H * len(rows) + 22
    css = [
        f"text{{font:500 14px {MONO};white-space:pre}}.p{{fill:{t['accent']}}}.k{{fill:{t['muted']}}}.v{{fill:{t['text']}}}",
        f".g{{fill:{t['green']}}}.title{{font-size:12px;fill:{t['muted']}}}",
        "@keyframes type{from{clip-path:inset(-4px 100% -4px -2px)}to{clip-path:inset(-4px -2px -4px -2px)}}",
        "@keyframes show{to{opacity:1}}",
        ".cur{animation:blink 1s steps(2,start) infinite}@keyframes blink{to{visibility:hidden}}",
        "@media (prefers-reduced-motion:reduce){.line{animation:none!important;clip-path:none}.cursor{opacity:1;animation:none}}",
    ]
    body: list[str] = []
    begin = 0.4
    for i, (kind, key, val) in enumerate(rows):
        y = TOP + i * LINE_H
        if kind == "cursor":
            css.append(f".cursor{{opacity:0;animation:show .01s linear {begin:.2f}s forwards}}")
            body.append(f'<g class="cursor"><text class="p" x="{PAD_X}" y="{y}">~ $ </text>'
                        f'<rect class="cur" x="{PAD_X+4*CHAR_W:.1f}" y="{y-12}" width="8" height="16" fill="{t["accent"]}"/></g>')
            continue
        if kind == "prompt":
            inner = f'<tspan class="p">~ $ </tspan><tspan class="v">{esc(val)}</tspan>'
            nchars = 4 + len(val)
        elif kind == "status":
            inner = (f'<tspan class="p">→ </tspan><tspan class="k">{esc(key.ljust(10))}</tspan>'
                     f'<tspan class="g">● </tspan><tspan class="v">{esc(val)}</tspan>')
            nchars = 14 + len(val)
        else:
            inner = f'<tspan class="p">→ </tspan><tspan class="k">{esc(key.ljust(10))}</tspan><tspan class="v">{esc(val)}</tspan>'
            nchars = 12 + len(val)
        dur = max(0.25, nchars * TYPE_SPEED)
        css.append(f".l{i}{{animation:type {dur:.2f}s steps({nchars}) {begin:.2f}s both}}")
        body.append(f'<text class="line l{i}" x="{PAD_X}" y="{y}">{inner}</text>')
        begin += dur + (0.35 if kind == "prompt" else 0.12)
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="profile.sh --live">',
        "<style>" + "".join(css) + "</style>",
        f'<rect width="{W}" height="{h}" rx="14" fill="{t["bg"]}" stroke="{t["border"]}"/>',
        f'<rect width="{W}" height="40" rx="14" fill="{t["card"]}"/><rect y="26" width="{W}" height="14" fill="{t["card"]}"/>',
        f'<line x1="0" y1="40.5" x2="{W}" y2="40.5" stroke="{t["border"]}"/>',
        '<circle cx="24" cy="20" r="6" fill="#ff5f57"/><circle cx="44" cy="20" r="6" fill="#febc2e"/><circle cx="64" cy="20" r="6" fill="#28c840"/>',
        f'<text class="title" x="{W/2}" y="24" text-anchor="middle">{esc(CONFIG["login"])}@github: ~ — profile.sh --live</text>',
    ] + body + ["</svg>"]
    return "\n".join(out)


def main() -> None:
    stats_path = OUT / "stats.json"
    stats = json.loads(stats_path.read_text()) if stats_path.exists() else None
    for theme in THEMES:
        write_svg(f"banner-{theme}.svg", render(stats, theme))


if __name__ == "__main__":
    main()
