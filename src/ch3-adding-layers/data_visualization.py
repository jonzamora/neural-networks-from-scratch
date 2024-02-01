"""
Spiral Data Visualization
The Data has 3 classes with 100 samples per class
"""

import matplotlib.pyplot as plt
import nnfs
from nnfs import datasets

nnfs.init()

X, y = datasets.spiral_data(samples=100, classes=3)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="brg")
plt.show()
