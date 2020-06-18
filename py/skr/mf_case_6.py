from sklearn import svm
from sklearn import datasets
import joblib
import pickle

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target

clf.fit(X, y)

with open('save/clf.pickle', 'wb') as f:
    pickle.dump(clf, f)

with open('save/clf.pickle', 'rb') as f:
    clf2 = pickle.load(f)

print("================")

# method2
joblib.dump(clf, 'save/clf.pkl')

clf3 = joblib.load('save/clf.pkl')
print(clf3.predict(X[0:1]))
# end of file
