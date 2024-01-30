"""
A Single Layer of 3 Neurons
Version 2: Dynamic (i.e. uses loops)
Layer's Output: A list of 3 values
"""

inputs = [1.0, 2.0, 3.0, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

# Output of Current Layer
layer_outputs = []

# For each neuron
for neuron_weights, neuron_bias in zip(weights, biases):
    # Zeroed output of given neuron
    neuron_output = 0

    # For each input and weight to the neuron
    for n_input, weight in zip(inputs, neuron_weights):
        # Multiply this input by the associated weight
        # and add to the neuron's output variable
        neuron_output += n_input * weight

    # Add bias
    neuron_output += neuron_bias

    # Append neuron's result to the layer's output list
    layer_outputs.append(neuron_output)

print(layer_outputs)
