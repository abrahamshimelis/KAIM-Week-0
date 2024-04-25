import pandas as pd
import numpy as np
import unittest
from scripts import DataCleaning

class TestDataCleaning(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({'A': [1, 2, np.nan, 4, 5]})
        self.data_cleaning = DataCleaning(self.df)

    def test_handle_missing_values(self):
        result = self.data_cleaning.handle_missing_values('A')
        self.assertEqual(result['A'].isnull().sum(), 0)