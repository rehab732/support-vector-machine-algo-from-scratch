# -*- coding: utf-8 -*-
"""Support_vector_machine.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ySgrdQXBOH3NoiPDOTE-3--kLytSCQF0
"""

import numpy as np
import pandas as pd

class svm:
  def __init__(self, learning_rate, no_of_iterations, lambda_parameter):
    self.learning_rate = learning_rate
    self.no_of_iterations = no_of_iterations
    self.lambda_parameter = lambda_parameter


  def fitting(self, X, y):
    # m->number of rows
    #n->number of columns
    self.m, self.n = X.shape
    self.w = np.zeros(self.n)
    self.b = 0
    self.X = X
    self.y = y
    #Gradiant Descent
    for i in range(self.no_of_iterations):
      self.update_weights()

# function update the w and b
  def update_weights(self):
    y_lable = np.where(self.y <=0, -1, 1) 

    for index, x_i in enumerate(self.X):
      condition = y_lable[index] * (np.dot(x_i, self.w) - self.b) >=1
      if(condition == True):
        dw = 2 * self.lambda_parameter * self.w
        db = 0
      else:
        dw = 2 *self.lambda_parameter * self.w - np.dot(x_i, y_lable[index])
        db = y_lable[index]
      self.w = self.w - self.learning_rate * dw
      self.b = self.b - self.learning_rate * db

# function predict lable for given input
  def predict(self, X):
    output = np.dot(X, self.w) - self.b
    predicted_value = np.sign(output)

    y_hat = np.where(predicted_value <= -1, 0, 1)
    return y_hat


  def accuracy(self, y, X):
    self.X = X
    self.y = y
    correct = 0
    for i in range(len(y)):
      if y[i] == X[i]:
        correct += 1
    return correct / float(len(y)) * 100.0

# Reading data
heart_data=pd.read_csv('/content/heart.csv')
heart_data.head()

heart_data.describe()

#separate featuers and target
#taken all featuers
features = heart_data.drop(columns='target', axis=1)
target = heart_data['target']
#print(features)
#print(target)

# Normalize data 
featuer_normalized = (features - features.mean()) / features.std()
features = featuer_normalized
#print(features)
#print(target)

# split data to train & test
#70% train , 30% test
X_train = features[0:212].to_numpy()
X_test = features[212:].to_numpy()
y_train = target[0:212].to_numpy()
y_test = target[212:].to_numpy()
#print(features.shape, X_train.shape, X_test.shape)

# training the model
classifier = svm(learning_rate=0.001, no_of_iterations=1000, lambda_parameter=0.01)
classifier.fitting(X_train, y_train)
#evaluate the model
#accuracy on training
X_train_predict = classifier.predict(X_train)
print('Accuracy of training data = ', classifier.accuracy(y_train, X_train_predict))
#accuracy on test
X_testing_predict = classifier.predict(X_test)
print('Accuracy of testing data = ', classifier.accuracy(y_test, X_testing_predict))

#separate featuers and target
#taken [trestbps,chol,thalach,bias,oldpeak]
heart_data.head()
sub_sample=heart_data.loc[:,['trestbps','thalach','chol','oldpeak']]
Target=heart_data['target']
sub_sample_normalized = (sub_sample - sub_sample.mean()) / sub_sample.std()
sub_sample = sub_sample_normalized
#print(sub_sample)
#print(Target)

# split data to train & test
#70% train , 30% test
Xsub_train = sub_sample[0:212].to_numpy()
Xsub_test = sub_sample[212:].to_numpy()
ysub_train = Target[0:212].to_numpy()
ysub_test = Target[212:].to_numpy()

# training the model
sub_classifier = svm(learning_rate=0.01, no_of_iterations=500, lambda_parameter=0.01)
sub_classifier.fitting(Xsub_train, ysub_train)
#evaluate the model
#accuracy on training
subX_train_predict = sub_classifier.predict(Xsub_train)
print('Accuracy of training data = ', sub_classifier.accuracy(ysub_train, subX_train_predict))
#accuracy on test
subX_test_predict = sub_classifier.predict(Xsub_test)
print('Accuracy of testing data = ', sub_classifier.accuracy(ysub_test, subX_test_predict))

#separate featuers and target
#taken [chol,age,thal,thalach]
XX=heart_data.loc[:,['age','thalach','chol','thal']]
yy=heart_data['target']
sub_normalized = (XX - XX.mean()) / XX.std()
XX = sub_normalized
#print(XX)
#print(yy)

# split data to train & test
#70% train , 30% test
XX_train = XX[0:212].to_numpy()
XX_test = XX[212:].to_numpy()
yy_train = yy[0:212].to_numpy()
yy_test = yy[212:].to_numpy()

# training the model
classify=svm(learning_rate=0.001, no_of_iterations=1000, lambda_parameter=0.001)
classify.fitting(XX_train, yy_train)
#evaluate the model
#accuracy on training
XX_train_predict = sub_classifier.predict(XX_train)
print('Accuracy of training data = ', classify.accuracy(yy_train, XX_train_predict))
#accuracy on test
XX_test_predict = classify.predict(XX_test)
print('Accuracy of testing data = ', sub_classifier.accuracy(yy_test, XX_test_predict))