import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score,precision_recall_fscore_support
from sklearn.linear_model import LogisticRegression

sensitivity_score = recall_score
def specificity_score(y_true, y_pred):
	p,r,f,s = precision_recall_fscore_support(y_true,y_pred)
	return r[0]

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=5)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Sensitivity:",sensitivity_score(y_test,y_pred))
print("Specificity:",specificity_score(y_test,y_pred))