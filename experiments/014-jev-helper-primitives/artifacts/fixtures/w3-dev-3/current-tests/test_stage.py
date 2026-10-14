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
        out = json.loads(exporter.export_records(*[[{'id': 343, 'title': '  Notes "final" ', 'owner': 'fay', 'project': 'apollo', 'status': 'active', 'amount': '264.56', 'confidential': False, 'created': '2026-06-16', 'region': 'us'}, {'id': 528, 'title': '\tQ3 report  ', 'owner': 'chen', 'project': 'apollo', 'status': 'active', 'amount': '477.27', 'confidential': False, 'created': '2026-06-07', 'region': 'us'}, {'id': 224, 'title': 'Q3 report', 'owner': 'ben', 'project': 'eos', 'status': 'active', 'amount': '744.5', 'confidential': False, 'created': '2026-07-09', 'region': 'APAC'}, {'id': 329, 'title': '  Vendor  list  ', 'owner': 'eli', 'project': 'borealis', 'status': 'archived', 'amount': '435', 'confidential': False, 'created': '2026-08-09', 'region': 'ch'}], {'name': 'eli', 'role': 'member', 'projects': ['apollo', 'eos'], 'regions': []}, {'since': '2026-03-10'}]))
        self.assertEqual(out.get('records'), [{'id': 224, 'title': 'Q3 report', 'owner': 'ben', 'amount': '744.5', 'project': 'eos'}, {'id': 343, 'title': 'Notes "final"', 'owner': 'fay', 'amount': '264.56', 'project': 'apollo'}, {'id': 528, 'title': 'Q3 report', 'owner': 'chen', 'amount': '477.27', 'project': 'apollo'}])

    def test_format_2(self):
        out = json.loads(exporter.export_records(*[[{'id': 512, 'title': 'The "north" plan', 'owner': 'fay', 'project': 'apollo', 'status': 'active', 'amount': '894.0', 'confidential': False, 'created': '2026-08-24', 'region': 'us'}, {'id': 208, 'title': 'Notes "final"', 'owner': 'ben', 'project': 'apollo', 'status': 'active', 'amount': '48', 'confidential': False, 'created': '2026-02-09', 'region': 'us'}, {'id': 413, 'title': ' Risk \t log  ', 'owner': 'eli', 'project': 'eos', 'status': 'archived', 'amount': '106.56', 'confidential': True, 'created': '2026-04-08', 'region': 'apac'}, {'id': 102, 'title': ' Audit prep  ', 'owner': 'ben', 'project': 'delta', 'status': 'archived', 'amount': '633', 'confidential': True, 'created': '2026-01-21', 'region': 'US'}, {'id': 168, 'title': '\tThe  "north" plan', 'owner': 'fay', 'project': 'delta', 'status': 'active', 'amount': '8.1', 'confidential': False, 'created': '2026-06-20', 'region': 'US'}], {'name': 'ben', 'role': 'member', 'projects': ['apollo'], 'regions': []}, {'since': '2026-07-04', 'max_records': 1}]))
        self.assertEqual(out.get('records'), [{'id': 512, 'title': 'The "north" plan', 'owner': 'fay', 'amount': '894.0', 'project': 'apollo'}])

    def test_region_3(self):
        out = json.loads(exporter.export_records(*[[{'id': 306, 'title': 'Ops review', 'owner': 'dara', 'project': 'cygnus', 'status': 'active', 'amount': '846.06', 'confidential': False, 'created': '2026-03-07', 'region': 'eu'}, {'id': 229, 'title': 'Ops review', 'owner': 'dara', 'project': 'cygnus', 'status': 'active', 'amount': '404.7', 'confidential': False, 'created': '2026-01-11', 'region': 'eu'}, {'id': 73, 'title': '  Notes "final"  ', 'owner': 'ben', 'project': 'borealis', 'status': 'active', 'amount': '540.3', 'confidential': True, 'created': '2026-02-18', 'region': 'us'}, {'id': 888, 'title': 'Budget, draft  ', 'owner': 'fay', 'project': 'eos', 'status': 'active', 'amount': '823.5', 'confidential': False, 'created': '2026-01-21', 'region': 'eu'}], {'name': 'eli', 'role': 'admin', 'projects': ['cygnus', 'delta'], 'regions': []}, {'include_archived': True, 'since': '2026-02-14', 'max_records': 3}]))
        self.assertEqual(out.get('records'), [{'id': 306, 'title': 'Ops review', 'owner': 'dara', 'amount': '846.06', 'project': 'cygnus'}])

    def test_region_4(self):
        out = json.loads(exporter.export_records(*[[{'id': 466, 'title': 'Notes "final"', 'owner': 'dara', 'project': 'delta', 'status': 'active', 'amount': '403', 'confidential': False, 'created': '2026-03-20', 'region': 'EU'}, {'id': 409, 'title': '\tQ3   report  ', 'owner': 'chen', 'project': 'delta', 'status': 'active', 'amount': '162', 'confidential': False, 'created': '2026-06-21', 'region': 'eu'}, {'id': 372, 'title': ' Ops   review', 'owner': 'dara', 'project': 'apollo', 'status': 'active', 'amount': '584', 'confidential': False, 'created': '2026-01-16', 'region': 'eu'}, {'id': 405, 'title': 'Notes "final"', 'owner': 'chen', 'project': 'borealis', 'status': 'active', 'amount': '183.47', 'confidential': False, 'created': '2026-04-08', 'region': 'ch'}, {'id': 742, 'title': 'Roadmap', 'owner': 'ben', 'project': 'delta', 'status': 'active', 'amount': '804', 'confidential': False, 'created': '2026-08-19', 'region': 'UK'}], {'name': 'fay', 'role': 'member', 'projects': ['delta'], 'regions': []}, {'purpose': 'report', 'since': '2026-04-03', 'max_records': 1}]))
        self.assertEqual(out.get('records'), [{'id': 409, 'title': 'Q3 report', 'owner': 'chen', 'amount': '162', 'project': 'delta'}])


if __name__ == "__main__":
    unittest.main()
