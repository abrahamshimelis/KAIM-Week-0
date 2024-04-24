import pandas as pd
import unittest
from scripts import WindAnalysis

class TestWindAnalysis(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'WS': [1, 2, 3, 4, 5, 6],
            'WD': [30, 60, 90, 120, 150, 180]
        })
        self.wind_analysis = WindAnalysis(self.df)

    def test_analyze_speed(self):
        result = self.wind_analysis.analyze_speed('WS')
        self.assertEqual(result['mean'], 3.5)

    def test_analyze_direction(self):
        result = self.wind_analysis.analyze_direction('WD')
        self.assertEqual(result['mean'], 105.0)
