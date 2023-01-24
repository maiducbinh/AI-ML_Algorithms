import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# random data
A = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46]
b = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# visualize data
plt.plot(A, b, 'ro')

# change row vector to column vector
A = np.array([A]).T
b = np.array([b]).T 

# create vector 1
ones = np.ones_like(A)
# = ones = np.ones((A.shape[0],1), dtype=np.int8)

#combine A and 1
A = np.concatenate((A, ones), axis = 1)

# use formular
# linalg: linear algebra
# dot: phep nhan 2 ma tran
x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b)

# data to draw
x0 = np.array([1, 46]).T
y0 = x[1][0] + x0 * x[0][0]

# test predicting data
x_test = 12
y_test = x.test * x[0][0] + x[1][0]

print(y_test)
plt.plot(x0, y0)
plt.show()