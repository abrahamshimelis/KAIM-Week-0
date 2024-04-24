import pandas as pd
from scripts import SummaryStatistics, DataQualityCheck, TimeSeriesAnalysis, CorrelationAnalysis, WindAnalysis

df = pd.read_csv('data/benin-malanville.csv')

# # Create a SummaryStatistics object
# summary_statistics = SummaryStatistics(df)

# # Calculate summary statistics
# result = summary_statistics.calculate()

# # Print the result
# for column, stats in result.items():
#     print(f"Column: {column}")
#     for stat, value in stats.items():
#         print(f"  {stat}: {value}")

# dq_check = DataQualityCheck(df)

# # Now you can use the methods in your class
# print(dq_check.check_missing_values())
# print(dq_check.check_outliers('GHI'))
# print(dq_check.check_incorrect_entries('GHI')) 


# # Create an instance of TimeSeriesAnalysis
# ts_analysis = TimeSeriesAnalysis(df)

# # Now you can use the analyze method in your class
# ts_analysis.analyze('GHI')

# # Create an instance of CorrelationAnalysis
# corr_analysis = CorrelationAnalysis(df)

# # Now you can use the analyze method in your class
# print(corr_analysis.analyze('GHI', 'DNI'))

# Create an instance of WindAnalysis
wind_analysis = WindAnalysis(df)

# Now you can use the analyze_speed and analyze_direction methods in your class
print(wind_analysis.analyze_speed('WS'))
print(wind_analysis.analyze_direction('WD'))