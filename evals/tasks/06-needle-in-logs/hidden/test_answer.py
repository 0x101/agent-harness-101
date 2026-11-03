import unittest

class T(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(open("answer.txt").read().strip(), "req-7f3a9c21")
