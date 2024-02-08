"""
Softmax Activation Function
Version 1: Loop implementation
"""
import math

# Values from the previous output when we described
# what a neural network is
layer_outputs = [4.8, 1.21, 2.385]

# "e" is a mathematical constant
E = math.e

# For each value in a vector, calculate the exponential value
exp_values = []
for output in layer_outputs:
    exp_values.append(E ** output)

print("Exponentiated Values:", exp_values)

# Now, we normalize the values
norm_base = sum(exp_values)
norm_values = []
for value in exp_values:
    norm_values.append(value / norm_base)

print("Normalized Exponentiated Values:", norm_values)
print("Sum of Normalized Exponentiated Values:", sum(norm_values))
