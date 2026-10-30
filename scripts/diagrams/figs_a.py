"""Chapters 1-4 replacement diagrams."""
import math

from lib import *

FIGS = {}


def fig(fid, name):
    def wrap(fn):
        FIGS[fid] = (name, fn)
        return fn
    return wrap


def particle_inset(cx, cy, r, pts, pr=7, fill='#3d7fc4'):
    cid = uid('ins')
    s = f'<defs><clipPath id="{cid}"><circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}"/></clipPath></defs>'
    s += circle(cx, cy, r, '#ffffff', MUTED, 1.5)
    s += f'<g clip-path="url(#{cid})">' + ''.join(circle(x, y, pr, fill, '#1d4f80', 1) for x, y in pts) + '</g>'
    return s


@fig('FR001', 'fig-01-06-states-of-matter.svg')
def states():
    b = ''
    # Solid: a block keeps its own shape on a surface.
    b += panel_label(30, 34, 'Solid')
    b += line(40, 220, 260, 220, MUTED, 2)
    b += path('M90,220 V140 L120,120 H220 V200 L190,220 Z', '#9db4c8', '#3e5a74', 2)
    b += path('M90,140 L120,120 H220 L190,140 Z', '#c3d3e1', '#3e5a74', 1.5)
    b += path('M190,140 L220,120 V200 L190,220 Z', '#7f9ab2', '#3e5a74', 1.5)
    b += line(90, 140, 190, 140, '#3e5a74', 1.5) + line(190, 140, 190, 220, '#3e5a74', 1.5)
    b += lines(150, 252, ['Fixed shape', 'Fixed volume'], 15)
    grid = [(110 + 19 * i, 318 + 19 * j) for i in range(5) for j in range(4)]
    b += particle_inset(148, 346, 52, grid, 8)
    b += text(148, 418, 'Particles packed in place', 13, fill=MUTED)
    # Liquid: same volume takes the shape of two different containers.
    b += panel_label(320, 34, 'Liquid')
    s1, _ = beaker(330, 120, 90, 100, 0.45, '#5aa0d8', 0.85)
    s2, _ = erlenmeyer(500, 220, 110, 130, 30, 40, 0.37, '#5aa0d8', 0.85)
    b += s1 + s2
    b += lines(440, 252, ['Takes the shape of its container', 'Fixed volume'], 15)
    liq = scatter_points(17, 396, 304, 92, 88, seed=3, minsep=17)
    b += particle_inset(440, 346, 52, liq, 8)
    b += text(440, 418, 'Particles close together, moving', 13, fill=MUTED)
    # Gas: fills whichever closed container holds it.
    b += panel_label(610, 34, 'Gas')
    for (x, y, w, h, seed) in ((625, 110, 90, 110, 5), (735, 70, 120, 150, 7)):
        b += rect(x, y, w, h, '#eaf6ea', GLASS, 2.2, 8)
        b += ''.join(circle(px, py, 3.2, '#3f8f4f', 'none', 0) for px, py in scatter_points(18, x + 8, y + 8, w - 16, h - 16, seed, 14))
    b += lines(740, 252, ['Fills the whole container', 'Volume set by the container'], 15)
    gas = scatter_points(6, 700, 306, 80, 80, seed=11, minsep=28)
    b += particle_inset(740, 346, 52, gas, 8, '#3f8f4f')
    b += text(740, 418, 'Particles far apart, moving freely', 13, fill=MUTED)
    return svg(880, 440, 'The three states of matter',
               'A solid block keeps its shape; the same liquid volume takes the shape of a beaker or a flask; '
               'a gas fills a small and a large closed container. Insets show particles packed in place, close '
               'together, and far apart.', b)


