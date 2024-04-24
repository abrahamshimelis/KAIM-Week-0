import pandas as pd
import numpy as np
import unittest
from scripts import DataQualityCheck

class TestDataQualityCheck(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5, np.nan],
            'B': [2, 3, 4, 5, 6, 100],  # 100 is an outlier
            'C': [1, 2, -3, 4, 5, 6]   # -3 is an incorrect entry
        })
        self.data_quality_check = DataQualityCheck(self.df)

    def test_check_missing_values(self):
        result = self.data_quality_check.check_missing_values()
        self.assertEqual(result['A'], 1)
        self.assertEqual(result['B'], 0)
        self.assertEqual(result['C'], 0)

    def test_check_outliers(self):
        result = self.data_quality_check.check_outliers('B', threshold=2)
        self.assertEqual(result['B'].values[0], 100)

    def test_check_incorrect_entries(self):
        result = self.data_quality_check.check_incorrect_entries('C')
        self.assertEqual(result['C'].values[0], -3)
