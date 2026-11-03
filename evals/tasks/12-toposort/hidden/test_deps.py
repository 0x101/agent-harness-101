import unittest
from deps import build_order, CycleError

class T(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(build_order({"b": [], "a": []}), ["a", "b"])
    def test_chain(self):
        self.assertEqual(build_order({"app": ["lib"], "lib": ["core"]}), ["core", "lib", "app"])
    def test_ties(self):
        g = {"web": ["api", "ui"], "api": ["db"], "ui": ["assets"], "db": [], "assets": []}
        self.assertEqual(build_order(g), ["assets", "db", "api", "ui", "web"])
    def test_cycle(self):
        with self.assertRaises(CycleError):
            build_order({"a": ["b"], "b": ["c"], "c": ["a"]})
    def test_empty(self):
        self.assertEqual(build_order({}), [])
