class WindAnalysis:
    def __init__(self, df):
        self.df = df

    def analyze_speed(self, column):
        return self.df[column].describe()

    def analyze_direction(self, column):
        return self.df[column].describe()
