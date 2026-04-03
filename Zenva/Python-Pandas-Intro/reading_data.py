#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

# read an Excel spreadsheet
"""
tracks = pd.read_excel('Tracks.xls', sheet_name=0)

print(tracks)
print(tracks.columns)
print(tracks['Milliseconds'])
"""

# read a CSV file
flights = pd.read_csv('flights.csv', index_col=False)
print(flights)

