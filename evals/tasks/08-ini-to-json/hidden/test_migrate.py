import json, subprocess, sys, unittest

EXPECTED = {
    "app": {"name": "harness-lab", "debug": False, "workers": 4},
    "database": {
        "primary": {"host": "db1.internal", "port": 5432, "ssl": True},
        "replica": {"host": "db2.internal", "port": 5433, "ssl": False},
    },
    "features": {"search": {"enabled": True, "index": "products_v2"}},
}

class T(unittest.TestCase):
    def test_migrate(self):
        p = subprocess.run([sys.executable, "migrate.py"], capture_output=True, text=True, timeout=60)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(json.load(open("config.json")), EXPECTED)
