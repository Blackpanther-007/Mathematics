import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def find_coefficients(A, d):
    X = np.linalg.lstsq(A, d, rcond=None)[0]
    return X

# Load data
df = pd.read_csv('C:/Users/HP/Documents/codes/Mathematics/Linear_algebra/least_square/dataset.csv')
print(df.head())

# Prepare data
x1 = df['x1'].values
x2 = df['x2'].values
x3 = df['x3'].values
y = df['y'].values

# Create design matrix with all features (including intercept)
A = np.column_stack([np.ones_like(x1), x1, x2, x3])
d = y.reshape(-1, 1)  # Make sure d is a column vector

# Calculate coefficients
X = find_coefficients(A, d)
print("\nCoefficients:")
print(f"Intercept (C): {X[0][0]:.4f}")
print(f"x1 coefficient (D): {X[1][0]:.4f}")
print(f"x2 coefficient: {X[2][0]:.4f}")
print(f"x3 coefficient: {X[3][0]:.4f}")

# Predictions
y_pred = A @ X

# Plotting actual vs predicted
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(y, y_pred, color='blue')
ax.plot([min(y), max(y)], [min(y), max(y)], 'r--')  # Perfect prediction line
ax.set_xlabel('Actual Values')
ax.set_ylabel('Predicted Values')
ax.set_title('Actual vs Predicted Values')
ax.grid(True)
plt.show()