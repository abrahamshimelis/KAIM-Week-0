# KAIM-Week-0
10 Academy: Artificial Intelligence Mastery - Week 0 Challenge
## Overview
This project focuses on setting up a Python environment using Git for version control and implementing CI/CD practices. It comprises two main tasks:

1. Git and GitHub Setup: Creating a Git repository for hosting all code and implementing a folder structure for better organization.
2. EDA & Stats: Performing Exploratory Data Analysis (EDA) on solar radiation and weather data to gain insights and prepare for the development of a Streamlit dashboard.

## Task 1: Git and GitHub Setup
### Tasks
- Setting up Python environment
- Git version control
- CI/CD implementation
- Project folder structure creation

## Task 2: Dashboard Development Using Streamlit
### Tasks
- Designing and developing a Streamlit dashboard for data visualization.
- Integrating Python scripts for data fetching and processing.
- Implementing interactive features for user customization.
- Deploying the dashboard to Streamlit Community Cloud.


Goal:
The goal is to analyze environmental data and create a strategy report that recommends where to install solar panels to help the company become more efficient and sustainable.

Objectives:
Perform Exploratory Data Analysis (EDA) analysis on the following:

- Summary Statistics: Calculate the mean, median, standard deviation, and other statistical measures for each numeric column to understand data distribution.

- Data Quality Check: Look for missing values, outliers, or incorrect entries (e.g., negative values where only positive should exist), especially in columns like GHI, DNI, and DHI.

- Time Series Analysis: Analyze how variables like GHI, DNI, DHI, and Tamb change over time. You can plot these metrics across the 'Timestamp' to identify patterns or anomalies.

- Correlation Analysis: Determine the correlation between different variables like solar radiation components (GHI, DHI, DNI) and temperature measures (TModA, TModB) to uncover relationships.

- Wind Analysis: Explore wind speed (WS, WSgust, WSstdev) and wind direction (WD, WDstdev) data to identify any trends or notable wind events.

- Temperature Analysis: Compare module temperatures (TModA, TModB) with ambient temperature (Tamb) to see how they are related or vary under different conditions.

- Histograms: Create histograms for variables like GHI, DNI, DHI, WS, and temperatures to visualize the frequency distribution of these variables.

- Box Plots: Use box plots to examine the spread and presence of outliers in the solar radiation and temperature data.

- Scatter Plots: Generate scatter plots to explore the relationships between pairs of variables, such as GHI vs. Tamb, WS vs. WSgust, or any other potentially interesting pairs.

- Data Cleaning: Based on the initial analysis, clean the dataset by handling anomalies and missing values, especially in columns like Comments which appear entirely null.

Tasks:
- Set up Python environment.
- Set up Git version control. 
- Create a GitHub repository and branches for tasks.
- Commit work with descriptive messages.
- Configure CI/CD.
- Conduct Exploratory Data Analysis (EDA) and statistical analysis.
- Integrate Python scripts for data processing.
- Develop a Streamlit dashboard with interactive features.
- Deploy the dashboard to Streamlit Community Cloud.
- Document the development process and usage instructions in README.md.