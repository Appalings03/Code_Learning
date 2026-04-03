import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#pandas

data = [15, 16, 18, 19, 22, 24, 29, 30, 34]
print("Moyenne : ", np.mean(data))
print("Median : ", np.median(data))
print("50%(median) : ", np.percentile(data,50))
print("25%", np.percentile(data, 25))
print("75%", np.percentile(data, 75))
print("Deviation Strandard : ",np.std(data))
print("Variance : ",np.var(data))

df = pd.read_csv('titanic.cvs')
print(df.head())
print(df.describe())
col = df['Fare']
print(col)

small_df = df[['Age', 'Sex', 'Survived']]
print(small_df.head())

df['Sex']
df['male'] = df['Sex'] == 'male'

#numpy
print(df['Fare'].values)
print(df[['Pclass', 'Fare', 'Age']].values)

arr = df[['Pclass', 'Fare', 'Age']].values
print(arr.shape) #(887, 3)

print(arr[0,1])
print(arr[0])
print(arr[:,2])

mask = arr[:, 2] < 18
print(mask)
print(arr[arr[:, 2] < 18])

arr = df[['Pclass', 'Fare', 'Age']].values
mask = arr[:, 2] < 18

print(mask.sum()) 
print((arr[:, 2] < 18).sum())

#matlib

plt.scatter(df['Age'], df['Fare'])