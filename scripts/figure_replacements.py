"""Apply and validate editorial figure replacements without altering source provenance."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

LEDGER = 'figure-replacements.json'
NOTICE_SHA256 = '93f80bd15e870d30b31a3f2185d4a3d03408696daa0f2643462e8d604ce24a6b'
SOURCED_FIELDS = ('title', 'creator', 'source_url', 'source_revision_url', 'download_url',
                  'license', 'license_url', 'retrieved', 'changes')
SOURCED_URLS = ('source_url', 'source_revision_url', 'download_url', 'license_url')
ORIGINAL_FIELDS = ('title', 'creator', 'license', 'license_url', 'created', 'basis')


def read_ledger(root):
    ledger = json.loads((root / LEDGER).read_text())
    if ledger.get('version') != 1 or not isinstance(ledger.get('entries'), list):
        raise ValueError('Unsupported figure replacement ledger format')
    return ledger


def image_paths(markdown):
    """Read the inline image form used by this edition, excluding ordinary links."""
    return re.findall(r'!\[[^\n]*?\]\((/images/[^\s)]+)\)', markdown)


def apply_entry(text, entry):
    """Reapply an approved block once; refuse to guess after conflicting edits."""
    before, after = entry['original_markdown'], entry['replacement']['markdown']
    if text.count(after) == 1 and before not in text:
        return text
    if text.count(before) != 1 or after in text:
        raise ValueError(f'{entry["id"]}: original figure block is missing or ambiguous')
    return text.replace(before, after, 1)


def apply_all(root):
    for entry in read_ledger(root)['entries']:
        if entry['status'] != 'installed':
            continue
        path = root / entry['markdown_file']
        text = path.read_text()
        updated = apply_entry(text, entry)
        if text != updated:
            path.write_text(updated)


def validate_ledger(root, manifest):
    """Check approved assets, source mappings, captions, and attribution metadata."""
    ledger = read_ledger(root)
    errors, mappings, ids = [], set(), set()
    pages = {p['file']: p for p in manifest['pages']}
    for entry in ledger['entries']:
        key = (entry['markdown_file'], entry['original_asset'])
        if entry['id'] in ids or key in mappings:
            errors.append(f'Duplicate replacement entry: {entry["id"]}')
        ids.add(entry['id'])
        mappings.add(key)
        if entry['status'] not in ('pending', 'installed'):
            errors.append(f'Invalid replacement status: {entry["id"]}')
        if manifest['assets'].get(entry['original_asset']) != entry['original_sha256']:
            errors.append(f'Replacement source checksum mismatch: {entry["id"]}')
        page = pages.get(entry['markdown_file'])
        if page is None:
            errors.append(f'Unknown replacement chapter: {entry["id"]}')
            continue
        original = root / 'source' / page['source']
        source_images = {'images/' + p for p in re.findall(r'<img\b[^>]*src="([^"]+)"', original.read_text())}
        if entry['original_asset'] not in source_images:
            errors.append(f'Replacement source does not belong to chapter: {entry["id"]}')
        if '/' + entry['original_asset'] not in image_paths(entry['original_markdown']):
            errors.append(f'Original figure block does not contain source image: {entry["id"]}')
        if entry['status'] != 'installed':
            if 'replacement' in entry:
                errors.append(f'Pending entry has an active replacement: {entry["id"]}')
            continue
        replacement = entry['replacement']
        text = (root / entry['markdown_file']).read_text()
        if text.count(replacement['markdown']) != 1:
            errors.append(f'Approved replacement block missing or duplicated: {entry["id"]}')
        if '/' + entry['original_asset'] in image_paths(text):
            errors.append(f'Replaced source notice still active: {entry["id"]}')
        assets = replacement['assets']
        if not assets:
            errors.append(f'Replacement has no assets: {entry["id"]}')
        declared = ['/' + a['path'] for a in assets]
        if sorted(declared) != sorted(image_paths(replacement['markdown'])):
            errors.append(f'Replacement block and asset list disagree: {entry["id"]}')
        if re.search(r'!\[\s*\]\(', replacement['markdown']):
            errors.append(f'Replacement lacks alternative text: {entry["id"]}')
        for asset in assets:
            path = Path(asset['path'])
            if path.is_absolute() or '..' in path.parts or not asset['path'].startswith('images/replacements/'):
                errors.append(f'Invalid replacement asset path: {entry["id"]}: {path}')
                continue
            target = root / path
            if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != asset['sha256']:
                errors.append(f'Missing or modified replacement asset: {path}')
            if asset['sha256'] == NOTICE_SHA256:
                errors.append(f'Replacement is an unavailable-image notice: {entry["id"]}')
            # Original diagrams drawn for this edition have no download source to record.
            fields, urls, date = ((ORIGINAL_FIELDS, ('license_url',), 'created') if asset.get('origin') == 'original'
                                  else (SOURCED_FIELDS, SOURCED_URLS, 'retrieved'))
            for field in fields:
                if not asset.get(field):
                    errors.append(f'Replacement attribution missing {field}: {entry["id"]}: {path}')
            for field in urls:
                if urlsplit(asset.get(field, '')).scheme != 'https':
                    errors.append(f'Replacement attribution needs HTTPS {field}: {entry["id"]}')
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', asset.get(date, '')):
                errors.append(f'Invalid {date} date: {entry["id"]}')
    return ledger, errors


if __name__ == '__main__':
    apply_all(Path(__file__).resolve().parents[1])