@fig('FR003', 'fig-01-08-distillation.svg')
def distillation():
    b = ''
    # Distilling flask on a burner.
    cx, cy, r = 160, 290, 70
    cid, cdef = clip(f'M{cx - 12},150 V{cy - r + 4} A{r},{r} 0 1 0 {cx + 12},{cy - r + 4} V150 Z')
    b += f'<defs>{cdef}</defs>'
    b += path(f'M{cx - 12},150 V{cy - r + 4} A{r},{r} 0 1 0 {cx + 12},{cy - r + 4} V150 Z', GLASS_FILL, 'none', 0)
    b += f'<g clip-path="url(#{cid})"><rect x="0" y="292" width="400" height="200" fill="#9ccbee"/>'
    b += ''.join(circle(x, y, 2.6, '#ffffff', '#6b8aa3', 0.8) for x, y in scatter_points(22, 100, 300, 120, 50, 4, 9))
    b += bubbles([(140, 325, 3), (175, 315, 4), (158, 300, 3)], 3) + '</g>'
    b += path(f'M{cx - 12},150 V{cy - r + 4} A{r},{r} 0 1 0 {cx + 12},{cy - r + 4} V150', 'none', GLASS, 2.2)
    b += rect(cx - 15, 130, 30, 20, '#b08968', '#6f4e37', 1.2, 3)  # stopper
    b += line(cx, 110, cx, 205, '#7b8794', 3) + circle(cx, 205, 4, '#c0392b', 'none', 0)  # thermometer
    b += burner(cx, 362)
    b += text(cx, 488, 'Heat', 15, weight='bold')
    b += line(70, 360, 250, 360, MUTED, 3)  # support ring
    # Side arm and condenser, inclined downward to the right.
    x0, y0, x1, y1 = cx + 12, 172, 600, 330
    b += line(x0, y0, x1, y1, GLASS, 9, extra=' stroke-linecap="round"')
    b += line(x0, y0, x1, y1, GLASS_FILL, 5, extra=' stroke-linecap="round"')
    ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
    b += (f'<g transform="translate(310,223) rotate({f(ang)})">' + rect(-140, -20, 280, 40, '#cfe8f7', GLASS, 2, 8) +
          line(-140, 0, 140, 0, GLASS, 8) + line(-140, 0, 140, 0, GLASS_FILL, 4) +
          ''.join(circle(-110 + 40 * k, 0, 2, '#6a9fc4', 'none', 0) for k in range(7)) + '</g>')
    # Coolant connections: in at the lower end, out at the upper end.
    b += path('M413,280 V330 H470', 'none', '#2b6cb0', 5) + arrow(470, 330, 445, 330, '#2b6cb0', 0.1, 10)
    b += path('M222,172 V112 H170', 'none', '#2b6cb0', 5)
    b += arrow(212, 112, 190, 112, '#2b6cb0', 0.1, 10)
    b += arrow(413, 285, 413, 280, '#2b6cb0', 0.1, 0.1)
    b += text(480, 336, 'Cooling water in', 14, anchor='start', fill='#2b6cb0')
    b += text(90, 100, 'Cooling water out', 14, anchor='start', fill='#2b6cb0')
    b += text(330, 170, 'Condenser', 15, weight='bold')
    # Vapor arrow in arm.
    b += arrow(250, 160, 300, 186, '#8a4fbf', 2, 9)
    b += text(278, 145, 'Water vapor', 14, fill='#8a4fbf')
    # Receiving flask with distillate drops.
    rf, _ = erlenmeyer(640, 470, 120, 120, 30, 40, 0.3, '#d6ebf7')
    b += rf
    b += path('M600,330 L628,352', 'none', GLASS, 6)
    b += circle(636, 380, 3.5, '#6aa6d6', 'none', 0) + circle(637, 405, 3, '#6aa6d6', 'none', 0)
    b += lines(640, 495, ['Receiving flask:', 'distilled water'], 15)
    b += lines(cx + 88, 300, ['Distilling flask:', 'NaCl(aq)'], 15, anchor='start')
    b += lines(cx + 88, 400, ['Salt (nonvolatile)', 'stays in the flask'], 13, anchor='start', fill=MUTED)
    b += line(cx + 85, 396, cx + 40, 335, MUTED, 1)
    return svg(780, 520, 'Distillation of salt water',
               'A burner heats salt water in a distilling flask with a thermometer. Water vapor passes into a '
               'sloping condenser cooled by water that enters at the lower end and leaves at the upper end. '
               'Condensed water drips into a receiving flask while the salt stays behind.', b)


