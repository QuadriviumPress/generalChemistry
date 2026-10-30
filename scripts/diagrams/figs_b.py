"""Chapters 6-13 replacement diagrams."""
import math
from lib import *

FIGS = {}

# Air wavelengths (nm) of selected strong visible lines, NIST Atomic Spectra Database.
H_LINES = [410.17, 434.05, 486.13, 656.28]
NE_LINES = [540.06, 585.25, 588.19, 594.48, 597.55, 602.00, 607.43, 609.62, 614.31, 616.36, 621.73,
            626.65, 630.48, 633.44, 638.30, 640.22, 650.65, 659.90, 667.83, 671.70, 692.95]
HG_LINES = [404.66, 407.78, 435.83, 546.07, 576.96, 579.07]


def fig(fid, name):
    def wrap(fn):
        FIGS[fid] = (name, fn)
        return fn
    return wrap


def spectrum_strip(x, y, w, h, lines_nm, lo=400, hi=700, scale=True, width=3):
    s = rect(x, y, w, h, '#111827', '#111827', 1)
    for nm in lines_nm:
        px = x + (nm - lo) / (hi - lo) * w
        s += rect(px - width / 2, y + 2, width, h - 4, wavelength_rgb(nm), 'none', 0)
    if scale:
        for nm in range(lo, hi + 1, 50):
            px = x + (nm - lo) / (hi - lo) * w
            s += line(px, y + h, px, y + h + 7, INK, 1.2) + text(px, y + h + 22, str(nm), 13)
    return s


def tube_glow(x, y, w, h, color, gid):
    s = (f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{color}" stop-opacity="0.45"/>'
         f'<stop offset="0.5" stop-color="{color}" stop-opacity="0.95"/><stop offset="1" stop-color="{color}" stop-opacity="0.45"/>'
         f'</linearGradient></defs>')
    return s + rect(x, y, w, h, f'url(#{gid})', GLASS, 2, h / 2)


@fig('FR026', 'fig-06-09-hydrogen-emission.svg')
def hydrogen_emission():
    b = panel_label(20, 30, '(a)') + text(52, 30, 'Excited hydrogen atoms', 16, anchor='start', weight='bold')
    b += tube_glow(40, 90, 200, 40, '#e8457d', 'hg')
    b += rect(30, 96, 14, 28, '#7b8794', INK, 1) + rect(236, 96, 14, 28, '#7b8794', INK, 1)
    b += lines(140, 160, ['Hydrogen discharge tube', 'glows red'], 14)
    b += panel_label(300, 30, '(b)') + text(332, 30, 'Light split by a prism', 16, anchor='start', weight='bold')
    b += line(240, 110, 330, 110, '#e8457d', 3)
    b += rect(330, 92, 6, 14, INK, 'none', 0) + rect(330, 114, 6, 14, INK, 'none', 0)
    b += text(333, 84, 'slit', 12)
    b += path('M400,145 L440,70 L480,145 Z', '#e3eef6', GLASS, 2) + text(392, 140, 'prism', 12, anchor='end')
    b += line(336, 110, 420, 110, '#e8457d', 3)
    sx, sw, sy = 300, 540, 260
    for nm in H_LINES:
        px = sx + (nm - 400) / 300 * sw
        b += line(462, 112, px, sy, wavelength_rgb(nm), 2)
    b += spectrum_strip(sx, sy, sw, 50, H_LINES, width=4)
    for nm, lab, anchor in zip(H_LINES, ('410.2', '434.0', '486.1', '656.3'), ('end', 'start', 'middle', 'middle')):
        px = sx + (nm - 400) / 300 * sw + {'end': -3, 'start': 3, 'middle': 0}[anchor]
        b += text(px, sy - 8, lab, 12, anchor=anchor, weight='bold')
    b += text(sx + sw / 2, sy + 52 + 40, 'Wavelength (nm)', 14)
    b += text(sx + (656.28 - 400) / 300 * sw, sy - 26, 'most intense', 12, fill='#b91c1c')
    b += text(430, 392, 'Line positions from NIST atomic data; line colors are display approximations.', 12, fill=MUTED)
    return svg(860, 405, 'Hydrogen emission spectrum',
               'A hydrogen discharge tube glows red. Its light passes through a slit and a prism, which separates '
               'it into four lines on a 400 to 700 nanometer scale: violet at 410.2, violet at 434.0, blue-green at '
               '486.1, and red at 656.3 nanometers, the most intense.', b)


