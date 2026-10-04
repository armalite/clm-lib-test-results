"""Visible tests for the requirements in force after stage 4.

Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import unittest

import invoice


class TestInvoice(unittest.TestCase):
    maxDiff = None

    def test_round_1(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-299', 'qty': 5, 'unit_price': '25.425'}, {'sku': 'SKU-257', 'qty': 6, 'unit_price': '11.977'}, {'sku': 'SKU-798', 'qty': 1, 'unit_price': '13.757'}], {'tier': 'standard', 'region': 'NZ'}]), {'subtotal': '212.75', 'discount': '0.00', 'tax': '31.91', 'total': '244.66'})

    def test_round_2(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-494', 'qty': 8, 'unit_price': '26.203'}, {'sku': 'SKU-757', 'qty': 5, 'unit_price': '2.417'}, {'sku': 'SKU-790', 'qty': 1, 'unit_price': '2.755'}], {'tier': 'standard', 'region': 'AU'}]), {'subtotal': '224.47', 'discount': '0.00', 'tax': '22.45', 'total': '246.92'})

    def test_tax_3(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-949', 'qty': 3, 'unit_price': '71.35'}, {'sku': 'SKU-712', 'qty': 6, 'unit_price': '66.53'}], {'tier': 'standard', 'region': 'JP'}]), {'subtotal': '613.23', 'discount': '0.00', 'tax': '73.59', 'total': '686.82'})

    def test_tax_4(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-141', 'qty': 6, 'unit_price': '20.05'}, {'sku': 'SKU-889', 'qty': 2, 'unit_price': '13.01'}], {'tier': 'standard', 'region': 'NZ'}]), {'subtotal': '146.32', 'discount': '0.00', 'tax': '21.95', 'total': '168.27'})

    def test_tier_5(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-432', 'qty': 8, 'unit_price': '41.24'}, {'sku': 'SKU-576', 'qty': 8, 'unit_price': '66.88'}], {'tier': 'silver', 'region': 'US'}]), {'subtotal': '864.96', 'discount': '25.95', 'tax': '0.00', 'total': '839.01'})

    def test_tier_6(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-607', 'qty': 1, 'unit_price': '55.17'}, {'sku': 'SKU-967', 'qty': 8, 'unit_price': '55.18'}], {'tier': 'gold', 'region': 'US'}]), {'subtotal': '496.61', 'discount': '34.76', 'tax': '0.00', 'total': '461.85'})

    def test_bulk_7(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-498', 'qty': 250, 'unit_price': '3.21'}, {'sku': 'SKU-985', 'qty': 5, 'unit_price': '33.11'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '887.80', 'discount': '0.00', 'tax': '0.00', 'total': '887.80'})

    def test_bulk_8(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-303', 'qty': 60, 'unit_price': '8.06'}, {'sku': 'SKU-695', 'qty': 6, 'unit_price': '83.78'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '986.28', 'discount': '0.00', 'tax': '0.00', 'total': '986.28'})

    def test_exempt_9(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-368', 'qty': 8, 'unit_price': '88.67'}, {'sku': 'SKU-768', 'qty': 6, 'unit_price': '41.30'}], {'tier': 'standard', 'region': 'NZ', 'tax_exempt': True}]), {'subtotal': '957.16', 'discount': '0.00', 'tax': '0.00', 'total': '957.16'})

    def test_exempt_10(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-882', 'qty': 7, 'unit_price': '79.07'}, {'sku': 'SKU-873', 'qty': 3, 'unit_price': '85.95'}], {'tier': 'standard', 'region': 'NZ', 'tax_exempt': True}]), {'subtotal': '811.34', 'discount': '0.00', 'tax': '0.00', 'total': '811.34'})

    def test_validate_11(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[], {'tier': 'standard', 'region': 'US'}])

    def test_validate_12(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[{'sku': 'SKU-528', 'qty': 7, 'unit_price': '-15.00'}, {'sku': 'SKU-856', 'qty': 7, 'unit_price': '14.07'}], {'tier': 'standard', 'region': 'US'}])

    def test_format_13(self):
        self.assertEqual(invoice.format_money(*['44054.72', 'AUD']), 'A$44,054.72')

    def test_format_14(self):
        self.assertEqual(invoice.format_money(*['5165.48', 'AUD']), 'A$5,165.48')


if __name__ == "__main__":
    unittest.main()
