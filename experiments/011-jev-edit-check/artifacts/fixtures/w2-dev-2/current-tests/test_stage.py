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
        out = json.loads(exporter.export_records(*[[{'id': 124, 'title': 'Ops review', 'owner': 'ben', 'project': 'delta', 'status': 'active', 'amount': '763.47', 'confidential': False, 'created': '2026-05-17'}, {'id': 771, 'title': 'Ops review', 'owner': 'chen', 'project': 'delta', 'status': 'active', 'amount': '777.13', 'confidential': False, 'created': '2026-05-19'}, {'id': 45, 'title': 'Roadmap', 'owner': 'ben', 'project': 'delta', 'status': 'active', 'amount': '572', 'confidential': False, 'created': '2026-07-28'}, {'id': 414, 'title': 'Notes "final"', 'owner': 'ben', 'project': 'delta', 'status': 'active', 'amount': '838.3', 'confidential': False, 'created': '2026-08-09'}], {'name': 'fay', 'role': 'member', 'projects': ['delta']}, {'include_archived': False, 'max_records': 1}]))
        self.assertEqual(out['records'], [{'id': 45, 'title': 'Roadmap', 'owner': 'ben', 'amount': '572'}])
        self.assertEqual(out['truncated'], True)

    def test_limit_2(self):
        out = json.loads(exporter.export_records(*[[{'id': 146, 'title': 'Notes "final"', 'owner': 'ben', 'project': 'cygnus', 'status': 'active', 'amount': '606.27', 'confidential': False, 'created': '2026-02-06'}, {'id': 281, 'title': 'Vendor list', 'owner': 'fay', 'project': 'cygnus', 'status': 'active', 'amount': '173', 'confidential': False, 'created': '2026-09-14'}, {'id': 764, 'title': 'Ops review', 'owner': 'ben', 'project': 'cygnus', 'status': 'active', 'amount': '692.06', 'confidential': False, 'created': '2026-02-27'}, {'id': 686, 'title': 'Audit prep', 'owner': 'ben', 'project': 'cygnus', 'status': 'active', 'amount': '885.9', 'confidential': False, 'created': '2026-07-17'}, {'id': 44, 'title': 'Ops review', 'owner': 'chen', 'project': 'cygnus', 'status': 'active', 'amount': '396.67', 'confidential': False, 'created': '2026-01-22'}, {'id': 887, 'title': 'Roadmap', 'owner': 'dara', 'project': 'cygnus', 'status': 'active', 'amount': '40', 'confidential': False, 'created': '2026-09-08'}], {'name': 'dara', 'role': 'member', 'projects': ['cygnus']}, {'max_records': 6}]))
        self.assertEqual(out['records'], [{'id': 44, 'title': 'Ops review', 'owner': 'chen', 'amount': '396.67'}, {'id': 146, 'title': 'Notes "final"', 'owner': 'ben', 'amount': '606.27'}, {'id': 281, 'title': 'Vendor list', 'owner': 'fay', 'amount': '173'}, {'id': 686, 'title': 'Audit prep', 'owner': 'ben', 'amount': '885.9'}, {'id': 764, 'title': 'Ops review', 'owner': 'ben', 'amount': '692.06'}, {'id': 887, 'title': 'Roadmap', 'owner': 'dara', 'amount': '40'}])
        self.assertEqual(out['truncated'], False)


if __name__ == "__main__":
    unittest.main()
