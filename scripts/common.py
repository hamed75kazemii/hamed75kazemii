"""Shared helpers for the profile asset generators (stdlib only)."""
from __future__ import annotations

import json
import os
import subprocess
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "profile"
CONFIG = json.loads((OUT / "config.json").read_text())

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

# Light mode uses a darker step of the same violet so it still passes 3:1 on white.
THEMES = {
    "dark": {
        "bg": "#0d1117", "card": "#161b22", "border": "#30363d", "grid": "#30363d",
        "text": "#e6edf3", "muted": "#8b949e", "accent": "#aa9bef",
        "accent_soft": "rgba(170,155,239,0.22)", "green": "#3fb950",
        "ramp": ["#aa9bef", "#8f7fe0", "#7565cf", "#5d4fb8", "#4a3f99", "#3a327a", "#2c2760"],
    },
    "light": {
        "bg": "#ffffff", "card": "#f6f8fa", "border": "#d0d7de", "grid": "#d8dee4",
        "text": "#1f2328", "muted": "#57606a", "accent": "#6f5fcf",
        "accent_soft": "rgba(111,95,207,0.18)", "green": "#1a7f37",
        "ramp": ["#6f5fcf", "#8575d9", "#9b8de2", "#b1a5ea", "#c6bdf1", "#d9d3f6", "#ebe7fa"],
    },
}


def esc(s: object) -> str:
    return escape(str(s))


def write_svg(name: str, svg: str) -> None:
    path = OUT / name
    path.write_text(svg.strip() + "\n")
    print(f"wrote {path.relative_to(ROOT)} ({path.stat().st_size // 1024} KB)")


def github_token() -> str | None:
    for key in ("GH_PAT", "GITHUB_TOKEN"):
        if os.environ.get(key):
            return os.environ[key]
    try:
        tok = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10)
        if tok.returncode == 0 and tok.stdout.strip():
            return tok.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return None


def graphql(query: str, variables: dict) -> dict:
    token = github_token()
    if not token:
        raise SystemExit("no GitHub token: set GH_PAT / GITHUB_TOKEN or run `gh auth login`")
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json",
                 "User-Agent": "profile-readme-generator"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = json.loads(resp.read())
    if payload.get("errors"):
        raise SystemExit(f"GraphQL errors: {payload['errors']}")
    return payload["data"]


def fmt(n: int) -> str:
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}k"
    return str(n)
