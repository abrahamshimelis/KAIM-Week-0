import unittest
import pandas as pd
from unittest.mock import patch
from scripts import TimeSeriesAnalysis  # Assuming your TimeSeriesAnalysis class is in a module named 'scripts'

class TestTimeSeriesAnalysis(unittest.TestCase):
    def setUp(self):
        # Sample data with formatted timestamp
        data = {
            'Date': ['8/9/2021 12:01:00 AM', '8/9/2021 12:02:00 AM', '8/9/2021 12:03:00 AM'],
            'Value': [100, 150, 200]
        }
        self.df = pd.DataFrame(data)
        self.df['Date'] = pd.to_datetime(self.df['Date'], format='%m/%d/%Y %I:%M:%S %p')

        self.time_series_analysis = TimeSeriesAnalysis(self.df)

    @patch("matplotlib.pyplot.show")
    def test_analyze(self, mock_show):
        # Call analyze method
        self.time_series_analysis.analyze('Date', 'Value')

        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()
