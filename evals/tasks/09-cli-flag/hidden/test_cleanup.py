import os, subprocess, sys, tempfile, time, unittest

def make(d):
    old = time.time() - 40 * 86400
    for n in ["b.log", "a.log", "keep.log"]:
        p = os.path.join(d, n); open(p, "w").write("x")
        if n != "keep.log":
            os.utime(p, (old, old))

class T(unittest.TestCase):
    def test_dry_run(self):
        d = tempfile.mkdtemp(); make(d)
        p = subprocess.run([sys.executable, "cleanup.py", d, "--dry-run"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(sorted(os.listdir(d)), ["a.log", "b.log", "keep.log"])
        lines = p.stdout.strip().splitlines()
        self.assertEqual(lines, [f"would delete {os.path.join(d, 'a.log')}", f"would delete {os.path.join(d, 'b.log')}"])
    def test_real(self):
        d = tempfile.mkdtemp(); make(d)
        p = subprocess.run([sys.executable, "cleanup.py", d], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(os.listdir(d), ["keep.log"])
