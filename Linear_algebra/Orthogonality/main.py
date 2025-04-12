import numpy as np

def gram_schmidt(A):
    """Converts a matrix A into an orthogonal matrix using Gram-Schmidt process.
    
    Args:
        A (np.array): Input matrix of shape (m, n).
        
    Returns:
        Q (np.array): Orthogonal matrix of same shape as A.
    """
    m, n = A.shape
    Q = np.zeros_like(A, dtype=float)
    
    for i in range(n):
        # Start with the i-th column of A
        v = A[:, i].astype(float)
        
        # Subtract projections onto previous vectors
        for j in range(i):
            q = Q[:, j]
            v -= np.dot(q, v) * q
        
        # Normalize to make it orthonormal
        norm = np.linalg.norm(v)
        if norm < 1e-10:  # Handle zero vectors (linear dependence)
            raise ValueError("Columns are linearly dependent.")
        Q[:, i] = v / norm
    
    return Q

A = np.array([[1, 2], [2, 4], [3, 7]])  # Note: np.array, not np.matrix
Q = gram_schmidt(A)

print("Original matrix A:\n", A)
print("\nOrthogonalized matrix Q:\n", Q)

QTQ = Q.T @ Q
print("\nQ^T Q (should be identity):\n", QTQ)