@fig('FR027', 'fig-06-13-emission-spectra.svg')
def emission_spectra():
    b = ''
    rows = [('(a) Hydrogen (H atoms)', H_LINES), ('(b) Neon', NE_LINES), ('(c) Mercury', HG_LINES)]
    x, w = 200, 620
    for i, (name, nm) in enumerate(rows):
        y = 30 + i * 80
        b += text(x - 14, y + 30, name, 15, anchor='end', weight='bold')
        b += spectrum_strip(x, y, w, 46, nm, scale=(i == 2), width=2.6)
    b += text(x + w / 2, 300, 'Wavelength (nm)', 14)
    b += text(430, 326, 'Selected strong visible lines from the NIST Atomic Spectra Database. Line widths and brightness are not to scale.',
              12, fill=MUTED)
    return svg(860, 340, 'Hydrogen, neon, and mercury spectra',
               'Three emission line spectra on a shared 400 to 700 nanometer scale. Hydrogen has four lines. Neon has '
               'many lines, mostly in the yellow, orange, and red. Mercury has violet lines near 405 and 436 '
               'nanometers, a green line at 546 nanometers, and a yellow pair near 577 and 579 nanometers.', b)


def co2(cx, cy, horizontal=True):
    dx, dy = (22, 0) if horizontal else (0, 22)
    s = ''
    for k in (-1, 1):
        ox, oy = cx + k * dx, cy + k * dy
        nx, ny = (0, 3) if horizontal else (3, 0)
        s += line(cx + nx, cy + ny, ox + nx, oy + ny, INK, 2) + line(cx - nx, cy - ny, ox - nx, oy - ny, INK, 2)
    s += circle(cx, cy, 9, '#3e4c59', '#1f2933', 1)
    s += circle(cx - dx, cy - dy, 10, '#d64545', '#7a1f1f', 1) + circle(cx + dx, cy + dy, 10, '#d64545', '#7a1f1f', 1)
    return s


@fig('FR029', 'fig-08-opener-co2-sio2.svg')
def co2_sio2():
    b = panel_label(20, 30, 'Dry ice, CO_2(s): a molecular solid')
    pts = []
    for r in range(3):
        for c in range(3):
            pts.append((70 + c * 110 + (r % 2) * 40, 90 + r * 80, (r + c) % 2 == 0))
    for i, (x, y, hz) in enumerate(pts):
        for (x2, y2, _) in pts[i + 1:]:
            if 0 < math.hypot(x2 - x, y2 - y) < 100:
                b += line(x, y, x2, y2, '#9aa5b1', 1.2, '3 4')
    for x, y, hz in pts:
        b += co2(x, y, hz)
    b += lines(200, 312, ['Strong C=O covalent bonds within each molecule;',
                          'weak intermolecular forces (dashed) between molecules'], 13)
    b += lines(200, 360, ['Volatile: sublimes at −78 °C (1 atm)'], 15, weight='bold')
    ox = 470
    b += panel_label(ox, 30, 'Quartz, SiO_2: a covalent network')
    gs, nx, ny, x0, y0 = 68, 6, 4, ox + 22, 70
    for r in range(ny):
        for c in range(nx):
            x, y = x0 + c * gs, y0 + r * gs
            if c < nx - 1:
                b += line(x, y, x + gs, y, INK, 2.5)
            if r < ny - 1:
                b += line(x, y, x, y + gs, INK, 2.5)
    for r in range(ny):
        for c in range(nx):
            x, y = x0 + c * gs, y0 + r * gs
            if c < nx - 1:
                b += circle(x + gs / 2, y, 8, '#d64545', '#7a1f1f', 1)
            if r < ny - 1:
                b += circle(x, y + gs / 2, 8, '#d64545', '#7a1f1f', 1)
            b += circle(x, y, 12, '#c9a227', '#7a6114', 1) + text(x, y + 4, 'Si', 10, weight='bold')
    b += lines(ox + 192, 312, ['Every atom is held by strong Si–O covalent bonds;',
                               'flattened sketch of a 3-D network (each Si bonds to 4 O)'], 13)
    b += lines(ox + 192, 360, ['Hard, with a high melting point'], 15, weight='bold')
    b += circle(320, 392, 7, '#d64545', '#7a1f1f', 1) + text(332, 397, 'O', 13, anchor='start')
    b += circle(380, 392, 7, '#3e4c59', '#1f2933', 1) + text(392, 397, 'C', 13, anchor='start')
    b += circle(440, 392, 9, '#c9a227', '#7a6114', 1) + text(454, 397, 'Si', 13, anchor='start')
    return svg(880, 410, 'Carbon dioxide and silicon dioxide',
               'Left: dry ice drawn as separate linear O=C=O molecules joined to each other only by weak '
               'intermolecular forces; it sublimes at minus 78 degrees Celsius. Right: quartz drawn as a continuous '
               'network in which every silicon atom is bonded to oxygen atoms that bridge to other silicon atoms; it '
               'is hard and high melting.', b)


