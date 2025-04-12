# Here we will convert a matrix into orthogonal matrix with basic methods for manupulation with Gramn-Schmidt 
import numpy as np

def orthonormal_vector_cal(A):#Returns Orthonormal Vectors 
    b = A[: , 1].reshape(-1, 1)
    X = A[: , 0].reshape(-1, 1)
    projection = ((X.T @ b) / (X.T @ X)) * X
    Y = b - projection
    return X, Y

A = np.matrix([[1,2],[2,4],[3,7]])
X, Y= orthonormal_vector_cal(A)

orthogonal_matrix = np.stack([X, Y])
print(orthogonal_matrix)