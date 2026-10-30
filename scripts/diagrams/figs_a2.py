"""Chapter 4 replacement diagrams (continued)."""
from lib import *
from figs_a import FIGS, fig, bulb, ion_beaker, ion_grid, AG, NO3, K, CRO


@fig('FR014', 'fig-04-04-electrolyte-conductivity.svg')
def conductivity():
    b = ''
    panels = [('(a)', 'Nonelectrolyte', 'solute molecules only', 'off', 'Almost no current: bulb off'),
              ('(b)', 'Weak electrolyte', 'mostly molecules, a few ions', 'dim', 'Some current: bulb dim'),
              ('(c)', 'Strong electrolyte', 'dissociated into ions', 'bright', 'More current: bulb bright')]
    for i, (lab, name, sub, state, result) in enumerate(panels):
        ox = 15 + i * 290
        b += panel_label(ox, 28, lab) + text(ox + 34, 28, name, 16, anchor='start', weight='bold')
        b += text(ox + 130, 50, sub, 13, fill=MUTED)
        # Battery, lamp, and two electrodes in series.
        b += rect(ox + 30, 78, 50, 28, '#e4e7eb', INK, 1.5, 3) + text(ox + 55, 97, '+ −', 14, weight='bold')
        b += bulb(ox + 200, 96, state)
        b += path(f'M{ox + 80},92 H{ox + 178}', 'none', INK, 2)
        b += path(f'M{ox + 30},92 H{ox + 12} V140 H{ox + 72} V165', 'none', INK, 2)
        b += path(f'M{ox + 200},130 V140 H{ox + 188} V165', 'none', INK, 2)
        if state == 'off':
            parts = ['mol'] * 8
        elif state == 'dim':
            parts = ['mol'] * 7 + ['+', '−']
        else:
            parts = ['+'] * 8 + ['−'] * 8
        pts = scatter_points(len(parts), ox + 92, 222, 80, 125, 17 + 5 * i, 24)
        inner = ''
        for (px, py), kind in zip(pts, parts):
            if kind == 'mol':
                inner += f'<ellipse cx="{f(px)}" cy="{f(py)}" rx="12" ry="7.5" fill="#b8c4cf" stroke="#52606d" stroke-width="1"/>'
            else:
                inner += ion(px, py, 9, '#d9534f' if kind == '+' else '#3d7fc4', kind, size=14)
        bk, _ = beaker(ox + 30, 175, 200, 190, 0.85, '#e3f1fa', 1, inner, marks=False)
        b += bk
        b += rect(ox + 66, 165, 12, 170, '#7b8794', INK, 1) + rect(ox + 182, 165, 12, 170, '#7b8794', INK, 1)
        b += text(ox + 130, 395, result, 14, weight='bold')
    b += text(450, 422, 'Same circuit and solute amount in each panel; brightness is qualitative.', 13, fill=MUTED)
    return svg(890, 440, 'Electrolytes and conductivity',
               'Three identical circuits each contain a battery, a light bulb, and two electrodes in a beaker. '
               'With a nonelectrolyte the beaker holds only neutral molecules and the bulb is off. With a weak '
               'electrolyte it holds mostly molecules and one ion pair, and the bulb glows dimly. With a strong '
               'electrolyte it holds only ions, and the bulb shines brightly.', b)


def ampul(cx, top, color):
    return test_tube(cx, top, 190, 46, 0.72, color, 0.95, closed=True)[0]


@fig('FR015', 'fig-04-ex08-breathalyzer.svg')
def breathalyzer():
    b = ''
    b += panel_label(60, 30, '(a) Before') + panel_label(470, 30, '(b) After')
    b += ampul(140, 70, '#f2a33a')
    b += ampul(560, 70, '#6aa84f')
    b += lines(140, 298, ['Cr_2O_7^{2−} (Cr^{6+})', 'yellow-orange'], 15)
    b += lines(560, 298, ['Cr^{3+}', 'green'], 15)
    b += arrow(220, 160, 480, 160, INK, 2.5, 12)
    b += lines(350, 110, ['Breath containing ethanol', 'is bubbled through'], 14)
    b += lines(350, 190, ['CH_3CH_2OH → CH_3COOH', '(ethanol oxidized)'], 14)
    b += lines(350, 236, ['Cr^{6+} → Cr^{3+}', '(chromium reduced)'], 14)
    b += text(350, 350, 'Schematic of the historical dichromate test; colors are qualitative.', 13, fill=MUTED)
    return svg(700, 370, 'Breathalyzer color change',
               'Two sealed ampuls. Before, the dichromate solution is yellow-orange. After breath containing ethanol '
               'is bubbled through it, ethanol is oxidized to acetic acid, chromium(VI) is reduced to chromium(III), '
               'and the solution is green.', b)


