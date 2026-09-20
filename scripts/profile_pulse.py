#!/usr/bin/env python3
"""Collect public GitHub project metrics and render a compact, dated SVG.

Run: python3 scripts/profile_pulse.py --output /tmp/profile-pulse
Uses the authenticated GitHub CLI. The Actions workflow supplies GH_TOKEN.
All reads must succeed before any output is replaced; stale data retains its date.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from html import escape
import json
from pathlib import Path
import subprocess
from urllib.parse import urlencode
import xml.etree.ElementTree as ET

OWNER = 'Jonathan1366'
REPOS = ('observe-system', 'blockchain-money-transfer', 'RevAuto')
COLORS = {'Go': '#00add8', 'TypeScript': '#a5b4fc', 'JavaScript': '#f1e05a', 'Makefile': '#89e051'}


def api(path, paginate=False):
    args = ['gh', 'api', path]
    if paginate:
        args += ['--paginate', '--slurp']
    result = subprocess.run(args, check=True, text=True, capture_output=True, timeout=90)
    value = json.loads(result.stdout)
    return [item for page in value for item in page] if paginate else value


def date_of(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(timezone.utc)


def count_days(commits, start, now):
    counts = [0] * 14
    seen = set()
    for commit in commits:
        if commit['sha'] in seen:
            continue
        seen.add(commit['sha'])
        when = date_of(commit['commit']['committer']['date'])
        day = (when.date() - start.date()).days
        if 0 <= day < 14 and start <= when <= now:
            counts[day] += 1
    return counts


def collect(repo, now):
    base = f'repos/{OWNER}/{repo}'
    meta = api(base)
    # Explicitly prevent private repository data from reaching a public profile.
    if meta.get('private'):
        raise ValueError(f'{repo} must be public')
    languages = api(base + '/languages')
    start = now.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=13)
    params = urlencode({'sha': meta['default_branch'], 'since': start.isoformat(), 'until': now.isoformat(), 'per_page': 100})
    commits = api(base + '/commits?' + params, paginate=True) if meta['size'] else []
    return {'name': repo, 'default_branch': meta['default_branch'], 'languages': languages,
            'daily_commits': count_days(commits, start, now), 'last_push': meta['pushed_at']}


def text(x, y, value, size=12, color='#c9d1d9', extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" {extra}>{escape(str(value))}</text>'


def render(data):
    rows = data['repositories']
    body = text(22, 29, 'PROJECT PULSE', 14, '#2dd4bf', 'font-weight="700" letter-spacing="1"')
    stamp = date_of(data['collected_at']).strftime('%d %b %Y %H:%M UTC')
    body += text(878, 29, 'UPDATED ' + stamp, 11, '#9da7b3', 'text-anchor="end"')
    body += text(22, 56, 'REPOSITORY', 10, '#9da7b3') + text(322, 56, 'LANGUAGE / CODE BYTES', 10, '#9da7b3')
    body += text(558, 56, 'COMMITS / 14 UTC DAYS', 10, '#9da7b3') + text(878, 56, 'LAST PUSH (UTC)', 10, '#9da7b3', 'text-anchor="end"')
    peak = max((max(row['daily_commits']) for row in rows), default=0)
    for i, row in enumerate(rows):
        y = 85 + i * 57
        body += text(22, y + 5, row['name'], 14, '#f0f6fc', 'font-weight="600"')
        langs = sorted(row['languages'].items(), key=lambda pair: pair[1], reverse=True)
        total = sum(n for _, n in langs)
        body += '<g class="fill">'
        if total:
            x = 322
            for name, n in langs:
                width = n / total * 194
                body += f'<rect x="{x:.4f}" y="{y+5}" width="{width:.4f}" height="7" fill="{COLORS.get(name,"#9da7b3")}"/>'
                x += width
            dominant, n = langs[0]
            body += text(322, y - 4, f'{dominant} {n/total:.1%}', 11, COLORS.get(dominant, '#c9d1d9'))
        else:
            body += text(322, y + 5, 'No language data', 11, '#9da7b3')
        body += '</g>'
        body += f'<path d="M558 {y+14}h132" stroke="#30363d"/>'
        for day, n in enumerate(row['daily_commits']):
            if n:
                height = n / max(peak, 1) * 24
                body += f'<rect class="activity" x="{558+day*9.5}" y="{y+14-height:.2f}" width="6" height="{height:.2f}" rx="1" fill="#2dd4bf"/>'
        body += text(724, y + 6, sum(row['daily_commits']), 13, '#e6edf3', 'text-anchor="end"')
        pushed = date_of(row['last_push']).strftime('%d %b %Y') if row['last_push'] else '—'
        body += text(878, y + 6, pushed, 11, '#9da7b3', 'text-anchor="end"')
        if i < len(rows) - 1:
            body += f'<path d="M22 {y+31}h856" stroke="#21262d"/>'
    scale = f'shared scale: 0–{peak} commits/day' if peak else 'no default-branch commits in this window'
    body += text(22, 256, f'GitHub API · {scale} · final day partial · scheduled every 5 min', 10, '#9da7b3')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="274" viewBox="0 0 900 274" role="img" aria-labelledby="title desc">
<title id="title">Automatically refreshed public project metrics</title><desc id="desc">{escape(json.dumps(data))}</desc>
<style>.fill{{animation:appear 1.2s ease-out}}.activity{{animation:appear 1.4s ease-out}}@keyframes load{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}@keyframes appear{{from{{opacity:.65}}to{{opacity:1}}}}@media(prefers-reduced-motion:reduce){{.fill,.activity{{animation:none}}}}</style>
<rect width="900" height="274" rx="12" fill="#0d1117"/><rect x="1" y="1" width="898" height="272" rx="11" fill="none" stroke="#30363d"/>
<g font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">{body}</g></svg>\n'''
    ET.fromstring(svg)
    return svg


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    now = datetime.now(timezone.utc).replace(microsecond=0)
    with ThreadPoolExecutor(max_workers=3) as pool:
        rows = list(pool.map(lambda repo: collect(repo, now), REPOS))
    data = {'collected_at': now.isoformat(), 'source': 'GitHub REST API', 'repositories': rows}
    svg = render(data)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'pulse.svg').write_text(svg)
    (args.output / 'metrics.json').write_text(json.dumps(data, indent=2) + '\n')
    print(f'Collected {len(rows)} public repositories at {data["collected_at"]}')


if __name__ == '__main__':
    main()