@fig('FR005', 'fig-01-16-gas-discharge-tube.svg')
def discharge_tube():
    b = ''
    # High-voltage supply.
    b += rect(300, 30, 200, 56, '#f5f7fa', INK, 1.8, 6)
    b += text(400, 54, 'High-voltage', 15, weight='bold') + text(400, 74, 'power supply', 15, weight='bold')
    b += text(318, 108, '−', 22, weight='bold') + text(482, 108, '+', 22, weight='bold')
    b += path('M320,86 V120 H110 V200', 'none', INK, 2) + path('M480,86 V120 H690 V200', 'none', INK, 2)
    # Tube.
    b += f'<defs><linearGradient id="glow" x1="0" x2="1"><stop offset="0" stop-color="#f6c6e6"/>' \
         f'<stop offset="0.5" stop-color="#f19ad3"/><stop offset="1" stop-color="#f6c6e6"/></linearGradient></defs>'
    b += rect(90, 200, 620, 80, 'url(#glow)', GLASS, 2.5, 40)
    b += rect(110, 215, 12, 50, '#7b8794', INK, 1.2) + rect(678, 215, 12, 50, '#7b8794', INK, 1.2)
    b += line(110, 200, 110, 215, INK, 2) + line(690, 200, 690, 215, INK, 2)
    b += text(116, 310, 'Cathode (−)', 15, weight='bold') + text(684, 310, 'Anode (+)', 15, weight='bold')
    for k in range(6):
        x = 170 + k * 80
        b += arrow(x, 240, x + 44, 240, '#1f4e8c', 2, 8)
    b += text(400, 232, 'Electrons travel from cathode to anode', 14, fill='#1f4e8c')
    b += text(400, 268, 'Gas at low pressure', 14, fill='#6b2d5c', italic=True)
    # Emitted light radiating outward.
    for x, y, dx, dy in ((240, 196, -14, -40), (400, 196, 0, -44), (560, 196, 14, -40),
                         (240, 284, -14, 40), (400, 284, 0, 44), (560, 284, 14, 40)):
        b += curve_arrow(x, y, x + dx / 2 + 8, y + dy / 2, x + dx, y + dy, '#d4568f', 2, 8)
    b += text(400, 352, 'Light emitted by the excited gas', 15, fill='#a83270', weight='bold')
    return svg(800, 370, 'Gas discharge tube',
               'A sealed glass tube of low-pressure gas has a cathode at the left and an anode at the right, both '
               'wired to a high-voltage supply. Arrows inside show electrons moving from cathode to anode, and '
               'arrows outside show light emitted by the glowing gas.', b)


