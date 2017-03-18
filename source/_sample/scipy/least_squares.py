#!/usr/bin/env python
"""least_squares.py: Demonstrate least-squares fitting method of SciPy.

References:
  * http://sagemath.wikispaces.com/numpy.linalg.lstsq
"""
from scipy.linalg import lstsq
import numpy as np
import matplotlib.pyplot as plt

# pylint: disable=invalid-name

# Sampling data set.
xd = np.array([72, 67, 65, 55, 25, 36, 56, 34,
               18, 71, 67, 48, 72, 51, 53])
yd = np.array([202, 186, 187, 180, 156, 169, 174,
               172, 153, 199, 193, 174, 198, 183, 178])

# Solve the linear least squares problem.
A = np.c_[xd[:, np.newaxis], np.ones(xd.shape[0])]
B = yd
X, residues, rank, s = lstsq(A, B)

# Show the regression curve (line).
a = X[0]
b = X[1]
print("Line: y = {:.3f}x {:+.3f}".format(a, b))

# Plot both the sampling data and the regression curve.
# pylint: disable=invalid-slice-index
plt.figure()
xs = np.r_[min(xd):max(xd):15j]
ys = a * xs + b

plt.plot(xs, ys, color='deeppink', label='regression curve')
plt.scatter(xd, yd, color='pink', marker='s', label='data set')
plt.legend()
plt.show()
