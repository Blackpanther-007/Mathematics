import numpy as np
import scipy.linalg as la

# Create the K matrix
K = la.toeplitz([2, -1, 0, 0, 0, 0])

# The given 7K⁻¹ matrix
K_inv_scaled = np.array([
    [6, 5, 4, 3, 2, 1],
    [5, 10, 8, 6, 4, 2],
    [4, 8, 12, 9, 6, 3],
    [3, 6, 9, 12, 8, 4],
    [2, 4, 6, 8, 10, 5],
    [1, 2, 3, 4, 5, 6]
])

# Verify K * (7K⁻¹) = 7I
result = K @ K_inv_scaled
print("K * (7K⁻¹):")
print(result)

# Calculate actual inverse using LU decomposition
P, L, U = la.lu(K)
L_inv = la.inv(L)
U_inv = la.inv(U)
K_inv = U_inv @ L_inv @ P.T  # Combine inverses and permutation matrix

print("\nActual inverse (K⁻¹):")
print(K_inv)

print("\n7 * actual inverse (7K⁻¹):")
print(7 * K_inv)