def bottle(cx, base, label, liquid):
    s, _ = beaker(cx - 45, base - 120, 90, 120, 0.55, liquid, 1, marks=False)
    return s + text(cx, base + 24, label, 15, weight='bold')


def cloud(cx, cy, rx, ry, seed):
    s = ''
    for x, y in scatter_points(14, cx - rx, cy - ry, 2 * rx, 2 * ry, seed, 6):
        s += circle(x, y, 13, '#ffffff', '#b8c4cf', 1)
    return s


@fig('FR031', 'fig-10-15-nh3-hcl-diffusion.svg')
def nh3_hcl():
    b = rect(0, 0, 860, 300, '#eef2f6', 'none', 0)
    b += bottle(110, 280, 'NH_3(aq)', '#e3f1fa') + bottle(750, 280, 'HCl(aq)', '#e3f1fa')
    for x, y in scatter_points(9, 160, 80, 300, 150, 3, 26):
        b += circle(x, y, 6, '#3d7fc4', '#1d4f80', 1)
    for x, y in scatter_points(7, 560, 80, 120, 150, 9, 26):
        b += circle(x, y, 7, '#3f9b4f', '#1f5f2a', 1)
    b += arrow(170, 60, 360, 60, '#1d4f80', 2, 10) + text(265, 48, 'NH_3(g) diffuses', 14, fill='#1d4f80', weight='bold')
    b += arrow(700, 60, 590, 60, '#1f5f2a', 2, 10) + text(645, 48, 'HCl(g)', 14, fill='#1f5f2a', weight='bold')
    b += cloud(520, 160, 34, 70, 4)
    b += text(520, 262, 'white NH_4Cl(s) forms', 14, weight='bold')
    b += text(430, 340, 'NH_3(g) + HCl(g) → NH_4Cl(s)', 18, weight='bold')
    b += text(430, 366, 'The fumes form closer to the HCl because NH_3 molecules diffuse faster.', 13, fill=MUTED)
    return svg(860, 380, 'Ammonia and hydrogen chloride diffusion',
               'Open containers of aqueous ammonia on the left and hydrochloric acid on the right release gas '
               'molecules that diffuse toward each other. Where they meet, closer to the hydrochloric acid, they form '
               'a white cloud of solid ammonium chloride.', b)


