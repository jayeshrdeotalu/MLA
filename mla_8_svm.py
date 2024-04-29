

import numpy as np
import pandas as pd
from sklearn import svm

iris = pd.read_csv('/content/8_SVM.csv')
iris[:4]

X = iris.iloc[:, :-1] # Syntax of iloc=> df.iloc[row_start:row_end, column_start:column_end]
X[:4]

y = iris.iloc[:, -1]
y[:4]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

clf = svm.SVC(kernel='rbf')
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
y_pred[:4]

# Evaluating the classifier accuracy
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
