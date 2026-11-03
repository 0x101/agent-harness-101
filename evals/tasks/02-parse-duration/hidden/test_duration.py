import unittest
from duration import parse_duration as p

class T(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(p("1h30m"), 5400)
        self.assertEqual(p("2h 5s"), 7205)
        self.assertEqual(p("90"), 90)
        self.assertEqual(p("  1d  "), 86400)
        self.assertEqual(p("1d2h3m4s"), 93784)
        self.assertEqual(p("0s"), 0)
    def test_invalid(self):
        for bad in ["", "   ", "5m1h", "1h1h", "1x", "-5s", "1.5h", "h", "1h 30"]:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    p(bad)
