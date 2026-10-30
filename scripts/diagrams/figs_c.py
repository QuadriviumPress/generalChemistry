"""Chapters 14-19 replacement diagrams."""
import math
from lib import *

FIGS = {}
NO2 = '#a0461e'


def fig(fid, name):
    def wrap(fn):
        FIGS[fid] = (name, fn)
        return fn
    return wrap


@fig('FR044', 'fig-14-03-flour-surface-area.svg')
def flour():
    b = panel_label(20, 30, 'Flour dispersed in air (left)')
    b += f'<defs><radialGradient id="fb"><stop offset="0" stop-color="#fde68a"/><stop offset="0.55" stop-color="#f59e0b" stop-opacity="0.9"/>' \
         f'<stop offset="1" stop-color="#ea580c" stop-opacity="0"/></radialGradient></defs>'
    b += f'<ellipse cx="200" cy="170" rx="150" ry="105" fill="url(#fb)"/>'
    for x, y in scatter_points(40, 90, 90, 220, 160, 5, 14):
        b += circle(x, y, 2.6, '#f8f1e4', '#8a6d1f', 0.8)
    b += burner(200, 238)
    b += lines(200, 368, ['Rapid burning: each particle', 'is surrounded by air'], 15, weight='bold')
    ox = 450
    b += panel_label(ox, 30, 'Pile of flour (right)')
    b += path(f'M{ox + 70},250 Q{ox + 130},170 {ox + 190},168 Q{ox + 250},170 {ox + 310},250 Z', '#f8f1e4', '#a8996f', 1.5)
    b += path(f'M{ox + 150},180 Q{ox + 190},166 {ox + 230},180', 'none', '#5c4033', 3)
    b += flame(ox + 190, 168, 70, 22)
    b += line(ox + 40, 250, ox + 340, 250, MUTED, 2)
    b += lines(ox + 190, 290, ['Only the exposed surface', 'is scorched'], 15, weight='bold')
    b += lines(ox + 190, 342, ['Same flour, far less surface', 'in contact with air'], 13, fill=MUTED)
    b += text(400, 418, 'Conceptual comparison, not a record of a particular experiment.', 13, fill=MUTED)
    return svg(820, 432, 'Surface area and reaction rate',
               'Left: flour sprayed into a burner flame is spread out as separate particles in air and burns as a '
               'large fireball. Right: a flame on a pile of the same flour only scorches its exposed surface.', b)


@fig('FR045', 'fig-14-04-catalysts.svg')
def catalysts():
    b = ''
    panels = [('No catalyst', '#eef6fb', 0, ['Decomposition too slow', 'to notice']),
              ('With iodide, I^−', '#c98a3b', 1, ['O_2 bubbles; brown from', 'small amounts of I_3^−']),
              ('With catalase (enzyme)', '#eef6fb', 2, ['Vigorous decomposition;', 'foam of O_2'])]
    for i, (title, col, rate, desc) in enumerate(panels):
        ox = 30 + i * 270
        b += text(ox + 100, 30, title, 16, weight='bold')
        inside = ''
        if rate == 1:
            inside = bubbles([(x, y, r) for (x, y), r in zip(scatter_points(16, ox + 30, 150, 140, 190, 3 + i, 18), [3, 4, 5] * 6)])
        elif rate == 2:
            inside = bubbles([(x, y, r) for (x, y), r in zip(scatter_points(40, ox + 20, 130, 160, 210, 8, 11), [3, 4, 5, 6] * 10)])
        cyl, ly = test_tube(ox + 100, 60, 300, 120, 0.72, col, 0.85, inside)
        b += cyl
        if rate == 2:
            b += path(f'M{ox + 40},{f(ly)} C{ox + 40},{f(ly - 45)} {ox + 70},{f(ly - 75)} {ox + 100},{f(ly - 75)} '
                      f'C{ox + 130},{f(ly - 75)} {ox + 160},{f(ly - 45)} {ox + 160},{f(ly)} Z', '#ffffff', '#9aa5b1', 1.2)
            b += ''.join(circle(x, y, 7, '#ffffff', '#cbd2d9', 1) for x, y in scatter_points(10, ox + 52, ly - 62, 96, 56, 2, 15))
        b += lines(ox + 100, 400, desc, 14)
    b += text(400, 456, '2H_2O_2(aq) → 2H_2O(l) + O_2(g)', 17, weight='bold')
    b += text(400, 480, 'Bubble amounts are qualitative, not measured rates.', 13, fill=MUTED)
    return svg(820, 494, 'Catalysts and hydrogen peroxide',
               'Three cylinders of hydrogen peroxide solution. With no catalyst nothing visible happens. With iodide '
               'the solution is brown and oxygen bubbles form. With the enzyme catalase, oxygen forms so vigorously '
               'that foam rises out of the liquid.', b)


