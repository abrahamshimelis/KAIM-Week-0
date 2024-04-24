import pandas as pd
from scripts import SummaryStatistics

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