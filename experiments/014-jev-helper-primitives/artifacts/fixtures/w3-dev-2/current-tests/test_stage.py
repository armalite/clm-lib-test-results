"""Visible tests for the rules introduced or changed in stage 7 only.

Earlier rules still apply; they are not repeated here.
Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import json
import unittest

import exporter


class TestStage(unittest.TestCase):
    maxDiff = None

    def test_format_1(self):
        out = json.loads(exporter.export_records(*[[{'id': 759, 'title': 'Vendor list', 'owner': 'ana', 'project': 'borealis', 'status': 'active', 'amount': '581.5', 'confidential': False, 'created': '2026-08-20', 'region': 'us'}, {'id': 413, 'title': 'The "north" plan', 'owner': 'eli', 'project': 'borealis', 'status': 'active', 'amount': '697.5', 'confidential': False, 'created': '2026-07-09', 'region': 'us'}, {'id': 43, 'title': 'Budget, draft', 'owner': 'dara', 'project': 'borealis', 'status': 'active', 'amount': '788.80', 'confidential': False, 'created': '2026-03-28', 'region': 'us', 'updated': '2026-04-01'}, {'id': 948, 'title': '\tBudget, draft ', 'owner': 'fay', 'project': 'delta', 'status': 'active', 'amount': '299', 'confidential': False, 'created': '2026-02-19', 'region': 'uk', 'updated': '2026-09-04'}], {'name': 'ben', 'role': 'admin', 'projects': ['borealis'], 'regions': ['uk']}, {'since': '2026-05-13', 'max_records': 3}]))
        self.assertEqual(out.get('records'), [{'id': 413, 'title': 'The "north" plan', 'owner': 'eli', 'amount': '697.5', 'project': 'borealis'}, {'id': 759, 'title': 'Vendor list', 'owner': 'ana', 'amount': '581.5', 'project': 'borealis'}, {'id': 948, 'title': 'Budget, draft', 'owner': 'fay', 'amount': '299', 'project': 'delta'}])

    def test_format_2(self):
        out = json.loads(exporter.export_records(*[[{'id': 682, 'title': 'Vendor \t list ', 'owner': 'eli', 'project': 'cygnus', 'status': 'active', 'amount': '833.65', 'confidential': False, 'created': '2026-08-13', 'region': 'us', 'updated': '2026-09-02'}, {'id': 430, 'title': 'Ops review', 'owner': 'dara', 'project': 'cygnus', 'status': 'active', 'amount': '119', 'confidential': False, 'created': '2026-04-12', 'region': 'us', 'updated': '2026-09-16'}, {'id': 355, 'title': '  Hiring plan, v2', 'owner': 'chen', 'project': 'apollo', 'status': 'active', 'amount': '76.79', 'confidential': True, 'created': '2026-08-18', 'region': 'apac'}, {'id': 127, 'title': 'Budget,  draft ', 'owner': 'eli', 'project': 'apollo', 'status': 'active', 'amount': '835.0', 'confidential': True, 'created': '2026-04-28', 'region': 'us', 'updated': '2026-08-18'}, {'id': 259, 'title': ' Notes "final" ', 'owner': 'ana', 'project': 'borealis', 'status': 'active', 'amount': '315.91', 'confidential': False, 'created': '2026-05-27', 'region': 'uk', 'updated': '2026-09-16'}], {'name': 'fay', 'role': 'admin', 'projects': ['cygnus', 'delta'], 'regions': ['ch', 'eu']}, {'include_archived': True}]))
        self.assertEqual(out.get('records'), [{'id': 259, 'title': 'Notes "final"', 'owner': 'ana', 'amount': '315.91', 'project': 'borealis'}, {'id': 430, 'title': 'Ops review', 'owner': 'dara', 'amount': '119', 'project': 'cygnus'}, {'id': 682, 'title': 'Vendor \t list', 'owner': 'eli', 'amount': '833.65', 'project': 'cygnus'}])

    def test_by_3(self):
        out = json.loads(exporter.export_records(*[[{'id': 565, 'title': 'The "north" plan', 'owner': 'dara', 'project': 'borealis', 'status': 'active', 'amount': '358.25', 'confidential': False, 'created': '2026-04-23', 'region': 'us', 'updated': '2026-05-01'}, {'id': 68, 'title': 'Notes "final"', 'owner': 'fay', 'project': 'borealis', 'status': 'active', 'amount': '347.42', 'confidential': False, 'created': '2026-06-03', 'region': 'us', 'updated': '2026-08-27'}, {'id': 848, 'title': '  Roadmap  ', 'owner': 'eli', 'project': 'delta', 'status': 'active', 'amount': '634.75', 'confidential': True, 'created': '2026-07-07', 'region': 'apac', 'updated': '2026-07-10'}, {'id': 374, 'title': '  Ops review ', 'owner': 'dara', 'project': 'delta', 'status': 'active', 'amount': '130.49', 'confidential': True, 'created': '2026-07-04', 'region': 'us'}], {'name': 'dara', 'role': 'admin', 'projects': ['borealis'], 'regions': ['apac']}, {}]))
        self.assertEqual(out.get('exported_by'), None)

    def test_by_4(self):
        out = json.loads(exporter.export_records(*[[{'id': 745, 'title': 'Vendor list', 'owner': 'ben', 'project': 'delta', 'status': 'active', 'amount': '819.45', 'confidential': False, 'created': '2026-07-17', 'region': 'us'}, {'id': 963, 'title': 'Q3 report ', 'owner': 'ben', 'project': 'delta', 'status': 'active', 'amount': '52.18', 'confidential': False, 'created': '2026-07-11', 'region': 'us'}, {'id': 8, 'title': 'Q3 report', 'owner': 'fay', 'project': 'cygnus', 'status': 'active', 'amount': '467.61', 'confidential': False, 'created': '2026-04-05', 'region': 'eu', 'updated': '2026-09-13'}, {'id': 180, 'title': 'Audit prep  ', 'owner': 'chen', 'project': 'borealis', 'status': 'active', 'amount': '814', 'confidential': True, 'created': '2026-02-19', 'region': 'eu'}], {'name': 'dara', 'role': 'admin', 'projects': ['delta', 'eos'], 'regions': []}, {'include_archived': True, 'since': '2026-02-16'}]))
        self.assertEqual(out.get('exported_by'), None)


if __name__ == "__main__":
    unittest.main()