def sealed_tube(cx, top, h, w, gas_op, liquid=None, solid=None):
    """Closed tube filled with NO2-colored gas of opacity gas_op; optional condensed phase at bottom."""
    inside = rect(cx - w, top - 10, 2 * w, h + 20, NO2, 'none', 0, 0, f' fill-opacity="{gas_op}"')
    if liquid:
        inside += rect(cx - w, top + h - liquid, 2 * w, liquid + 10, '#f4ecd8', '#c9b98f', 1)
    if solid:
        base = top + h
        inside += path(f'M{cx - w},{base} V{base - solid} L{cx - 8},{base - solid - 6} L{cx + 4},{base - solid + 2} '
                       f'L{cx + w},{base - solid - 4} V{base} Z', '#ffffff', '#9aa5b1', 1)
    s, _ = test_tube(cx, top, h, 2 * w, 0, None, inside=inside, closed=True)
    return s


def bath(x, y, w, h, fill, label):
    return rect(x, y, w, h, fill, GLASS, 2, 6, ' fill-opacity="0.8"') + text(x + w / 2, y + h + 22, label, 14, weight='bold')


@fig('FR046', 'fig-15-01-n2o4-temperature.svg')
def n2o4_temperature():
    b = ''
    states = [('Dry ice, −78 °C', '#e5e7eb', 0.0, None, 34, ['Colorless solid N_2O_4']),
              ('Warming above −9.3 °C', None, 0.25, 30, None, ['N_2O_4 melts and evaporates;', 'some vapor forms NO_2']),
              ('Room temperature', None, 0.6, None, None, ['N_2O_4(g) and NO_2(g)', 'at equilibrium'])]
    for i, (title, bathc, op, liq, sol, desc) in enumerate(states):
        cx = 130 + i * 270
        b += text(cx, 30, title, 15, weight='bold')
        if bathc:
            b += rect(cx - 70, 170, 140, 120, '#f3f4f6', GLASS, 2, 6)
            b += ''.join(rect(x, y, 16, 12, '#ffffff', '#cbd2d9', 1, 2) for x, y in scatter_points(14, cx - 64, 180, 120, 100, 3, 20))
        b += sealed_tube(cx, 60, 210, 22, op, liq, sol)
        b += lines(cx, 318 + 6, desc, 14)
        if i < 2:
            b += arrow(cx + 70, 160, cx + 200, 160, INK, 2, 10)
    b += text(400, 392, 'N_2O_4(g)', 18, weight='bold', anchor='end') + eq_arrow(410, 450, 386) + text(460, 392, '2NO_2(g)', 18, weight='bold', anchor='start')
    b += text(358, 412, 'colorless', 13, fill=MUTED) + text(498, 412, 'red-brown', 13, fill=NO2)
    return svg(800, 424, 'Dinitrogen tetroxide warming',
               'Three views of one sealed tube. In dry ice it holds colorless solid N2O4. As it warms above minus 9.3 '
               'degrees Celsius, the N2O4 melts and evaporates and the gas turns pale brown. At room temperature it '
               'holds a red-brown equilibrium mixture of N2O4 and NO2 gas.', b)


def syringe(x, y, vol, op, label):
    """Horizontal syringe; gas column length proportional to volume (15 mL = 300 px)."""
    L = vol * 20
    s = rect(x, y, 330, 60, GLASS_FILL, 'none', 0)
    s += rect(x, y + 2, L, 56, NO2, 'none', 0, 0, f' fill-opacity="{op}"')
    s += path(f'M{x + 330},{y} H{x} V{y + 60} H{x + 330}', 'none', GLASS, 2.2)
    s += path(f'M{x},{y + 22} H{x - 30} V{y + 38} H{x}', GLASS_FILL, GLASS, 2)
    s += rect(x + L, y + 4, 12, 52, '#52606d', '#1f2933', 1) + rect(x + L + 12, y + 24, 350 - L, 12, '#9aa5b1', '#52606d', 1)
    s += rect(x + 360, y - 6, 10, 72, '#9aa5b1', '#52606d', 1)
    for k in range(0, 16, 5):
        s += line(x + k * 20, y + 60, x + k * 20, y + 68, INK, 1) + text(x + k * 20, y + 82, str(k), 11)
    return s + text(x + 400, y + 36, label, 15, anchor='start', weight='bold')


