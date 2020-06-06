import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

iris_X = iris.data
iris_y = iris.target

print('total size %d ' % len(iris_X))
# print(iris_X)
# print(iris_y)

X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)

print('train size %d' % len(X_train))
print('test size %d' % len(X_test))

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

print(knn.predict(X_test))
print(y_test)

# file end