@fig('FR032', 'fig-10-16-graham-diffusion.svg')
def graham():
    x0, k = 50, 26  # px per cm

    def X(cm):
        return x0 + k * cm
    b = rect(X(0) - 10, 120, X(30) - X(0) + 20, 56, '#f3f8fb', GLASS, 2.2, 28)
    b += circle(X(3.3), 148, 20, '#ffffff', '#9aa5b1', 1.5) + circle(X(28.0), 148, 20, '#ffffff', '#9aa5b1', 1.5)
    for x, y in scatter_points(9, X(18.8) + 4, 128, 46, 40, 2, 8):
        b += circle(x, y, 9, '#ffffff', '#b8c4cf', 1)
    b += line(X(18.8), 110, X(18.8), 186, '#c0392b', 2, '5 3')
    b += lines(X(3.3), 92, ['Cotton with', 'NH_3(aq)'], 14)
    b += lines(X(28.0), 92, ['Cotton with', 'HCl(aq)'], 14)
    b += lines(X(18.8), 72, ['NH_4Cl(s) first', 'appears here'], 14, fill='#c0392b', weight='bold')
    # Ruler.
    b += rect(X(0), 200, X(30) - X(0), 34, '#fdf6e3', '#8a8170', 1.2)
    for cm in range(31):
        hgt = 14 if cm % 5 == 0 else 7
        b += line(X(cm), 200, X(cm), 200 + hgt, '#5c5546', 1)
        if cm % 5 == 0:
            b += text(X(cm), 230, str(cm), 12)
    b += text(X(30) + 18, 230, 'cm', 12, anchor='start')
    for a, c, lab in ((3.3, 18.8, '18.8 − 3.3 = 15.5 cm'), (18.8, 28.0, '28.0 − 18.8 = 9.2 cm')):
        b += arrow(X(a), 262, X(c), 262, INK, 1.5, 8, both=True) + text((X(a) + X(c)) / 2, 286, lab, 14, weight='bold')
        b += line(X(a), 236, X(a), 272, MUTED, 1, '2 2') + line(X(c), 236, X(c), 272, MUTED, 1, '2 2')
    b += text(450, 330, 'Observed ratio of distances: 15.5 / 9.2 = 1.7', 16, weight='bold')
    b += text(450, 354, 'Graham’s law prediction, √(molar mass HCl / molar mass NH_3): 1.47', 15)
    return svg(900, 372, 'Measuring relative diffusion rates',
               'A tube has cotton soaked in aqueous ammonia at 3.3 centimeters and cotton soaked in hydrochloric acid '
               'at 28.0 centimeters on a ruler. White ammonium chloride first appears with its left edge at 18.8 '
               'centimeters, 15.5 centimeters from the ammonia and 9.2 centimeters from the acid. The observed ratio '
               'is 1.7, compared with 1.47 predicted by Graham’s law.', b)


@fig('FR033', 'fig-11-01-dye-diffusion.svg')
def dye_diffusion():
    b = ''
    stages = [('Drop just added', 30, 0.95), ('Spreading', 70, 0.55), ('Evenly mixed', None, 0.22)]
    for i, (lab, r, op) in enumerate(stages):
        ox = 30 + i * 270
        gid = uid('dye')
        if r:
            inside = (f'<defs><radialGradient id="{gid}"><stop offset="0" stop-color="#2b59c3" stop-opacity="{op}"/>'
                      f'<stop offset="1" stop-color="#2b59c3" stop-opacity="0"/></radialGradient></defs>'
                      f'<ellipse cx="{ox + 100}" cy="{130 + r * 0.8}" rx="{r * 1.2}" ry="{r}" fill="url(#{gid})"/>')
            bk, _ = beaker(ox, 80, 200, 220, 0.85, '#eef6fb', 1, inside, marks=False)
        else:
            bk, _ = beaker(ox, 80, 200, 220, 0.85, '#9fb6e6', 1, marks=False)
        b += bk + text(ox + 100, 330, lab, 15, weight='bold')
        if i < 2:
            b += arrow(ox + 212, 190, ox + 258, 190, INK, 2, 10)
    b += path('M118,24 h24 v40 l-6,14 h-12 l-6,-14 Z', '#2b59c3', GLASS, 1.5)
    b += text(160, 50, 'dye solution', 13, anchor='start', fill=MUTED)
    b += text(410, 372, 'Qualitative sequence with no stirring; time intervals and concentrations are not to scale.', 13, fill=MUTED)
    return svg(820, 386, 'Dye diffusing in water',
               'Three beakers in sequence. First, a concentrated drop of blue dye has just entered still water. Next, '
               'the dye has spread into a larger, fainter cloud. Finally, the whole beaker is evenly pale blue.', b)


