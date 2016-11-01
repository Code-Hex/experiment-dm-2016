#!/usr/bin/env python
import numpy as np

class LinearRegression:
    theta = None

    def fit(self, x, y):
    	# self.theta = np.dot(np.dot(np.linalg.inv(np.dot(x.T,x)), x.T), y)
        self.theta = np.dot(np.linalg.solve(np.dot(x.T, x), x.T), y)

    def predict(self, x):
        return np.dot(x, self.theta)

    def score(self, x, y):
        error = self.predict(x) - y
        # Ordinary Least Squares (OLS)
        ols = (error ** 2).sum()
        return ols


# http://ie.u-ryukyu.ac.jp/~tnal/2016/info4/dm/2016info4dm-w5.pdf
class RidgeRegression(LinearRegression):
    alpha = None

    def __init__(self,  alpha=0.1):
        self.alpha = alpha

    def fit(self, input, output):
        xTx = np.dot(input.T, input)
        I = np.eye(len(xTx))
        # self.theta = np.dot(np.dot(np.linalg.inv(xTx + self.alpha * I), input.T),output)
        self.theta =np.dot(np.linalg.solve(xTx + self.alpha * I, input.T), output)

