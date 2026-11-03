import unittest
from shop.checkout import total

class T(unittest.TestCase):
    def test_no_code(self):
        self.assertEqual(total([(10.0, 2)]), 21.6)
    def test_welcome(self):
        self.assertEqual(total([(100.0, 1)], "WELCOME10"), 97.2)

if __name__ == "__main__":
    unittest.main()
