"""
A Single Layer of 3 Neurons
Version 3: NumPy version (see vanilla_python for non-NumPy layers)
Layer's Output: A NumPy array of 3 values
"""
import numpy as np

inputs = np.array([1.0, 2.0, 3.0, 2.5])
weights = np.array([[0.2, 0.8, -0.5, 1],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]])
biases = np.array([2.0, 3.0, 0.5])

layer_outputs = np.dot(weights, inputs) + biases
print(layer_outputs)
