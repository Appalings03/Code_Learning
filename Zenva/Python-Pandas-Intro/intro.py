#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# DataFrame: a 2D table with rows and columns
df_data = {
    'col1': np.random.rand(5),
    'col2': np.random.rand(5),
    'col3': np.random.rand(5)
}

df = pd.DataFrame(df_data)

# fetch some rows
#print(df[:1])

# fetch a col
#print(df['col1'])

# fetch multiple cols
print(df[['col1', 'col2']])
