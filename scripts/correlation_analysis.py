class CorrelationAnalysis:
    def __init__(self, df):
        self.df = df

    def analyze(self, column1, column2):
        return self.df[column1].corr(self.df[column2])
