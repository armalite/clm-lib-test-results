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
        out = json.loads(exporter.export_records(*[[{'id': 289, 'title': '\tNotes "final" ', 'owner': 'chen', 'project': 'apollo', 'status': 'active', 'amount': '650.43', 'confidential': False, 'created': '2026-06-19', 'region': 'us', 'updated': '2026-09-26'}, {'id': 840, 'title': 'Vendor \t list ', 'owner': 'eli', 'project': 'apollo', 'status': 'active', 'amount': '50.07', 'confidential': False, 'created': '2026-02-01', 'region': 'us', 'updated': '2026-02-15'}, {'id': 405, 'title': '  The "north" plan ', 'owner': 'ana', 'project': 'apollo', 'status': 'active', 'amount': '670', 'confidential': False, 'created': '2026-01-23', 'region': 'us', 'updated': '2026-06-13'}, {'id': 652, 'title': 'The "north" plan', 'owner': 'ana', 'project': 'borealis', 'status': 'active', 'amount': '574.74', 'confidential': True, 'created': '2026-05-22', 'region': 'eu'}, {'id': 380, 'title': '\tRisk   log  ', 'owner': 'ben', 'project': 'cygnus', 'status': 'archived', 'amount': '158.56', 'confidential': False, 'created': '2026-03-13', 'region': 'ch', 'updated': '2026-03-15'}, {'id': 863, 'title': 'Vendor  list', 'owner': 'eli', 'project': 'borealis', 'status': 'active', 'amount': '611.84', 'confidential': False, 'created': '2026-04-26', 'region': 'uk', 'updated': '2026-04-26'}], {'name': 'chen', 'role': 'member', 'projects': ['apollo', 'eos'], 'regions': ['ch', 'us']}, {'include_archived': True, 'max_records': 3}]))
        self.assertEqual(out.get('records'), [{'id': 289, 'title': 'Notes "final"', 'owner': 'chen', 'amount': '650.43', 'project': 'apollo'}, {'id': 405, 'title': 'The "north" plan', 'owner': 'ana', 'amount': '670', 'project': 'apollo'}, {'id': 840, 'title': 'Vendor \t list', 'owner': 'eli', 'amount': '50.07', 'project': 'apollo'}])

    def test_format_2(self):
        out = json.loads(exporter.export_records(*[[{'id': 157, 'title': 'Hiring plan, v2', 'owner': 'ben', 'project': 'eos', 'status': 'active', 'amount': '298', 'confidential': False, 'created': '2026-04-12', 'region': 'us', 'updated': '2026-04-20'}, {'id': 147, 'title': 'Notes "final"', 'owner': 'eli', 'project': 'eos', 'status': 'active', 'amount': '502.25', 'confidential': False, 'created': '2026-05-13', 'region': 'us', 'updated': '2026-07-22'}, {'id': 988, 'title': ' Notes "final"', 'owner': 'fay', 'project': 'delta', 'status': 'active', 'amount': '449.4', 'confidential': True, 'created': '2026-02-01', 'region': 'uk', 'updated': '2026-09-26'}], {'name': 'eli', 'role': 'member', 'projects': ['eos'], 'regions': ['apac', 'uk']}, {'include_archived': True, 'since': '2026-02-12'}]))
        self.assertEqual(out.get('records'), [{'id': 147, 'title': 'Notes "final"', 'owner': 'eli', 'amount': '502.25', 'project': 'eos'}, {'id': 157, 'title': 'Hiring plan, v2', 'owner': 'ben', 'amount': '298', 'project': 'eos'}])

    def test_by_3(self):
        out = json.loads(exporter.export_records(*[[{'id': 288, 'title': ' Vendor \t list ', 'owner': 'fay', 'project': 'delta', 'status': 'active', 'amount': '754.1', 'confidential': False, 'created': '2026-08-08', 'region': 'us', 'updated': '2026-09-23'}, {'id': 503, 'title': ' Budget,   draft', 'owner': 'dara', 'project': 'delta', 'status': 'active', 'amount': '311', 'confidential': False, 'created': '2026-01-04', 'region': 'us', 'updated': '2026-09-22'}, {'id': 709, 'title': 'Roadmap', 'owner': 'fay', 'project': 'delta', 'status': 'archived', 'amount': '624.5', 'confidential': False, 'created': '2026-06-19', 'region': 'eu'}, {'id': 365, 'title': 'Audit prep', 'owner': 'fay', 'project': 'eos', 'status': 'archived', 'amount': '172.99', 'confidential': False, 'created': '2026-08-10', 'region': 'us', 'updated': '2026-09-25'}, {'id': 608, 'title': 'Audit  prep ', 'owner': 'chen', 'project': 'apollo', 'status': 'active', 'amount': '713', 'confidential': False, 'created': '2026-07-09', 'region': 'uk'}], {'name': 'ana', 'role': 'admin', 'projects': ['delta'], 'regions': []}, {'max_records': 1}]))
        self.assertEqual(out.get('exported_by'), None)

    def test_by_4(self):
        out = json.loads(exporter.export_records(*[[{'id': 731, 'title': 'The "north"   plan', 'owner': 'chen', 'project': 'eos', 'status': 'active', 'amount': '185.4', 'confidential': False, 'created': '2026-08-07', 'region': 'us', 'updated': '2026-08-23'}, {'id': 97, 'title': 'Budget,  draft  ', 'owner': 'ana', 'project': 'eos', 'status': 'active', 'amount': '491.17', 'confidential': False, 'created': '2026-02-19', 'region': 'us'}, {'id': 744, 'title': '  The "north"   plan  ', 'owner': 'dara', 'project': 'eos', 'status': 'active', 'amount': '457.9', 'confidential': False, 'created': '2026-04-10', 'region': 'us', 'updated': '2026-05-10'}, {'id': 62, 'title': 'Vendor list', 'owner': 'chen', 'project': 'borealis', 'status': 'active', 'amount': '576.9', 'confidential': False, 'created': '2026-07-11', 'region': 'ch', 'updated': '2026-07-17'}, {'id': 546, 'title': 'Risk log ', 'owner': 'fay', 'project': 'apollo', 'status': 'active', 'amount': '319.50', 'confidential': True, 'created': '2026-01-09', 'region': 'uk'}, {'id': 829, 'title': 'Vendor list', 'owner': 'ben', 'project': 'apollo', 'status': 'active', 'amount': '582', 'confidential': False, 'created': '2026-07-19', 'region': 'apac', 'updated': '2026-07-19'}], {'name': 'ana', 'role': 'admin', 'projects': ['eos'], 'regions': []}, {'include_archived': False, 'since': '2026-07-16'}]))
        self.assertEqual(out.get('exported_by'), None)


if __name__ == "__main__":
    unittest.main()
