import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model

# random data
A = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46]
b = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

A = np.array([A]).T
b = np.array([b]).T 

# create model
lr = linear_model.LinearRegression()

# fit(train the model)
lr.fit(A,b)

# draw random data
plt.plot(A, b, 'ro')
print(lr.intercept_)
print(lr.coef_)
# draw line
# y = ax + b, a : coefficient, b: intercept
x0 = np.array([[1, 46]]).T
y0 = x0 * lr.coef_ + lr.intercept_

plt.plot(x0, y0)
plt.show()