@fig('FR047', 'fig-15-12-compression.svg')
def compression():
    b = ''
    rows = [('(a)', 15, 0.35, '15 mL at equilibrium'), ('(b)', 7.5, 0.7, 'Just after compression to 7.5 mL'),
            ('(c)', 7.5, 0.55, 'Later, at the new equilibrium')]
    notes = ['', 'All concentrations double; darker', 'Some NO_2 forms N_2O_4: lighter than (b),\nstill darker than (a)']
    for i, (lab, vol, op, title) in enumerate(rows):
        y = 40 + i * 120
        b += panel_label(20, y + 36, lab) + syringe(90, y, vol, op, title)
        for k, part in enumerate(notes[i].split('\n')):
            if part:
                b += text(490, y + 58 + 18 * k, part, 13, anchor='start', fill=MUTED)
    b += text(450, 420, 'Color intensity tracks the NO_2 concentration (schematic).', 13, fill=MUTED)
    return svg(900, 434, 'Compressing an N2O4 and NO2 mixture',
               'Three syringes. (a) 15 milliliters of a red-brown equilibrium mixture. (b) Immediately after '
               'compression to 7.5 milliliters the gas is darker. (c) After the system re-establishes equilibrium, it '
               'is lighter than in (b) but still darker than in (a).', b)


@fig('FR048', 'fig-15-13-temperature-shift.svg')
def temperature_shift():
    b = ''
    rows = [('Ice water', '#d6ebf7', 0.2, 'Shift toward N_2O_4: lighter'), ('Room temperature', None, 0.5, 'Reference mixture'),
            ('Boiling water', '#fbd5c5', 0.85, 'Shift toward NO_2: darker')]
    for i, (title, bathc, op, desc) in enumerate(rows):
        cx = 130 + i * 260
        if bathc:
            bk, _ = beaker(cx - 80, 130, 160, 170, 0.8, bathc, 1, marks=False)
            b += bk
            if i == 2:
                b += bubbles([(cx - 50, 250, 4), (cx + 40, 230, 5), (cx + 55, 270, 3), (cx - 30, 200, 3)])
            else:
                b += ''.join(rect(x, y, 18, 14, '#ffffff', '#9ccbee', 1, 2) for x, y in ((cx - 60, 170), (cx + 38, 182), (cx - 52, 240), (cx + 40, 256)))
        b += sealed_tube(cx, 60, 210, 20, op)
        b += text(cx, 30, title, 15, weight='bold') + text(cx, 330, desc, 14)
    b += text(400, 380, 'N_2O_4(g)', 18, weight='bold', anchor='end') + eq_arrow(410, 450, 374) + text(460, 380, '2NO_2(g)', 18, weight='bold', anchor='start')
    b += text(400, 404, 'The forward reaction is endothermic. Same tube and contents in each view.', 13, fill=MUTED)
    return svg(780, 418, 'Temperature and the N2O4 equilibrium',
               'One sealed tube of N2O4 and NO2 shown in ice water, at room temperature, and in boiling water. The gas '
               'is pale in ice water, red-brown at room temperature, and darkest in boiling water.', b)


INDICATORS = [  # name, [(pH, color)] stops
    ('Thymol blue', [(1.2, '#d7301f'), (2.8, '#f2d22e'), (8.0, '#f2d22e'), (9.6, '#2b6cb0')]),
    ('Bromophenol blue', [(3.0, '#f2d22e'), (4.6, '#2b6cb0')]),
    ('Methyl red', [(4.8, '#d7301f'), (6.0, '#f2d22e')]),
    ('Bromocresol purple', [(5.2, '#f2d22e'), (6.8, '#7b3294')]),
    ('Bromothymol blue', [(6.0, '#f2d22e'), (7.6, '#2b6cb0')]),
    ('Phenol red', [(6.6, '#f2d22e'), (8.0, '#d7301f')]),
    ('Phenolphthalein', [(8.2, '#f7f7f7'), (10.0, '#e0218a')]),
]


