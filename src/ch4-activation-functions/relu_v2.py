"""
Rectified Linear Units (ReLU) Activation Function
Version 2: Loop implementation with max() function
"""

inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]

output = []

for i in inputs:
    output.append(max(0, i))

print(output)