@fig('FR016', 'fig-04-11-silver-dichromate.svg')
def silver_dichromate():
    b = ''
    ag = [(AG, 'Ag^+', 14)] * 4 + [(NO3, 'NO_3^−', 16)] * 4
    kd = [(K, 'K^+', 13)] * 4 + [(CRO, 'Cr_2O_7^{2−}', 22)] * 2
    b += ion_beaker(30, 70, 190, 190, ion_grid(52, 110, 148, 130, ag, 3))
    b += ion_beaker(260, 70, 190, 190, ion_grid(285, 112, 140, 126, kd, 21, 46))
    b += text(125, 290, 'AgNO_3(aq)', 16, weight='bold') + text(355, 290, 'K_2Cr_2O_7(aq)', 16, weight='bold')
    b += arrow(470, 165, 540, 165, INK, 2.5, 12) + text(505, 150, 'mix', 14, italic=True)
    solid = path('M580,300 Q598,250 640,244 H722 Q762,250 780,300 Z', '#b3412e', '#7a2417', 1)
    for sx in (640, 720):
        solid += ion(sx, 270, 18, CRO, 'Cr_2O_7^{2−}', size=8)
        solid += ion(sx - 26, 288, 11, AG, 'Ag^+', size=8) + ion(sx + 26, 288, 11, AG, 'Ag^+', size=8)
    free = ion_grid(588, 112, 184, 110, [(K, 'K^+', 13)] * 4 + [(NO3, 'NO_3^−', 16)] * 4, 9, 40)
    b += ion_beaker(570, 60, 220, 250, free, 0.78, solid)
    b += line(770, 280, 812, 250, MUTED, 1) + lines(815, 238, ['red', 'Ag_2Cr_2O_7(s)'], 14, anchor='start')
    b += text(680, 340, 'K^+ and NO_3^− remain in solution', 15, weight='bold')
    b += text(450, 380, '2Ag^+(aq) + Cr_2O_7^{2−}(aq) → Ag_2Cr_2O_7(s)', 18, weight='bold')
    b += text(450, 404, 'Water molecules are omitted for clarity. Each dichromate ion stays intact.', 13, fill=MUTED)
    return svg(900, 420, 'Silver dichromate precipitation',
               'A beaker of silver and nitrate ions is mixed with a beaker of potassium and dichromate ions. In the '
               'product beaker, four silver ions and two dichromate ions form a red solid at the bottom, while four '
               'potassium ions and four nitrate ions remain dissolved.', b)


@fig('FR019', 'fig-04-14-acid-carbonate.svg')
def acid_carbonate():
    b = ''
    inner = bubbles([(x, y, r) for (x, y), r in zip(scatter_points(24, 130, 200, 200, 125, 4, 16), [3, 4, 5, 3, 6] * 6)])
    bk, ly = beaker(110, 120, 240, 220, 0.72, '#e3f1fa', 1, inner)
    b += bk
    b += bubbles([(170, 184, 5), (250, 182, 6), (300, 185, 4), (210, 186, 4)])
    for x in (160, 230, 290):
        b += curve_arrow(x, 140, x - 10, 110, x + 4, 76, '#5b6b7a', 1.8, 8)
    b += text(230, 62, 'CO_2(g) escapes', 15, weight='bold', fill='#334e68')
    # Dropper adding acid.
    b += path('M410,40 h28 v70 l-8,40 h-12 l-8,-40 Z', '#eef4f8', GLASS, 2) + rect(408, 14, 32, 28, '#c05746', '#7a2e22', 1.2, 8)
    b += path('M414,110 l-2,0', 'none', GLASS, 1)
    b += f'<ellipse cx="424" cy="172" rx="4" ry="6" fill="#bcd9f0" stroke="#3d7fc4"/>'
    b += curve_arrow(424, 182, 400, 200, 340, 210, MUTED, 1.4, 7, '4 3')
    b += lines(460, 70, ['Dilute HNO_3(aq)', 'added'], 15, anchor='start')
    b += lines(370, 300, ['Na_2CO_3(aq)'], 15, anchor='start')
    b += text(300, 395, '2HNO_3(aq) + Na_2CO_3(aq) → 2NaNO_3(aq) + H_2O(l) + CO_2(g)', 17, weight='bold')
    return svg(600, 420, 'Nitric acid and sodium carbonate',
               'Dilute nitric acid is dropped into a beaker of sodium carbonate solution. Many bubbles form in the '
               'solution, and arrows show carbon dioxide gas escaping.', b)


