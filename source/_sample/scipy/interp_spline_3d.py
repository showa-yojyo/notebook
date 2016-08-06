#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""interp_spline_3d.py: Demonstrate spline interpolation.
"""
from scipy.interpolate import splprep, splev
import numpy as np
import matplotlib.pyplot as plt
# pylint: disable=unused-import
from mpl_toolkits.mplot3d import Axes3D

# pylint: disable=invalid-name, bad-whitespace

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
for i, xyz in zip(u, np.asarray(splev(u, tck)).T):
    print("f({:.3f}) = {}".format(i, xyz))

# Plot points and the curve.
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(xs=points[0], ys=points[1], zs=points[2],
           color='black', label='target points')
ax.plot(xs=tck[1][0], ys=tck[1][1], zs=tck[1][2],
        color='pink', label='control points')

params = np.linspace(u[0], u[-1], num=50, endpoint=True)
values = splev(params, tck)
ax.plot(xs=values[0], ys=values[1], zs=values[2],
        color='deeppink', label='cubic spline')

for pt in points.T:
    ptlabel = "({:d}, {:d}, {:d})".format(pt[0], pt[1], pt[2])
    ax.text(pt[0], pt[1], pt[2], ptlabel, color='black')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
plt.show()
