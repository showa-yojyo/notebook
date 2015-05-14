#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""polynomial.py: Demonstrate how to draw a polynomial curve.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(111)

# Let f be the polynomial whose roots are 0, 1, and 3.
f = np.poly1d([1, -4, 3, 0])
x = np.linspace(-2, 4, 50)

# Draw the curve of y = f(x).
ax1.plot(x, f(x))

# Draw tangent lines at x = -1, 0, .., 3.
slope = f.deriv()
for i in range(-1, 4):
    ax1.plot(x, slope(i) * (x - i) + f(i))

plt.show()
