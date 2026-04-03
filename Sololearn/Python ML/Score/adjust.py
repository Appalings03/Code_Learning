import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression()
model.fit(X_train, y_train)

print("Predict Proba:")
print(model.predict_proba(X_test))

y_pred = model.predict_proba(X_test)[:, 1] > 0.75 #regression originale

print("Precision:",precision_score(y_test,y_pred))
print("recall", recall_score(y_test,y_pred))