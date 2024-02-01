"""
2 Hidden Layers with 3 Neurons in NumPy
Layer's Output: A (3,3) NumPy array
"""
import numpy as np

inputs = np.array([[1.0, 2.0, 3.0, 2.5],
                   [2.0, 5.0, -1.0, 2.0],
                   [-1.5, 2.7, 3.3, -0.8]])

# Layer 1: First Set of Weights and Biases (3,4) -> (4,3) after transpose
weights = np.array([[0.2, 0.8, -0.5, 1.0],
                    [0.5, -0.91, 0.26, -0.5],
                    [-0.26, -0.27, 0.17, 0.87]])
biases = np.array([2.0, 3.0, 0.5])

# Layer 2: Second Set of Weights and Biases (3,3)
weights2 = np.array([[0.1, -0.14, 0.5],
                    [-0.5, 0.12, -0.33],
                    [-0.44, 0.73, -0.13]])
biases2 = np.array([-1.0, 2.0, -0.5])

layer1_outputs = np.dot(inputs, weights.T) + biases
layer2_outputs = np.dot(layer1_outputs, weights2.T) + biases2

print(layer2_outputs)
