import pandas as pd
import unittest
from scripts import Histograms

class TestHistograms(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        self.histograms = Histograms(self.df)

    def test_create(self):
        # This is a visual test, so there's no assert statement
        self.histograms.create('A')