@fig('FR008', 'fig-03-01-one-mole-samples.svg')
def one_mole():
    b = ''
    cards = [
        ('Carbon', 'C', '12.01 g', 'atoms', 'atom'),
        ('Copper', 'Cu', '63.55 g', 'atoms', 'atom'),
        ('Water', 'H_2O', '18.02 g', 'molecules', 'water'),
        ('Sucrose', 'C_{12}H_{22}O_{11}', '342.30 g', 'molecules', 'big'),
        ('Sodium chloride', 'NaCl', '58.44 g', 'formula units', 'ionic'),
    ]
    for i, (name, formula, mass, kind, icon) in enumerate(cards):
        x = 20 + i * 172
        b += rect(x, 20, 160, 270, '#f7fafc', '#9aa5b1', 1.5, 10)
        b += text(x + 80, 50, name, 16, weight='bold') + text(x + 80, 76, formula, 16)
        cy = 135
        if icon == 'atom':
            col = '#3e4c59' if formula == 'C' else '#c46a2b'
            b += ''.join(circle(x + 52 + 19 * c + (9 if r % 2 else 0), cy - 22 + 19 * r, 9, col, '#00000040', 1)
                         for r in range(3) for c in range(3))
        elif icon == 'water':
            for dx, dy in ((-30, -18), (22, -10), (-8, 22)):
                ox, oy = x + 80 + dx, cy + dy
                b += circle(ox - 11, oy + 8, 6, '#ffffff', MUTED, 1) + circle(ox + 11, oy + 8, 6, '#ffffff', MUTED, 1)
                b += circle(ox, oy, 10, '#d64545', '#00000040', 1)
        elif icon == 'big':
            for dy in (-22, 18):
                b += rect(x + 30, cy + dy - 12, 100, 24, '#e6c97a', '#8a6d1f', 1.2, 12)
            b += text(x + 80, cy + 4, 'one molecule each', 11, fill=MUTED)
        else:
            for r in range(4):
                for c in range(4):
                    na = (r + c) % 2 == 0
                    b += circle(x + 50 + 20 * c, cy - 30 + 20 * r, 6 if na else 9, '#8e6bbf' if na else '#4caf50', '#00000040', 1)
        b += text(x + 80, 205, '1 mol = ' + mass, 16, weight='bold')
        b += text(x + 80, 232, '6.022 × 10^{23}', 15)
        b += text(x + 80, 254, kind, 15)
    b += text(440, 318, 'Each sample contains the same number of particles; the masses differ because the particles differ.',
              14, fill=MUTED)
    return svg(880, 336, 'One mole of five substances',
               'Five cards give the mass of one mole: carbon 12.01 g and copper 63.55 g of atoms, water 18.02 g and '
               'sucrose 342.30 g of molecules, and sodium chloride 58.44 g of formula units. Each mole contains '
               '6.022 × 10^23 particles.', b)


def pile(cx, base, w, h, fill, stroke):
    return path(f'M{f(cx - w / 2)},{f(base)} Q{f(cx - w / 4)},{f(base - h * 0.9)} {f(cx)},{f(base - h)} '
                f'Q{f(cx + w / 4)},{f(base - h * 0.9)} {f(cx + w / 2)},{f(base)} Z', fill, stroke, 1.5)


@fig('FR009', 'fig-03-07-ammonium-dichromate.svg')
def ammonium_dichromate():
    b = ''
    b += line(40, 200, 330, 200, MUTED, 2) + line(470, 200, 840, 200, MUTED, 2)
    b += pile(185, 200, 200, 90, '#f08a24', '#a4510f')
    b += ''.join(circle(x, y, 2, '#ffd08a', 'none', 0) for x, y in scatter_points(30, 120, 140, 130, 50, 2, 9) if y > 200 - 90 * (1 - ((x - 185) / 100) ** 2) + 6)
    b += lines(185, 232, ['(NH_4)_2Cr_2O_7(s)', 'orange solid'], 15)
    b += arrow(345, 160, 455, 160, INK, 2.5, 12) + text(400, 148, 'heat', 14, italic=True)
    b += pile(650, 200, 240, 110, '#4f7d3a', '#2f4f22')
    b += ''.join(circle(x, y, 2.2, '#8fbf6f', 'none', 0) for x, y in scatter_points(30, 560, 120, 180, 70, 6, 10) if y > 200 - 110 * (1 - ((x - 650) / 120) ** 2) + 6)
    b += lines(650, 232, ['Cr_2O_3(s)', 'green solid'], 15)
    for x, lab in ((570, 'N_2(g)'), (735, '4H_2O(g)')):
        b += curve_arrow(x, 110, x - 10, 75, x + 6, 42, '#5b6b7a', 2, 9)
        b += text(x + 10, 30, lab, 15, fill='#334e68', weight='bold')
    b += text(450, 300, '(NH_4)_2Cr_2O_7(s) → Cr_2O_3(s) + N_2(g) + 4H_2O(g)', 18, weight='bold')
    # Atom inventory.
    rows = [('N', 2, '0 + 2 + 0'), ('H', 8, '0 + 0 + 8'), ('Cr', 2, '2 + 0 + 0'), ('O', 7, '3 + 0 + 4')]
    x0 = 230
    b += text(x0, 340, 'Atom', 14, weight='bold') + text(x0 + 150, 340, 'Reactant', 14, weight='bold')
    b += text(x0 + 330, 340, 'Products (Cr_2O_3 + N_2 + 4H_2O)', 14, weight='bold')
    for i, (el, n, prod) in enumerate(rows):
        y = 364 + i * 22
        b += text(x0, y, el, 14) + text(x0 + 150, y, str(n), 14) + text(x0 + 330, y, f'{prod} = {n}', 14)
    b += line(x0 - 40, 346, x0 + 470, 346, '#9aa5b1', 1)
    b += text(450, 460, 'Heat and light are also released. Particle structure is not shown.', 13, fill=MUTED)
    return svg(900, 476, 'Ammonium dichromate decomposition',
               'An orange pile of ammonium dichromate is heated and becomes a larger green pile of chromium(III) '
               'oxide while nitrogen gas and water vapor escape. Below, the balanced equation and a table show 2 N, '
               '8 H, 2 Cr, and 7 O atoms on each side.', b)


