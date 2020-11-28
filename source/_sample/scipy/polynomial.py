#!/usr/bin/env python
"""polynomial.py: Demonstrate equation solvers of SciPy.
"""
from numpy.polynomial.polynomial import Polynomial

# pylint: disable=invalid-name

# Define a polynomial x^3 - 2 x^2 + x - 2.
f = Polynomial([-2, 1, -2, 1])
print("polynomial: ", f)

# Solve f(x) == 0.
print("roots: ", f.roots())