@fig('FR049', 'fig-16-opener-indicators.svg')
def indicators():
    x0, w, lo, hi = 190, 620, 1, 10
    b = ''
    for i, (name, stops) in enumerate(INDICATORS):
        y = 20 + i * 44
        gid = uid('ind')
        b += f'<defs><linearGradient id="{gid}" x1="{x0}" x2="{x0 + w}" gradientUnits="userSpaceOnUse">'
        b += ''.join(f'<stop offset="{f((p - lo) / (hi - lo))}" stop-color="{c}"/>' for p, c in stops) + '</linearGradient></defs>'
        b += rect(x0, y, w, 30, f'url(#{gid})', '#9aa5b1', 1, 4)
        b += text(x0 - 12, y + 20, name, 14, anchor='end', weight='bold')
    yb = 20 + len(INDICATORS) * 44
    for p in range(lo, hi + 1):
        px = x0 + (p - lo) / (hi - lo) * w
        b += line(px, yb - 6, px, yb + 2, INK, 1.2) + text(px, yb + 18, str(p), 13)
    b += text(x0 + w / 2, yb + 40, 'pH', 14, weight='bold')
    b += text(430, yb + 64, 'Transition ranges follow Figure 16.23; colors are approximate.', 12, fill=MUTED)
    return svg(840, yb + 78, 'Indicator colors from pH 1 to 10',
               'Seven color bars across pH 1 to 10. Thymol blue changes red to yellow near pH 1.2 to 2.8 and yellow '
               'to blue near 8.0 to 9.6. Bromophenol blue goes yellow to blue, methyl red red to yellow, bromocresol '
               'purple yellow to purple, bromothymol blue yellow to blue, phenol red yellow to red, and phenolphthalein '
               'colorless to pink, each over its own range.', b)


def octahedron(cx, cy, ligands, metal='Cu^{2+}'):
    """ligands: axial top, axial bottom, then four equatorial (back-left, back-right, front-right, front-left)."""
    pos = [(0, -70), (0, 70), (-50, -18), (50, -18), (60, 22), (-60, 22)]
    s = ''
    for (dx, dy), lab in zip(pos, ligands):
        s += line(cx, cy, cx + dx, cy + dy, INK, 2)
    for (dx, dy), lab in zip(pos, ligands):
        col = '#3d7fc4' if lab.startswith('NH') else '#d64545'
        s += circle(cx + dx, cy + dy, 17, '#ffffff', col, 2) + text(cx + dx, cy + dy + 4, lab, 10, weight='bold', fill=col)
    return s + circle(cx, cy, 16, '#2f6db5', '#1d4f80', 1) + text(cx, cy + 4, metal, 10, weight='bold', fill='#ffffff')


@fig('FR053', 'fig-17-04-copper-ammonia.svg')
def copper_ammonia():
    b = ''
    bk, _ = beaker(40, 40, 170, 170, 0.75, '#9fd0f0', 1, marks=False)
    b += bk + text(125, 236, 'CuSO_4(aq): pale blue', 14, weight='bold')
    bk, _ = beaker(500, 40, 170, 170, 0.75, '#2f3fa8', 1, marks=False)
    b += bk + text(585, 236, 'After NH_3(aq): deep blue-violet', 14, weight='bold')
    b += arrow(250, 125, 460, 125, INK, 2.5, 12) + text(355, 112, '+ NH_3(aq)', 15, weight='bold')
    b += lines(355, 150, ['NH_3 replaces four', 'equatorial H_2O ligands'], 13, fill=MUTED)
    b += octahedron(125, 350, ['H_2O'] * 6) + text(125, 450, '[Cu(H_2O)_6]^{2+}', 15, weight='bold')
    b += octahedron(585, 350, ['H_2O', 'H_2O', 'NH_3', 'NH_3', 'NH_3', 'NH_3'])
    b += text(585, 450, '[Cu(NH_3)_4(H_2O)_2]^{2+}', 15, weight='bold')
    b += text(585, 470, 'often written [Cu(NH_3)_4]^{2+}', 13, fill=MUTED)
    b += text(355, 498, 'Schematic colors; the two axial positions keep H_2O ligands.', 12, fill=MUTED)
    return svg(720, 510, 'Copper complex ion formation',
               'A pale blue copper(II) sulfate solution turns deep blue-violet when aqueous ammonia is added. Below, '
               'the hexaaquacopper(II) ion has six water ligands, and in the ammine complex four ammonia molecules '
               'replace the four equatorial water ligands while two axial water ligands remain.', b)