@fig('FR020', 'fig-04-16-ph-paper-meter.svg')
def ph_paper_meter():
    b = ''
    b += panel_label(30, 30, 'pH paper') + panel_label(470, 30, 'pH meter')
    chart = ['#d7301f', '#f26b2a', '#f7a43b', '#f2d649', '#c9d94e']
    for k, c in enumerate(chart):
        x = 40 + k * 66
        b += rect(x, 70, 56, 40, c, '#52606d', 1, 4) + text(x + 28, 130, str(k + 1), 15, weight='bold')
    b += text(200, 156, 'Reference chart (schematic colors)', 13, fill=MUTED)
    b += rect(150, 190, 22, 150, '#f4efe4', '#8a8170', 1.2, 2) + rect(150, 196, 22, 36, '#e5522a', '#8a8170', 1, 1)
    b += arrow(176, 210, 136, 116, MUTED, 1.5, 8, '4 3')
    b += lines(196, 270, ['Test strip matches', 'the chart near pH 2'], 15, anchor='start')
    b += text(200, 356, 'Approximate value by color comparison', 14, weight='bold')
    # Meter.
    b += rect(480, 70, 220, 130, '#e4e7eb', INK, 2, 12) + rect(500, 88, 180, 66, '#cfe8c6', '#3e4c59', 1.5, 4)
    b += text(590, 140, '1.70', 44, weight='bold', extra=' font-family="Menlo, Consolas, monospace"')
    b += text(590, 182, 'pH', 15, weight='bold')
    b += path('M590,200 C590,240 640,240 640,270 V300', 'none', INK, 2.5)
    bk, _ = beaker(590, 300, 100, 80, 0.6, '#f6d0c8', 1, marks=False)
    b += bk + rect(628, 296, 24, 74, '#dfe7ee', GLASS, 1.8, 10)
    b += text(560, 356, 'Numerical reading', 14, weight='bold', anchor='end')
    b += text(560, 376, 'to 0.01 pH unit', 14, anchor='end')
    return svg(740, 400, 'pH paper and a pH meter',
               'Left: a pH test strip compared with a reference chart of five schematic colors numbered 1 to 5; the '
               'strip matches the color near pH 2. Right: a pH meter whose probe is in a sample beaker displays a '
               'reading of 1.70.', b)


@fig('FR021', 'fig-04-21-copper-silver-nitrate.svg')
def copper_silver():
    b = ''

    def coil(cx, top, silver):
        s = line(cx, top - 20, cx, top + 20, '#b87333', 5)
        for k in range(7):
            y = top + 30 + k * 22
            s += f'<ellipse cx="{cx}" cy="{y}" rx="34" ry="9" fill="none" stroke="#b87333" stroke-width="5"/>'
            if silver:
                s += ''.join(path(f'M{f(cx + dx)},{f(y + 4)} l-4,-9 4,4 4,-6 2,8', '#c9ced6', '#6b7280', 0.8)
                             for dx in (-30, -12, 10, 26))
        return s
    b += panel_label(20, 30, 'At the start') + panel_label(330, 30, 'Later')
    bk, _ = beaker(40, 60, 210, 230, 0.8, '#eef6fb', 1, coil(145, 90, False), marks=False)
    b += bk + coil(145, 90, False)
    bk2, _ = beaker(350, 60, 210, 230, 0.8, '#7fb2e5', 0.9, coil(455, 90, True), marks=False)
    b += bk2 + line(455, 70, 455, 110, '#b87333', 5)
    b += lines(145, 315, ['Copper coil in', 'colorless AgNO_3(aq)'], 15)
    b += lines(455, 315, ['Silver crystals on the coil;', 'blue Cu^{2+}(aq) in solution'], 15)
    b += arrow(262, 175, 336, 175, INK, 2.5, 12)
    # Particle view.
    ox = 600
    b += panel_label(ox, 30, 'At the copper surface')
    b += rect(ox, 60, 270, 230, '#f5f9fc', '#9aa5b1', 1.2, 8)
    for r in range(4):
        for c in range(4):
            b += circle(ox + 20 + 22 * c, 120 + 24 * r, 11, '#c4773b', '#7a4a23', 1)
    b += text(ox + 54, 230, 'Cu(s)', 14, weight='bold')
    for y in (128, 176):
        b += circle(ox + 112, y, 10, '#c9ced6', '#6b7280', 1) + text(ox + 112, y + 4, 'Ag', 9, weight='bold')
    b += ion(ox + 200, 120, 12, AG, 'Ag^+', size=10) + arrow(ox + 186, 122, ox + 128, 128, '#52606d', 1.5, 8)
    b += text(ox + 168, 102, 'gains e^−', 12)
    b += ion(ox + 210, 220, 14, '#2f6db5', 'Cu^{2+}', size=10) + arrow(ox + 98, 190, ox + 194, 214, '#2f6db5', 1.5, 8)
    b += text(ox + 168, 255, 'Cu loses 2e^−', 12, fill='#2f6db5')
    b += text(450, 370, 'Cu(s) + 2Ag^+(aq) → Cu^{2+}(aq) + 2Ag(s)', 18, weight='bold')
    b += text(450, 394, 'Schematic. Water molecules and nitrate ions are omitted from the particle view.', 13, fill=MUTED)
    return svg(890, 410, 'Copper displacing silver',
               'A copper coil in colorless silver nitrate solution becomes coated with silver crystals as the solution '
               'turns blue. A particle view shows silver ions gaining electrons to deposit as silver atoms on the '
               'copper surface while copper atoms leave as copper(II) ions.', b)


