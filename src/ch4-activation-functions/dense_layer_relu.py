"""
This is a Dense Layer implementation with NumPy
Input to Layer: (n_samples=300, n_inputs=2)
Size after Forward Pass: (n_samples=300, n_inputs=2) * (n_inputs=2, n_neurons=3) = (300, 3)
"""
import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()


class DenseLayer:
    # Layer initialization
    def __init__(self, n_inputs, n_neurons):
        # Initialize weights and biases
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        self.output = None

    # Forward Pass
    def forward(self, inputs):
        # Calculate output values from inputs, weights, and biases
        self.output = np.dot(inputs, self.weights) + self.biases


# ReLU activation function
class ReLU:
    # Forward pass
    def __init__(self):
        self.output = None

    def forward(self, inputs):
        # Calculate output values from input
        self.output = np.maximum(0, inputs)


def main():

    # Create dataset
    X, y = spiral_data(samples=100, classes=3)

    # Create a Dense layer with 2 input features and 3 output values
    dense1 = DenseLayer(n_inputs=2, n_neurons=3)

    # Create ReLU activation (to be used with Dense layer)
    activation1 = ReLU()

    # Perform a forward pass of our training data through this layer
    dense1.forward(X)

    # Forward pass through ReLU activation function
    # Takes in output from previous layer
    activation1.forward(dense1.output)

    # Let's see output of the first few samples:
    print(activation1.output[:5])


if __name__ == "__main__":
    main()
