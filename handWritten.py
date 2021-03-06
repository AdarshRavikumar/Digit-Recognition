# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:57:54 2018

@author: Adarsh
"""

# Classification template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('train.csv')
X = dataset.iloc[:,1: ].values
y = dataset.iloc[:,0].values

for i in range(0,100):
    plt.imshow(np.array(X[i]).reshape(28,28), cmap='gray')
    plt.axis('off')
    plt.title(str(y[i]))


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting classifier to the Training set

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier()

classifier.fit(X_train,y_train)
# Create your classifier here

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(y_test, y_pred)
acc=accuracy_score(y_test,y_pred)
