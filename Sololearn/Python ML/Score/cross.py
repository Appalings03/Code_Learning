import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

X_train,X_test,y_train,y_test = train_test_split(X,y)

#bluiding the model
model =LogisticRegression()
model.fit(X_train,y_train)

#evaluating the model
y_pred = model.predict(X_test)

print("Accuray:{0:.5f}".format(accuracy_score(y_test,y_pred)))
print("Precision:{0:.5f}".format(precision_score(y_test,y_pred)))
print("Recall:{0:.5f}".format(recall_score(y_test,y_pred)))
print("F1 Score:{0:.5f}".format(f1_score(y_test,y_pred)))