@fig('FR054', 'fig-17-09-chromium-hydroxide.svg')
def chromium_hydroxide():
    b = ''
    susp = ''.join(circle(x, y, 2.4, '#5b4a6b', 'none', 0) for x, y in scatter_points(70, 330, 110, 140, 110, 3, 7))
    specs = [(40, '#7b4fa8', 0.75, '', ['Violet [Cr(H_2O)_6]^{3+}(aq)'], '+ 6 M H_2SO_4'),
             (310, '#8c7a8f', 0.6, susp, ['Cr(OH)_3(s) suspension', '(brownish purple)'], ''),
             (580, '#3f8f4f', 0.75, '', ['Green [Cr(OH)_4]^−(aq)'], '+ 6 M NaOH')]
    for x, col, op, inside, lab, reagent in specs:
        bk, _ = beaker(x, 70, 180, 170, 0.75, col, op, inside, marks=False)
        b += bk + lines(x + 90, 266, lab, 14, weight='bold')
    b += arrow(300, 150, 232, 150, INK, 2.5, 12) + text(266, 134, '+ acid', 14, weight='bold')
    b += arrow(500, 150, 568, 150, INK, 2.5, 12) + text(534, 134, '+ base', 14, weight='bold')
    b += text(130, 40, '6 M H_2SO_4 added', 13, fill=MUTED) + text(400, 40, 'Starting suspension', 13, fill=MUTED)
    b += text(670, 40, '6 M NaOH added', 13, fill=MUTED)
    b += text(400, 330, 'Cr(OH)_3(s) + 3H_3O^+(aq) → [Cr(H_2O)_6]^{3+}(aq)', 15)
    b += text(400, 356, 'Cr(OH)_3(s) + OH^−(aq) → [Cr(OH)_4]^−(aq)', 15)
    b += text(400, 384, 'Amphoteric: dissolves in both acid and base. Colors are schematic.', 13, fill=MUTED)
    return svg(800, 398, 'Amphoteric chromium(III) hydroxide',
               'A center beaker holds a brownish purple suspension of chromium(III) hydroxide. Adding sulfuric acid '
               'gives a violet solution of hexaaquachromium(III) ions, and adding sodium hydroxide gives a green '
               'solution of tetrahydroxochromate(III) ions.', b)


def box(x, y, w, h, rows, fill='#f7fafc', size=13):
    s = rect(x, y, w, h, fill, '#9aa5b1', 1.3, 8)
    top = y + h / 2 - (len(rows) - 1) * size * 0.65 + size * 0.35
    return s + lines(x + w / 2, top, rows, size, gap=size * 1.3)


def small_tube(cx, top, liquid, ppt=None):
    inside = ''
    if ppt:
        inside = path(f'M{cx - 20},{top + 130} Q{cx},{top + 104} {cx + 20},{top + 130} V{top + 150} H{cx - 20} Z', ppt, '#52606d', 1)
    s, _ = test_tube(cx, top, 140, 34, 0.6, liquid, 1, inside)
    return s


