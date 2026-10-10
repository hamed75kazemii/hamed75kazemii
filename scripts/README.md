# profile generators

Stdlib-only Python 3.11+. Run from the repo root:

```sh
python3 scripts/cards.py    # GitHub stats + languages -> profile/stats.json, card-stats-*.svg, languages-*.svg
python3 scripts/banner.py   # terminal banner (reads profile/stats.json)
python3 scripts/radar.py    # radars from profile/skills.json + profile/langmix.json
```

- `profile/avatar.jpg` is refreshed from your GitHub avatar on every banner run and embedded in the banner.
- Needs a token: `GH_PAT` (recommended, so private contributions count) or `GITHUB_TOKEN`,
  or a logged-in `gh` CLI locally.
- Edit `profile/config.json` for name / role / typing lines, `profile/skills.json` and
  `profile/langmix.json` for the radars. `.github/workflows/profile.yml` redraws everything daily.
