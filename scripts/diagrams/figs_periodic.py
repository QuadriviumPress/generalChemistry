"""Periodic tables with current IUPAC names and CIAAW atomic weights.

Figure masses are the 2024 abridged standard atomic weights. Appendix masses are
the 2024 standard values; an interval element is stored as its conventional
atomic weight. Bracketed values are mass numbers of the longest-lived isotopes
from the IUPAC atomic-weights table of 2021.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib

# name, symbol, Z, kind, appendix mass, figure mass
# kind: alkali, alkaline, metal, metalloid, nonmetal, halogen, noble
ELEMENTS = [
    ('Hydrogen', 'H', 1, 'nonmetal', '1.008‡', '1.008'),
    ('Helium', 'He', 2, 'noble', '4.002602(2)', '4.0026'),
    ('Lithium', 'Li', 3, 'alkali', '6.94‡', '6.94'),
    ('Beryllium', 'Be', 4, 'alkaline', '9.0121831(5)', '9.0122'),
    ('Boron', 'B', 5, 'metalloid', '10.81‡', '10.81'),
    ('Carbon', 'C', 6, 'nonmetal', '12.011‡', '12.011'),
    ('Nitrogen', 'N', 7, 'nonmetal', '14.007‡', '14.007'),
    ('Oxygen', 'O', 8, 'nonmetal', '15.999‡', '15.999'),
    ('Fluorine', 'F', 9, 'halogen', '18.998403162(5)', '18.998'),
    ('Neon', 'Ne', 10, 'noble', '20.1797(6)', '20.180'),
    ('Sodium', 'Na', 11, 'alkali', '22.98976928(2)', '22.990'),
    ('Magnesium', 'Mg', 12, 'alkaline', '24.305‡', '24.305'),
    ('Aluminum', 'Al', 13, 'metal', '26.9815384(3)', '26.982'),
    ('Silicon', 'Si', 14, 'metalloid', '28.085‡', '28.085'),
    ('Phosphorus', 'P', 15, 'nonmetal', '30.973761998(5)', '30.974'),
    ('Sulfur', 'S', 16, 'nonmetal', '32.06‡', '32.06'),
    ('Chlorine', 'Cl', 17, 'halogen', '35.45‡', '35.45'),
    ('Argon', 'Ar', 18, 'noble', '39.95‡', '39.95'),
    ('Potassium', 'K', 19, 'alkali', '39.0983(1)', '39.098'),
    ('Calcium', 'Ca', 20, 'alkaline', '40.078(4)', '40.078'),
    ('Scandium', 'Sc', 21, 'metal', '44.955907(4)', '44.956'),
    ('Titanium', 'Ti', 22, 'metal', '47.867(1)', '47.867'),
    ('Vanadium', 'V', 23, 'metal', '50.9415(1)', '50.942'),
    ('Chromium', 'Cr', 24, 'metal', '51.9961(6)', '51.996'),
    ('Manganese', 'Mn', 25, 'metal', '54.938043(2)', '54.938'),
    ('Iron', 'Fe', 26, 'metal', '55.845(2)', '55.845'),
    ('Cobalt', 'Co', 27, 'metal', '58.933194(3)', '58.933'),
    ('Nickel', 'Ni', 28, 'metal', '58.6934(4)', '58.693'),
    ('Copper', 'Cu', 29, 'metal', '63.546(3)', '63.546'),
    ('Zinc', 'Zn', 30, 'metal', '65.38(2)', '65.38'),
    ('Gallium', 'Ga', 31, 'metal', '69.723(1)', '69.723'),
    ('Germanium', 'Ge', 32, 'metalloid', '72.630(8)', '72.630'),
    ('Arsenic', 'As', 33, 'metalloid', '74.921595(6)', '74.922'),
    ('Selenium', 'Se', 34, 'nonmetal', '78.971(8)', '78.971'),
    ('Bromine', 'Br', 35, 'halogen', '79.904‡', '79.904'),
    ('Krypton', 'Kr', 36, 'noble', '83.798(2)', '83.798'),
    ('Rubidium', 'Rb', 37, 'alkali', '85.4678(3)', '85.468'),
    ('Strontium', 'Sr', 38, 'alkaline', '87.62(1)', '87.62'),
    ('Yttrium', 'Y', 39, 'metal', '88.905838(2)', '88.906'),
    ('Zirconium', 'Zr', 40, 'metal', '91.222(3)', '91.222'),
    ('Niobium', 'Nb', 41, 'metal', '92.90637(1)', '92.906'),
    ('Molybdenum', 'Mo', 42, 'metal', '95.95(1)', '95.95'),
    ('Technetium', 'Tc', 43, 'metal', '[97]*', '[97]'),
    ('Ruthenium', 'Ru', 44, 'metal', '101.07(2)', '101.07'),
    ('Rhodium', 'Rh', 45, 'metal', '102.90549(2)', '102.91'),
    ('Palladium', 'Pd', 46, 'metal', '106.42(1)', '106.42'),
    ('Silver', 'Ag', 47, 'metal', '107.8682(2)', '107.87'),
    ('Cadmium', 'Cd', 48, 'metal', '112.414(4)', '112.41'),
    ('Indium', 'In', 49, 'metal', '114.818(1)', '114.82'),
    ('Tin', 'Sn', 50, 'metal', '118.710(7)', '118.71'),
    ('Antimony', 'Sb', 51, 'metalloid', '121.760(1)', '121.76'),
    ('Tellurium', 'Te', 52, 'metalloid', '127.60(3)', '127.60'),
    ('Iodine', 'I', 53, 'halogen', '126.90447(3)', '126.90'),
    ('Xenon', 'Xe', 54, 'noble', '131.293(6)', '131.29'),
    ('Cesium', 'Cs', 55, 'alkali', '132.90545196(6)', '132.91'),
    ('Barium', 'Ba', 56, 'alkaline', '137.327(7)', '137.33'),
    ('Lanthanum', 'La', 57, 'metal', '138.90547(7)', '138.91'),
    ('Cerium', 'Ce', 58, 'metal', '140.116(1)', '140.12'),
    ('Praseodymium', 'Pr', 59, 'metal', '140.90766(1)', '140.91'),
    ('Neodymium', 'Nd', 60, 'metal', '144.242(3)', '144.24'),
    ('Promethium', 'Pm', 61, 'metal', '[145]*', '[145]'),
    ('Samarium', 'Sm', 62, 'metal', '150.36(2)', '150.36'),
    ('Europium', 'Eu', 63, 'metal', '151.964(1)', '151.96'),
    ('Gadolinium', 'Gd', 64, 'metal', '157.249(2)', '157.25'),
    ('Terbium', 'Tb', 65, 'metal', '158.925354(7)', '158.93'),
    ('Dysprosium', 'Dy', 66, 'metal', '162.500(1)', '162.50'),
    ('Holmium', 'Ho', 67, 'metal', '164.930329(5)', '164.93'),
    ('Erbium', 'Er', 68, 'metal', '167.259(3)', '167.26'),
    ('Thulium', 'Tm', 69, 'metal', '168.934219(5)', '168.93'),
    ('Ytterbium', 'Yb', 70, 'metal', '173.045(10)', '173.05'),
    ('Lutetium', 'Lu', 71, 'metal', '174.96669(5)', '174.97'),
    ('Hafnium', 'Hf', 72, 'metal', '178.486(6)', '178.49'),
    ('Tantalum', 'Ta', 73, 'metal', '180.94788(2)', '180.95'),
    ('Tungsten', 'W', 74, 'metal', '183.84(1)', '183.84'),
    ('Rhenium', 'Re', 75, 'metal', '186.207(1)', '186.21'),
    ('Osmium', 'Os', 76, 'metal', '190.23(3)', '190.23'),
    ('Iridium', 'Ir', 77, 'metal', '192.217(2)', '192.22'),
    ('Platinum', 'Pt', 78, 'metal', '195.084(9)', '195.08'),
    ('Gold', 'Au', 79, 'metal', '196.966570(4)', '196.97'),
    ('Mercury', 'Hg', 80, 'metal', '200.592(3)', '200.59'),
    ('Thallium', 'Tl', 81, 'metal', '204.38‡', '204.38'),
    ('Lead', 'Pb', 82, 'metal', '207.2‡', '207.2'),
    ('Bismuth', 'Bi', 83, 'metal', '208.98040(1)', '208.98'),
    ('Polonium', 'Po', 84, 'metal', '[209]*', '[209]'),
    ('Astatine', 'At', 85, 'halogen', '[210]*', '[210]'),
    ('Radon', 'Rn', 86, 'noble', '[222]*', '[222]'),
    ('Francium', 'Fr', 87, 'alkali', '[223]*', '[223]'),
    ('Radium', 'Ra', 88, 'alkaline', '[226]*', '[226]'),
    ('Actinium', 'Ac', 89, 'metal', '[227]*', '[227]'),
    ('Thorium', 'Th', 90, 'metal', '232.0377(4)*', '232.04'),
    ('Protactinium', 'Pa', 91, 'metal', '231.03588(1)*', '231.04'),
    ('Uranium', 'U', 92, 'metal', '238.02891(3)*', '238.03'),
    ('Neptunium', 'Np', 93, 'metal', '[237]*', '[237]'),
    ('Plutonium', 'Pu', 94, 'metal', '[244]*', '[244]'),
    ('Americium', 'Am', 95, 'metal', '[243]*', '[243]'),
    ('Curium', 'Cm', 96, 'metal', '[247]*', '[247]'),
    ('Berkelium', 'Bk', 97, 'metal', '[247]*', '[247]'),
    ('Californium', 'Cf', 98, 'metal', '[251]*', '[251]'),
    ('Einsteinium', 'Es', 99, 'metal', '[252]*', '[252]'),
    ('Fermium', 'Fm', 100, 'metal', '[257]*', '[257]'),
    ('Mendelevium', 'Md', 101, 'metal', '[258]*', '[258]'),
    ('Nobelium', 'No', 102, 'metal', '[259]*', '[259]'),
    ('Lawrencium', 'Lr', 103, 'metal', '[262]*', '[262]'),
    ('Rutherfordium', 'Rf', 104, 'metal', '[267]*', '[267]'),
    ('Dubnium', 'Db', 105, 'metal', '[270]*', '[270]'),
    ('Seaborgium', 'Sg', 106, 'metal', '[269]*', '[269]'),
    ('Bohrium', 'Bh', 107, 'metal', '[270]*', '[270]'),
    ('Hassium', 'Hs', 108, 'metal', '[270]*', '[270]'),
    ('Meitnerium', 'Mt', 109, 'metal', '[278]*', '[278]'),
    ('Darmstadtium', 'Ds', 110, 'metal', '[281]*', '[281]'),
    ('Roentgenium', 'Rg', 111, 'metal', '[281]*', '[281]'),
    ('Copernicium', 'Cn', 112, 'metal', '[285]*', '[285]'),
    ('Nihonium', 'Nh', 113, 'metal', '[286]*', '[286]'),
    ('Flerovium', 'Fl', 114, 'metal', '[289]*', '[289]'),
    ('Moscovium', 'Mc', 115, 'metal', '[289]*', '[289]'),
    ('Livermorium', 'Lv', 116, 'metal', '[293]*', '[293]'),
    ('Tennessine', 'Ts', 117, 'halogen', '[293]*', '[293]'),
    ('Oganesson', 'Og', 118, 'noble', '[294]*', '[294]'),
]

assert len(ELEMENTS) == 118 and len({e[2] for e in ELEMENTS}) == 118

# Fills. Dark fills use white type.
FILLS = {
    'alkali': ('#6d4c9a', '#ffffff'),
    'alkaline': ('#2f7d62', '#ffffff'),
    'metal': ('#7eaea8', '#1f2933'),
    'metalloid': ('#e0a33c', '#1f2933'),
    'nonmetal': ('#cbb892', '#1f2933'),
    'halogen': ('#c44536', '#ffffff'),
    'noble': ('#243e6a', '#ffffff'),
}
SIMPLE = {
    'alkali': ('#3d7ea6', '#ffffff'),
    'alkaline': ('#3d7ea6', '#ffffff'),
    'metal': ('#3d7ea6', '#ffffff'),
    'metalloid': ('#e0a33c', '#1f2933'),
    'nonmetal': ('#c4b48a', '#1f2933'),
    'halogen': ('#c4b48a', '#1f2933'),
    'noble': ('#c4b48a', '#1f2933'),
}
OLD_GROUPS = {
    1: '1A', 2: '2A', 3: '3B', 4: '4B', 5: '5B', 6: '6B', 7: '7B', 8: '8B',
    9: '8B', 10: '8B', 11: '1B', 12: '2B', 13: '3A', 14: '4A', 15: '5A',
    16: '6A', 17: '7A', 18: '8A',
}

DESC_SIMPLE = (
    'Periodic table of the 118 elements with official IUPAC symbols, arranged by increasing atomic number. '
    'Metals are blue, to the lower left of an orange staircase. Nonmetals are bronze, to the upper right. '
    'Boron, silicon, germanium, arsenic, antimony, and tellurium are gold. '
    'The lanthanides and actinides are shown in two rows below the main table.'
)
DESC_MASS = (
    'Periodic table with IUPAC group numbers 1 to 18 and the older U.S. A and B numbers. '
    'Each cell shows the atomic number, symbol, and an abridged atomic mass. '
    'Alkali metals are purple, alkaline earth metals green, other metals teal, metalloids gold, '
    'nonmetals tan, halogens red, and noble gases dark blue. '
    'The lanthanides and actinides are in two rows below.'
)


def place(z):
    """Return (row, column) for the main table, or (series, index) for the f block."""
    if z == 1:
        return ('main', 1, 1)
    if z == 2:
        return ('main', 1, 18)
    if 3 <= z <= 4:
        return ('main', 2, z - 2)
    if 5 <= z <= 10:
        return ('main', 2, z + 8)
    if 11 <= z <= 12:
        return ('main', 3, z - 10)
    if 13 <= z <= 18:
        return ('main', 3, z)
    if 19 <= z <= 36:
        return ('main', 4, z - 18)
    if 37 <= z <= 54:
        return ('main', 5, z - 36)
    if z == 55:
        return ('main', 6, 1)
    if z == 56:
        return ('main', 6, 2)
    if z == 57:
        return ('main', 6, 3)
    if 58 <= z <= 71:
        return ('lan', z - 57)
    if 72 <= z <= 86:
        return ('main', 6, z - 68)
    if z == 87:
        return ('main', 7, 1)
    if z == 88:
        return ('main', 7, 2)
    if z == 89:
        return ('main', 7, 3)
    if 90 <= z <= 103:
        return ('act', z - 89)
    if 104 <= z <= 118:
        return ('main', 7, z - 100)
    raise ValueError(z)


def _cell(x, y, w, h, element, masses, palette):
    _name, symbol, z, kind, _full, short = element
    fill, ink = palette[kind]
    body = lib.rect(x, y, w, h, fill, '#ffffff', 1.2)
    if masses:
        body += lib.text(x + 4, y + 11, str(z), 9, anchor='start', fill=ink)
        body += lib.text(x + w / 2, y + h * 0.58, symbol, 15, weight='bold', fill=ink)
        body += lib.text(x + w / 2, y + h - 5, short, 8, fill=ink)
    else:
        body += lib.text(x + w / 2, y + 13, str(z), 9, fill=ink)
        body += lib.text(x + w / 2, y + h * 0.72, symbol, 14, weight='bold', fill=ink)
    return body


def _staircase(ox, oy, cw, ch, gap):
    """Metal/nonmetal boundary through groups 13–17, in cell-boundary units."""
    def pt(col, row):
        return ox + col * (cw + gap) - gap / 2, oy + row * (ch + gap) - gap / 2

    corners = [(12, 1), (12, 2), (13, 2), (13, 4), (14, 4), (14, 5), (16, 5), (16, 7)]
    points = [pt(c, r) for c, r in corners]
    d = 'M' + ' L'.join(f'{lib.f(x)},{lib.f(y)}' for x, y in points)
    return lib.path(d, 'none', '#e06a12', 3.5, ' stroke-linejoin="round" stroke-linecap="round"')


def _legend(x, y, items):
    body, cx = '', x
    for label, fill, span in items:
        body += lib.rect(cx, y, 12, 12, fill, '#ffffff', 0.8)
        body += lib.text(cx + 16, y + 10, label, 11, anchor='start')
        cx += span
    return body


def draw(masses):
    cw, ch, gap = (62, 48, 2) if masses else (46, 40, 2)
    left, top = 108, 46 if masses else 36
    width = left + 18 * (cw + gap) + 16
    f_top = top + 7 * (ch + gap) + 28
    height = f_top + 2 * (ch + gap) + (36 if masses else 28)
    palette = FILLS if masses else SIMPLE
    body = ''
    if masses:
        body += lib.text(left + 9 * (cw + gap), 16, 'Group', 13, weight='bold')
        for g in range(1, 19):
            x = left + (g - 1) * (cw + gap) + cw / 2
            body += lib.text(x, 32, str(g), 11, weight='bold')
            body += lib.text(x, 44, OLD_GROUPS[g], 9, fill=lib.MUTED)
    else:
        body += lib.text(left + 9 * (cw + gap), 18, 'Group', 13, weight='bold')
        for g in range(1, 19):
            x = left + (g - 1) * (cw + gap) + cw / 2
            body += lib.text(x, top - 8, str(g), 11, weight='bold')
    for period in range(1, 8):
        y = top + (period - 1) * (ch + gap) + ch / 2 + 4
        body += lib.text(left - 14, y, str(period), 12, weight='bold', fill=lib.MUTED)
    for element in ELEMENTS:
        slot = place(element[2])
        if slot[0] == 'main':
            _band, period, group = slot
            x = left + (group - 1) * (cw + gap)
            y = top + (period - 1) * (ch + gap)
        elif slot[0] == 'lan':
            x = left + (slot[1] + 1) * (cw + gap)
            y = f_top
        else:
            x = left + (slot[1] + 1) * (cw + gap)
            y = f_top + ch + gap
        body += _cell(x, y, cw, ch, element, masses, palette)
    if not masses:
        body += _staircase(left, top, cw, ch, gap)
    body += lib.text(left - 8, f_top + ch * 0.65, 'Lanthanides', 11, anchor='end', fill=lib.MUTED)
    body += lib.text(left - 8, f_top + ch + gap + ch * 0.65, 'Actinides', 11, anchor='end', fill=lib.MUTED)
    legend_y = f_top + 2 * (ch + gap) + 8
    if masses:
        body += _legend(left, legend_y, [
            ('Alkali metals', FILLS['alkali'][0], 130),
            ('Alkaline earth metals', FILLS['alkaline'][0], 180),
            ('Other metals', FILLS['metal'][0], 120),
            ('Metalloids', FILLS['metalloid'][0], 110),
            ('Nonmetals', FILLS['nonmetal'][0], 110),
            ('Halogens', FILLS['halogen'][0], 100),
            ('Noble gases', FILLS['noble'][0], 120),
        ])
    else:
        body += _legend(left, legend_y, [
            ('Metals', SIMPLE['metal'][0], 90),
            ('Metalloids', SIMPLE['metalloid'][0], 110),
            ('Nonmetals', SIMPLE['nonmetal'][0], 110),
        ])
    title = 'Periodic table of the elements' if masses else 'Periodic table in order of increasing atomic number'
    desc = DESC_MASS if masses else DESC_SIMPLE
    return lib.svg(width, height, title, desc, body)


def fig_simple():
    return draw(False)


def fig_masses():
    return draw(True)


def appendix_table():
    """MyST list-table body for Appendix H, in alphabetical order."""
    rows = [
        '- - List of Elements',
        '  - List of Elements',
        '  - List of Elements',
        '  - List of Elements',
        '- - Name',
        '  - Symbol',
        '  - Atomic Number',
        '  - Atomic Mass',
    ]
    for name, symbol, z, _kind, mass, _short in sorted(ELEMENTS, key=lambda e: e[0]):
        shown = mass.replace('[', '\\[').replace(']', '\\]').replace('*', '\\*')
        rows += [f'- - {name}', f'  - {symbol}', f'  - {z}', f'  - {shown}']
    note_star = (
        '\\*Element has no stable isotope. A value enclosed in brackets, e.g. \\[209\\], indicates the mass number '
        'of the longest-lived isotope of the element. Three such elements (Th, Pa, and U) do have a characteristic '
        'terrestrial isotopic composition, and a standard atomic weight is given for them. An uncertainty in the last '
        'digit is shown by the number in parentheses; e.g., 4.002602(2) indicates ±0.000002.'
    )
    note_dagger = (
        '‡The standard atomic weight is an interval. The value shown is the conventional atomic weight for calculations. '
        'The intervals are H \\[1.00784, 1.00811\\], Li \\[6.938, 6.997\\], B \\[10.806, 10.821\\], C \\[12.0096, 12.0116\\], '
        'N \\[14.00643, 14.00728\\], O \\[15.99903, 15.99977\\], Mg \\[24.304, 24.307\\], Si \\[28.084, 28.086\\], '
        'S \\[32.059, 32.076\\], Cl \\[35.446, 35.457\\], Ar \\[39.792, 39.963\\], Br \\[79.901, 79.907\\], '
        'Tl \\[204.382, 204.385\\], and Pb \\[206.14, 207.94\\].'
    )
    for note in (note_star, note_dagger):
        rows.append(f'- - {note}')
        rows += [f'  - {note}'] * 3
    return '\n'.join(rows) + '\n'


FIGS = {
    'FR066': ('fig-01-24-periodic-table.svg', fig_simple),
    'FR067': ('fig-h-periodic-table.svg', fig_masses),
}