def buret(cx, top, h, color, opacity=0.9, level=0.75):
    s = rect(cx - 9, top, 18, h, GLASS_FILL, GLASS, 1.8, 2)
    s += rect(cx - 7, top + h * (1 - level), 14, h * level - 2, color, 'none', 0, 0, f' fill-opacity="{opacity}"')
    for k in range(1, 8):
        y = top + k * h / 8
        s += line(cx - 9, y, cx - 3, y, GLASS, 1)
    s += rect(cx - 13, top + h, 26, 10, '#9aa5b1', INK, 1.2, 2)
    s += path(f'M{cx - 3},{top + h + 10} V{top + h + 34} l3,6 3,-6 V{top + h + 10}', GLASS_FILL, GLASS, 1.5)
    return s


@fig('FR022', 'fig-04-23-permanganate-titration.svg')
def permanganate_titration():
    b = ''
    purple = '#8e2a8e'
    for i, (lab, title) in enumerate((('(a)', 'Before the endpoint'), ('(b)', 'At the endpoint'))):
        ox = 40 + i * 330
        b += panel_label(ox, 30, lab) + text(ox + 32, 30, title, 16, anchor='start', weight='bold')
        b += buret(ox + 140, 50, 170, purple)
        b += text(ox + 165, 120, 'KMnO_4(aq)', 14, anchor='start')
        if i == 0:
            plume = (f'<defs><radialGradient id="pl"><stop offset="0" stop-color="{purple}" stop-opacity="0.85"/>'
                     f'<stop offset="1" stop-color="{purple}" stop-opacity="0"/></radialGradient></defs>'
                     f'<ellipse cx="{ox + 140}" cy="378" rx="34" ry="16" fill="url(#pl)"/>')
            fl, _ = erlenmeyer(ox + 140, 420, 170, 150, 40, 50, 0.6, '#e6edf2', 1, plume)
            b += fl
            b += lines(ox + 140, 452, ['Purple appears where titrant enters,', 'then fades as MnO_4^− is consumed'], 14)
        else:
            fl, _ = erlenmeyer(ox + 140, 420, 170, 150, 40, 50, 0.6, '#ecc8e9', 1)
            b += fl
            b += lines(ox + 140, 452, ['Faint purple persists throughout:', 'excess MnO_4^− marks the endpoint'], 14)
        b += text(ox + 140, 408, 'oxalic acid solution', 13, fill=MUTED)
    return svg(700, 490, 'Permanganate titration of oxalic acid',
               'Two titration setups with purple permanganate solution in a buret. Before the endpoint, a purple '
               'plume appears where the drop enters the nearly colorless oxalic acid solution and then fades. At '
               'the endpoint, the whole solution is faintly purple.', b)


@fig('FR023', 'fig-04-24-ascorbic-acid-titration.svg')
def ascorbic_titration():
    b = ''
    states = [('(a)', 'Start', '#f2d22e', 'Yellow (acidic)'), ('(b)', 'Endpoint', '#8fc04a', 'Green'),
              ('(c)', 'Excess NaOH', '#3d7fc4', 'Blue (basic)')]
    for i, (lab, title, col, desc) in enumerate(states):
        ox = 20 + i * 230
        b += panel_label(ox, 30, lab) + text(ox + 32, 30, title, 16, anchor='start', weight='bold')
        b += buret(ox + 110, 50, 150, '#eef6fb', 1, 0.75 - 0.18 * i)
        fl, _ = erlenmeyer(ox + 110, 390, 160, 140, 38, 46, 0.45, col, 0.9)
        b += fl + text(ox + 110, 420, desc, 15, weight='bold')
    b += text(20 + 110 + 30, 120, 'NaOH(aq)', 14, anchor='start')
    b += text(355, 456, 'Ascorbic acid solution with bromothymol blue indicator; colors are schematic.', 13, fill=MUTED)
    return svg(710, 470, 'Ascorbic acid titration',
               'Three stages of titrating ascorbic acid with sodium hydroxide from a buret, using bromothymol blue. '
               'The solution is yellow at the start, green at the endpoint, and blue after excess base is added.', b)
