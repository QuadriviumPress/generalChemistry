"""Small SVG drawing kit shared by the replacement diagrams."""
import html
import math
import re

INK = '#1f2933'
MUTED = '#52606d'
GLASS = '#4f6475'
GLASS_FILL = '#f3f8fb'
WATER = '#d6ebf7'
FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"

_ids = [0]


def uid(prefix='c'):
    _ids[0] += 1
    return f'{prefix}{_ids[0]}'


def reset_ids():
    _ids[0] = 0


def f(v):
    """Format a coordinate compactly."""
    return ('%.1f' % v).rstrip('0').rstrip('.')


def parse_rich(s):
    """Split chemistry markup into (text, mode). _2 or _{..} subscripts; ^+ or ^{..} superscripts."""
    tokens, buf, i = [], '', 0
    while i < len(s):
        c = s[i]
        if c in '_^' and i + 1 < len(s):
            if buf:
                tokens.append((buf, 'n'))
                buf = ''
            mode = 'sub' if c == '_' else 'sup'
            if s[i + 1] == '{':
                j = s.index('}', i + 2)
                group, i = s[i + 2:j], j + 1
            elif c == '_' and s[i + 1].isdigit():
                m = re.match(r'\d+', s[i + 1:])
                group, i = m.group(), i + 1 + len(m.group())
            else:
                group, i = s[i + 1], i + 2
            tokens.append((group, mode))
        else:
            buf += c
            i += 1
    if buf:
        tokens.append((buf, 'n'))
    return tokens


SHIFT = {'n': 0.0, 'sub': 0.32, 'sup': -0.42}


def rich(s, size=15):
    out, cur = [], 0.0
    for text, mode in parse_rich(s):
        target = SHIFT[mode]
        attrs = ''
        if abs(target - cur) > 1e-9:
            attrs += f' dy="{f((target - cur) * size)}"'
        if mode != 'n':
            attrs += ' font-size="70%"'
        out.append(f'<tspan{attrs}>{html.escape(text, quote=False)}</tspan>' if attrs else html.escape(text, quote=False))
        cur = target
    return ''.join(out)


def text(x, y, s, size=15, anchor='middle', weight=None, fill=INK, italic=False, extra=''):
    a = f'x="{f(x)}" y="{f(y)}" font-size="{size}"'
    if anchor != 'start':
        a += f' text-anchor="{anchor}"'
    if weight:
        a += f' font-weight="{weight}"'
    if fill != INK:
        a += f' fill="{fill}"'
    if italic:
        a += ' font-style="italic"'
    return f'<text {a}{extra}>{rich(s, size)}</text>'


def lines(x, y, rows, size=15, gap=None, **kw):
    gap = gap or size * 1.3
    return ''.join(text(x, y + i * gap, r, size=size, **kw) for i, r in enumerate(rows))


def panel_label(x, y, s, size=16):
    return text(x, y, s, size=size, anchor='start', weight='bold')


def arrowhead(x, y, angle, size=9, fill=INK):
    a1, a2 = angle + math.radians(155), angle - math.radians(155)
    p = [(x, y), (x + size * math.cos(a1), y + size * math.sin(a1)),
         (x + size * math.cos(a2), y + size * math.sin(a2))]
    return '<polygon points="%s" fill="%s"/>' % (' '.join(f'{f(a)},{f(b)}' for a, b in p), fill)


def arrow(x1, y1, x2, y2, color=INK, width=2, head=9, dash=None, both=False):
    ang = math.atan2(y2 - y1, x2 - x1)
    ex, ey = x2 - head * 0.6 * math.cos(ang), y2 - head * 0.6 * math.sin(ang)
    sx, sy = (x1 + head * 0.6 * math.cos(ang), y1 + head * 0.6 * math.sin(ang)) if both else (x1, y1)
    d = f' stroke-dasharray="{dash}"' if dash else ''
    s = (f'<line x1="{f(sx)}" y1="{f(sy)}" x2="{f(ex)}" y2="{f(ey)}" stroke="{color}" '
         f'stroke-width="{width}"{d}/>' + arrowhead(x2, y2, ang, head, color))
    if both:
        s += arrowhead(x1, y1, ang + math.pi, head, color)
    return s


def curve_arrow(x1, y1, cx, cy, x2, y2, color=INK, width=2, head=9, dash=None):
    ang = math.atan2(y2 - cy, x2 - cx)
    ex, ey = x2 - head * 0.6 * math.cos(ang), y2 - head * 0.6 * math.sin(ang)
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<path d="M{f(x1)},{f(y1)} Q{f(cx)},{f(cy)} {f(ex)},{f(ey)}" fill="none" stroke="{color}" '
            f'stroke-width="{width}"{d}/>' + arrowhead(x2, y2, ang, head, color))


