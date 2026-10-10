"""`profile.sh --live` banner: a 1-bit dithered portrait (VISUAL.MAP) next to a SYSTEM.INFO
panel. Writes profile/banner-{dark,light}.svg. Needs Pillow for the portrait.

Portrait source: profile/portrait.png (optional cut-out with alpha) else profile/avatar.jpg,
which is refreshed from your GitHub avatar on every run."""
from __future__ import annotations

import json
import math
import random
import urllib.request

from common import CONFIG, MONO, OUT, THEMES, esc, fmt, write_svg

W, H = 1180, 610
PANEL_Y, PANEL_H = 88, 472
LEFT = (35, 418)            # x, width
RIGHT = (476, 669)
VIS = (49, 124, 390, 414)   # portrait clip box
CELL = CONFIG.get("portrait_cell", 2)
ROW_Y0, ROW_STEP = 153, 23
CHAR = 8.45                 # px per glyph at 14px monospace (textLength keeps it exact)

PALETTE = {
    "dark": {"bg0": "#0A101F", "bg1": "#0D1628", "panel": "#101B30", "border": "#25344C",
             "accent": "#22D3EE", "muted": "#8291A8", "text": "#DDE7F5", "live": "#FF4D5A",
             "ok": "#10B981", "ink": "#AA9BEF", "pill": "#13263B"},
    "light": {"bg0": "#E6EAF2", "bg1": "#FFFFFF", "panel": "#F6F8FA", "border": "#D0D7DE",
              "accent": "#0E7490", "muted": "#57606A", "text": "#1F2328", "live": "#D1242F",
              "ok": "#1A7F37", "ink": "#6F5FCF", "pill": "#EAEEF5"},
}
AVATAR = OUT / "avatar.jpg"
PORTRAIT = OUT / "portrait.png"


