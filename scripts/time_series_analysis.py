import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

class TimeSeriesAnalysis:
    def __init__(self, df):
        self.df = df

    def analyze(self, time_column, column1):
        self.df[time_column] = pd.to_datetime(self.df[time_column])
        self.df.set_index(time_column, inplace=True)

        fig, ax = plt.subplots()
        ax.plot(self.df.index, self.df[column1])
        ax.set_xlabel(time_column)
        ax.set_ylabel(column1)

        st.pyplot(fig.figure)
