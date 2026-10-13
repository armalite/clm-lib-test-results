"""Visible tests for the rules introduced or changed in stage 2 only.

Earlier rules still apply; they are not repeated here.
Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import json
import unittest

import exporter


class TestStage(unittest.TestCase):
    maxDiff = None

    def test_format_1(self):
        out = json.loads(exporter.export_records(*[[{'id': 863, 'title': 'Q3 report', 'owner': 'ana', 'project': 'borealis', 'status': 'active', 'amount': '524.73', 'confidential': False, 'created': '2026-03-11'}, {'id': 535, 'title': 'Notes "final"', 'owner': 'ana', 'project': 'borealis', 'status': 'active', 'amount': '771.0', 'confidential': False, 'created': '2026-06-15'}, {'id': 606, 'title': 'Audit prep', 'owner': 'ana', 'project': 'borealis', 'status': 'archived', 'amount': '493.37', 'confidential': True, 'created': '2026-09-15'}, {'id': 973, 'title': 'Audit prep', 'owner': 'ana', 'project': 'borealis', 'status': 'active', 'amount': '880.99', 'confidential': False, 'created': '2026-01-13'}], {'name': 'ben', 'role': 'member', 'projects': ['apollo', 'delta']}, {}]))
        self.assertEqual(out['records'], [])

    def test_format_2(self):
        out = json.loads(exporter.export_records(*[[{'id': 4, 'title': 'Q3 report', 'owner': 'chen', 'project': 'apollo', 'status': 'active', 'amount': '893.25', 'confidential': False, 'created': '2026-07-12'}, {'id': 151, 'title': 'Risk log', 'owner': 'eli', 'project': 'eos', 'status': 'active', 'amount': '733', 'confidential': False, 'created': '2026-08-14'}, {'id': 183, 'title': 'Budget, draft', 'owner': 'ana', 'project': 'delta', 'status': 'active', 'amount': '480.0', 'confidential': False, 'created': '2026-05-12'}, {'id': 512, 'title': 'Q3 report', 'owner': 'ana', 'project': 'cygnus', 'status': 'active', 'amount': '688.0', 'confidential': False, 'created': '2026-07-24'}, {'id': 819, 'title': 'Ops review', 'owner': 'ana', 'project': 'apollo', 'status': 'active', 'amount': '110', 'confidential': False, 'created': '2026-07-15'}], {'name': 'eli', 'role': 'member', 'projects': ['delta', 'eos']}, {}]))
        self.assertEqual(out['records'], [{'id': 151, 'title': 'Risk log', 'owner': 'eli', 'amount': '733'}, {'id': 183, 'title': 'Budget, draft', 'owner': 'ana', 'amount': '480.0'}])


if __name__ == "__main__":
    unittest.main()
