"""Visible tests for the requirements in force after stage 8.

Run from /task/workspace:  python -m unittest discover -s /task/fixtures/current-tests
"""

import unittest

import invoice


class TestInvoice(unittest.TestCase):
    maxDiff = None

    def test_round_1(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-181', 'qty': 8, 'unit_price': '13.097'}, {'sku': 'SKU-741', 'qty': 1, 'unit_price': '28.917'}, {'sku': 'SKU-224', 'qty': 7, 'unit_price': '22.127'}], {'tier': 'standard', 'region': 'JP', 'coupon': '40.00'}]), {'subtotal': '288.58', 'discount': '40.00', 'shipping': '0.00', 'tax': '24.86', 'total': '273.44'})

    def test_round_2(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-135', 'qty': 1, 'unit_price': '23.775'}, {'sku': 'SKU-719', 'qty': 1, 'unit_price': '22.965'}], {'tier': 'platinum', 'region': 'JP', 'coupon': '300.00'}]), {'subtotal': '46.74', 'discount': '46.74', 'shipping': '7.50', 'tax': '0.75', 'total': '8.25'})

    def test_validate_3(self):
        with self.assertRaises(ValueError):
            invoice.compute_invoice(*[[{'sku': 'SKU-642', 'qty': 0, 'unit_price': '33.85'}, {'sku': 'SKU-886', 'qty': 0, 'unit_price': '24.52'}], {'tier': 'standard', 'region': 'AU'}])

    def test_validate_4(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-102', 'qty': 0, 'unit_price': '23.92'}, {'sku': 'SKU-684', 'qty': 3, 'unit_price': '28.95'}], {'tier': 'platinum', 'region': 'US', 'coupon': '40.00'}]), {'subtotal': '86.85', 'discount': '48.68', 'shipping': '7.50', 'tax': '0.00', 'total': '45.67'})

    def test_bulk_5(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-538', 'qty': 100, 'unit_price': '2.93'}, {'sku': 'SKU-349', 'qty': 7, 'unit_price': '1.50'}], {'tier': 'platinum', 'region': 'NZ', 'coupon': '300.00'}]), {'subtotal': '274.20', 'discount': '274.20', 'shipping': '7.50', 'tax': '1.12', 'total': '8.62'})

    def test_bulk_6(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-935', 'qty': 80, 'unit_price': '2.77'}, {'sku': 'SKU-187', 'qty': 3, 'unit_price': '46.29'}], {'tier': 'standard', 'region': 'NZ', 'coupon': '300.00'}]), {'subtotal': '338.31', 'discount': '300.00', 'shipping': '7.50', 'tax': '6.87', 'total': '52.68'})

    def test_tier_7(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-615', 'qty': 8, 'unit_price': '5.24'}, {'sku': 'SKU-653', 'qty': 6, 'unit_price': '51.63'}, {'sku': 'SKU-355', 'qty': 1, 'unit_price': '44.11'}], {'tier': 'silver', 'region': 'AU', 'coupon': '300.00'}]), {'subtotal': '395.81', 'discount': '307.92', 'shipping': '7.50', 'tax': '9.54', 'total': '104.93'})

    def test_tier_8(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-292', 'qty': 1, 'unit_price': '58.84'}, {'sku': 'SKU-414', 'qty': 4, 'unit_price': '19.14'}], {'tier': 'gold', 'region': 'NZ'}]), {'subtotal': '135.40', 'discount': '10.83', 'shipping': '0.00', 'tax': '18.69', 'total': '143.26'})

    def test_stack_9(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-666', 'qty': 50, 'unit_price': '1.97'}, {'sku': 'SKU-535', 'qty': 7, 'unit_price': '19.08'}, {'sku': 'SKU-162', 'qty': 4, 'unit_price': '19.71'}], {'tier': 'gold', 'region': 'AU', 'coupon': '20.00'}]), {'subtotal': '301.05', 'discount': '36.99', 'shipping': '0.00', 'tax': '26.41', 'total': '290.47'})

    def test_stack_10(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-781', 'qty': 50, 'unit_price': '2.62'}, {'sku': 'SKU-523', 'qty': 1, 'unit_price': '23.06'}, {'sku': 'SKU-434', 'qty': 6, 'unit_price': '29.52'}], {'tier': 'silver', 'region': 'AU', 'coupon': '20.00'}]), {'subtotal': '318.08', 'discount': '24.00', 'shipping': '0.00', 'tax': '29.41', 'total': '323.49'})

    def test_coupon_11(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-816', 'qty': 3, 'unit_price': '29.78'}], {'tier': 'platinum', 'region': 'JP', 'coupon': '5.00'}]), {'subtotal': '89.34', 'discount': '13.93', 'shipping': '7.50', 'tax': '8.29', 'total': '91.20'})

    def test_coupon_12(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-796', 'qty': 4, 'unit_price': '25.83'}], {'tier': 'platinum', 'region': 'AU', 'coupon': '5.00'}]), {'subtotal': '103.32', 'discount': '15.33', 'shipping': '7.50', 'tax': '9.55', 'total': '105.04'})

    def test_ship_13(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-380', 'qty': 1, 'unit_price': '105.70'}], {'tier': 'silver', 'region': 'JP', 'coupon': '5.00'}]), {'subtotal': '105.70', 'discount': '7.11', 'shipping': '7.50', 'tax': '10.61', 'total': '116.70'})

    def test_ship_14(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-562', 'qty': 1, 'unit_price': '103.38'}], {'tier': 'platinum', 'region': 'NZ', 'coupon': '300.00'}]), {'subtotal': '103.38', 'discount': '103.38', 'shipping': '7.50', 'tax': '1.12', 'total': '8.62'})

    def test_tax_15(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-511', 'qty': 6, 'unit_price': '50.13'}, {'sku': 'SKU-337', 'qty': 3, 'unit_price': '15.80'}, {'sku': 'SKU-323', 'qty': 4, 'unit_price': '15.07'}], {'tier': 'gold', 'region': 'AU', 'coupon': '40.00'}]), {'subtotal': '408.46', 'discount': '72.68', 'shipping': '0.00', 'tax': '33.58', 'total': '369.36'})

    def test_tax_16(self):
        self.assertEqual(invoice.compute_invoice(*[[{'sku': 'SKU-569', 'qty': 7, 'unit_price': '7.66'}, {'sku': 'SKU-766', 'qty': 8, 'unit_price': '32.43'}, {'sku': 'SKU-904', 'qty': 4, 'unit_price': '47.13'}], {'tier': 'gold', 'region': 'US', 'coupon': '20.00'}]), {'subtotal': '501.58', 'discount': '60.13', 'shipping': '0.00', 'tax': '0.00', 'total': '441.45'})

    def test_refund_17(self):
        with self.assertRaises(ValueError):
            invoice.compute_refund(*[[{'sku': 'SKU-800', 'qty': 3, 'unit_price': '6.49'}, {'sku': 'SKU-390', 'qty': 2, 'unit_price': '1.34'}, {'sku': 'SKU-962', 'qty': 4, 'unit_price': '12.06'}], {'tier': 'standard', 'region': 'AU', 'coupon': '40.00'}, {'SKU-390': 3}])

    def test_refund_18(self):
        self.assertEqual(invoice.compute_refund(*[[{'sku': 'SKU-474', 'qty': 50, 'unit_price': '50.27'}, {'sku': 'SKU-972', 'qty': 2, 'unit_price': '18.72'}, {'sku': 'SKU-736', 'qty': 1, 'unit_price': '48.57'}], {'tier': 'silver', 'region': 'NZ'}, {'SKU-474': 1}]), '0.00')


if __name__ == "__main__":
    unittest.main()
