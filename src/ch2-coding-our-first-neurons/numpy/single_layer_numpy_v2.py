"""
A Single Layer of 3 Neurons in NumPy
Version 2: Uses Matrix Product and Matrix Transposition on Weight Matrix for 1 batch of inputs
Layer's Output: A (3,3) NumPy array
"""
import numpy as np

inputs = np.array([[1.0, 2.0, 3.0, 2.5],
                   [2.0, 5.0, -1.0, 2.0],
                   [-1.5, 2.7, 3.3, -0.8]])

weights = np.array([[0.2, 0.8, -0.5, 1.0],
                    [0.5, -0.91, 0.26, -0.5],
                    [-0.26, -0.27, 0.17, 0.87]])

biases = np.array([2.0, 3.0, 0.5])

layer_outputs = np.dot(inputs, weights.T) + biases
print(layer_outputs)
