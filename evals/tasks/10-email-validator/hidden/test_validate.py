import unittest
from validate import is_valid_email as v

class T(unittest.TestCase):
    def test_good(self):
        for s in ["a@b.co", "first.last+tag@mail.example.org", "x_y-z@sub-domain.io", "A1@B2.cd"]:
            self.assertTrue(v(s), s)
    def test_bad(self):
        for s in ["", "plain", "a@@b.co", "a@b", ".a@b.co", "a.@b.co", "a..b@c.co", "a@-b.co",
                  "a@b-.co", "a@b.c", "a@b.c0", "a b@c.co", "a@b..co", "a@" + "x" * 64 + ".com", "a!@b.co"]:
            self.assertFalse(v(s), s)