@fig('FR010', 'fig-03-09-candle-combustion.svg')
def candle():
    b = ''
    cx = 260
    fl, _ = erlenmeyer(cx, 400, 300, 330, 70, 90, 0, None)
    b += fl
    b += rect(cx - 18, 290, 36, 108, '#f4ead5', '#a8996f', 1.5, 3)
    b += line(cx, 290, cx, 280, INK, 2) + flame(cx, 284, 46, 12)
    # Droplets on the upper inner glass.
    pts = [(cx - 30, 92), (cx - 30, 118), (cx - 30, 142), (cx + 30, 100), (cx + 30, 128), (cx + 30, 150),
           (cx - 41, 178), (cx + 43, 184), (cx - 53, 206), (cx + 55, 210)]
    b += ''.join(f'<ellipse cx="{x}" cy="{y}" rx="3.5" ry="5" fill="#9ccbee" stroke="#3d7fc4" stroke-width="1"/>' for x, y in pts)
    b += line(cx + 50, 184, 470, 140, MUTED, 1)
    b += lines(476, 130, ['Water droplets condense', 'on the cooler glass'], 15, anchor='start')
    b += curve_arrow(cx + 6, 232, cx + 30, 200, cx + 10, 160, '#5b6b7a', 1.8, 8)
    b += curve_arrow(cx - 6, 232, cx - 30, 200, cx - 10, 160, '#5b6b7a', 1.8, 8)
    b += lines(476, 236, ['Hot products rise:', 'CO_2(g) and H_2O(g)'], 15, anchor='start')
    b += line(cx + 30, 210, 470, 230, MUTED, 1)
    b += lines(476, 340, ['Candle wax', '(a hydrocarbon)'], 15, anchor='start')
    b += line(cx + 20, 340, 470, 336, MUTED, 1)
    b += text(330, 446, 'hydrocarbon + O_2(g) → CO_2(g) + H_2O(g)', 17, weight='bold')
    return svg(680, 470, 'Candle burning in a flask',
               'A lit candle stands inside a large flask. Arrows show hot carbon dioxide and water vapor rising, '
               'and water droplets have condensed on the cooler upper glass.', b)


def ion_beaker(x, y, w, h, ions, level=0.8, solid=None, liquid='#e3f1fa'):
    """Beaker with labeled ions. ions: list of (px, py, fill, label, r)."""
    inner = ''.join(ion(px, py, r, fc, lab, size=10 if len(lab) > 3 else 11) for px, py, fc, lab, r in ions)
    s, ly = beaker(x, y, w, h, level, liquid, 1, inner + (solid or ''), marks=False)
    return s


