"""Visible tests for the requirements in force after stage 4.

Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import unittest

import invoice


class TestInvoice(unittest.TestCase):
    maxDiff = None

    def test_round_1(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-858', 'qty': 1, 'unit_price': '16.545'}, {'sku': 'SKU-209', 'qty': 8, 'unit_price': '19.477'}, {'sku': 'SKU-261', 'qty': 2, 'unit_price': '11.795'}], {'tier': 'standard', 'region': 'AU'}]), {'subtotal': '195.95', 'discount': '0.00', 'tax': '19.60', 'total': '215.55'})

    def test_round_2(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-967', 'qty': 7, 'unit_price': '27.965'}, {'sku': 'SKU-155', 'qty': 7, 'unit_price': '5.937'}, {'sku': 'SKU-261', 'qty': 1, 'unit_price': '29.947'}], {'tier': 'standard', 'region': 'AU'}]), {'subtotal': '267.26', 'discount': '0.00', 'tax': '26.73', 'total': '293.99'})

    def test_tax_3(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-585', 'qty': 4, 'unit_price': '37.17'}, {'sku': 'SKU-715', 'qty': 5, 'unit_price': '10.86'}], {'tier': 'standard', 'region': 'JP'}]), {'subtotal': '202.98', 'discount': '0.00', 'tax': '24.36', 'total': '227.34'})

    def test_tax_4(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-359', 'qty': 8, 'unit_price': '83.32'}, {'sku': 'SKU-845', 'qty': 2, 'unit_price': '46.61'}], {'tier': 'standard', 'region': 'AU'}]), {'subtotal': '759.78', 'discount': '0.00', 'tax': '75.98', 'total': '835.76'})

    def test_tier_5(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-150', 'qty': 8, 'unit_price': '58.44'}, {'sku': 'SKU-679', 'qty': 3, 'unit_price': '89.36'}], {'tier': 'silver', 'region': 'US'}]), {'subtotal': '735.60', 'discount': '14.71', 'tax': '0.00', 'total': '720.89'})

    def test_tier_6(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-511', 'qty': 2, 'unit_price': '79.36'}, {'sku': 'SKU-729', 'qty': 3, 'unit_price': '62.44'}], {'tier': 'gold', 'region': 'US'}]), {'subtotal': '346.04', 'discount': '17.30', 'tax': '0.00', 'total': '328.74'})

    def test_bulk_7(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-682', 'qty': 60, 'unit_price': '5.02'}, {'sku': 'SKU-356', 'qty': 2, 'unit_price': '64.51'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '415.16', 'discount': '0.00', 'tax': '0.00', 'total': '415.16'})

    def test_bulk_8(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-744', 'qty': 250, 'unit_price': '6.19'}, {'sku': 'SKU-372', 'qty': 3, 'unit_price': '44.69'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '1495.87', 'discount': '0.00', 'tax': '0.00', 'total': '1495.87'})

    def test_exempt_9(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-973', 'qty': 4, 'unit_price': '75.96'}, {'sku': 'SKU-223', 'qty': 6, 'unit_price': '30.58'}], {'tier': 'standard', 'region': 'AU', 'tax_exempt': True}]), {'subtotal': '487.32', 'discount': '0.00', 'tax': '0.00', 'total': '487.32'})

    def test_exempt_10(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-713', 'qty': 1, 'unit_price': '75.91'}, {'sku': 'SKU-179', 'qty': 2, 'unit_price': '36.21'}], {'tier': 'standard', 'region': 'AU', 'tax_exempt': True}]), {'subtotal': '148.33', 'discount': '0.00', 'tax': '0.00', 'total': '148.33'})

    def test_validate_11(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[{'sku': 'SKU-631', 'qty': 0, 'unit_price': '40.34'}, {'sku': 'SKU-153', 'qty': 3, 'unit_price': '9.23'}], {'tier': 'standard', 'region': 'US'}])

    def test_validate_12(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[{'sku': 'SKU-906', 'qty': 5, 'unit_price': '-10.00'}, {'sku': 'SKU-710', 'qty': 4, 'unit_price': '48.31'}], {'tier': 'standard', 'region': 'US'}])

    def test_format_13(self):
        self.assertEqual(invoice.format_money(*['79124.47', 'NZD']), 'NZ$79124.47')

    def test_format_14(self):
        self.assertEqual(invoice.format_money(*['730.8', 'AUD']), 'A$730.80')


if __name__ == "__main__":
    unittest.main()
