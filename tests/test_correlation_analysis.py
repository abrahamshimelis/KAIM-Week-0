import pandas as pd
import unittest
from scripts import CorrelationAnalysis

class TestCorrelationAnalysis(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5, 6],
            'B': [2, 3, 4, 5, 6, 7]
        })
        self.correlation_analysis = CorrelationAnalysis(self.df)

    def test_analyze(self):
        result = self.correlation_analysis.analyze('A', 'B')
        self.assertAlmostEqual(result, 1.0, places=5)
