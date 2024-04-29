
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

irisData = load_iris()
irisData

X = irisData.data
y = irisData.target
X[:5]

y[:5]

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size = 0.2)

knn = KNeighborsClassifier(n_neighbors=7)

knn.fit(X_train, y_train)

y_pred=knn.predict(X_test)
y_pred

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

