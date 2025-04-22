import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def rms_error_cal(X, Y, C):
    y = np.matmul(X, C)
    e = np.sqrt( np.matmul((Y - y).T ,(Y -y))/len(Y) )
    return e
def linear_regression(x, y):
    z = np.ones((len(x),1))
    X = np.column_stack([x, z])
    Y = np.array(y).reshape(-1, 1)
    inter = np.linalg.inv(np.matmul(X.T, X))
    C = np.matmul(inter, np.matmul(X.T, Y))
    e = rms_error_cal(X, Y, C)
    y1 = X @ C
    return C, y1, e 



x = [1,2,3,4,5]
y = [1,3,6,9,13]
c, Y, e= linear_regression(x, y)
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.plot(x, Y)
plt.show()