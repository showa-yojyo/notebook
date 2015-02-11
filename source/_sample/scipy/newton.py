# -*- coding: utf-8 -*-
"""Demonstrate equation solvers of SciPy.
"""
from scipy.optimize import newton
import numpy as np

def func(x):
    """A function."""
    return x - 2 * np.sqrt(x - 1)

# Solve func(x) == 0.
root_guess = 1.5
print("Root:", newton(func, root_guess))
