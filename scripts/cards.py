"""GitHub stats card + language bar, self-hosted (no third-party stats service).
Fetches via GraphQL, caches numbers in profile/stats.json for banner.py."""
from __future__ import annotations

import datetime as dt
import json

from common import CONFIG, MONO, OUT, SANS, THEMES, esc, fmt, graphql, write_svg

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    name
    followers { totalCount }
    pullRequests { totalCount }
    issues { totalCount }
    repositoriesContributedTo(first: 1, contributionTypes: [COMMIT, PULL_REQUEST, ISSUE, REPOSITORY]) { totalCount }
    contributionsCollection(from: $from, to: $to) {
      totalCommitContributions
      restrictedContributionsCount
    }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false, orderBy: {field: PUSHED_AT, direction: DESC}) {
      totalCount
      nodes {
        name
        stargazerCount
        pushedAt
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name } }
        }
      }
    }
  }
}
"""


def fetch() -> dict:
    now = dt.datetime.now(dt.timezone.utc)
    start = now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    data = graphql(QUERY, {"login": CONFIG["login"], "from": start.isoformat(), "to": now.isoformat()})["user"]
    repos = data["repositories"]["nodes"]
    excluded = set(CONFIG.get("exclude_repos_from_languages", []))
    langs: dict[str, int] = {}
    for r in repos:
        if r["name"] in excluded:
            continue
        for e in r["languages"]["edges"]:
            langs[e["node"]["name"]] = langs.get(e["node"]["name"], 0) + e["size"]
    total = sum(langs.values()) or 1
    ranked = sorted(langs.items(), key=lambda kv: -kv[1])
    top = ranked[: CONFIG.get("max_languages", 6)]
    rest = sum(v for _, v in ranked[len(top):])
    lang_rows = [{"name": k, "pct": round(100 * v / total, 1)} for k, v in top]
    if rest:
        lang_rows.append({"name": "Other", "pct": round(100 * rest / total, 1)})
    cc = data["contributionsCollection"]
    last_push = max((r["pushedAt"] for r in repos), default=None)
    return {
        "login": CONFIG["login"],
        "name": CONFIG["display_name"],
        "year": now.year,
        "generated_at": now.isoformat(timespec="seconds"),
        "stars": sum(r["stargazerCount"] for r in repos),
        "commits_this_year": cc["totalCommitContributions"] + cc["restrictedContributionsCount"],
        "pull_requests": data["pullRequests"]["totalCount"],
        "issues": data["issues"]["totalCount"],
        "contributed_to": data["repositoriesContributedTo"]["totalCount"],
        "followers": data["followers"]["totalCount"],
        "public_repos": data["repositories"]["totalCount"],
        "last_push": last_push[:10] if last_push else "—",
        "languages": lang_rows,
    }


def stats_card(s: dict, theme: str) -> str:
    t = THEMES[theme]
    w, h = 480, 210
    rows = [
        ("Total stars", s["stars"]),
        (f"Commits in {s['year']}", s["commits_this_year"]),
        ("Pull requests", s["pull_requests"]),
        ("Issues", s["issues"]),
        ("Contributed to", s["contributed_to"]),
        ("Followers", s["followers"]),
    ]
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="GitHub statistics">',
        f'<rect width="{w}" height="{h}" rx="14" fill="{t["bg"]}" stroke="{t["border"]}"/>',
        f'<style>.t{{font:700 16px {SANS};fill:{t["accent"]}}}.k{{font:500 12px {SANS};fill:{t["muted"]}}}'
        f'.v{{font:700 13px {MONO};fill:{t["text"]}}}.hero{{font:800 44px {MONO};fill:{t["text"]}}}'
        f'.hl{{font:600 11px {SANS};fill:{t["muted"]}}}'
        f'.row{{animation:fade .5s ease both}}@keyframes fade{{from{{opacity:0;transform:translateX(-6px)}}to{{opacity:1;transform:none}}}}'
        f'@media (prefers-reduced-motion:reduce){{.row{{animation:none}}}}</style>',
        f'<text class="t" x="24" y="34">{esc(s["name"])}\'s GitHub stats</text>',
    ]
    y0 = 66
    for i, (k, v) in enumerate(rows):
        y = y0 + i * 24
        out.append(f'<g class="row" style="animation-delay:{0.1*i:.1f}s">')
        out.append(f'<circle cx="28" cy="{y-4}" r="3" fill="{t["accent"]}"/>')
        out.append(f'<text class="k" x="40" y="{y}">{esc(k)}</text>')
        out.append(f'<text class="v" x="270" y="{y}" text-anchor="end">{esc(fmt(v))}</text>')
        out.append("</g>")
    # hero: public repos, with a soft ring
    cx, cy = 390, 118
    out.append(f'<circle cx="{cx}" cy="{cy}" r="58" fill="{t["card"]}" stroke="{t["border"]}"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="58" fill="none" stroke="{t["accent"]}" stroke-width="3" '
               f'stroke-dasharray="364" stroke-dashoffset="364" transform="rotate(-90 {cx} {cy})">'
               f'<animate attributeName="stroke-dashoffset" from="364" to="0" dur="1.2s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1"/></circle>')
    out.append(f'<text class="hero" x="{cx}" y="{cy+10}" text-anchor="middle">{s["public_repos"]}</text>')
    out.append(f'<text class="hl" x="{cx}" y="{cy+32}" text-anchor="middle">public repos</text>')
    out.append("</svg>")
    return "\n".join(out)


def languages_card(s: dict, theme: str) -> str:
    t = THEMES[theme]
    langs = s["languages"]
    w = 480
    cols = 3
    legend_rows = -(-len(langs) // cols)
    h = 96 + legend_rows * 22
    bar_x, bar_y, bar_w, bar_h, gap = 24, 54, w - 48, 12, 2
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="most used languages">',
        f'<rect width="{w}" height="{h}" rx="14" fill="{t["bg"]}" stroke="{t["border"]}"/>',
        f'<style>.t{{font:700 16px {SANS};fill:{t["accent"]}}}.k{{font:500 12px {SANS};fill:{t["text"]}}}'
        f'.p{{font:500 11px {MONO};fill:{t["muted"]}}}</style>',
        f'<text class="t" x="24" y="34">Most used languages</text>',
        f'<clipPath id="bar"><rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="6"/></clipPath>',
        f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="6" fill="{t["card"]}"/>',
        '<g clip-path="url(#bar)">',
    ]
    x = bar_x
    total_pct = sum(l["pct"] for l in langs) or 100
    for i, l in enumerate(langs):
        seg = bar_w * l["pct"] / total_pct
        color = t["ramp"][min(i, len(t["ramp"]) - 1)]
        out.append(f'<rect x="{x:.1f}" y="{bar_y}" width="{max(seg-gap,0):.1f}" height="{bar_h}" fill="{color}">'
                   f'<animate attributeName="width" from="0" to="{max(seg-gap,0):.1f}" dur="0.9s" begin="{0.08*i:.2f}s" fill="freeze"/></rect>')
        x += seg
    out.append("</g>")
    col_w = (w - 48) / cols
    for i, l in enumerate(langs):
        r, c = divmod(i, cols)
        lx = bar_x + c * col_w
        ly = bar_y + 44 + r * 22
        color = t["ramp"][min(i, len(t["ramp"]) - 1)]
        out.append(f'<rect x="{lx:.1f}" y="{ly-9}" width="10" height="10" rx="3" fill="{color}"/>')
        out.append(f'<text class="k" x="{lx+16:.1f}" y="{ly}">{esc(l["name"])}</text>')
        out.append(f'<text class="p" x="{lx+col_w-8:.1f}" y="{ly}" text-anchor="end">{l["pct"]}%</text>')
    out.append("</svg>")
    return "\n".join(out)


def main() -> None:
    s = fetch()
    (OUT / "stats.json").write_text(json.dumps(s, indent=2) + "\n")
    print("wrote profile/stats.json")
    for theme in THEMES:
        write_svg(f"card-stats-{theme}.svg", stats_card(s, theme))
        write_svg(f"languages-{theme}.svg", languages_card(s, theme))


if __name__ == "__main__":
    main()
