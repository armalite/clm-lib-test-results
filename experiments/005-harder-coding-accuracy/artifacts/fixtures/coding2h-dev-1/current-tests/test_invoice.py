"""Visible tests for the requirements in force after stage 8.

Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import unittest

import invoice


class TestInvoice(unittest.TestCase):
    maxDiff = None

    def test_round_1(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-616', 'qty': 1, 'unit_price': '1.885'}, {'sku': 'SKU-199', 'qty': 1, 'unit_price': '2.635'}, {'sku': 'SKU-170', 'qty': 1, 'unit_price': '15.645'}], {'tier': 'platinum', 'region': 'US', 'coupon': '5.00'}]), {'subtotal': '20.16', 'discount': '6.52', 'shipping': '7.50', 'tax': '0.00', 'total': '21.14'})

    def test_round_2(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-694', 'qty': 1, 'unit_price': '16.765'}, {'sku': 'SKU-975', 'qty': 1, 'unit_price': '20.235'}, {'sku': 'SKU-249', 'qty': 1, 'unit_price': '27.255'}], {'tier': 'standard', 'region': 'NZ', 'coupon': '300.00'}]), {'subtotal': '64.26', 'discount': '64.26', 'shipping': '7.50', 'tax': '1.12', 'total': '8.62'})

    def test_validate_3(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[], {'tier': 'gold', 'region': 'US', 'coupon': '20.00'}])

    def test_validate_4(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[], {'tier': 'gold', 'region': 'NZ', 'coupon': '20.00'}])

    def test_bulk_5(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-971', 'qty': 89, 'unit_price': '2.55'}, {'sku': 'SKU-693', 'qty': 6, 'unit_price': '20.13'}], {'tier': 'standard', 'region': 'US', 'coupon': '300.00'}]), {'subtotal': '325.04', 'discount': '300.00', 'shipping': '7.50', 'tax': '0.00', 'total': '32.54'})

    def test_bulk_6(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-231', 'qty': 50, 'unit_price': '3.94'}, {'sku': 'SKU-712', 'qty': 7, 'unit_price': '1.40'}], {'tier': 'silver', 'region': 'NZ', 'coupon': '5.00'}]), {'subtotal': '187.10', 'discount': '5.10', 'shipping': '0.00', 'tax': '27.30', 'total': '209.30'})

    def test_tier_7(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-186', 'qty': 7, 'unit_price': '28.06'}], {'tier': 'silver', 'region': 'US'}]), {'subtotal': '196.42', 'discount': '3.93', 'shipping': '0.00', 'tax': '0.00', 'total': '192.49'})

    def test_tier_8(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-937', 'qty': 4, 'unit_price': '47.56'}], {'tier': 'gold', 'region': 'JP', 'coupon': '5.00'}]), {'subtotal': '190.24', 'discount': '19.82', 'shipping': '0.00', 'tax': '17.04', 'total': '187.46'})

    def test_stack_9(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-127', 'qty': 50, 'unit_price': '3.90'}, {'sku': 'SKU-472', 'qty': 6, 'unit_price': '37.07'}, {'sku': 'SKU-748', 'qty': 1, 'unit_price': '12.27'}], {'tier': 'gold', 'region': 'NZ'}]), {'subtotal': '410.19', 'discount': '18.78', 'shipping': '0.00', 'tax': '58.71', 'total': '450.12'})

    def test_stack_10(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-560', 'qty': 80, 'unit_price': '3.16'}, {'sku': 'SKU-886', 'qty': 1, 'unit_price': '20.56'}, {'sku': 'SKU-789', 'qty': 5, 'unit_price': '43.17'}], {'tier': 'platinum', 'region': 'NZ'}]), {'subtotal': '463.93', 'discount': '23.64', 'shipping': '0.00', 'tax': '66.04', 'total': '506.33'})

    def test_coupon_11(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-951', 'qty': 7, 'unit_price': '10.12'}], {'tier': 'silver', 'region': 'US', 'coupon': '15.00'}]), {'subtotal': '70.84', 'discount': '16.12', 'shipping': '7.50', 'tax': '0.00', 'total': '62.22'})

    def test_coupon_12(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-948', 'qty': 1, 'unit_price': '44.84'}, {'sku': 'SKU-306', 'qty': 5, 'unit_price': '18.67'}], {'tier': 'gold', 'region': 'AU', 'coupon': '5.00'}]), {'subtotal': '138.19', 'discount': '15.66', 'shipping': '0.00', 'tax': '12.25', 'total': '134.78'})

    def test_ship_13(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-112', 'qty': 1, 'unit_price': '101.31'}], {'tier': 'gold', 'region': 'JP'}]), {'subtotal': '101.31', 'discount': '8.10', 'shipping': '7.50', 'tax': '10.07', 'total': '110.78'})

    def test_ship_14(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-314', 'qty': 1, 'unit_price': '99.99'}], {'tier': 'standard', 'region': 'AU'}]), {'subtotal': '99.99', 'discount': '0.00', 'shipping': '7.50', 'tax': '10.75', 'total': '118.24'})

    def test_tax_15(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-336', 'qty': 2, 'unit_price': '4.87'}, {'sku': 'SKU-648', 'qty': 2, 'unit_price': '59.81'}], {'tier': 'platinum', 'region': 'AU'}]), {'subtotal': '129.36', 'discount': '12.94', 'shipping': '0.00', 'tax': '11.64', 'total': '128.06'})

    def test_tax_16(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-228', 'qty': 5, 'unit_price': '27.76'}, {'sku': 'SKU-900', 'qty': 7, 'unit_price': '42.16'}], {'tier': 'standard', 'region': 'US', 'coupon': '5.00'}]), {'subtotal': '433.92', 'discount': '5.00', 'shipping': '0.00', 'tax': '0.00', 'total': '428.92'})

    def test_refund_17(self):
        self.assertEqual(invoice.compute_refund(*[[{'sku': 'SKU-176', 'qty': 3, 'unit_price': '36.89'}, {'sku': 'SKU-935', 'qty': 1, 'unit_price': '5.48'}], {'tier': 'standard', 'region': 'AU'}, {'SKU-176': 1}]), '40.58')

    def test_refund_18(self):
        self.assertEqual(invoice.compute_refund(*[[{'sku': 'SKU-921', 'qty': 55, 'unit_price': '2.13'}, {'sku': 'SKU-947', 'qty': 2, 'unit_price': '20.28'}], {'tier': 'gold', 'region': 'US', 'coupon': '12.50'}, {'SKU-921': 55, 'SKU-947': 2}]), '131.26')


if __name__ == "__main__":
    unittest.main()
