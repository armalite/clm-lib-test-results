"""Visible tests for the requirements in force after stage 4.

Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import unittest

import invoice


class TestInvoice(unittest.TestCase):
    maxDiff = None

    def test_round_1(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-775', 'qty': 3, 'unit_price': '9.635'}, {'sku': 'SKU-681', 'qty': 3, 'unit_price': '8.285'}, {'sku': 'SKU-449', 'qty': 6, 'unit_price': '26.165'}], {'tier': 'standard', 'region': 'NZ'}]), {'subtotal': '210.75', 'discount': '0.00', 'tax': '31.61', 'total': '242.36'})

    def test_round_2(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-302', 'qty': 1, 'unit_price': '8.547'}, {'sku': 'SKU-436', 'qty': 2, 'unit_price': '25.093'}, {'sku': 'SKU-267', 'qty': 7, 'unit_price': '26.467'}], {'tier': 'standard', 'region': 'NZ'}]), {'subtotal': '244.00', 'discount': '0.00', 'tax': '36.60', 'total': '280.60'})

    def test_tax_3(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-462', 'qty': 6, 'unit_price': '16.13'}, {'sku': 'SKU-504', 'qty': 4, 'unit_price': '16.46'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '162.62', 'discount': '0.00', 'tax': '0.00', 'total': '162.62'})

    def test_tax_4(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-815', 'qty': 1, 'unit_price': '70.19'}, {'sku': 'SKU-324', 'qty': 4, 'unit_price': '72.38'}], {'tier': 'standard', 'region': 'AU'}]), {'subtotal': '359.71', 'discount': '0.00', 'tax': '35.97', 'total': '395.68'})

    def test_tier_5(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-992', 'qty': 2, 'unit_price': '56.47'}, {'sku': 'SKU-344', 'qty': 6, 'unit_price': '9.50'}], {'tier': 'gold', 'region': 'US'}]), {'subtotal': '169.94', 'discount': '8.50', 'tax': '0.00', 'total': '161.44'})

    def test_tier_6(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-441', 'qty': 4, 'unit_price': '81.58'}, {'sku': 'SKU-313', 'qty': 6, 'unit_price': '51.34'}], {'tier': 'platinum', 'region': 'US'}]), {'subtotal': '634.36', 'discount': '0.00', 'tax': '0.00', 'total': '634.36'})

    def test_bulk_7(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-674', 'qty': 120, 'unit_price': '5.37'}, {'sku': 'SKU-357', 'qty': 8, 'unit_price': '77.62'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '1233.14', 'discount': '0.00', 'tax': '0.00', 'total': '1233.14'})

    def test_bulk_8(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-805', 'qty': 60, 'unit_price': '1.06'}, {'sku': 'SKU-981', 'qty': 6, 'unit_price': '45.86'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '335.58', 'discount': '0.00', 'tax': '0.00', 'total': '335.58'})

    def test_exempt_9(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-384', 'qty': 1, 'unit_price': '6.43'}, {'sku': 'SKU-470', 'qty': 6, 'unit_price': '65.63'}], {'tier': 'standard', 'region': 'AU', 'tax_exempt': True}]), {'subtotal': '400.21', 'discount': '0.00', 'tax': '0.00', 'total': '400.21'})

    def test_exempt_10(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-553', 'qty': 1, 'unit_price': '39.65'}, {'sku': 'SKU-894', 'qty': 2, 'unit_price': '34.63'}], {'tier': 'standard', 'region': 'AU', 'tax_exempt': True}]), {'subtotal': '108.91', 'discount': '0.00', 'tax': '0.00', 'total': '108.91'})

    def test_validate_11(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[{'sku': 'SKU-595', 'qty': 5, 'unit_price': '-11.00'}, {'sku': 'SKU-113', 'qty': 7, 'unit_price': '11.87'}], {'tier': 'standard', 'region': 'US'}])

    def test_validate_12(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[], {'tier': 'standard', 'region': 'US'}])

    def test_format_13(self):
        self.assertEqual(invoice.format_money(*['32565.55', 'AUD']), 'A$32,565.55')

    def test_format_14(self):
        self.assertEqual(invoice.format_money(*['117.5', 'NZD']), 'NZ$117.50')


if __name__ == "__main__":
    unittest.main()
