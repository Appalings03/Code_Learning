# coding: utf-8
import pandas as pd
flights = pd.read_csv('flights.csv', index_col=False)
flights

# fetch all January flights
flights['MONTH'] == 1
flights[flights['MONTH'] == 1]

# fetch all flights that happened on the first of the month
flights[flights['DAY_OF_MONTH'] == 1]

# fetch all flights leaving New York
flights[flights['ORIGIN_STATE_NM'] == 'New York']

long_flights = flights[flights['DISTANCE'] > 4000]
long_flights

# long flights starting in Hawaii
long_flights[long_flights['ORIGIN_STATE_NM'] == "Hawaii"]

# long flights starting or ending in Hawaii
long_flights[(long_flights['ORIGIN_STATE_NM'] == "Hawaii") | (long_flights['DEST_STATE_NM'] == "Hawaii")]

# long flights in January
flights[(flights['DISTANCE'] > 4000) & (flights['MONTH'] == 1)]

# long flights not in January
flights[(flights['DISTANCE'] > 4000) & ~(flights['MONTH'] == 1)]
