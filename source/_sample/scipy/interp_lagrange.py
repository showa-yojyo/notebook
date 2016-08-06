#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""interp_lagrange.py: Demonstrate Lagrange interpolating.
"""
from scipy.interpolate import lagrange
import numpy as np

# pylint: disable=invalid-name

# x-coordinates of a set of datapoints
x = np.array([-1.5, -0.75, 0, 0.75, 1.5])

# y-coordinates of a set of datapoints
y = np.array([-14.1014, -0.931596, 0, 0.931596, 14.1014])

# Compute Lagrange interpolating polynomial.
f = lagrange(x, y)

print("Interpolating polynomial: \n", f)
