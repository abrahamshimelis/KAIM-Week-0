import pandas as pd
import unittest
from scripts import TemperatureAnalysis

class TestTemperatureAnalysis(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'TModA': [20, 21, 22, 23, 24, 25],
            'Tamb': [15, 16, 17, 18, 19, 20]
        })
        self.temperature_analysis = TemperatureAnalysis(self.df)

    def test_compare(self):
        result = self.temperature_analysis.compare('TModA', 'Tamb')
        self.assertAlmostEqual(result.iloc[0, 1], 1.0, places=5)
