# -*- coding: utf-8 -*-
"""Demonstrate equation solvers of SciPy.
"""
from numpy.polynomial.polynomial import Polynomial, polyval

# Define a polynomial x^3 - 2 x^2 + x - 2.
f = Polynomial([-2, 1, -2, 1])
print("polynomial: ", f)

# Solve f(x) == 0.
print("roots: ", f.roots())