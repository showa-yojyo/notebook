# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial import KDTree

# Genrate 3D points: (0, 0, 0), (0, 0, 10), (0, 0, 20), ...
x, y, z = np.mgrid[0:100:10, 0:100:10, 0:100:10]
points = list(zip(x.ravel(), y.ravel(), z.ravel()))

# Construct a KDTree.
tree = KDTree(points)

# A target point included in [0, 100) * [0, 100) * [0, 100).
target = np.random.random_sample(3) * 100.
print("Target: {0}".format(target))

# Query for the closest point.
dist, index = tree.query(target, eps=0.01)
print("Closest: {0}".format(tree.data[index]))
print("Distance: {0}".format(dist))
