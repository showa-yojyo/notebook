#!/usr/bin/env python
"""lu.py: Demonstrate LU decomposition.
"""
import numpy as np
from scipy.linalg import lu

# pylint: disable=invalid-name

A = np.array([[1, 2, 2],
              [2, 5, 6],
              [3, 8, 12]])

print("LU decomposition (A = PLU): ")
P, L, U = lu(A)
print("P: \n", P)
print("L: \n", L)
print("U: \n", U)
print("PLU: \n", P @ L @ U)
