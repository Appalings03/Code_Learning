from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
import pandas as pd


df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

model = DecisionTreeClassifier()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=22)
model.fit(X_train, y_train)

print(model.predict([[3,True,22,1,0,7.25]]))
y_pred = model.predict(X_test)
print("Accuracy : ", accuracy_score(y_test, y_pred))
print("Precision : " , precision_score(y_test,y_pred))
print("Recall : ", recall_score(y_test,y_pred))
