import pandas as pd
from scripts import SummaryStatistics, DataQualityCheck

df = pd.read_csv('data/benin-malanville.csv')

# Create a SummaryStatistics object
summary_statistics = SummaryStatistics(df)

# Calculate summary statistics
result = summary_statistics.calculate()

# Print the result
for column, stats in result.items():
    print(f"Column: {column}")
    for stat, value in stats.items():
        print(f"  {stat}: {value}")

dq_check = DataQualityCheck(df)

# Now you can use the methods in your class
print(dq_check.check_missing_values())
print(dq_check.check_outliers('GHI'))
print(dq_check.check_incorrect_entries('GHI')) 