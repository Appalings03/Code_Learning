import pandas as pd

from sklearn.linear_model import LogisticRegression

df = pd.read_csv("titanic.cvs")
X = df[['Fare', 'Age']].values
y = df['Survived'].values
model = LogisticRegression()
model.fit(X, y)
print(model.coef_, model.intercept_)
