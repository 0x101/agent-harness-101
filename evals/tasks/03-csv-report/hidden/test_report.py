import csv, json, subprocess, sys, unittest
from collections import defaultdict

class T(unittest.TestCase):
    def test_summary(self):
        out = subprocess.run([sys.executable, "report.py"], capture_output=True, text=True, timeout=60)
        self.assertEqual(out.returncode, 0, out.stderr)
        exp = defaultdict(lambda: {"orders": 0, "total": 0.0})
        for r in csv.DictReader(open("sales.csv")):
            exp[r["region"]]["orders"] += 1
            exp[r["region"]]["total"] += float(r["amount"])
        got = json.load(open("summary.json"))
        self.assertEqual(set(got), set(exp))
        for k, v in exp.items():
            self.assertEqual(got[k]["orders"], v["orders"])
            self.assertAlmostEqual(got[k]["total"], round(v["total"], 2), places=2)
        top = max(exp, key=lambda k: exp[k]["total"])
        self.assertIn(top, out.stdout)
