"""
How to compute the matrix product in Python with NumPy
"""
import numpy as np

a = [1, 2, 3]
b = [2, 3, 4]

a = np.array([a])  # shape: (1,3) row vector
b = np.array([b]).T  # shape: (3,1) column vector

print(np.dot(a, b))
