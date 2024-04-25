import matplotlib.pyplot as plt

class BoxPlots:
    def __init__(self, df):
        self.df = df

    def create(self, column):
        plt.boxplot(self.df[column])
        plt.ylabel(column)
        plt.title(f'Box plot of {column}')
        plt.show()