AG, NA, CL, NO3, K, CRO = '#8c96a3', '#7b5cc4', '#3f9b4f', '#d9534f', '#e08e2b', '#c0392b'


def ion_grid(x, y, w, h, specs, seed, sep=36):
    """Place a list of (fill, label, r) ions at well-separated positions."""
    pts = scatter_points(len(specs), x, y, w, h, seed, sep)
    return [(px, py, fc, lab, r) for (px, py), (fc, lab, r) in zip(pts, specs)]


@fig('FR012', 'fig-03-ex15-silver-chloride.svg')
def silver_chloride():
    b = ''
    ag = [(AG, 'Ag^+', 14)] * 4 + [(NO3, 'NO_3^−', 16)] * 4
    nacl = [(NA, 'Na^+', 14)] * 4 + [(CL, 'Cl^−', 15)] * 4
    b += ion_beaker(30, 70, 190, 190, ion_grid(52, 110, 148, 130, ag, 3))
    b += ion_beaker(260, 70, 190, 190, ion_grid(282, 110, 148, 130, nacl, 8))
    b += text(125, 290, 'AgNO_3(aq)', 16, weight='bold') + text(355, 290, 'NaCl(aq)', 16, weight='bold')
    b += arrow(470, 165, 540, 165, INK, 2.5, 12) + text(505, 150, 'mix', 14, italic=True)
    solid = path('M582,300 Q600,268 640,262 H720 Q760,268 778,300 Z', '#f1f3f5', '#9aa5b1', 1)
    for i in range(4):
        sx = 616 + i * 34
        solid += ion(sx, 288, 12, AG, 'Ag^+', size=9) + ion(sx + 14, 270, 12, CL, 'Cl^−', size=9)
    free = ion_grid(588, 120, 184, 100, [(NA, 'Na^+', 14)] * 4 + [(NO3, 'NO_3^−', 16)] * 4, 5, 40)
    b += ion_beaker(570, 60, 220, 250, free, 0.78, solid)
    b += text(680, 340, 'AgCl(s) settles; Na^+ and NO_3^− stay in solution', 15, weight='bold')
    b += line(760, 285, 812, 250, MUTED, 1) + lines(815, 240, ['white', 'AgCl(s)'], 14, anchor='start')
    b += text(430, 380, 'Ag^+(aq) + Cl^−(aq) → AgCl(s)', 18, weight='bold')
    b += text(430, 404, 'Water molecules are omitted for clarity.', 13, fill=MUTED)
    return svg(880, 420, 'Silver chloride precipitation',
               'A beaker of silver and nitrate ions and a beaker of sodium and chloride ions are mixed. In the '
               'product beaker, four silver ions and four chloride ions form white solid AgCl at the bottom, while '
               'four sodium ions and four nitrate ions remain dissolved.', b)


def bulb(cx, cy, state):
    glow = {'off': ('#f2f2f2', 0), 'dim': ('#fbe7a1', 0.35), 'bright': ('#ffd23f', 1)}[state]
    s = ''
    if glow[1]:
        s += circle(cx, cy, 34 + 14 * glow[1], '#ffe066', 'none', 0, f' fill-opacity="{0.25 + 0.2 * glow[1]}"')
        if state == 'bright':
            for k in range(8):
                a = k * math.pi / 4
                s += line(cx + 34 * math.cos(a), cy + 34 * math.sin(a), cx + 46 * math.cos(a), cy + 46 * math.sin(a), '#e0a800', 2.5)
    s += circle(cx, cy, 22, glow[0], '#6b7280', 1.8)
    s += path(f'M{cx - 8},{cy + 4} l4,-10 4,10 4,-10 4,10', 'none', '#8a6d1f', 1.5)
    s += rect(cx - 10, cy + 20, 20, 14, '#9aa5b1', '#52606d', 1.2, 2)
    return s


