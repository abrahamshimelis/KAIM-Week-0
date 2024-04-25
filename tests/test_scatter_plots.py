import pandas as pd
import unittest
from scripts import ScatterPlots

class TestScatterPlots(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 3, 4, 5, 6]})
        self.scatter_plots = ScatterPlots(self.df)

    def test_create(self):
        # This is a visual test, so there's no assert statement
        self.scatter_plots.create('A', 'B')