def capillary(cx, top, bottom, r, level_y, liquid, meniscus=-1, glass_w=3):
    """Vertical tube; meniscus=-1 concave (water), +1 convex (mercury)."""
    sag = r * 0.9 * meniscus
    liq = f'M{f(cx - r)},{f(bottom)} V{f(level_y)} Q{f(cx)},{f(level_y - sag * 2)} {f(cx + r)},{f(level_y)} V{f(bottom)} Z'
    s = rect(cx - r, top, 2 * r, bottom - top, GLASS_FILL, 'none', 0)
    s += path(liq, liquid, 'none', 0)
    s += line(cx - r - glass_w / 2, top, cx - r - glass_w / 2, bottom, GLASS, glass_w)
    s += line(cx + r + glass_w / 2, top, cx + r + glass_w / 2, bottom, GLASS, glass_w)
    return s


def reservoir(x, y, w, h, level_y, liquid):
    s = rect(x, level_y, w, y + h - level_y, liquid, 'none', 0)
    s += path(f'M{f(x)},{f(y)} V{f(y + h)} H{f(x + w)} V{f(y)}', 'none', GLASS, 2.4)
    return s


@fig('FR035', 'fig-11-11-capillary-rise.svg')
def capillary_rise():
    water = '#7fb8e6'
    surf = 300
    b = reservoir(40, 250, 760, 130, surf, water)
    tubes = [(130, 12), (250, 7), (360, 4)]
    hk = 480
    for cx, r in tubes:
        b += capillary(cx, 60, 360, r, surf - hk / r, water)
    b += lines(245, 36, ['Narrower tube → higher rise'], 15, weight='bold')
    # Tilted tube with the same radius as the middle tube.
    theta = math.radians(35)
    h_mid = hk / 7
    px, py = 560, 360
    L = 330
    s_top = (py - (surf - h_mid)) / math.cos(theta)
    cid = uid('tilt')
    g = f'<g transform="rotate({f(math.degrees(theta))} {px} {py})">'
    g += rect(px - 7, py - L, 14, L, GLASS_FILL, 'none', 0)
    g += path(f'M{px - 7},{py} V{f(py - s_top)} Q{px},{f(py - s_top + 10)} {px + 7},{f(py - s_top)} V{py} Z', water, 'none', 0)
    g += line(px - 8.5, py - L, px - 8.5, py, GLASS, 3) + line(px + 8.5, py - L, px + 8.5, py, GLASS, 3) + '</g>'
    b += g
    y_eq = surf - h_mid
    x_tilt = px + s_top * math.sin(theta)
    b += line(250 + 14, y_eq, x_tilt + 30, y_eq, '#c0392b', 1.6, '6 4')
    b += arrow(700, surf, 700, y_eq, '#c0392b', 1.6, 8, both=True) + text(712, (surf + y_eq) / 2 + 5, 'h', 16, anchor='start', fill='#c0392b', italic=True)
    b += line(x_tilt + 10, y_eq, 700, y_eq, '#c0392b', 1.6, '6 4')
    b += lines(530, 100, ['Tilted tube, same radius', 'as the middle tube:', 'same vertical height h'], 14, weight='bold')
    b += text(420, 408, 'Glass capillaries in water (rise exaggerated for clarity)', 13, fill=MUTED)
    b += text(60, 292, 'water', 13, anchor='start', fill='#1d4f80')
    return svg(820, 420, 'Capillary rise of water',
               'Three vertical glass capillaries of decreasing width stand in water; the water rises highest in the '
               'narrowest tube. A tilted tube with the same width as the middle tube has its water surface at the same '
               'vertical height above the reservoir, marked h.', b)


