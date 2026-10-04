"""Visible tests for the requirements in force after stage 6.

Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import unittest

import invoice


class TestInvoice(unittest.TestCase):
    maxDiff = None

    def test_round_1(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-633', 'qty': 7, 'unit_price': '20.167'}, {'sku': 'SKU-753', 'qty': 8, 'unit_price': '11.437'}, {'sku': 'SKU-668', 'qty': 1, 'unit_price': '7.497'}], {'tier': 'standard', 'region': 'JP'}]), {'subtotal': '240.17', 'discount': '0.00', 'shipping': '0.00', 'tax': '24.02', 'total': '264.19'})

    def test_round_2(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-457', 'qty': 1, 'unit_price': '5.305'}, {'sku': 'SKU-187', 'qty': 1, 'unit_price': '8.185'}], {'tier': 'gold', 'region': 'AU'}]), {'subtotal': '13.50', 'discount': '1.08', 'shipping': '7.50', 'tax': '1.24', 'total': '21.16'})

    def test_validate_3(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[], {'tier': 'silver', 'region': 'JP'}])

    def test_validate_4(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-493', 'qty': 0, 'unit_price': '4.22'}, {'sku': 'SKU-332', 'qty': 1, 'unit_price': '57.59'}], {'tier': 'gold', 'region': 'US'}]), {'subtotal': '57.59', 'discount': '4.61', 'shipping': '7.50', 'tax': '0.00', 'total': '60.48'})

    def test_bulk_5(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-178', 'qty': 50, 'unit_price': '3.42'}, {'sku': 'SKU-643', 'qty': 8, 'unit_price': '37.11'}], {'tier': 'standard', 'region': 'NZ'}]), {'subtotal': '450.78', 'discount': '0.00', 'shipping': '0.00', 'tax': '67.62', 'total': '518.40'})

    def test_bulk_6(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-269', 'qty': 50, 'unit_price': '1.76'}, {'sku': 'SKU-387', 'qty': 3, 'unit_price': '37.23'}], {'tier': 'gold', 'region': 'NZ'}]), {'subtotal': '190.89', 'discount': '8.94', 'shipping': '0.00', 'tax': '27.29', 'total': '209.24'})

    def test_tier_7(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-192', 'qty': 4, 'unit_price': '33.37'}, {'sku': 'SKU-619', 'qty': 1, 'unit_price': '51.91'}], {'tier': 'platinum', 'region': 'NZ'}]), {'subtotal': '185.39', 'discount': '18.54', 'shipping': '0.00', 'tax': '25.03', 'total': '191.88'})

    def test_tier_8(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-883', 'qty': 4, 'unit_price': '44.12'}, {'sku': 'SKU-763', 'qty': 8, 'unit_price': '34.53'}, {'sku': 'SKU-583', 'qty': 7, 'unit_price': '46.64'}], {'tier': 'gold', 'region': 'US'}]), {'subtotal': '779.20', 'discount': '62.34', 'shipping': '0.00', 'tax': '0.00', 'total': '716.86'})

    def test_stack_9(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-134', 'qty': 50, 'unit_price': '2.98'}, {'sku': 'SKU-801', 'qty': 5, 'unit_price': '5.81'}, {'sku': 'SKU-868', 'qty': 1, 'unit_price': '8.37'}], {'tier': 'silver', 'region': 'NZ'}]), {'subtotal': '171.52', 'discount': '0.75', 'shipping': '0.00', 'tax': '25.62', 'total': '196.39'})

    def test_stack_10(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-587', 'qty': 50, 'unit_price': '1.65'}, {'sku': 'SKU-459', 'qty': 2, 'unit_price': '24.61'}, {'sku': 'SKU-963', 'qty': 7, 'unit_price': '13.67'}], {'tier': 'gold', 'region': 'US'}]), {'subtotal': '219.16', 'discount': '11.59', 'shipping': '0.00', 'tax': '0.00', 'total': '207.57'})

    def test_ship_11(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-563', 'qty': 1, 'unit_price': '101.74'}], {'tier': 'platinum', 'region': 'AU'}]), {'subtotal': '101.74', 'discount': '10.17', 'shipping': '7.50', 'tax': '9.16', 'total': '108.23'})

    def test_ship_12(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-301', 'qty': 1, 'unit_price': '99.99'}], {'tier': 'standard', 'region': 'JP'}]), {'subtotal': '99.99', 'discount': '0.00', 'shipping': '7.50', 'tax': '10.00', 'total': '117.49'})

    def test_tax_13(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-151', 'qty': 7, 'unit_price': '12.25'}], {'tier': 'gold', 'region': 'AU'}]), {'subtotal': '85.75', 'discount': '6.86', 'shipping': '7.50', 'tax': '7.89', 'total': '94.28'})

    def test_tax_14(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-766', 'qty': 8, 'unit_price': '19.54'}, {'sku': 'SKU-203', 'qty': 3, 'unit_price': '35.39'}], {'tier': 'platinum', 'region': 'US'}]), {'subtotal': '262.49', 'discount': '26.25', 'shipping': '0.00', 'tax': '0.00', 'total': '236.24'})


if __name__ == "__main__":
    unittest.main()
