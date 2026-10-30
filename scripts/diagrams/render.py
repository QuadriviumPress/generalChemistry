"""Regenerate the original replacement diagrams in images/replacements.

Usage: python3 scripts/diagrams/render.py [--check] [FR001,FR003,...]
--check compares the generated SVGs with the installed files instead of writing them.
"""
import hashlib
import sys
from pathlib import Path

import lib
from figs_a import FIGS as A
from figs_a2 import FIGS as A2
from figs_b import FIGS as B
from figs_c import FIGS as C
from figs_periodic import FIGS as P

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'images/replacements'
FIGS = {**A, **A2, **B, **C, **P}


def main(args):
    check = '--check' in args
    only = {i for a in args if a != '--check' for i in a.split(',')}
    stale = []
    for fid, (name, draw) in sorted(FIGS.items()):
        if only and fid not in only:
            continue
        lib.reset_ids()
        svg = draw()
        target = OUT / name
        if check:
            if not target.is_file() or target.read_text() != svg:
                stale.append(name)
        else:
            target.write_text(svg)
            print(f'{fid} {name} {hashlib.sha256(svg.encode()).hexdigest()}')
    if stale:
        sys.exit('Generated diagrams differ from installed files: ' + ', '.join(stale))
    if check:
        print(f'{len(FIGS) if not only else len(only)} diagrams match their generator.')


if __name__ == '__main__':
    main(sys.argv[1:])
