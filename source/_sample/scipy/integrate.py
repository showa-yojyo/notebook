#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""integrate.py: Demonstrate some SciPy integration functions.
"""
from scipy.integrate import trapz, simps, quad
import numpy as np

# pylint: disable=invalid-name

def f(t):
    """Integrand function."""

    return np.sin(t)

# Define sample points.
x = np.linspace(0, np.pi, num=100, endpoint=True)
y = f(x)

# Compute the integral by using trapezoid rule.
print("Trapezoid method: ", trapz(y, x))

# Compute the integral by using Simpsons's rule.
print("Simpson's method: ", simps(y, x))

# Compute the integral by using QUADPACK (Fortran).
# interval of integration; 0 to pi.
I3 = quad(f, x[0], x[-1])
print("QUADPACK: ", I3)
