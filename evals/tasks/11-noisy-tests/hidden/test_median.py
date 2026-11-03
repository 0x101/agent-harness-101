import pathlib, unittest
from mathutils import median

class T(unittest.TestCase):
    def test_median(self):
        self.assertEqual(median([4, 1, 3, 2]), 2.5)
        self.assertEqual(median([3, 1, 2]), 2)
        self.assertEqual(median([1, 2]), 1.5)
        self.assertEqual(median([7]), 7)
    def test_tests_untouched(self):
        self.assertIn("2.5", pathlib.Path("tests/test_mathutils.py").read_text())
