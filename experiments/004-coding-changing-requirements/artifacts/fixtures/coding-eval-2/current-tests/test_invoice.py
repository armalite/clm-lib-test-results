"""Visible tests for the requirements in force after stage 4.

Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import unittest

import invoice


class TestInvoice(unittest.TestCase):
    maxDiff = None

    def test_round_1(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-783', 'qty': 7, 'unit_price': '17.097'}, {'sku': 'SKU-570', 'qty': 8, 'unit_price': '8.527'}, {'sku': 'SKU-946', 'qty': 3, 'unit_price': '15.885'}], {'tier': 'standard', 'region': 'AU'}]), {'subtotal': '235.56', 'discount': '0.00', 'tax': '23.56', 'total': '259.12'})

    def test_round_2(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-811', 'qty': 5, 'unit_price': '4.137'}, {'sku': 'SKU-166', 'qty': 8, 'unit_price': '20.825'}, {'sku': 'SKU-832', 'qty': 5, 'unit_price': '1.137'}], {'tier': 'standard', 'region': 'NZ'}]), {'subtotal': '192.98', 'discount': '0.00', 'tax': '19.30', 'total': '212.28'})

    def test_tax_3(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-645', 'qty': 7, 'unit_price': '59.01'}, {'sku': 'SKU-417', 'qty': 8, 'unit_price': '30.33'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '655.71', 'discount': '0.00', 'tax': '65.57', 'total': '721.28'})

    def test_tax_4(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-517', 'qty': 3, 'unit_price': '69.69'}, {'sku': 'SKU-635', 'qty': 2, 'unit_price': '53.30'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '315.67', 'discount': '0.00', 'tax': '31.57', 'total': '347.24'})

    def test_tier_5(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-965', 'qty': 7, 'unit_price': '61.78'}, {'sku': 'SKU-640', 'qty': 1, 'unit_price': '15.32'}], {'tier': 'platinum', 'region': 'US'}]), {'subtotal': '447.78', 'discount': '44.78', 'tax': '40.30', 'total': '443.30'})

    def test_tier_6(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-663', 'qty': 8, 'unit_price': '52.66'}, {'sku': 'SKU-590', 'qty': 7, 'unit_price': '9.41'}], {'tier': 'silver', 'region': 'US'}]), {'subtotal': '487.15', 'discount': '14.61', 'tax': '47.25', 'total': '519.79'})

    def test_bulk_7(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-925', 'qty': 250, 'unit_price': '4.68'}, {'sku': 'SKU-247', 'qty': 7, 'unit_price': '16.42'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '1167.94', 'discount': '0.00', 'tax': '116.79', 'total': '1284.73'})

    def test_bulk_8(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-192', 'qty': 120, 'unit_price': '2.09'}, {'sku': 'SKU-169', 'qty': 8, 'unit_price': '43.53'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '573.96', 'discount': '0.00', 'tax': '57.40', 'total': '631.36'})

    def test_exempt_9(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-403', 'qty': 2, 'unit_price': '7.97'}, {'sku': 'SKU-976', 'qty': 1, 'unit_price': '33.17'}], {'tier': 'standard', 'region': 'AU', 'tax_exempt': True}]), {'subtotal': '49.11', 'discount': '0.00', 'tax': '0.00', 'total': '49.11'})

    def test_exempt_10(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-331', 'qty': 3, 'unit_price': '14.16'}, {'sku': 'SKU-560', 'qty': 8, 'unit_price': '80.19'}], {'tier': 'standard', 'region': 'AU', 'tax_exempt': True}]), {'subtotal': '684.00', 'discount': '0.00', 'tax': '0.00', 'total': '684.00'})

    def test_validate_11(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[], {'tier': 'standard', 'region': 'US'}])

    def test_validate_12(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[], {'tier': 'standard', 'region': 'US'}])

    def test_format_13(self):
        self.assertEqual(invoice.format_money(*['662.1', 'NZD']), 'NZ$662.10')

    def test_format_14(self):
        self.assertEqual(invoice.format_money(*['35482.10', 'AUD']), 'A$35,482.10')


if __name__ == "__main__":
    unittest.main()
