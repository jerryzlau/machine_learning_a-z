#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 16:26:46 2018

@author: foppylau
"""

# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

"""
# take care of missing data
# fill in missing cells with the mean of that column
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# encode the country variable
# assign a number for each unique value in this column
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
# split the column into one colum per unique value with 1 representing it's presence
# this will help remove ordering bias of the dataset
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()

# encode the purchased variable
labelencoder_Y = LabelEncoder()
y = labelencoder_Y.fit_transform(y)
"""

# split into training set and test set
# training set trains the model
# test set validates the accuracy of the model
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

"""
# Feature scaling only need to be done to features that have a huge range
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""

