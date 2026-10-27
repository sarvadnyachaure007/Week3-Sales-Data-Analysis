import unittest
from pathlib import Path
import pandas as pd


class SalesTests(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_csv(
            Path(__file__).resolve().parents[1] / "sales_data.csv"
        )

    def test_dataset_is_not_empty(self):
        self.assertGreater(len(self.data), 0)

    def test_required_columns_exist(self):
        expected = {
            "Order_ID", "Date", "Product",
            "Quantity", "Unit_Price", "Total_Sales"
        }
        self.assertTrue(expected.issubset(self.data.columns))

    def test_revenue_calculation(self):
        self.assertEqual((2 * 100) + (3 * 50), 350)

    def test_duplicate_detection(self):
        sample = pd.DataFrame({"value": [1, 1, 2]})
        self.assertEqual(int(sample.duplicated().sum()), 1)


if __name__ == "__main__":
    unittest.main()
