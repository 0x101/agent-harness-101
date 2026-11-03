import unittest
from lru import LRUCache

class T(unittest.TestCase):
    def test_read_refreshes(self):
        c = LRUCache(2); c.put("a", 1); c.put("b", 2); c.get("a"); c.put("c", 3)
        self.assertEqual(c.get("a"), 1); self.assertIsNone(c.get("b"))
    def test_update_existing(self):
        c = LRUCache(2); c.put("a", 1); c.put("a", 2); c.put("b", 3)
        self.assertEqual(len(c), 2); self.assertEqual(c.get("a"), 2); self.assertEqual(c.get("b"), 3)
    def test_update_refreshes(self):
        c = LRUCache(2); c.put("a", 1); c.put("b", 2); c.put("a", 9); c.put("c", 3)
        self.assertEqual(c.get("a"), 9); self.assertIsNone(c.get("b"))
    def test_capacity(self):
        c = LRUCache(3)
        for i in range(10): c.put(i, i)
        self.assertEqual(len(c), 3); self.assertEqual(sorted(c.data), [7, 8, 9])
