import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

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
        stats = data.describe()
        st.write(stats)

        # Create a single select dropdown for choosing the solar irradiance column
        selected_column = st.selectbox("Select Solar Irradiance Column", selectable_columns)

        # Perform time series analysis for the selected solar irradiance column
        st.subheader(f"Time Series Analysis for {selected_column}")
        time_series_analysis(data, "Timestamp", selected_column)

    else:
        st.error("Timestamp column not found in the dataset.")

# Time Series Analysis Function
def time_series_analysis(data, time_column, column1):
    data[time_column] = pd.to_datetime(data[time_column])
    data.set_index(time_column, inplace=True)

    fig, ax = plt.subplots()
    ax.plot(data.index, data[column1])
    ax.set_xlabel(time_column)
    ax.set_ylabel(column1)

    st.pyplot(fig)

# Main function to run the app
def main():
    analyze_solar_irradiance_patterns()

# Run the app
if __name__ == "__main__":
    main()
