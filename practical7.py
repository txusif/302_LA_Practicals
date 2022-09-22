# Vector Applications:
# Classify given data using support vector machines (SVM).

import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import datasets
cancer_data = datasets.load_breast_cancer()
print(cancer_data.data[5])
print(cancer_data.data.shape)

# target set
print(cancer_data.target)

cancer_data = datasets.load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(
    cancer_data.data, cancer_data.target, test_size=0.4, random_state=109)

# classifier
cls = svm.SVC(kernel="linear")

# train the model
cls.fit(x_train, y_train)

# pedict the response
pred = cls.predict(x_test)

# accuracy
print("accuracy:", metrics.accuracy_score(y_test, y_pred=pred))

# precision
print("precision:", metrics.precision_score(y_test, y_pred=pred))

# recall
print("recall:", metrics.recall_score(y_test, y_pred=pred))

print(metrics.classification_report(y_test, y_pred=pred))

# loading the datset
letters = datasets.load_digits()

# classifier
clf = svm.SVC(gamma=0.001, C=100)
# training the classifier
x, y = letters.data[:-10], letters.target[:-10]
clf.fit(x, y)

# predicting the o/p
print(clf.predict(letters.data[:-10]))
plt.imshow(letters.images[9], interpolation='nearest')
plt.show()