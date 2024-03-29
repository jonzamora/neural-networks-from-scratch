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


def main():

    # Create dataset
    X, y = spiral_data(samples=100, classes=3)

    # Create a Dense layer with 2 input features and 3 output values
    dense1 = DenseLayer(n_inputs=2, n_neurons=3)

    # Perform a forward pass of our training data through this layer
    dense1.forward(X)

    # Let's see output of the first few samples:
    print(dense1.output[:5])


if __name__ == "__main__":
    main()
