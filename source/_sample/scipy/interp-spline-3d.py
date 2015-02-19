# -*- coding: utf-8 -*-
"""Demonstrate spline interpolation.
"""
from scipy.interpolate import splprep, splev
import numpy as np

# Set 3D points.
points = np.array(
    [[0, 100, 100,   0],  # x
     [0,   0, 100, 100],  # y
     [0,  50, 100, 150]]) # z

# Interpolate points by a 3D curve.
tck, u = splprep(points)

# Print the spline curve.
np.set_printoptions(formatter={'float': '{:.3f}'.format}, precision=3)
print("knot vector:\n", tck[0])
print("control points:\n", np.array(tck[1]))
print("degree:\n", tck[2])
print("parameter values: \n", u)

# Evaluate the curve at each parameter i in u.
for i in u:
    xyz = np.array(splev(i, tck))
    print("f({:.3f}) = {}".format(i, xyz))
