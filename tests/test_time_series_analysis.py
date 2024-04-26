import pandas as pd
import unittest
from unittest.mock import patch
from scripts import TimeSeriesAnalysis

class TestTimeSeriesAnalysis(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5, 6],
            'B': [2, 3, 4, 5, 6, 7]
        })
        self.time_series_analysis = TimeSeriesAnalysis(self.df)

    @patch("matplotlib.pyplot.show")
    def test_analyze(self, mock_show):
        self.time_series_analysis.analyze('A')
        mock_show.assert_called_once()