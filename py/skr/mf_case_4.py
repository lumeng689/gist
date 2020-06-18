import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print(knn.score(X_test, y_test))

knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
print("scores:==")
print(scores)
print("mean of score:")
print(scores.mean())

# param
k_range = range(1, 31)
k_scores = []

print("!score keys:")
print(sorted(sklearn.metrics.SCORERS.keys()))

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
    loss = -cross_val_score(knn, X, y, cv=10, scoring='neg_mean_squared_error')
    # k_scores.append(scores.mean())
    k_scores.append(loss.mean())

plt.plot(k_range, k_scores)
plt.xlabel('Value of k for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()

# end of file
