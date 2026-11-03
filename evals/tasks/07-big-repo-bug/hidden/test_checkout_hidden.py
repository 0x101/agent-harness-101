import pathlib, unittest
from shop.checkout import total

class T(unittest.TestCase):
    def test_codes(self):
        self.assertEqual(total([(10.0, 2)]), 21.6)
        self.assertEqual(total([(100.0, 1)], "WELCOME10"), 97.2)
        self.assertEqual(total([(40.0, 1)], "HALF"), 21.6)
        self.assertEqual(total([(80.0, 1)], "VIP25"), 64.8)
        self.assertEqual(total([(80.0, 1)], "BOGUS"), 86.4)
    def test_tests_untouched(self):
        self.assertIn("97.2", pathlib.Path("tests/test_checkout.py").read_text())
