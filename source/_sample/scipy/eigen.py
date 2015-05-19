#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Demonstrate computing eigenvalues and eigenvectors.
"""
import numpy as np
from scipy import linalg

# Let A be a 3x3 matrix.
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
    print(eigvec[:,i])
