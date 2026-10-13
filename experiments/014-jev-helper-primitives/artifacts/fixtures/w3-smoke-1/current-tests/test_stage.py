"""Visible tests for the rules introduced or changed in stage 5 only.

Earlier rules still apply; they are not repeated here.
Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import json
import unittest

import exporter


class TestStage(unittest.TestCase):
    maxDiff = None

    def test_conf_1(self):
        out = json.loads(exporter.export_records(*[[{'id': 938, 'title': ' Vendor list  ', 'owner': 'chen', 'project': 'borealis', 'status': 'active', 'amount': '421.96', 'confidential': True, 'created': '2026-03-11', 'region': 'us'}, {'id': 361, 'title': 'Audit   prep ', 'owner': 'dara', 'project': 'borealis', 'status': 'active', 'amount': '766.1', 'confidential': True, 'created': '2026-04-13', 'region': 'us'}, {'id': 52, 'title': 'Notes "final"', 'owner': 'eli', 'project': 'apollo', 'status': 'active', 'amount': '529', 'confidential': False, 'created': '2026-01-09', 'region': 'apac'}], {'name': 'dara', 'role': 'admin', 'projects': ['borealis', 'eos'], 'regions': ['us']}, {'include_archived': True, 'purpose': 'regulator'}]))
        self.assertEqual(out.get('records'), [{'id': 52, 'title': 'Notes "final"', 'owner': 'eli', 'amount': '529'}, {'id': 361, 'title': 'Audit prep', 'owner': 'dara', 'amount': '766.1'}, {'id': 938, 'title': 'Vendor list', 'owner': 'chen', 'amount': '421.96'}])

    def test_conf_2(self):
        out = json.loads(exporter.export_records(*[[{'id': 553, 'title': ' Budget,   draft ', 'owner': 'eli', 'project': 'apollo', 'status': 'active', 'amount': '371.97', 'confidential': True, 'created': '2026-07-25', 'region': 'us'}, {'id': 486, 'title': ' Notes "final"', 'owner': 'eli', 'project': 'apollo', 'status': 'active', 'amount': '745.55', 'confidential': True, 'created': '2026-02-21', 'region': 'us'}, {'id': 726, 'title': '  Risk \t log ', 'owner': 'eli', 'project': 'borealis', 'status': 'active', 'amount': '66', 'confidential': False, 'created': '2026-04-14', 'region': 'ch'}], {'name': 'ben', 'role': 'admin', 'projects': ['apollo', 'delta'], 'regions': ['eu']}, {'include_archived': True, 'purpose': 'regulator'}]))
        self.assertEqual(out.get('records'), [{'id': 486, 'title': 'Notes "final"', 'owner': 'eli', 'amount': '745.55'}, {'id': 553, 'title': 'Budget, draft', 'owner': 'eli', 'amount': '371.97'}, {'id': 726, 'title': 'Risk log', 'owner': 'eli', 'amount': '66'}])

    def test_by_3(self):
        out = json.loads(exporter.export_records(*[[{'id': 525, 'title': '\tRoadmap  ', 'owner': 'dara', 'project': 'cygnus', 'status': 'active', 'amount': '278', 'confidential': False, 'created': '2026-07-07', 'region': 'us'}, {'id': 29, 'title': '  Notes  "final" ', 'owner': 'chen', 'project': 'cygnus', 'status': 'active', 'amount': '371.5', 'confidential': False, 'created': '2026-01-21', 'region': 'us'}, {'id': 40, 'title': ' Roadmap  ', 'owner': 'chen', 'project': 'eos', 'status': 'archived', 'amount': '559.79', 'confidential': False, 'created': '2026-04-08', 'region': 'ch'}], {'name': 'ana', 'role': 'admin', 'projects': ['cygnus', 'delta'], 'regions': ['apac', 'uk']}, {'purpose': 'regulator'}]))
        self.assertEqual(out.get('exported_by'), None)

    def test_by_4(self):
        out = json.loads(exporter.export_records(*[[{'id': 452, 'title': 'Risk   log ', 'owner': 'ana', 'project': 'delta', 'status': 'active', 'amount': '746.75', 'confidential': False, 'created': '2026-08-04', 'region': 'us'}, {'id': 685, 'title': 'Q3 report', 'owner': 'ben', 'project': 'delta', 'status': 'active', 'amount': '767.7', 'confidential': False, 'created': '2026-06-15', 'region': 'us'}, {'id': 843, 'title': 'Vendor list ', 'owner': 'chen', 'project': 'eos', 'status': 'active', 'amount': '593', 'confidential': False, 'created': '2026-05-06', 'region': 'ch'}], {'name': 'eli', 'role': 'admin', 'projects': ['delta', 'eos'], 'regions': []}, {'purpose': 'audit'}]))
        self.assertEqual(out.get('exported_by'), None)


if __name__ == "__main__":
    unittest.main()
