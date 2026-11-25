"""Render GitHub's public contribution data without third-party chart services."""
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
import re

USER = 'HarshitK2814'

class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.days = {}
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'td' and 'data-date' in a and 'data-level' in a:
            self.days[date.fromisoformat(a['data-date'])] = int(a['data-level'])

def render(days, total, dark):
    bg, fg, muted, border = ('#0d1117','#e6edf3','#9198a1','#3d444d') if dark else ('#ffffff','#1f2328','#59636e','#d1d9e0')
    colors = ['#161b22','#0e4429','#006d32','#26a641','#39d353'] if dark else ['#eff2f5','#9be9a8','#40c463','#30a14e','#216e39']
    first = min(days)
    sunday = first.toordinal() - (first.weekday() + 1) % 7
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="880" height="225" viewBox="0 0 880 225" role="img" aria-label="{total:,} contributions in the last year"><style>text{{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif;fill:{fg};font-size:12px}}.muted{{fill:{muted}}}</style>', f'<rect width="880" height="225" fill="{bg}"/>',f'<text x="10" y="25" style="font-size:18px">{total:,} contributions in the last year</text>', f'<rect x="10" y="42" width="860" height="170" rx="6" fill="{bg}" stroke="{border}"/>']
    seen = set()
    for day, level in sorted(days.items()):
        week, weekday = divmod(day.toordinal() - sunday, 7)
        x, y = 64 + week * 15, 78 + weekday * 15
        month = (day.year, day.month)
        if month not in seen:
            seen.add(month)
            if week < 52:
                svg.append(f'<text x="{x}" y="66">{day:%b}</text>')
        svg.append(f'<rect x="{x}" y="{y}" width="11" height="11" rx="2" fill="{colors[level]}"/>')
    for label, row in [('Mon',1),('Wed',3),('Fri',5)]:
        svg.append(f'<text x="25" y="{87+row*15}">{label}</text>')
    svg.append('<text class="muted" x="26" y="197">Learn how we count contributions</text><text class="muted" x="700" y="197">Less</text>')
    for i, color in enumerate(colors):
        svg.append(f'<rect x="{733+i*15}" y="186" width="11" height="11" rx="2" fill="{color}"/>')
    svg.append('<text class="muted" x="813" y="197">More</text></svg>')
    return '\n'.join(svg) + '\n'

if __name__ == '__main__':
    request = Request(f'https://github.com/users/{USER}/contributions', headers={'User-Agent':'profile-calendar'})
    with urlopen(request, timeout=30) as response:
        source = response.read().decode()
    calendar = Calendar()
    calendar.feed(source)
    match = re.search(r'([\d,]+)\s+contributions?\s+in the last year', source)
    if not match or len(calendar.days) < 350:
        raise RuntimeError('Incomplete GitHub calendar; keeping existing images')
    total = int(match.group(1).replace(',', ''))
    Path('assets').mkdir(exist_ok=True)
    for theme in ['light','dark']:
        Path(f'assets/contributions-{theme}.svg').write_text(render(calendar.days,total,theme=='dark'),encoding='utf-8')
    print(f'Rendered {len(calendar.days)} days; {total} contributions')
