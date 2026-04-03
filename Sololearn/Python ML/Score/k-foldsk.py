from sklearn.model_selection import KFold
import pandas as pd

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Age','Fare']].values[:6]
y = df['Survived'].values[:6]

kf =KFold(n_splits=3,shuffle=True)
for train,test in kf.split(X):
	print(train,test)
