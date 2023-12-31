#!/usr/bin/env python
"""odeint.py: Demonstrate solving an ordinary differential equation by using
odeint.

References:
  * Solving Ordinary Differential Equations (ODEs) using Python
"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# pylint: disable=invalid-name

# Solve y''(t) + a y'(t) + b y(t) == 0.

# pylint: disable=unused-argument
def deriv(y, t):
    """Return derivatives of the array y."""
    a = 3.0
    b = 2.0
    # y[0] : y'
    # y[1] : y''
    return np.array([
        y[1], # (y[0])'
        -(a * y[0] + b * y[1]) # (y[1])'
        ])

time = np.linspace(0.0, 10.0, 1000)
yinit = np.array([0.0005, 0.2]) # initial values
y = odeint(deriv, yinit, time)

plt.figure()
# y[:,0] is the first column of y
plt.plot(time, y[:, 0], color='deeppink')
plt.xlabel("t")
plt.ylabel("y")
plt.show()
