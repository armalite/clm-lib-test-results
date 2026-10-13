"""Visible tests for the rules introduced or changed in stage 5 only.

Earlier rules still apply; they are not repeated here.
Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import json
import unittest

import exporter


class TestStage(unittest.TestCase):
    maxDiff = None

    def test_limit_1(self):
        out = json.loads(exporter.export_records(*[[{'id': 645, 'title': 'Hiring plan, v2', 'owner': 'chen', 'project': 'delta', 'status': 'active', 'amount': '229.2', 'confidential': False, 'created': '2026-04-19'}, {'id': 781, 'title': 'Ops review', 'owner': 'chen', 'project': 'delta', 'status': 'active', 'amount': '628.65', 'confidential': False, 'created': '2026-06-27'}, {'id': 872, 'title': 'Vendor list', 'owner': 'eli', 'project': 'delta', 'status': 'active', 'amount': '803.5', 'confidential': False, 'created': '2026-01-10'}], {'name': 'dara', 'role': 'member', 'projects': ['delta', 'eos']}, {'max_records': 3}]))
        self.assertEqual(out['records'], [{'id': 645, 'title': 'Hiring plan, v2', 'owner': 'chen', 'amount': '229.2'}, {'id': 781, 'title': 'Ops review', 'owner': 'chen', 'amount': '628.65'}, {'id': 872, 'title': 'Vendor list', 'owner': 'eli', 'amount': '803.5'}])
        self.assertEqual(out['truncated'], False)

    def test_limit_2(self):
        out = json.loads(exporter.export_records(*[[{'id': 908, 'title': 'Notes "final"', 'owner': 'dara', 'project': 'borealis', 'status': 'active', 'amount': '68.98', 'confidential': False, 'created': '2026-08-03'}, {'id': 411, 'title': 'Notes "final"', 'owner': 'ana', 'project': 'borealis', 'status': 'active', 'amount': '283.8', 'confidential': False, 'created': '2026-03-11'}, {'id': 211, 'title': 'Vendor list', 'owner': 'eli', 'project': 'borealis', 'status': 'active', 'amount': '273.2', 'confidential': False, 'created': '2026-05-09'}, {'id': 715, 'title': 'Audit prep', 'owner': 'eli', 'project': 'borealis', 'status': 'active', 'amount': '630.77', 'confidential': False, 'created': '2026-01-02'}, {'id': 683, 'title': 'The "north" plan', 'owner': 'fay', 'project': 'borealis', 'status': 'active', 'amount': '49.86', 'confidential': False, 'created': '2026-05-03'}, {'id': 685, 'title': 'Roadmap', 'owner': 'dara', 'project': 'borealis', 'status': 'active', 'amount': '543.29', 'confidential': False, 'created': '2026-04-25'}], {'name': 'chen', 'role': 'member', 'projects': ['borealis']}, {'purpose': 'audit', 'max_records': 1}]))
        self.assertEqual(out['records'], [{'id': 211, 'title': 'Vendor list', 'owner': 'eli', 'amount': '273.2'}])
        self.assertEqual(out['truncated'], True)


if __name__ == "__main__":
    unittest.main()
