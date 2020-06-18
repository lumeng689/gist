import sklearn
from sklearn.datasets import load_digits
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import learning_curve
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt

iris = load_digits()
X = iris.data
y = iris.target

train_sizes, train_loss, test_loss = learning_curve(SVC(gamma=0.001), X, y, cv=10, scoring="neg_mean_squared_error",
                                                    train_sizes=[0.1, 0.25, 0.5, 0.75, 1])
train_loss_mean = -np.mean(train_loss, axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)

plt.plot(train_sizes, train_loss_mean, 'o-', color='r', label='Training')
plt.plot(train_sizes, test_loss_mean, 'o-', color='g', label='Cross-Validation')

plt.xlabel('Training examples')
plt.ylabel('Loss')
plt.legend(loc='best')

plt.show()
# end of file
