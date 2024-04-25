# Exploratory Data Analysis (EDA) Modules

This package contains several Python classes for performing Exploratory Data Analysis (EDA) on a dataset. Each class is responsible for a specific task in the EDA process.

## Modules

1. **SummaryStatistics**: This class calculates summary statistics such as mean, median, and standard deviation for each numeric column in the dataset.

2. **DataQualityCheck**: This class checks for data quality issues such as missing values, outliers, and incorrect entries in the dataset.

3. **TimeSeriesAnalysis**: This class performs time series analysis on the dataset, analyzing how certain variables change over time.

4. **Histograms**: This class creates histograms for specified variables to visualize their frequency distribution.

5. **BoxPlots**: This class creates box plots for specified variables to examine their spread and presence of outliers.

6. **ScatterPlots**: This class generates scatter plots to explore the relationships between pairs of variables.

7. **DataCleaning**: This class cleans the dataset by handling anomalies and missing values.

## Usage

To use these modules, you need to import them into your Python script. Here's an example:

```python
from scripts import SummaryStatistics, DataQualityCheck, TimeSeriesAnalysis, CorrelationAnalysis, WindAnalysis, TemperatureAnalysis, DataCleaning, Histograms, BoxPlots, ScatterPlots