@fig('FR055', 'fig-17-11-qualitative-analysis.svg')
def qual_analysis():
    b = box(300, 10, 300, 52, ['Solution containing Ag^+, Pb^{2+}, and Hg_2^{2+}', '(with other cations)'])
    b += arrow(450, 62, 450, 98, INK, 2, 9) + text(460, 86, '+ 6 M HCl', 13, anchor='start', weight='bold')
    b += panel_label(300, 120, '(a)')
    b += small_tube(380, 100, '#eef6fb', '#f4f5f7')
    b += box(420, 118, 240, 68, ['White precipitate:', 'AgCl, PbCl_2, Hg_2Cl_2'])
    # Branch 1: hot water extracts PbCl2.
    b += path('M380,250 V280 H160 V300', 'none', INK, 2) + arrowhead(160, 304, math.pi / 2)
    b += lines(262, 250, ['hot water dissolves PbCl_2;', 'then + Na_2CrO_4'], 13)
    b += panel_label(60, 330, '(b)') + small_tube(160, 310, '#fff7d6', '#f2c200')
    b += box(200, 330, 180, 56, ['Yellow PbCrO_4(s)', 'confirms Pb^{2+}'])
    # Branch 2: a second portion of the precipitate with ammonia.
    b += path('M380,250 V280 H600 V300', 'none', INK, 2) + arrowhead(600, 304, math.pi / 2)
    b += lines(492, 250, ['second portion of precipitate', '+ NH_3(aq)'], 13)
    b += panel_label(500, 330, '(c)') + small_tube(600, 310, '#eef6fb', '#2d2d2d')
    b += box(640, 316, 250, 84, ['Black solid: Hg(l) + Hg(NH_2)Cl(s)', 'Solution: [Ag(NH_3)_2]^+(aq)'], size=12)
    b += path('M600,460 V490 H760 V505', 'none', INK, 2) + arrowhead(760, 509, math.pi / 2)
    b += text(620, 484, 'decant solution; + HCl', 13, anchor='start')
    b += panel_label(660, 540, '(d)') + small_tube(760, 512, '#eef6fb', '#f4f5f7')
    b += box(800, 530, 140, 56, ['White AgCl(s)', 'confirms Ag^+'])
    b += text(330, 690, 'Schematic flowchart; precipitate colors are representative.', 13, fill=MUTED)
    return svg(960, 706, 'Separating group 1 cations',
               'Flowchart. Adding 6 M HCl to a solution containing silver, lead, and mercury(I) ions gives a white '
               'precipitate of AgCl, PbCl2, and Hg2Cl2 (a). Hot water dissolves PbCl2, and sodium chromate then '
               'gives yellow PbCrO4 (b). Aqueous ammonia added to a second portion of the precipitate leaves a black '
               'solid of mercury and Hg(NH2)Cl and dissolves silver as the diammine complex (c). Adding HCl to the '
               'decanted solution reprecipitates white AgCl (d).', b)


@fig('FR056', 'fig-18-06-endothermic.svg')
def endothermic():
    b = ''
    slush = ''.join(circle(x, y, 4, '#ffffff', '#b8c4cf', 1) for x, y in scatter_points(40, 150, 210, 180, 60, 2, 9))
    fl, _ = erlenmeyer(240, 300, 220, 220, 50, 70, 0.4, '#e9eef3', 1, slush)
    b += fl
    b += path('M110,300 H370 V318 H110 Z', '#dbeafe', '#7fa9d6', 1.2)
    b += rect(60, 318, 360, 60, '#c69c6d', '#7c5a35', 1.5, 4)
    for k in range(5):
        b += line(70, 330 + k * 10, 410, 330 + k * 10, '#a77d4f', 0.8)
    b += line(372, 309, 460, 300, MUTED, 1) + lines(466, 296, ['Water under the flask', 'freezes; flask sticks', 'to the wood'], 14, anchor='start')
    for x, y, x2, y2 in ((70, 170, 132, 210), (410, 170, 348, 210), (90, 260, 140, 268), (395, 262, 345, 268)):
        b += arrow(x, y, x2, y2, '#c0392b', 2.2, 10)
    b += lines(466, 160, ['Heat flows from the', 'surroundings into', 'the reaction mixture'], 14, anchor='start', fill='#c0392b')
    b += line(320, 240, 460, 230, MUTED, 1) + lines(466, 236, ['Slushy solid forms', 'as the mixture cools'], 14, anchor='start')
    b += text(320, 418, 'Ba(OH)_2·8H_2O(s) + 2NH_4SCN(s) → Ba(SCN)_2(aq) + 2NH_3(aq) + 10H_2O(l)', 15, weight='bold')
    b += text(320, 442, 'ΔH > 0 (endothermic), yet the reaction is spontaneous.', 14)
    return svg(660, 460, 'A spontaneous endothermic reaction',
               'A flask of barium hydroxide and ammonium thiocyanate sits on a wet wooden block. Arrows show heat '
               'flowing from the surroundings into the flask, the mixture becomes a slush, and the water under the '
               'flask freezes it to the wood.', b)


SUITS = [('♠', INK), ('♥', '#c53030'), ('♦', '#c53030'), ('♣', INK)]
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def card_row(x, y, cards):
    s = ''
    for k, (r, si) in enumerate(cards):
        sym, col = SUITS[si]
        cx = x + k * 37
        s += rect(cx, y, 34, 48, '#ffffff', '#9aa5b1', 1, 4)
        s += text(cx + 17, y + 20, r, 13, weight='bold', fill=col) + text(cx + 17, y + 40, sym, 15, fill=col)
    return s


