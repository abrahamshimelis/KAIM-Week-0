import matplotlib.pyplot as plt

class ScatterPlots:
    def __init__(self, df):
        self.df = df

    def create(self, column1, column2):
        plt.scatter(self.df[column1], self.df[column2])
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.title(f'Scatter plot of {column1} vs {column2}')
        plt.show()