def eq_arrow(x1, x2, y, color=INK):
    """Equilibrium half-arrows."""
    h = 5
    return (f'<path d="M{f(x1)},{f(y - 3)} H{f(x2)} l-{h + 3},-{h}" fill="none" stroke="{color}" stroke-width="1.8"/>'
            f'<path d="M{f(x2)},{f(y + 3)} H{f(x1)} l{h + 3},{h}" fill="none" stroke="{color}" stroke-width="1.8"/>')


def line(x1, y1, x2, y2, color=INK, width=1.5, dash=None, extra=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{color}" stroke-width="{width}"{d}{extra}/>'


def rect(x, y, w, h, fill='none', stroke=INK, sw=1.5, rx=0, extra=''):
    r = f' rx="{f(rx)}"' if rx else ''
    return (f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}"{r} fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{extra}/>')


def circle(x, y, r, fill='none', stroke=INK, sw=1.2, extra=''):
    return f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{extra}/>'


def path(d, fill='none', stroke=INK, sw=1.5, extra=''):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{extra}/>'


def ion(x, y, r, fill, label, color='#fff', size=None, stroke=None):
    size = size or max(9, r * 0.85)
    return (circle(x, y, r, fill, stroke or '#00000055', 1) +
            text(x, y + size * 0.36, label, size=size, fill=color, weight='bold'))


def clip(shape_d):
    cid = uid('clip')
    return cid, f'<clipPath id="{cid}"><path d="{shape_d}"/></clipPath>'


def vessel(outline_d, inner_d, top, bottom, level, liquid, opacity=1.0, glass=GLASS, inside=''):
    """Draw a vessel from an outline path; liquid fills inner_d below the level fraction."""
    cid, cdef = clip(inner_d)
    ly = bottom - (bottom - top) * level
    liq = ''
    if level > 0 and liquid:
        liq = f'<rect x="-10" y="{f(ly)}" width="2000" height="{f(bottom - ly + 20)}" fill="{liquid}" fill-opacity="{opacity}"/>'
    return (f'<defs>{cdef}</defs>' + path(inner_d, GLASS_FILL, 'none', 0) +
            f'<g clip-path="url(#{cid})">{liq}{inside}</g>' + path(outline_d, 'none', glass, 2.2,
                                                                    ' stroke-linejoin="round"')), cid, ly


def beaker(x, y, w, h, level=0.6, liquid=WATER, opacity=1.0, inside='', marks=True):
    r = 10
    outline = (f'M{f(x - 7)},{f(y - 3)} Q{f(x)},{f(y)} {f(x)},{f(y + 8)} V{f(y + h - r)} '
               f'Q{f(x)},{f(y + h)} {f(x + r)},{f(y + h)} H{f(x + w - r)} Q{f(x + w)},{f(y + h)} {f(x + w)},{f(y + h - r)} '
               f'V{f(y + 8)} Q{f(x + w)},{f(y)} {f(x + w + 7)},{f(y - 3)}')
    inner = (f'M{f(x)},{f(y)} V{f(y + h - r)} Q{f(x)},{f(y + h)} {f(x + r)},{f(y + h)} H{f(x + w - r)} '
             f'Q{f(x + w)},{f(y + h)} {f(x + w)},{f(y + h - r)} V{f(y)} Z')
    s, cid, ly = vessel(outline, inner, y, y + h, level, liquid, opacity, inside=inside)
    if marks:
        for k in range(1, 4):
            yy = y + h - k * h / 4.5
            s += line(x + 6, yy, x + 18, yy, GLASS, 1)
    return s, ly


def erlenmeyer(cx, bottom, bw=120, h=140, nw=34, nh=40, level=0.35, liquid=WATER, opacity=1.0, inside=''):
    top = bottom - h
    shoulder = top + nh
    r = 8
    xl, xr = cx - bw / 2, cx + bw / 2
    outline = (f'M{f(cx - nw / 2 - 5)},{f(top)} H{f(cx - nw / 2)} V{f(shoulder)} L{f(xl + 2)},{f(bottom - r)} '
               f'Q{f(xl)},{f(bottom)} {f(xl + r)},{f(bottom)} H{f(xr - r)} Q{f(xr)},{f(bottom)} {f(xr - 2)},{f(bottom - r)} '
               f'L{f(cx + nw / 2)},{f(shoulder)} V{f(top)} H{f(cx + nw / 2 + 5)}')
    inner = (f'M{f(cx - nw / 2)},{f(top)} V{f(shoulder)} L{f(xl + 2)},{f(bottom - r)} Q{f(xl)},{f(bottom)} {f(xl + r)},{f(bottom)} '
             f'H{f(xr - r)} Q{f(xr)},{f(bottom)} {f(xr - 2)},{f(bottom - r)} L{f(cx + nw / 2)},{f(shoulder)} V{f(top)} Z')
    s, cid, ly = vessel(outline, inner, shoulder, bottom, level, liquid, opacity, inside=inside)
    return s, ly


def test_tube(cx, top, h, w=34, level=0.6, liquid=WATER, opacity=1.0, inside='', closed=False, liquid_top=None):
    r = w / 2
    xl, xr = cx - r, cx + r
    bottom = top + h
    outline = (f'M{f(xl - 3)},{f(top)} H{f(xl)} V{f(bottom - r)} A{f(r)},{f(r)} 0 0 0 {f(xr)},{f(bottom - r)} '
               f'V{f(top)} H{f(xr + 3)}')
    inner = f'M{f(xl)},{f(top)} V{f(bottom - r)} A{f(r)},{f(r)} 0 0 0 {f(xr)},{f(bottom - r)} V{f(top)} Z'
    s, cid, ly = vessel(outline, inner, top, bottom, level, liquid, opacity, inside=inside)
    if closed:
        s += rect(xl - 4, top - 14, w + 8, 16, '#7b8794', '#3e4c59', 1.2, 3)
    return s, ly


def bubbles(points, r=4, stroke='#5a7184'):
    return ''.join(circle(x, y, rr if rr else r, '#ffffffcc', stroke, 1) for x, y, rr in points)


def flame(cx, base, h=40, w=18):
    outer = (f'M{f(cx)},{f(base - h)} C{f(cx + w)},{f(base - h * 0.45)} {f(cx + w * 0.8)},{f(base)} {f(cx)},{f(base)} '
             f'C{f(cx - w * 0.8)},{f(base)} {f(cx - w)},{f(base - h * 0.45)} {f(cx)},{f(base - h)} Z')
    inner = (f'M{f(cx)},{f(base - h * 0.55)} C{f(cx + w * 0.45)},{f(base - h * 0.25)} {f(cx + w * 0.35)},{f(base - 2)} {f(cx)},{f(base - 2)} '
             f'C{f(cx - w * 0.35)},{f(base - 2)} {f(cx - w * 0.45)},{f(base - h * 0.25)} {f(cx)},{f(base - h * 0.55)} Z')
    return path(outer, '#f7a530', '#d9731a', 1) + path(inner, '#fde68a', 'none', 0)


def burner(cx, top):
    """Bunsen burner whose flame tip touches y=top."""
    s = flame(cx, top + 46, 44, 13)
    s += rect(cx - 7, top + 46, 14, 50, '#9aa5b1', '#3e4c59', 1.2)
    s += path(f'M{f(cx - 26)},{f(top + 104)} H{f(cx + 26)} L{f(cx + 18)},{f(top + 94)} H{f(cx - 18)} Z', '#7b8794', '#3e4c59', 1.2)
    return s


def scatter_points(n, x, y, w, h, seed=1, minsep=0):
    """Deterministic pseudo-random points inside a rectangle."""
    pts, state = [], seed * 9301 + 49297
    tries = 0
    while len(pts) < n and tries < n * 400:
        tries += 1
        state = (state * 9301 + 49297) % 233280
        px = x + (state / 233280) * w
        state = (state * 9301 + 49297) % 233280
        py = y + (state / 233280) * h
        if all((px - a) ** 2 + (py - b) ** 2 >= minsep ** 2 for a, b in pts):
            pts.append((px, py))
    return pts


def _opaque(m):
    return f'{m.group(1)}="#{m.group(2)}" {m.group(1)}-opacity="{int(m.group(3), 16) / 255:.2f}"'


def svg(w, h, title, desc, body):
    body = re.sub(r'(fill|stroke)="#([0-9a-fA-F]{6})([0-9a-fA-F]{2})"', _opaque, body)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-labelledby="t d" font-family="{html.escape(FONT)}">\n'
            f'<title id="t">{html.escape(title)}</title>\n<desc id="d">{html.escape(desc)}</desc>\n'
            f'<rect width="{w}" height="{h}" fill="#ffffff"/>\n{body}\n</svg>\n')


def wavelength_rgb(nm):
    """Approximate display color for a visible wavelength (display aid, not colorimetry)."""
    if nm < 440:
        r, g, b = -(nm - 440) / 60, 0, 1
    elif nm < 490:
        r, g, b = 0, (nm - 440) / 50, 1
    elif nm < 510:
        r, g, b = 0, 1, -(nm - 510) / 20
    elif nm < 580:
        r, g, b = (nm - 510) / 70, 1, 0
    elif nm < 645:
        r, g, b = 1, -(nm - 645) / 65, 0
    else:
        r, g, b = 1, 0, 0
    if nm < 420:
        k = 0.3 + 0.7 * (nm - 380) / 40
    elif nm > 700:
        k = 0.3 + 0.7 * (780 - nm) / 80
    else:
        k = 1
    return '#%02x%02x%02x' % tuple(int(round(255 * (c * k) ** 0.8)) for c in (r, g, b))
