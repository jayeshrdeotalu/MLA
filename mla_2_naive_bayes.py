

from sklearn.datasets import load_iris
iris = load_iris()
iris['data'][:5], iris['target'][:5]

X = iris.data
y = iris.target
X[:5]

y[:5]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)
y_pred

from sklearn import metrics
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)

print("Gaussian Naive Bayes model Precision(in %):", metrics.precision_score(y_test, y_pred, average='micro')*100)

