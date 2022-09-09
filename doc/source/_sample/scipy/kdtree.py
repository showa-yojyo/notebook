#!/usr/bin/env python
"""kdtree.py: Demonstrate class KDTree of SciPy.
"""
import numpy as np
from scipy.spatial import KDTree

# pylint: disable=invalid-name

# Genrate 3D points: (0, 0, 0), (0, 0, 10), (0, 0, 20), ...
x, y, z = np.mgrid[0:100:10, 0:100:10, 0:100:10]
points = list(zip(x.ravel(), y.ravel(), z.ravel()))

# Construct a KDTree.
tree = KDTree(points)

# A target point included in [0, 100) * [0, 100) * [0, 100).
target = [43.831, 54.762, 83.131]
print(f"Target: {target}")

# Query for the closest point.
dist, index = tree.query(target, eps=0.01)
print(f"Closest: {tree.data[index]}")
print(f"Distance: {dist}")