@fig('FR057', 'fig-18-07-playing-cards.svg')
def playing_cards():
    b = panel_label(20, 30, 'New, unshuffled deck: one particular order')
    b += card_row(20, 46, [(r, 0) for r in RANKS] + [(RANKS[0], 1), (RANKS[1], 1), (RANKS[2], 1)])
    b += text(630, 76, '… rest in suit order', 14, anchor='start')
    b += text(20, 124, 'This single arrangement is one microstate.', 14, anchor='start', fill=MUTED)
    b += panel_label(20, 170, 'Shuffled deck: any one of 52! possible orders')
    state = 7
    for row in range(3):
        cards = []
        for _ in range(16):
            state = (state * 1103515245 + 12345) % 2 ** 31
            cards.append((RANKS[state % 13], (state >> 8) % 4))
        y = 186 + row * 62
        b += card_row(20, y, cards) + text(630, y + 30, f'… one possible order', 14, anchor='start', fill=MUTED)
    b += text(20, 392, '52! ≈ 8 × 10^{67} ≈ 10^{68} possible orders. Each specific order is one microstate;', 15, anchor='start', weight='bold')
    b += text(20, 414, 'a randomly shuffled deck could be in any of them.', 15, anchor='start', weight='bold')
    return svg(820, 430, 'Ordered and shuffled playing cards',
               'Top: a new deck in suit order, ace through king of spades followed by hearts. This one arrangement is a '
               'single microstate. Bottom: three different random sequences, each one of 52 factorial, about 8 times '
               '10 to the 67th, possible orders.', b)


@fig('FR058', 'fig-19-02-zinc-copper-sulfate.svg')
def zinc_copper():
    b = ''
    deposit = ''.join(circle(x, y, 2.4, '#1f1f1f', 'none', 0) for x, y in scatter_points(50, 176, 130, 48, 160, 5, 5))
    bk, ly = beaker(80, 60, 240, 250, 0.75, '#6fa8dc', 0.9, marks=False)
    b += bk + rect(188, 30, 24, 260, '#b8c0c8', '#52606d', 1.4, 2) + deposit
    b += line(226, 200, 360, 160, MUTED, 1) + lines(366, 150, ['Zinc strip coated', 'with fine black Cu particles'], 14, anchor='start')
    b += lines(200, 340, ['Cu^{2+}(aq) in a single beaker'], 14, weight='bold')
    ox = 470
    b += rect(ox, 200, 330, 120, '#f5f9fc', '#9aa5b1', 1.2, 8)
    b += rect(ox + 14, 210, 70, 100, '#b8c0c8', '#52606d', 1)
    b += text(ox + 49, 300, 'Zn(s)', 13, weight='bold')
    b += ion(ox + 150, 236, 15, '#7b8794', 'Zn^{2+}', size=10) + arrow(ox + 86, 236, ox + 133, 236, '#52606d', 1.5, 8)
    b += circle(ox + 92, 284, 7, '#1f1f1f', 'none', 0) + ion(ox + 200, 284, 15, '#2f6db5', 'Cu^{2+}', size=10)
    b += arrow(ox + 184, 284, ox + 102, 284, '#2f6db5', 1.5, 8)
    b += text(ox + 260, 240, 'Zn loses 2e^−', 12) + text(ox + 260, 288, 'Cu^{2+} gains 2e^−', 12, fill='#2f6db5')
    b += text(ox + 165, 190, 'Electrons transfer directly at the zinc surface', 13, weight='bold')
    b += text(400, 380, 'Zn(s) + Cu^{2+}(aq) → Zn^{2+}(aq) + Cu(s)', 18, weight='bold')
    b += text(400, 404, 'One compartment, no external circuit; compare the separated half-cells of Figure 19.3.', 13, fill=MUTED)
    return svg(820, 418, 'Zinc in copper(II) sulfate',
               'A zinc strip stands in blue copper(II) sulfate solution in one beaker and becomes coated with fine '
               'black copper particles. A particle view shows zinc atoms leaving as zinc ions while copper(II) ions '
               'gain electrons directly at the zinc surface and deposit as copper.', b)


