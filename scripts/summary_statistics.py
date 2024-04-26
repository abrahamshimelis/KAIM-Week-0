class SummaryStatistics:
    def __init__(self, df):
        self.df = df

    def calculate(self):
        # Exclude 'Timestamp' column from the calculation
        numeric_cols = self.df.select_dtypes(include='number').columns
        stats = self.df[numeric_cols].describe()
        return stats
