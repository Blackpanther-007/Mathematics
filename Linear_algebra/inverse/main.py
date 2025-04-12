import numpy as np

A = np.matrix([[1,0],[0,1],[1,1]])
V = np.matrix([[2,3,4]]).T
X = A@ np.linalg.inv(A.T@A) @ A.T @V
print(X)
