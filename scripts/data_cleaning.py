from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd

class DataCleaning:
    def __init__(self, df):
        self.df = df

    def handle_missing_values(self, column):
        # Check if all values in the column are missing
        if self.df[column].isna().all():
            # If all values are missing, fill with a default value
            # For numeric columns, you might use 0 or another default value
            # For non-numeric columns, you might use an empty string or another default value
            self.df[column].fillna(0, inplace=True)
            return self.df

        # Identify the data type of the column
        dtype = self.df[column].dtype

        # Choose the imputation strategy based on the data type
        if np.issubdtype(dtype, np.number):
            # Use mean imputation for numeric columns
            strategy = 'mean'
        else:
            # Use most frequent imputation for non-numeric columns
            strategy = 'most_frequent'

        # Create the imputer
        imputer = SimpleImputer(strategy=strategy)

        # Perform the imputation
        self.df[column] = imputer.fit_transform(self.df[column].values.reshape(-1, 1))

        return self.df