@fig('FR036', 'fig-11-12-menisci.svg')
def menisci():
    hg = '#a9b1bb'
    b = panel_label(20, 30, '(a)') + text(52, 30, 'Glass capillary in mercury', 16, anchor='start', weight='bold')
    surf = 230
    b += reservoir(40, 170, 320, 130, surf, hg)
    b += capillary(200, 60, 290, 10, surf + 40, hg, meniscus=1)
    b += line(40, surf, 360, surf, '#c0392b', 1.5, '6 4')
    b += lines(260, 120, ['Mercury level inside', 'the tube is lower'], 14, anchor='start')
    b += line(255, 125, 214, 262, MUTED, 1)
    b += text(60, 222, 'outside level', 12, anchor='start', fill='#c0392b')
    b += panel_label(420, 30, '(b)') + text(452, 30, 'Meniscus shapes in glass', 16, anchor='start', weight='bold')
    b += capillary(520, 70, 280, 34, 170, '#7fb8e6', meniscus=-1, glass_w=4)
    b += capillary(720, 70, 280, 34, 170, hg, meniscus=1, glass_w=4)
    b += lines(520, 306, ['Water: concave', 'adhesion to glass is strong'], 14)
    b += lines(720, 306, ['Mercury: convex', 'cohesion dominates'], 14)
    return svg(860, 350, 'Menisci of water and mercury',
               'Left: a glass capillary in mercury, where the mercury inside the tube stands below the outside level '
               'and has a convex surface. Right: wide glass tubes showing that water forms a concave meniscus and '
               'mercury forms a convex meniscus.', b)


def layered_tube(cx, top, layers, label):
    """layers: list of (fraction, fill, opacity, name) from top to bottom."""
    h, w = 250, 70
    inside, y = '', top + 30
    usable = h - 30
    for frac, fill, op, _ in layers:
        lh = usable * frac
        inside += rect(cx - 50, y, 100, lh + (40 if fill == layers[-1][1] else 0), fill, 'none', 0, 0, f' fill-opacity="{op}"')
        y += lh
    s, _ = test_tube(cx, top, h, w, 0, None, inside=inside)
    y = top + 30
    for frac, fill, op, name in layers:
        lh = usable * frac
        s += line(cx + w / 2 + 6, y + lh / 2, cx + w / 2 + 22, y + lh / 2, MUTED, 1)
        s += lines(cx + w / 2 + 26, y + lh / 2 - 2, name, 13, anchor='start')
        y += lh
    return s + text(cx + 40, top + h + 34, label, 15, weight='bold')


@fig('FR039', 'fig-13-05-immiscible-liquids.svg')
def immiscible():
    b = panel_label(20, 30, '(a)') + panel_label(420, 30, '(b)')
    b += layered_tube(120, 50, [(0.48, '#9b4fb0', 0.75, ['Hexane + I_2 (violet)', '0.66 g/mL']),
                                (0.52, '#e7f1f8', 1, ['Water', '1.00 g/mL'])], 'Hexane floats on water')
    b += layered_tube(520, 50, [(0.48, '#e7f1f8', 1, ['Water', '1.00 g/mL']),
                                (0.52, '#9b4fb0', 0.75, ['CCl_4 + I_2 (violet)', '1.59 g/mL'])], 'CCl_4 sinks below water')
    b += text(420, 368, 'Hexane and CCl_4 are miscible with each other, so each is shown with water in a separate tube.', 13, fill=MUTED)
    return svg(840, 382, 'Water with hexane and with carbon tetrachloride',
               'Two test tubes. In the first, a violet layer of hexane containing iodine floats on colorless water. '
               'In the second, colorless water floats on a violet layer of carbon tetrachloride containing iodine. '
               'Densities are labeled: hexane 0.66, water 1.00, and carbon tetrachloride 1.59 grams per milliliter.', b)


def crown(cx, cy, R=46):
    s = ''
    pts = [(cx + R * math.cos(2 * math.pi * k / 18 - math.pi / 2), cy + R * math.sin(2 * math.pi * k / 18 - math.pi / 2)) for k in range(18)]
    s += path('M' + ' L'.join(f'{f(x)},{f(y)}' for x, y in pts) + ' Z', 'none', INK, 1.8)
    for k, (x, y) in enumerate(pts):
        s += circle(x, y, 6 if k % 3 == 0 else 4, '#d64545' if k % 3 == 0 else '#52606d', 'none', 0)
    s += ion(cx, cy, 16, '#8e6bbf', 'K^+', size=13)
    for k in range(0, 18, 3):
        x, y = pts[k]
        s += line(x + (cx - x) * 0.2, y + (cy - y) * 0.2, cx + (x - cx) * 0.4, cy + (y - cy) * 0.4, '#8e6bbf', 1, '2 2')
    return s


