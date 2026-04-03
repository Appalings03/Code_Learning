# coding: utf-8
import pandas as pd
import numpy as np
flights = pd.read_csv('flights.csv', index_col=False)
flights
# group flights by month
flights_by_month = flights.groupby('MONTH')
flights_by_month
# fetch all December flights
flights_by_month.get_group(12)
# total distance travelled by all flights per month
flights_by_month['DISTANCE'].aggregate(np.sum)
flights_by_month['DISTANCE'].aggregate(np.mean)
flights_by_month['DISTANCE'].aggregate(np.max)
flights_by_month['DISTANCE'].aggregate(np.min)
# get the max total distance travelled and the month
flights_by_month['DISTANCE'].aggregate(np.sum).max()
flights_by_month['DISTANCE'].aggregate(np.sum).idxmax()
# get the min total distance travelled and the month
flights_by_month['DISTANCE'].aggregate(np.sum).min()
flights_by_month['DISTANCE'].aggregate(np.sum).idxmin()
# number of cancelled flights per month
flights_by_month['CANCELLED'].aggregate(np.sum)
