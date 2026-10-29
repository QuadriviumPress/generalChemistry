#!/usr/bin/env python3
"""Check complete source coverage, provenance, figures, and local references."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'source/manifest.json').read_text())
errors = []
pages = manifest['pages']
chapters = [p for p in pages if p['file'].startswith('chapters/')]
appendices = [p for p in pages if p['title'].startswith('Appendix ')]
if len(pages) != 36 or len(chapters) != 24 or len(appendices) != 9:
    errors.append('Expected 36 source pages: 24 chapters, 9 appendices, preface, license, and credits')
if {int(re.match(r'Chapter (\d+):', p['title'])[1]) for p in chapters} != set(range(1, 25)):
    errors.append('Chapter numbering is incomplete')

documents = {}
labels = {}
for page in pages:
    original = ROOT / 'source' / page['source']
    if not original.is_file() or hashlib.sha256(original.read_bytes()).hexdigest() != page['source_sha256']:
        errors.append(f'Original source missing or modified: {original}')
    path = ROOT / page['file']
    if not path.is_file():
        errors.append(f'Missing converted page: {path}')
        continue
    text = path.read_text()
    if not re.search(r'^# ', text, re.M):
        errors.append(f'Missing page title: {path}')
    if 'CHEMISTRYTOKEN' in text or 'CHEMISTRYFOOTNOTE' in text:
        errors.append(f'Unexpanded conversion marker: {path}')
    # A single source figure can appear again when a spanning table cell is
    # expanded. Every original image must appear at least once.
    source_images = [image for image in re.findall(r'<img\b[^>]*src="([^"]+)"', original.read_text())
                     if not image.startswith('shared/')]
    for image in source_images:
        if '/images/' + image not in text:
            errors.append(f'Lost figure {image} in {path.name}')
    if re.search(r'!\[\]\(', text):
        errors.append(f'Figure missing alternative text: {path}')
    documents[page['file']] = text

for name in ('index.md', 'SOURCES.md'):
    documents[name] = (ROOT / name).read_text()

for name, text in documents.items():
    found = re.findall(r'^\s*\(([^()\n]+)\)=$', text, re.M)
    labels[name] = set(found)
    if len(found) != len(set(found)):
        errors.append(f'Duplicate cross-reference labels: {name}')
    used = set(re.findall(r'\[\^(chem-\d+)\]', re.sub(r'^\[\^chem-\d+\]:', '', text, flags=re.M)))
    defined = set(re.findall(r'^\[\^(chem-\d+)\]:', text, re.M))
    if used != defined:
        errors.append(f'Footnote mismatch: {name}: used-only {used - defined}, defined-only {defined - used}')

for name, text in documents.items():
    # Source images and rewritten references use root-relative paths; include
    # ordinary relative links from authored front matter as well.
    # Avoid treating chemical square brackets inside LaTeX as Markdown links.
    prose = re.sub(r'\$\$.*?\$\$|(?<!\\)\$[^$\n]*(?<!\\)\$', '', text, flags=re.S)
    for href in re.findall(r'(?<!\\)\]\(([^\s)]+)\)', prose):
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc:
            continue
        target = unquote(parsed.path)
        target_path = ROOT / target.lstrip('/') if target.startswith('/') else ROOT / name / '..' / target
        target_path = target_path.resolve() if target else ROOT / name
        if not target_path.is_file():
            errors.append(f'Broken local link: {name}: {href}')
        elif parsed.fragment and target_path.suffix == '.md':
            key = str(target_path.relative_to(ROOT))
            if parsed.fragment not in labels.get(key, set()):
                errors.append(f'Broken local fragment: {name}: {href}')

for asset, checksum in manifest['assets'].items():
    path = ROOT / asset
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != checksum:
        errors.append(f'Missing or modified source asset: {asset}')

toc = (ROOT / 'myst.yml').read_text()
for name in documents:
    if name not in toc:
        errors.append(f'Page missing from table of contents: {name}')

if errors:
    raise SystemExit('\n'.join(errors))
print(f'Verified {len(chapters)} chapters, {len(appendices)} appendices, all {len(pages)} source pages, '
      f'{len(manifest["assets"])} local assets, and {sum(map(len, labels.values()))} cross-reference targets.')
