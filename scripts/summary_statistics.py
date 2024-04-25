class SummaryStatistics:
    def __init__(self, df):
        self.df = df

    def calculate(self):
        return self.df.describe()