"""Visible tests for the requirements in force after stage 4.

Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import unittest

import invoice


class TestInvoice(unittest.TestCase):
    maxDiff = None

    def test_round_1(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-417', 'qty': 2, 'unit_price': '20.813'}, {'sku': 'SKU-622', 'qty': 7, 'unit_price': '13.943'}, {'sku': 'SKU-800', 'qty': 6, 'unit_price': '7.455'}], {'tier': 'standard', 'region': 'NZ'}]), {'subtotal': '183.96', 'discount': '0.00', 'tax': '27.59', 'total': '211.55'})

    def test_round_2(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-728', 'qty': 4, 'unit_price': '27.185'}, {'sku': 'SKU-968', 'qty': 1, 'unit_price': '27.185'}, {'sku': 'SKU-507', 'qty': 7, 'unit_price': '8.265'}], {'tier': 'standard', 'region': 'AU'}]), {'subtotal': '193.78', 'discount': '0.00', 'tax': '19.38', 'total': '213.16'})

    def test_tax_3(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-758', 'qty': 3, 'unit_price': '88.08'}, {'sku': 'SKU-955', 'qty': 1, 'unit_price': '46.70'}], {'tier': 'standard', 'region': 'NZ'}]), {'subtotal': '310.94', 'discount': '0.00', 'tax': '46.64', 'total': '357.58'})

    def test_tax_4(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-968', 'qty': 6, 'unit_price': '4.78'}, {'sku': 'SKU-456', 'qty': 7, 'unit_price': '43.06'}], {'tier': 'standard', 'region': 'NZ'}]), {'subtotal': '330.10', 'discount': '0.00', 'tax': '49.52', 'total': '379.62'})

    def test_tier_5(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-641', 'qty': 8, 'unit_price': '27.85'}, {'sku': 'SKU-799', 'qty': 8, 'unit_price': '82.50'}], {'tier': 'platinum', 'region': 'US'}]), {'subtotal': '882.80', 'discount': '88.28', 'tax': '0.00', 'total': '794.52'})

    def test_tier_6(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-771', 'qty': 8, 'unit_price': '52.92'}, {'sku': 'SKU-318', 'qty': 6, 'unit_price': '66.56'}], {'tier': 'gold', 'region': 'US'}]), {'subtotal': '822.72', 'discount': '57.59', 'tax': '0.00', 'total': '765.13'})

    def test_bulk_7(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-636', 'qty': 250, 'unit_price': '8.06'}, {'sku': 'SKU-761', 'qty': 5, 'unit_price': '23.19'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '1929.45', 'discount': '0.00', 'tax': '0.00', 'total': '1929.45'})

    def test_bulk_8(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-867', 'qty': 60, 'unit_price': '8.19'}, {'sku': 'SKU-109', 'qty': 6, 'unit_price': '76.22'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '948.72', 'discount': '0.00', 'tax': '0.00', 'total': '948.72'})

    def test_validate_9(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[], {'tier': 'standard', 'region': 'US'}])

    def test_validate_10(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[{'sku': 'SKU-363', 'qty': -2, 'unit_price': '75.47'}, {'sku': 'SKU-370', 'qty': 7, 'unit_price': '71.78'}], {'tier': 'standard', 'region': 'US'}])

    def test_format_11(self):
        self.assertEqual(invoice.format_money(*['89115.73', 'NZD']), 'NZ$89115.73')

    def test_format_12(self):
        self.assertEqual(invoice.format_money(*['700.0', 'USD']), 'US$700.00')


if __name__ == "__main__":
    unittest.main()
