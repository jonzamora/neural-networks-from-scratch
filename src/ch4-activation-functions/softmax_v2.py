"""
Softmax Activation Function
Version 1: NumPy implementation
"""
import numpy as np

# Values from the previous output when we described
# what a neural network is
layer_outputs = np.array([4.8, 1.21, 2.385])

# For each value in a vector, calculate the exponential value
exp_values = np.exp(layer_outputs)
print("Exponentiated Values:", exp_values)

# Now, we normalize the values
norm_values = exp_values / np.sum(exp_values)
print("Normalized Exponentiated Values:", norm_values)
print("Sum of Normalized Exponentiated Values:", np.sum(norm_values))
