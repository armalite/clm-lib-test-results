"""Visible tests for the requirements in force after stage 6.

Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import unittest

import invoice


class TestInvoice(unittest.TestCase):
    maxDiff = None

    def test_round_1(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-208', 'qty': 1, 'unit_price': '29.865'}, {'sku': 'SKU-135', 'qty': 1, 'unit_price': '26.295'}, {'sku': 'SKU-523', 'qty': 1, 'unit_price': '17.515'}], {'tier': 'gold', 'region': 'JP'}]), {'subtotal': '73.68', 'discount': '5.89', 'shipping': '7.50', 'tax': '7.53', 'total': '82.82'})

    def test_round_2(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-717', 'qty': 3, 'unit_price': '22.067'}, {'sku': 'SKU-287', 'qty': 8, 'unit_price': '10.087'}], {'tier': 'gold', 'region': 'AU'}]), {'subtotal': '146.90', 'discount': '11.75', 'shipping': '0.00', 'tax': '13.51', 'total': '148.66'})

    def test_validate_3(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[], {'tier': 'silver', 'region': 'US'}])

    def test_validate_4(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[{'sku': 'SKU-317', 'qty': 0, 'unit_price': '3.64'}, {'sku': 'SKU-605', 'qty': 1, 'unit_price': '54.96'}], {'tier': 'standard', 'region': 'US'}])

    def test_bulk_5(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-684', 'qty': 110, 'unit_price': '1.28'}, {'sku': 'SKU-850', 'qty': 2, 'unit_price': '30.86'}], {'tier': 'silver', 'region': 'JP'}]), {'subtotal': '188.44', 'discount': '1.23', 'shipping': '0.00', 'tax': '18.72', 'total': '205.93'})

    def test_bulk_6(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-314', 'qty': 100, 'unit_price': '2.31'}, {'sku': 'SKU-957', 'qty': 3, 'unit_price': '2.49'}], {'tier': 'silver', 'region': 'JP'}]), {'subtotal': '215.37', 'discount': '0.15', 'shipping': '0.00', 'tax': '21.52', 'total': '236.74'})

    def test_tier_7(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-261', 'qty': 1, 'unit_price': '55.58'}], {'tier': 'platinum', 'region': 'JP'}]), {'subtotal': '55.58', 'discount': '5.56', 'shipping': '7.50', 'tax': '5.75', 'total': '63.27'})

    def test_tier_8(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-627', 'qty': 8, 'unit_price': '38.80'}], {'tier': 'platinum', 'region': 'JP'}]), {'subtotal': '310.40', 'discount': '31.04', 'shipping': '0.00', 'tax': '27.94', 'total': '307.30'})

    def test_stack_9(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-326', 'qty': 100, 'unit_price': '3.62'}, {'sku': 'SKU-861', 'qty': 7, 'unit_price': '6.70'}, {'sku': 'SKU-963', 'qty': 4, 'unit_price': '33.21'}], {'tier': 'platinum', 'region': 'US'}]), {'subtotal': '505.54', 'discount': '17.97', 'shipping': '0.00', 'tax': '0.00', 'total': '487.57'})

    def test_stack_10(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-991', 'qty': 100, 'unit_price': '2.62'}, {'sku': 'SKU-319', 'qty': 1, 'unit_price': '55.07'}, {'sku': 'SKU-967', 'qty': 8, 'unit_price': '32.79'}], {'tier': 'silver', 'region': 'JP'}]), {'subtotal': '553.19', 'discount': '6.35', 'shipping': '0.00', 'tax': '54.68', 'total': '601.52'})

    def test_ship_11(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-263', 'qty': 1, 'unit_price': '102.05'}], {'tier': 'gold', 'region': 'US'}]), {'subtotal': '102.05', 'discount': '8.16', 'shipping': '7.50', 'tax': '0.00', 'total': '101.39'})

    def test_ship_12(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-571', 'qty': 1, 'unit_price': '99.99'}], {'tier': 'standard', 'region': 'NZ'}]), {'subtotal': '99.99', 'discount': '0.00', 'shipping': '7.50', 'tax': '16.12', 'total': '123.61'})

    def test_tax_13(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-716', 'qty': 7, 'unit_price': '44.78'}], {'tier': 'standard', 'region': 'NZ'}]), {'subtotal': '313.46', 'discount': '0.00', 'shipping': '0.00', 'tax': '47.02', 'total': '360.48'})

    def test_tax_14(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-279', 'qty': 7, 'unit_price': '37.98'}, {'sku': 'SKU-622', 'qty': 7, 'unit_price': '28.23'}, {'sku': 'SKU-689', 'qty': 6, 'unit_price': '6.62'}], {'tier': 'gold', 'region': 'US'}]), {'subtotal': '503.19', 'discount': '40.26', 'shipping': '0.00', 'tax': '0.00', 'total': '462.93'})


if __name__ == "__main__":
    unittest.main()
