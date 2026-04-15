import unittest
from exercises import scan, total


class TestPointOfSale(unittest.TestCase):
    """
    Kata 5 - Point of Sale kata
    Create a simple app for scanning bar codes to sell products.

    Requirements:
    1. Barcode '12345' should display price '$7.25'
    2. Barcode '23456' should display price '$12.50'
    3. Barcode '99999' should display 'Error: barcode not found'
    4. Empty barcode should display 'Error: empty barcode'
    5. Introduce a concept of total command where it is possible to scan multiple items.
       The command would display the sum of the scanned product prices.
    """

    # Requirement 1
    req1_test_data = [
        ("12345", "$7.25"),
    ]

    # Requirement 2
    req2_test_data = [
        ("23456", "$12.50"),
    ]

    # Requirement 3
    req3_test_data = [
        ("99999", "Error: barcode not found"),
        ("11111", "Error: barcode not found"),
        ("ABCDE", "Error: barcode not found"),
    ]

    # Requirement 4
    req4_test_data = [
        ("", "Error: empty barcode"),
    ]

    # Requirement 5
    req5_test_data = [
        (["12345"],          "$7.25"),
        (["23456"],          "$12.50"),
        (["12345", "23456"], "$19.75"),
        (["99999"],          "$0.00"),
        ([],                 "$0.00"),
    ]

    def test_scan_barcode_12345_should_display_price_7_25(self):
        """
        Requirement 1: Barcode '12345' should display price '$7.25'.
        """
        for barcode, expected in self.req1_test_data:
            with self.subTest(barcode=barcode):
                self.assertEqual(scan(barcode), expected)

    def test_scan_barcode_23456_should_display_price_12_50(self):
        """
        Requirement 2: Barcode '23456' should display price '$12.50'.
        """
        for barcode, expected in self.req2_test_data:
            with self.subTest(barcode=barcode):
                self.assertEqual(scan(barcode), expected)

    def test_scan_unknown_barcode_should_display_error_barcode_not_found(self):
        """
        Requirement 3: Barcode '99999' should display 'Error: barcode not found'.
        """
        for barcode, expected in self.req3_test_data:
            with self.subTest(barcode=barcode):
                self.assertEqual(scan(barcode), expected)

    def test_scan_empty_barcode_should_display_error_empty_barcode(self):
        """
        Requirement 4: Empty barcode should display 'Error: empty barcode'.
        """
        for barcode, expected in self.req4_test_data:
            with self.subTest(barcode=barcode):
                self.assertEqual(scan(barcode), expected)

    def test_total_should_display_sum_of_scanned_product_prices(self):
        """
        Requirement 5: total command should display the sum of scanned product prices.
        """
        for barcodes, expected in self.req5_test_data:
            with self.subTest(barcodes=barcodes):
                self.assertEqual(total(barcodes), expected)


if __name__ == "__main__":
    unittest.main()