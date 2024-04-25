class TemperatureAnalysis:
    def __init__(self, df):
        self.df = df

    def compare(self, column1, column2):
        return self.df[[column1, column2]].corr()
