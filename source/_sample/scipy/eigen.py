#!/usr/bin/env python
"""eigen.py: Demonstrate computing eigenvalues and eigenvectors for a regular
matrix.
"""
import numpy as np
from scipy import linalg

# pylint: disable=invalid-name

# Let A be a 3x3 regular matrix.
A = np.array([[2, -1, -1],
              [-1, 1, 0],
              [-1, 0, 1]])

# Compute the eigenvalues and eigenvectors of A.
eigval, eigvec = linalg.eig(A)

print("eigenvalues: ")
for val in eigval:
    print(val)

print("eigenvectors: ")
for i in range(A.shape[0]):
    print(eigvec[:, i])
