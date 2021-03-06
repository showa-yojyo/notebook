#!/usr/bin/env python
"""interp_spline_interest.py: Demonstrate spline interpolation.
"""
from scipy.interpolate import splrep, splev
import numpy as np
import matplotlib.pyplot as plt

# pylint: disable=invalid-name

# Interest rates of Jan, Feb, Mar, Jun, Dec.
x = np.array([1, 2, 3, 6, 12])
y = np.array([0.080, 0.100, 0.112, 0.144, 0.266])

# Interpolate the rates.
tck = splrep(x, y)

# Print the spline curve.
np.set_printoptions(formatter={'float': '{:.3f}'.format})
print("knot vector:\n", tck[0])
print("control points:\n", tck[1])
print("degree:\n", tck[2])

# Evaluate interest rates for each month.
for i in range(1, 13):
    print(f"month[{i:02d}]: {float(splev(i, tck)):.3f}%")

# Plot the interest curve.
time = np.linspace(1, 12, 1000, endpoint=True)
rate = splev(time, tck)

plt.figure()
plt.plot(time, rate, color='deeppink')
plt.xlabel("Month")
plt.ylabel("Rate (%)")
plt.show()
