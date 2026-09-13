import numpy as np

# ====================================
# STATE VECTOR
# ====================================

X = np.array([
    [0.0],   # x
    [0.5],   # x_dot
    [10.0],  # theta
    [0.0]    # theta_dot
])

# ====================================
# A MATRIX
# ====================================

A = np.array([
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

# ====================================
# PRINT
# ====================================

print("State Vector X:")
print(X)

print("\nA Matrix:")
print(A)

print("\nNext State Estimate:")
print(A @ X)