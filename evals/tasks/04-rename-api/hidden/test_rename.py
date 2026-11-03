import pathlib, re, unittest, warnings
from users import core, billing, emails, admin, reports, search

class T(unittest.TestCase):
    def test_new_name(self):
        self.assertEqual(core.get_user(1)["name"], "Ada")
    def test_alias_warns(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            self.assertEqual(core.get_usr(2)["name"], "Grace")
        self.assertTrue(any(issubclass(x.category, DeprecationWarning) for x in w))
    def test_callers_updated(self):
        for f in pathlib.Path("users").glob("*.py"):
            if f.name == "core.py":
                continue
            self.assertNotRegex(f.read_text(), r"get_usr\b", f.name)
        self.assertEqual(billing.billing_name(1), "Ada")
        self.assertTrue(search.search_exists(2))
        self.assertFalse(admin.admin_exists(9))