# ---------------------------------------------------------------- portrait
def refresh_avatar() -> None:
    try:
        req = urllib.request.Request(f"https://github.com/{CONFIG['login']}.png?size=460",
                                     headers={"User-Agent": "profile-readme-generator"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        if data[:3] == b"\xff\xd8\xff" or data[:8] == b"\x89PNG\r\n\x1a\n":
            AVATAR.write_bytes(data)
    except Exception as exc:  # offline: keep the committed copy
        print(f"avatar refresh skipped: {exc}")


def dither(ink_dark: bool) -> tuple[list[list[int]], int]:
    """Floyd-Steinberg, serpentine. ink_dark: dots where the photo is dark (else where it is bright)."""
    from PIL import Image, ImageOps

    src = PORTRAIT if PORTRAIT.exists() else AVATAR
    img = Image.open(src).convert("RGBA")
    cols, rows = VIS[2] // CELL, VIS[3] // CELL
    img = ImageOps.fit(img, (cols, rows), Image.LANCZOS, centering=(0.5, 0.35))
    gray = ImageOps.autocontrast(img.convert("L"), cutoff=1)
    alpha = img.getchannel("A")
    px, ap = gray.load(), alpha.load()
    gamma = CONFIG.get("portrait_gamma", 1.0)
    has_alpha = PORTRAIT.exists()
    # density field: how much ink each cell wants (0..1)
    field = [[0.0] * cols for _ in range(rows)]
    for y in range(rows):
        for x in range(cols):
            v = px[x, y] / 255
            d = (1 - v) if ink_dark else v
            d = d ** gamma
            if has_alpha:
                m = ap[x, y] / 255
            else:  # soft elliptical vignette so the square photo fades into the panel
                nx, ny = (x - cols / 2) / (cols / 2), (y - rows * 0.45) / (rows * 0.6)
                r = math.hypot(nx, ny)
                m = 1.0 if r < 0.62 else max(0.0, 1 - (r - 0.62) / 0.38)
            field[y][x] = d * m
    out = [[0] * cols for _ in range(rows)]
    pts = 0
    for y in range(rows):
        rng = range(cols) if y % 2 == 0 else range(cols - 1, -1, -1)
        step = 1 if y % 2 == 0 else -1
        for x in rng:
            old = field[y][x]
            new = 1 if old >= 0.5 else 0
            out[y][x] = new
            pts += new
            err = old - new
            if 0 <= x + step < cols:
                field[y][x + step] += err * 7 / 16
            if y + 1 < rows:
                if 0 <= x - step < cols:
                    field[y + 1][x - step] += err * 3 / 16
                field[y + 1][x] += err * 5 / 16
                if 0 <= x + step < cols:
                    field[y + 1][x + step] += err * 1 / 16
    return out, pts


def portrait_svg(bits: list[list[int]], p: dict) -> str:
    """Rows -> run-length <path>s, bundled into bands that reveal top-down, plus a scan loop."""
    x0, y0 = VIS[0], VIS[1]
    rows = len(bits)
    bands = 48
    per = max(1, math.ceil(rows / bands))
    out = [f'<g clip-path="url(#visualClip)" shape-rendering="crispEdges" fill="{p["ink"]}">']
    for b in range(0, rows, per):
        d = []
        for y in range(b, min(b + per, rows)):
            row = bits[y]
            x = 0
            while x < len(row):
                if row[x]:
                    run = 1
                    while x + run < len(row) and row[x + run]:
                        run += 1
                    d.append(f"M{x0 + x*CELL} {y0 + y*CELL}h{run*CELL}v{CELL}h-{run*CELL}z")
                    x += run
                else:
                    x += 1
        if not d:
            continue
        begin = 0.1 + (b / rows) * 2.8
        out.append(f'<g opacity="0"><animate attributeName="opacity" begin="{begin:.2f}s" dur=".8s" values="0;1" fill="freeze"/>'
                   f'<path d="{"".join(d)}"/></g>')
    out.append("</g>")
    # scan line: sweeps the map every few seconds after the reveal
    out.append(f'<g clip-path="url(#visualClip)"><rect x="{x0}" y="{y0-40}" width="{VIS[2]}" height="40" fill="url(#scan)" opacity=".9">'
               f'<animateTransform attributeName="transform" type="translate" begin="3.4s" dur="5s" repeatCount="indefinite" '
               f'values="0 0;0 {VIS[3]+40};0 {VIS[3]+40}" keyTimes="0;.45;1"/></rect></g>')
    return "\n".join(out)


# ---------------------------------------------------------------- panels
def rows_for(stats: dict | None) -> list[tuple[str, str]]:
    rows = [tuple(r) for r in CONFIG["system_info"]]
    return rows


def render(bits, pts, stats: dict | None, theme: str) -> str:
    p = PALETTE[theme]
    mono = f'font-family="{MONO}"'
    lx, lw = LEFT
    rx, rw = RIGHT
    vx, vy, vw, vh = VIS
    handle = f"@{CONFIG['login']}"
    o = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{esc(CONFIG["display_name"])}\'s live system profile</title>',
        '<desc id="desc">Animated terminal profile with a dithered portrait and system info.</desc>',
        '<defs>',
        f'<filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#02050B" flood-opacity=".28"/></filter>',
        f'<clipPath id="visualClip"><rect x="{vx}" y="{vy}" width="{vw}" height="{vh}" rx="3"/></clipPath>',
        f'<linearGradient id="scan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p["accent"]}" stop-opacity="0"/>'
        f'<stop offset="1" stop-color="{p["accent"]}" stop-opacity=".35"/></linearGradient>',
        '</defs>',
        f'<rect width="{W}" height="{H}" rx="18" fill="{p["bg0"]}"/>',
        f'<rect x="13" y="13" width="{W-26}" height="{H-26}" rx="13" fill="{p["bg1"]}" stroke="{p["border"]}" filter="url(#shadow)"/>',
        f'<path d="M13 62H{W-13}" stroke="{p["border"]}"/>',
        '<circle cx="38" cy="38" r="6" fill="#FF5F57"/><circle cx="59" cy="38" r="6" fill="#FEBC2E"/><circle cx="80" cy="38" r="6" fill="#28C840"/>',
        f'<text x="{W/2}" y="43" text-anchor="middle" fill="{p["muted"]}" {mono} font-size="13" letter-spacing=".4">profile.sh --live</text>',
        # left panel
        f'<rect x="{lx}" y="{PANEL_Y}" width="{lw}" height="{PANEL_H}" rx="6" fill="{p["panel"]}" stroke="{p["border"]}"/>',
        f'<path d="M{lx} 124H{lx+lw}" stroke="{p["border"]}"/>',
        f'<text x="{vx}" y="111" fill="{p["accent"]}" {mono} font-size="13" font-weight="700" letter-spacing="1.2">VISUAL.MAP</text>',
        f'<text x="{vx+vw-1}" y="111" text-anchor="end" fill="{p["muted"]}" {mono} font-size="11">{vw//CELL}×{vh//CELL} / 1-BIT</text>',
        f'<path d="M{vx} 141h12M{vx} 141v12M{vx+vw} 141h-12M{vx+vw} 141v12M{vx} 539h12M{vx} 539v-12M{vx+vw} 539h-12M{vx+vw} 539v-12" fill="none" stroke="{p["accent"]}" opacity=".55"/>',
        portrait_svg(bits, p),
        f'<text x="{vx+9}" y="551" fill="{p["muted"]}" {mono} font-size="10">PTS {pts} · FS/SERPENTINE · CELL {CELL}PX</text>',
        # right panel
        f'<rect x="{rx}" y="{PANEL_Y}" width="{rw}" height="{PANEL_H}" rx="6" fill="{p["panel"]}" stroke="{p["border"]}"/>',
        f'<path d="M{rx} 124H{rx+rw}" stroke="{p["border"]}"/>',
        f'<text x="{rx+14}" y="111" fill="{p["accent"]}" {mono} font-size="13" font-weight="700" letter-spacing="1.2">SYSTEM.INFO</text>',
    ]
    # LIVE + handle pill
    pill_w = len(handle) * CHAR + 30
    pill_x = rx + rw - 14 - pill_w
    o.append(f'<circle cx="{pill_x-56}" cy="107" r="4" fill="{p["live"]}"><animate attributeName="opacity" values="1;.25;1" dur="1.6s" repeatCount="indefinite"/></circle>')
    o.append(f'<text x="{pill_x-46}" y="111" fill="{p["live"]}" {mono} font-size="12" font-weight="700">LIVE</text>')
    o.append(f'<rect x="{pill_x}" y="96" width="{pill_w:.0f}" height="22" rx="11" fill="{p["pill"]}" stroke="{p["border"]}"/>')
    o.append(f'<text x="{pill_x+pill_w/2:.0f}" y="111" text-anchor="middle" fill="{p["accent"]}" {mono} font-size="14" font-weight="700">{esc(handle)}</text>')
    # rows with dotted leaders
    kx, vend = rx + 15, rx + rw - 18
    for i, (k, v) in enumerate(rows_for(stats)):
        y = ROW_Y0 + i * ROW_STEP
        v = v.format(**(stats or {}))
        k_end = kx + len(k) * CHAR
        v_start = vend - len(v) * CHAR
        o.append(f'<g opacity="0"><animate attributeName="opacity" begin="{0.4+i*0.08:.2f}s" dur=".6s" values="0;1" fill="freeze"/>')
        o.append(f'<text x="{kx}" y="{y}" fill="{p["muted"]}" {mono} font-size="14" textLength="{len(k)*CHAR:.1f}" lengthAdjust="spacingAndGlyphs">{esc(k)}</text>')
        if v_start - k_end > 16:
            o.append(f'<path d="M{k_end+8:.0f} {y-4}H{v_start-8:.0f}" stroke="{p["border"]}" stroke-dasharray="1 3"/>')
        o.append(f'<text x="{vend}" y="{y}" text-anchor="end" fill="{p["text"]}" {mono} font-size="14" textLength="{len(v)*CHAR:.1f}" lengthAdjust="spacingAndGlyphs">{esc(v)}</text>')
        o.append("</g>")
    # footer
    o.append(f'<path d="M{rx+14} 530H{rx+rw-14}" stroke="{p["border"]}"/>')
    o.append(f'<text x="{rx+14}" y="548" fill="{p["ok"]}" {mono} font-size="11">● ALL SYSTEMS NOMINAL</text>')
    right = CONFIG.get("footer_right", "")
    if stats:
        right = right.format(**stats) if right else f"{stats['public_repos']} REPOS · {fmt(stats['commits_this_year']).upper()} COMMITS {stats['year']}"
    o.append(f'<text x="{rx+rw-14}" y="548" text-anchor="end" fill="{p["muted"]}" {mono} font-size="11">{esc(right)}</text>')
    o.append("</svg>")
    return "\n".join(o)


def main() -> None:
    refresh_avatar()
    stats_path = OUT / "stats.json"
    stats = json.loads(stats_path.read_text()) if stats_path.exists() else None
    mode = CONFIG.get("portrait_ink", "auto")   # auto: positive image on both surfaces
    for theme in PALETTE:
        ink_dark = (theme == "light") if mode == "auto" else (mode == "dark")
        bits, pts = dither(ink_dark)
        print(f"{theme}: portrait {len(bits[0])}x{len(bits)} cells, {pts} points")
        write_svg(f"banner-{theme}.svg", render(bits, pts, stats, theme))


if __name__ == "__main__":
    main()
