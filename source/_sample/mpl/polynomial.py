#!/usr/bin/env python
"""polynomial.py: Demonstrate how to draw a polynomial curve.
"""
import matplotlib.pyplot as plt
from numpy import (linspace, poly1d)

cur_fig = plt.figure()
cur_axes = cur_fig.add_subplot(111)

# pylint: disable=invalid-name
# Let f be the polynomial whose roots are 0, 1, and 3.
f = poly1d([1, -4, 3, 0])
x = linspace(-2, 4, 50)

# Draw the curve of y = f(x).
cur_axes.plot(x, f(x))

# Draw tangent lines at x = -1, 0, .., 3.
slope = f.deriv()
for i in range(-1, 4):
    cur_axes.plot(x, slope(i) * (x - i) + f(i))

plt.show()
