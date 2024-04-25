import pandas as pd
import unittest
from scripts import SummaryStatistics

class TestSummaryStatistics(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 3, 4, 5, 6]})
        self.summary_statistics = SummaryStatistics(self.df)

    def test_calculate(self):
        result = self.summary_statistics.calculate()
        self.assertEqual(result['A']['mean'], 3)
        self.assertEqual(result['B']['mean'], 4)

if __name__ == '__main__':
    unittest.main()