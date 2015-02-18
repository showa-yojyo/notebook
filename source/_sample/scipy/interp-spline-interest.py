# -*- coding: utf-8 -*-
"""Demonstrate spline interpolation.
"""
from scipy.interpolate import splrep, splev
import numpy as np

# Interest rates of Jan, Feb, Mar, Jun, Dec.
x = np.array([1, 2, 3, 6, 12])
y = np.array([0.080, 0.100, 0.112, 0.144, 0.266])

# Interpolate the rates.
tck = splrep(x, y)

# Print the spline curve.
np.set_printoptions(formatter={'float': '{:.3f}'.format})
print("knot vector:\n", tck[0])
print("control points:\n", tck[1])
print("degree (order - 1):\n", tck[2])

# Evaluate interest rates for each month.
for i in range(1, 13):
    print("month[{0:02d}]: {1:.3f}%".format(
        i, float(splev(i, tck))))
