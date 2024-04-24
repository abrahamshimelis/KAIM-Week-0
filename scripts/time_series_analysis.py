import matplotlib.pyplot as plt

class TimeSeriesAnalysis:
    def __init__(self, df):
        self.df = df

    def analyze(self, column):
        self.df[column].plot()
        plt.show()
