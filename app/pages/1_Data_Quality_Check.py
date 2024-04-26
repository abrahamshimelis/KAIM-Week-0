# main.py

import streamlit as st
import pandas as pd
import os
from scripts import DataQualityCheck

# Function to get the absolute path of the data folder
def get_data_folder_path():
    current_file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(os.path.dirname(current_file_path))
    data_folder_path = os.path.join(parent_directory, "data")
    return data_folder_path

# Data Quality Check
def data_quality_check():
    st.title("Data Quality Check")
    
    # Specify file paths for the three regions directly
    data_folder_path = get_data_folder_path()
    file_paths = {
        "Benin-Malanville": os.path.join(data_folder_path, "benin-malanville.csv"),
        "Sierra Leone-Bumbuna": os.path.join(data_folder_path, "sierraleone-bumbuna.csv"),
        "Togo-Dapaong_QC": os.path.join(data_folder_path, "togo-dapaong_qc.csv")
    }

    # Create columns for each region's table horizontally
    col1, col2, col3 = st.columns(3)

    for idx, (region, file_path) in enumerate(file_paths.items(), start=1):
        with col1 if idx % 3 == 1 else col2 if idx % 3 == 2 else col3:
            st.subheader(region)
            try:
                data = pd.read_csv(file_path)
                
                # Initialize DataQualityCheck class
                data_checker = DataQualityCheck(data)
                
                # Perform data quality check
                missing_values = data_checker.check_missing_values()
                
                # Display missing values as a table
                st.write(missing_values)
            except FileNotFoundError:
                st.write(f"File not found at path: {file_path}")

# Main function to run the app
def main():
    data_quality_check()

# Run the app
if __name__ == "__main__":
    main()
