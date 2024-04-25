import pandas as pd
import unittest
from scripts import BoxPlots

class TestBoxPlots(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        self.box_plots = BoxPlots(self.df)

    def test_create(self):
        # This is a visual test, so there's no assert statement
        self.box_plots.create('A')