@fig('FR040', 'fig-13-08-crown-ether.svg')
def crown_ether():
    b = panel_label(20, 30, '(a)') + text(52, 30, 'KMnO_4 in isopropanol', 16, anchor='start', weight='bold')
    crystals = ''.join(path(f'M{f(x)},{f(y)} l6,-8 7,5 -3,7 Z', '#3b0f3f', 'none', 0) for x, y in
                       [(92, 292), (104, 296), (116, 290), (126, 296), (100, 284), (114, 282)])
    t, _ = test_tube(112, 60, 250, 60, 0.75, '#f6f8fa', 1, crystals)
    b += t + lines(112, 340, ['Colorless liquid;', 'purple solid does not dissolve'], 14)
    b += panel_label(300, 30, '(b)') + text(332, 30, 'With a little 18-crown-6', 16, anchor='start', weight='bold')
    t2, _ = test_tube(392, 60, 250, 60, 0.75, '#a43a8f', 0.85)
    b += t2 + lines(392, 340, ['Reddish-purple solution', 'of permanganate ions'], 14)
    b += rect(540, 70, 300, 250, '#f7fafc', '#9aa5b1', 1.2, 10)
    b += crown(640, 180)
    b += text(640, 256, '[K(18-crown-6)]^+', 14, weight='bold')
    b += ion(780, 180, 22, '#8e2a8e', 'MnO_4^−', size=11)
    b += lines(690, 290, ['K^+ is held by six ether O atoms (red)'], 13, fill=MUTED)
    return svg(860, 384, 'Crown ether dissolves permanganate',
               'First tube: dark purple potassium permanganate crystals sit undissolved in colorless isopropanol. '
               'Second tube: with a little 18-crown-6 added, the liquid is reddish purple. An inset shows a potassium '
               'ion held at the center of the 18-membered crown ether ring by six oxygen atoms, beside a separate '
               'permanganate ion.', b)


@fig('FR041', 'fig-13-22-tyndall-effect.svg')
def tyndall():
    b = rect(0, 0, 860, 330, '#2d3748', 'none', 0)
    b += rect(20, 150, 70, 44, '#9aa5b1', '#cbd2d9', 1.5, 6) + text(55, 214, 'light', 13, fill='#e4e7eb')
    b += line(90, 172, 840, 172, '#fde68a', 1.2, '2 6')
    for i, (cx, colloid) in enumerate(((300, False), (620, True))):
        b += rect(cx - 70, 50, 140, 240, '#c53030', '#e2e8f0', 2, 6, ' fill-opacity="0.55"')
        if colloid:
            b += f'<defs><linearGradient id="bm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff7cc" stop-opacity="0"/>' \
                 f'<stop offset="0.5" stop-color="#fff7cc" stop-opacity="1"/><stop offset="1" stop-color="#fff7cc" stop-opacity="0"/></linearGradient></defs>'
            b += rect(cx - 70, 160, 140, 24, 'url(#bm)', 'none', 0)
            for k in range(5):
                x = cx - 50 + k * 25
                b += arrow(x, 166, x - 6, 140, '#fff7cc', 1.2, 6) + arrow(x + 8, 178, x + 14, 204, '#fff7cc', 1.2, 6)
    b += lines(300, 312, ['True solution: beam not visible'], 14, fill='#f7fafc', weight='bold')
    b += lines(620, 312, ['Colloid (with gelatin): beam scattered'], 14, fill='#f7fafc', weight='bold')
    b += text(300, 34, 'Red food coloring in water', 13, fill='#e4e7eb')
    b += text(620, 34, 'Same solution plus gelatin', 13, fill='#e4e7eb')
    b += text(430, 350, 'Dotted line marks the beam path through air and the true solution, where it is not seen from the side.', 12, fill=MUTED)
    return svg(860, 364, 'Tyndall effect',
               'A light beam crosses two cylinders of red food coloring in water. In the true solution on the left '
               'the beam cannot be seen from the side. In the cylinder on the right, which also contains gelatin, the '
               'beam is visible because the colloidal particles scatter light.', b)
