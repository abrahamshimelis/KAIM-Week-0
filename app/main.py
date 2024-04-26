# main.py

import streamlit as st
import pandas as pd
from scipy import stats
import numpy as np
   
# Main function to run the app
def main():
    st.title("MoonLight Energy Solutions Data Analysis Dashboard")
    st.text("To identifying high-potential regions for solar installation and enhancing operational efficiency and sustainability")
    st.subheader("- Data Quality Check")
    st.subheader("- Time Series Analysis")
    st.subheader("- Analyze Solar Irradiance Patterns")
    st.subheader("- Temperature and Cleaning Trends")
    st.subheader("- Wind Conditions Analysis")

# Run the app
if __name__ == "__main__":
    main()
