import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression

X =[[1,1],[2,2],[3,3],[4,4]]
y =[0,0,1,1]

X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=27)

print('X_train',X_train)
print('X_test',X_test)
