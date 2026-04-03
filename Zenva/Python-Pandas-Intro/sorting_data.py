# coding: utf-8
import pandas as pd
flights = pd.read_csv('flights.csv', index_col=False)
flights

# sort values by a column
flights.sort_values(by=['DISTANCE'])
flights.sort_values(by=['DISTANCE'], ascending=False)

# sort by AIR_TIME descending
flights.sort_values(by=['AIR_TIME'], ascending=False)

# sort values by multiple columns
flights.sort_values(by=['DISTANCE', 'AIR_TIME'], ascending=False)
