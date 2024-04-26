import streamlit as st
import pandas as pd
import os
import sys

# Get the absolute path of the scripts directory
scripts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts')

# Add the scripts directory to sys.path
sys.path.append(scripts_dir)
from scripts import TimeSeriesAnalysis

# Function to get the absolute path of the data folder
def get_data_folder_path():
    current_file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(os.path.dirname(current_file_path))
    data_folder_path = os.path.join(parent_directory, "data")
    return data_folder_path

# Time Series Analysis
def time_series_analysis():
    st.title("Time Series Analysis")

    # Specify file paths for the three regions directly
    data_folder_path = get_data_folder_path()
    file_paths = {
        "Benin-Malanville": os.path.join(data_folder_path, "benin-malanville.csv"),
        "Sierra Leone-Bumbuna": os.path.join(data_folder_path, "sierraleone-bumbuna.csv"),
        "Togo-Dapaong_QC": os.path.join(data_folder_path, "togo-dapaong_qc.csv")
    }

    # Create columns for each region's analysis horizontally
    col1, col2, col3 = st.columns(3)

    for idx, (region, file_path) in enumerate(file_paths.items(), start=1):
        with col1 if idx % 3 == 1 else col2 if idx % 3 == 2 else col3:
            st.subheader(region)
            try:
                data = pd.read_csv(file_path)

                if "Timestamp" in data.columns:
                    # Convert Timestamp to datetime format
                    data["Timestamp"] = pd.to_datetime(data["Timestamp"])

                    # Initialize TimeSeriesAnalysis class
                    ts_analysis = TimeSeriesAnalysis(data)

                    # Perform time series analysis
                    selectable_columns = [col for col in data.columns if col != "Timestamp"]
                    unique_key = f"{region}_{file_path}"

                    # Display select box for column selection
                    selected_column = st.selectbox(f"Select Column {region}", selectable_columns, key=unique_key)

                    # Analyze time series data based on selection
                    ts_analysis.analyze("Timestamp", selected_column)
                else:
                    st.write(f"Timestamp column not found in the dataset for {region}.")
            except FileNotFoundError:
                st.write(f"File not found at path: {file_path}")

# Main function to run the app
def main():
    time_series_analysis()

# Run the app
if __name__ == "__main__":
    main()
