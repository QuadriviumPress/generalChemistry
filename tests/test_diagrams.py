"""The installed original diagrams must match their generator."""
from pathlib import Path
import subprocess
import sys
import unittest

RENDER = Path(__file__).resolve().parents[1] / 'scripts/diagrams/render.py'


class DiagramGeneratorTests(unittest.TestCase):
    def test_installed_diagrams_match_generator(self):
        result = subprocess.run([sys.executable, str(RENDER), '--check'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
