import matplotlib.pyplot as plt

class Histograms:
    def __init__(self, df):
        self.df = df

    def create(self, column):
        plt.hist(self.df[column])
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {column}')
        plt.show()