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
