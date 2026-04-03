# coding: utf-8
import pandas as pd
flights = pd.read_csv('flights.csv', index_col=False)

# view the first and last few rows and columns
flights

# selecting a column
flights['ORIGIN']

# select multiple columns (origin and destination airports)
flights[['ORIGIN', 'DEST']]

# select the first few rows
flights[:3]

# select a row and column entry in the DataFrame
flights.iloc[0,0]

# selecting the 3rd row and 2nd col
flights.iloc[2, 1]

# mixing row indices with string column names
flights.iloc[2, flights.columns.get_loc('DAY_OF_MONTH')]
flights.iloc[:3, flights.columns.get_loc('DAY_OF_MONTH')]
flights.iloc[0, [flights.columns.get_loc('ORIGIN'), flights.columns.get_loc('DEST')]]
flights.iloc[:3, [flights.columns.get_loc('ORIGIN'), flights.columns.get_loc('DEST')]]
