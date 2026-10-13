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
        out = json.loads(exporter.export_records(*[[{'id': 648, 'title': ' Budget, \t draft  ', 'owner': 'eli', 'project': 'eos', 'status': 'active', 'amount': '220.92', 'confidential': False, 'created': '2026-05-10', 'region': 'us'}, {'id': 500, 'title': '  Vendor  list  ', 'owner': 'dara', 'project': 'eos', 'status': 'active', 'amount': '685', 'confidential': False, 'created': '2026-02-13', 'region': 'us'}, {'id': 825, 'title': 'Audit  prep  ', 'owner': 'eli', 'project': 'eos', 'status': 'active', 'amount': '188', 'confidential': False, 'created': '2026-03-06', 'region': 'us'}, {'id': 120, 'title': ' Roadmap', 'owner': 'ana', 'project': 'apollo', 'status': 'active', 'amount': '594.5', 'confidential': False, 'created': '2026-05-21', 'region': 'uk'}, {'id': 711, 'title': 'Notes "final"', 'owner': 'eli', 'project': 'cygnus', 'status': 'active', 'amount': '276.5', 'confidential': False, 'created': '2026-01-28', 'region': 'apac'}, {'id': 307, 'title': 'Roadmap', 'owner': 'eli', 'project': 'eos', 'status': 'active', 'amount': '577.2', 'confidential': False, 'created': '2026-08-04', 'region': 'US'}], {'name': 'ben', 'role': 'admin', 'projects': ['eos'], 'regions': ['EU', 'uk']}, {'include_archived': False, 'since': '2026-04-03'}]))
        self.assertEqual(out.get('records'), [{'id': 120, 'title': 'Roadmap', 'owner': 'ana', 'amount': '594.5', 'project': 'apollo'}, {'id': 307, 'title': 'Roadmap', 'owner': 'eli', 'amount': '577.2', 'project': 'eos'}, {'id': 648, 'title': 'Budget, draft', 'owner': 'eli', 'amount': '220.92', 'project': 'eos'}])

    def test_format_2(self):
        out = json.loads(exporter.export_records(*[[{'id': 300, 'title': '\tAudit  prep  ', 'owner': 'eli', 'project': 'delta', 'status': 'active', 'amount': '469.7', 'confidential': False, 'created': '2026-03-16', 'region': 'us'}, {'id': 407, 'title': '\tRisk log  ', 'owner': 'chen', 'project': 'delta', 'status': 'active', 'amount': '9.12', 'confidential': False, 'created': '2026-08-26', 'region': 'us'}, {'id': 664, 'title': ' Audit  prep  ', 'owner': 'chen', 'project': 'delta', 'status': 'active', 'amount': '262.2', 'confidential': False, 'created': '2026-01-25', 'region': 'us'}, {'id': 684, 'title': 'Q3 report', 'owner': 'fay', 'project': 'apollo', 'status': 'archived', 'amount': '532.75', 'confidential': False, 'created': '2026-01-17', 'region': 'ch'}, {'id': 403, 'title': 'Roadmap', 'owner': 'dara', 'project': 'apollo', 'status': 'archived', 'amount': '148.20', 'confidential': True, 'created': '2026-03-10', 'region': 'UK'}, {'id': 541, 'title': 'Q3 report', 'owner': 'fay', 'project': 'borealis', 'status': 'archived', 'amount': '566.1', 'confidential': False, 'created': '2026-03-14', 'region': 'UK'}], {'name': 'ana', 'role': 'admin', 'projects': ['delta', 'eos'], 'regions': ['APAC', 'US']}, {'since': '2026-03-01'}]))
        self.assertEqual(out.get('records'), [{'id': 300, 'title': 'Audit prep', 'owner': 'eli', 'amount': '469.7', 'project': 'delta'}, {'id': 407, 'title': 'Risk log', 'owner': 'chen', 'amount': '9.12', 'project': 'delta'}])

    def test_region_3(self):
        out = json.loads(exporter.export_records(*[[{'id': 944, 'title': 'Budget, draft', 'owner': 'chen', 'project': 'borealis', 'status': 'active', 'amount': '595.51', 'confidential': False, 'created': '2026-02-05', 'region': 'ch'}, {'id': 386, 'title': 'Notes "final"', 'owner': 'fay', 'project': 'borealis', 'status': 'active', 'amount': '501.75', 'confidential': False, 'created': '2026-07-07', 'region': 'ch'}, {'id': 258, 'title': '  Vendor  list ', 'owner': 'ana', 'project': 'borealis', 'status': 'active', 'amount': '182.43', 'confidential': False, 'created': '2026-05-26', 'region': 'EU'}], {'name': 'chen', 'role': 'member', 'projects': ['borealis'], 'regions': ['UK', 'US']}, {'include_archived': True, 'purpose': 'report', 'since': '2026-04-25'}]))
        self.assertEqual(out.get('records'), [{'id': 258, 'title': 'Vendor list', 'owner': 'ana', 'amount': '182.43', 'project': 'borealis'}, {'id': 386, 'title': 'Notes "final"', 'owner': 'fay', 'amount': '501.75', 'project': 'borealis'}])

    def test_region_4(self):
        out = json.loads(exporter.export_records(*[[{'id': 709, 'title': 'Budget, draft', 'owner': 'ana', 'project': 'borealis', 'status': 'active', 'amount': '713.77', 'confidential': False, 'created': '2026-08-09', 'region': 'CH'}, {'id': 425, 'title': 'Audit prep ', 'owner': 'fay', 'project': 'borealis', 'status': 'active', 'amount': '424.4', 'confidential': False, 'created': '2026-04-11', 'region': 'CH'}, {'id': 613, 'title': 'Hiring plan, v2', 'owner': 'ana', 'project': 'borealis', 'status': 'archived', 'amount': '793', 'confidential': False, 'created': '2026-06-28', 'region': 'ch'}], {'name': 'chen', 'role': 'member', 'projects': ['borealis'], 'regions': []}, {'purpose': 'audit', 'since': '2026-03-16', 'max_records': 3}]))
        self.assertEqual(out.get('records'), [{'id': 425, 'title': 'Audit prep', 'owner': 'fay', 'amount': '424.4', 'project': 'borealis'}, {'id': 709, 'title': 'Budget, draft', 'owner': 'ana', 'amount': '713.77', 'project': 'borealis'}])


if __name__ == "__main__":
    unittest.main()
