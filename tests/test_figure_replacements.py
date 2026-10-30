"""Regression checks for preserving source coverage while replacing missing art."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from figure_replacements import NOTICE_SHA256, apply_entry, image_paths, validate_ledger


class FigureReplacementTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for directory in ('source', 'chapters', 'images/replacements'):
            (self.root / directory).mkdir(parents=True)
        (self.root / 'source/chapter.html').write_text('<img src="section_01/missing.jpg">')
        asset = self.root / 'images/replacements/photo.jpg'
        asset.write_bytes(b'An independently sourced photograph')
        before = '![Unavailable figure](/images/section_01/missing.jpg)\n\nOld caption.'
        after = '![A photographed specimen](/images/replacements/photo.jpg)\n\nNew caption and credit.'
        self.entry = {
            'id': 'FR001', 'markdown_file': 'chapters/ch-01.md',
            'original_asset': 'images/section_01/missing.jpg', 'original_sha256': 'original checksum',
            'original_markdown': before, 'status': 'installed',
            'replacement': {'markdown': after, 'assets': [{
                'path': 'images/replacements/photo.jpg',
                'sha256': hashlib.sha256(asset.read_bytes()).hexdigest(),
                'title': 'Specimen', 'creator': 'Photographer',
                'source_url': 'https://example.org/photo',
                'source_revision_url': 'https://example.org/photo?revision=1',
                'download_url': 'https://example.org/photo.jpg',
                'license': 'CC BY 4.0', 'license_url': 'https://creativecommons.org/licenses/by/4.0/',
                'retrieved': '2026-10-30', 'changes': 'None',
            }]},
        }
        self.manifest = {'assets': {self.entry['original_asset']: 'original checksum'},
                         'pages': [{'file': 'chapters/ch-01.md', 'source': 'chapter.html'}]}
        (self.root / 'chapters/ch-01.md').write_text(after)

    def validate(self):
        (self.root / 'figure-replacements.json').write_text(json.dumps({'version': 1, 'entries': [self.entry]}))
        return validate_ledger(self.root, self.manifest)[1]

    def test_reimport_reapplies_once_and_is_idempotent(self):
        source = '# Chapter\n\n' + self.entry['original_markdown'] + '\n'
        result = apply_entry(source, self.entry)
        self.assertIn(self.entry['replacement']['markdown'], result)
        self.assertEqual(apply_entry(result, self.entry), result)

    def test_reimport_refuses_conflicting_or_duplicated_blocks(self):
        for source in ('Edited caption with missing original block', self.entry['original_markdown'] * 2):
            with self.subTest(source=source), self.assertRaises(ValueError):
                apply_entry(source, self.entry)

    def test_valid_ledger_preserves_mapping(self):
        self.assertEqual(self.validate(), [])

    def test_corrupt_photo_is_rejected(self):
        (self.root / 'images/replacements/photo.jpg').write_bytes(b'corrupted')
        self.assertTrue(any('modified replacement asset' in e for e in self.validate()))

    def test_wrong_source_provenance_is_rejected(self):
        self.entry['original_sha256'] = 'invented checksum'
        self.assertTrue(any('source checksum mismatch' in e for e in self.validate()))

    def test_source_from_another_chapter_is_rejected(self):
        (self.root / 'source/chapter.html').write_text('<img src="section_01/another.jpg">')
        self.assertTrue(any('does not belong to chapter' in e for e in self.validate()))

    def test_unavailable_notice_cannot_be_installed_as_a_replacement(self):
        source_notice = Path(__file__).resolve().parents[1] / 'images/section_05/937a8cabe266463c54be6b0d196c18ae.jpg'
        (self.root / 'images/replacements/photo.jpg').write_bytes(source_notice.read_bytes())
        self.entry['replacement']['assets'][0]['sha256'] = NOTICE_SHA256
        self.assertTrue(any('is an unavailable-image notice' in e for e in self.validate()))

    def test_missing_credit_metadata_is_rejected(self):
        del self.entry['replacement']['assets'][0]['creator']
        self.assertTrue(any('attribution missing creator' in e for e in self.validate()))

    def use_original_diagram(self):
        asset = self.entry['replacement']['assets'][0]
        for field in ('source_url', 'source_revision_url', 'download_url', 'retrieved', 'changes'):
            del asset[field]
        asset.update({'origin': 'original', 'created': '2026-10-30', 'basis': 'Caption and surrounding text',
                      'license': 'CC BY-NC-SA 3.0', 'license_url': 'https://creativecommons.org/licenses/by-nc-sa/3.0/'})
        return asset

    def test_original_diagram_needs_no_download_source(self):
        self.use_original_diagram()
        self.assertEqual(self.validate(), [])

    def test_original_diagram_needs_its_basis_and_date(self):
        asset = self.use_original_diagram()
        del asset['basis']
        asset['created'] = 'today'
        errors = self.validate()
        self.assertTrue(any('attribution missing basis' in e for e in errors))
        self.assertTrue(any('Invalid created date' in e for e in errors))

    def test_restored_notice_is_rejected(self):
        path = self.root / 'chapters/ch-01.md'
        path.write_text(self.entry['original_markdown'])
        errors = self.validate()
        self.assertTrue(any('replacement block missing' in e for e in errors))
        self.assertTrue(any('notice still active' in e for e in errors))

    def test_comment_link_does_not_count_as_an_image(self):
        self.assertEqual(image_paths('<!-- /images/section_01/missing.jpg -->'), [])
        self.assertEqual(image_paths('[Source](/images/section_01/missing.jpg)'), [])


if __name__ == '__main__':
    unittest.main()
