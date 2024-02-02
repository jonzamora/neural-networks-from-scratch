"""
Rectified Linear Units (ReLU) Activation Function
Version 3: NumPy implementation with np.maximum()
"""
import numpy as np

inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]

output = np.maximum(0, inputs)

print(output)
