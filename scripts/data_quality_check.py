from scipy import stats
import numpy as np

class DataQualityCheck:
    def __init__(self, df):
        self.df = df

    def check_missing_values(self):
        return self.df.isnull().sum()

    # significantly different from other observations.
    def check_outliers(self, column):
        z_scores = stats.zscore(self.df[column])
        abs_z_scores = np.abs(z_scores)
        return self.df[abs_z_scores > 3]

    # In this case, it checks for negative values
    def check_incorrect_entries(self, column):
        return self.df[self.df[column] < 0]
