import streamlit as st
import pandas as pd
import os
import sys

# Get the absolute path of the scripts directory
scripts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts')

# Add the scripts directory to sys.path
sys.path.append(scripts_dir)

from scripts import SummaryStatistics, TimeSeriesAnalysis

# Function to get the absolute path of the data folder
def get_data_folder_path():
    current_file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(os.path.dirname(current_file_path))
    data_folder_path = os.path.join(parent_directory, "data")
    return data_folder_path

# Load dataset from file
def load_dataset(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        st.error(f"File not found at path: {file_path}")
        return None

# Analyze Solar Irradiance Patterns
def analyze_solar_irradiance_patterns():
    st.title("Analyze Solar Irradiance Patterns")

    # Specify file paths for the three regions directly
    data_folder_path = get_data_folder_path()
    file_paths = {
        "Benin-Malanville": os.path.join(data_folder_path, "benin-malanville.csv"),
        "Sierra Leone-Bumbuna": os.path.join(data_folder_path, "sierraleone-bumbuna.csv"),
        "Togo-Dapaong_QC": os.path.join(data_folder_path, "togo-dapaong_qc.csv")
    }

    # Select a region to analyze
    selected_region = st.selectbox("Select Region", list(file_paths.keys()))

    # Load and preprocess the selected dataset
    data = load_dataset(file_paths[selected_region])

    # Check if 'Timestamp' column exists in the dataset
    if "Timestamp" in data.columns:
        # Exclude 'Timestamp', 'Comments', and 'ModA' columns from the dropdown options
        excluded_columns = ["Timestamp", "Comments"]
        selectable_columns = [col for col in data.columns if col not in excluded_columns]

        # Calculate summary statistics for the dataset
        st.subheader("Summary Statistics")
        summary_stats = SummaryStatistics(data)
        stats_table = summary_stats.calculate()
        st.write(stats_table)

        # Create a single select dropdown for choosing the solar irradiance column
        selected_column = st.selectbox("Select Solar Irradiance Column", selectable_columns)

        # Initialize TimeSeriesAnalysis class
        ts_analysis = TimeSeriesAnalysis(data)

        # Perform time series analysis for the selected solar irradiance column
        st.subheader(f"Time Series Analysis for {selected_column}")
        ts_analysis.analyze("Timestamp", selected_column)

    else:
        st.error("Timestamp column not found in the dataset.")

# Main function to run the app
def main():
    analyze_solar_irradiance_patterns()

# Run the app
if __name__ == "__main__":
    main()
