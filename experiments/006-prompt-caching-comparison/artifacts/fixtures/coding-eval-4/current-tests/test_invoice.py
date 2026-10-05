"""Visible tests for the requirements in force after stage 4.

Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import unittest

import invoice


class TestInvoice(unittest.TestCase):
    maxDiff = None

    def test_round_1(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-559', 'qty': 8, 'unit_price': '28.873'}, {'sku': 'SKU-251', 'qty': 7, 'unit_price': '25.143'}, {'sku': 'SKU-191', 'qty': 3, 'unit_price': '17.753'}], {'tier': 'standard', 'region': 'AU'}]), {'subtotal': '460.24', 'discount': '0.00', 'tax': '46.02', 'total': '506.26'})

    def test_round_2(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-651', 'qty': 3, 'unit_price': '8.707'}, {'sku': 'SKU-320', 'qty': 8, 'unit_price': '2.887'}, {'sku': 'SKU-989', 'qty': 1, 'unit_price': '22.125'}], {'tier': 'standard', 'region': 'NZ'}]), {'subtotal': '71.34', 'discount': '0.00', 'tax': '7.13', 'total': '78.47'})

    def test_tax_3(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-246', 'qty': 6, 'unit_price': '60.20'}, {'sku': 'SKU-178', 'qty': 3, 'unit_price': '78.92'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '597.96', 'discount': '0.00', 'tax': '59.80', 'total': '657.76'})

    def test_tax_4(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-647', 'qty': 2, 'unit_price': '79.56'}, {'sku': 'SKU-154', 'qty': 8, 'unit_price': '45.21'}], {'tier': 'standard', 'region': 'AU'}]), {'subtotal': '520.80', 'discount': '0.00', 'tax': '52.08', 'total': '572.88'})

    def test_tier_5(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-364', 'qty': 3, 'unit_price': '30.57'}, {'sku': 'SKU-459', 'qty': 2, 'unit_price': '73.89'}], {'tier': 'platinum', 'region': 'US'}]), {'subtotal': '239.49', 'discount': '23.95', 'tax': '21.55', 'total': '237.09'})

    def test_tier_6(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-518', 'qty': 8, 'unit_price': '18.31'}, {'sku': 'SKU-535', 'qty': 6, 'unit_price': '56.35'}], {'tier': 'gold', 'region': 'US'}]), {'subtotal': '484.58', 'discount': '33.92', 'tax': '45.07', 'total': '495.73'})

    def test_bulk_7(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-468', 'qty': 250, 'unit_price': '7.09'}, {'sku': 'SKU-841', 'qty': 3, 'unit_price': '55.05'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '1724.95', 'discount': '0.00', 'tax': '172.50', 'total': '1897.45'})

    def test_bulk_8(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-702', 'qty': 120, 'unit_price': '4.62'}, {'sku': 'SKU-135', 'qty': 4, 'unit_price': '44.30'}], {'tier': 'standard', 'region': 'US'}]), {'subtotal': '703.88', 'discount': '0.00', 'tax': '70.39', 'total': '774.27'})

    def test_exempt_9(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-523', 'qty': 1, 'unit_price': '18.21'}, {'sku': 'SKU-444', 'qty': 1, 'unit_price': '45.31'}], {'tier': 'standard', 'region': 'NZ', 'tax_exempt': True}]), {'subtotal': '63.52', 'discount': '0.00', 'tax': '0.00', 'total': '63.52'})

    def test_exempt_10(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-495', 'qty': 7, 'unit_price': '41.70'}, {'sku': 'SKU-905', 'qty': 5, 'unit_price': '76.56'}], {'tier': 'standard', 'region': 'NZ', 'tax_exempt': True}]), {'subtotal': '674.70', 'discount': '0.00', 'tax': '0.00', 'total': '674.70'})

    def test_validate_11(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[{'sku': 'SKU-882', 'qty': 8, 'unit_price': '-19.00'}, {'sku': 'SKU-727', 'qty': 7, 'unit_price': '11.10'}], {'tier': 'standard', 'region': 'US'}])

    def test_validate_12(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[{'sku': 'SKU-594', 'qty': -2, 'unit_price': '37.87'}, {'sku': 'SKU-682', 'qty': 5, 'unit_price': '38.80'}], {'tier': 'standard', 'region': 'US'}])

    def test_format_13(self):
        self.assertEqual(invoice.format_money(*['973.5', 'USD']), 'US$973.50')

    def test_format_14(self):
        self.assertEqual(invoice.format_money(*['90694.10', 'AUD']), 'A$90694.10')


if __name__ == "__main__":
    unittest.main()
