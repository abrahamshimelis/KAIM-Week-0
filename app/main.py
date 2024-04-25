# main.py

import streamlit as st
import pandas as pd
from scipy import stats
import numpy as np

# Importing the DataQualityCheck class from scripts.py
from scripts import DataQualityCheck

# Function to upload CSV files
def upload_files():
    uploaded_files = {}
    
    for region in ["Benin-Malanville", "Sierra Leone-Bumbuna", "Togo-Dapaong_QC"]:
        st.sidebar.write(f"Upload data file for {region}:")
        uploaded_file = st.sidebar.file_uploader(f"Choose a CSV file for {region}", type="csv")
        if uploaded_file is not None:
            uploaded_files[region] = uploaded_file
    
    return uploaded_files

# Data Quality Check
def data_quality_check(uploaded_files):
    for region, file in uploaded_files.items():
        st.subheader(f"Data Quality Check - {region}")
        data = pd.read_csv(file)
        
        # Initialize DataQualityCheck class
        data_checker = DataQualityCheck(data)
        
        # Perform data quality check
        missing_values = data_checker.check_missing_values()
        
        # Display missing values
        st.write("Missing Values:")
        st.write(missing_values)
        
        
# Main function to run the app
def main():
    st.title("MoonLight Energy Solutions Data Analysis Dashboard")
    
    # Upload CSV files section on the sidebar
    uploaded_files = upload_files()
    
    if uploaded_files:
        # Perform Data Quality Check for each region
        data_quality_check(uploaded_files)

# Run the app
if __name__ == "__main__":
    main()
