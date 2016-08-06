#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""linear_equation.py: Demonstrate solving linear equations by using SciPy.
"""
import numpy as np
from scipy.linalg import solve

# pylint: disable=invalid-name

A = np.array([[2, -1, 2],
              [1, -1, -2],
              [-2, 1, -1]])

b = np.array([[8],
              [-1],
              [-6]])

print("Solve Ax = b: \n", solve(A, b))