@fig('FR059', 'fig-19-galvanic-cell.svg')
def galvanic():
    b = ''
    bk, _ = beaker(60, 170, 220, 200, 0.75, '#e6ebf0', 1, marks=False)
    b += bk
    bk, _ = beaker(560, 170, 220, 200, 0.75, '#6fa8dc', 0.9, marks=False)
    b += bk
    b += rect(158, 120, 24, 220, '#b8c0c8', '#52606d', 1.4, 2) + rect(658, 120, 24, 220, '#c4773b', '#7a4a23', 1.4, 2)
    # Salt bridge.
    b += path('M240,330 V150 Q240,110 280,110 H560 Q600,110 600,150 V330', 'none', GLASS, 34, ' stroke-linejoin="round"')
    b += path('M240,330 V150 Q240,110 280,110 H560 Q600,110 600,150 V330', 'none', '#f4ecd8', 28)
    b += arrow(480, 104, 360, 104, '#3d7fc4', 2, 8) + arrow(360, 117, 480, 117, '#c0392b', 2, 8)
    b += text(420, 172, 'Salt bridge (e.g., KNO_3 or Na_2SO_4)', 14, weight='bold')
    b += text(420, 198, 'anions move toward the Zn compartment', 13, fill='#3d7fc4')
    b += text(420, 220, 'cations move toward the Cu compartment', 13, fill='#c0392b')
    # External circuit with voltmeter.
    b += path('M170,120 V40 H380', 'none', INK, 2) + path('M460,40 H670 V120', 'none', INK, 2)
    b += circle(420, 40, 30, '#ffffff', INK, 2) + text(420, 47, 'V', 20, weight='bold')
    b += arrow(220, 26, 320, 26, '#1d4f80', 2, 9) + arrow(520, 26, 620, 26, '#1d4f80', 2, 9)
    b += text(270, 18, 'e^−', 14, fill='#1d4f80', weight='bold') + text(570, 18, 'e^−', 14, fill='#1d4f80', weight='bold')
    b += lines(170, 400, ['Anode: Zn(s) in Zn^{2+}(aq)', 'Zn(s) → Zn^{2+}(aq) + 2e^−'], 14)
    b += lines(670, 400, ['Cathode: Cu(s) in Cu^{2+}(aq)', 'Cu^{2+}(aq) + 2e^− → Cu(s)'], 14)
    return svg(840, 446, 'Galvanic cell with a salt bridge',
               'A zinc electrode in zinc ion solution and a copper electrode in copper(II) ion solution are joined by '
               'a wire through a voltmeter and by a salt bridge. Electrons flow through the wire from zinc to copper; '
               'in the salt bridge, anions move toward the zinc compartment and cations toward the copper compartment.', b)


@fig('FR060', 'fig-19-08-dichromate-iodide.svg')
def dichromate_iodide():
    b = ''
    bk, _ = beaker(30, 60, 150, 150, 0.7, '#f2b134', 0.95, marks=False)
    b += bk + lines(105, 236, ['Na_2Cr_2O_7(aq)', 'yellow'], 14)
    b += text(205, 140, '+', 26, weight='bold')
    bk, _ = beaker(230, 60, 150, 150, 0.7, '#f3f6f8', 1, marks=False)
    b += bk + lines(305, 236, ['NaI(aq)', 'colorless'], 14)
    b += arrow(400, 135, 470, 135, INK, 2.5, 12) + text(435, 120, 'acidic', 12, italic=True)
    bk, _ = beaker(490, 40, 200, 180, 0.72, '#8a4b14', 0.9, marks=False)
    b += bk + lines(590, 246, ['Deep amber mixture:', 'green Cr^{3+}(aq) and brown I_2(aq)'], 14)
    b += text(360, 314, 'Electron transfer', 15, weight='bold')
    b += text(360, 338, 'I^− loses electrons (oxidized) → I_2', 14)
    b += text(360, 360, 'Cr in Cr_2O_7^{2−} (+6) gains electrons (reduced) → Cr^{3+} (+3)', 14)
    b += text(360, 386, 'Colors are schematic.', 12, fill=MUTED)
    return svg(720, 400, 'Dichromate and iodide',
               'A yellow sodium dichromate solution and a colorless sodium iodide solution are combined under acidic '
               'conditions to give a deep amber mixture containing green chromium(III) and brown iodine. Iodide is '
               'oxidized to iodine and chromium is reduced from +6 to +3.', b)
