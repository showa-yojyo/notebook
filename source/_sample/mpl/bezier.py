#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bezier.py: Demonstrate how to draw Bezier curves.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np

# Unset the face color.
mpl.rcParams['patch.facecolor'] = 'none'

fig = plt.figure()
ax1 = fig.add_subplot(111)

# Define a quadric Bezier curve as path1.
verts1 = np.array([[0., 0.], [2., 4.], [4., 0.]])
codes1 = [Path.MOVETO, Path.CURVE3, Path.CURVE3]

path1 = Path(verts1, codes1)
patch1 = patches.PathPatch(path1, edgecolor='blue', lw=2, alpha=0.5)
ax1.add_patch(patch1)
ax1.plot(verts1[:, 0], verts1[:, 1], color='blue', alpha=0.5)

# Define a cubic Bezier curve as path2.
verts2 = np.array([[0., 0.], [0.5, 3.5], [1., 4.], [4., 0.]])
codes2 = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4,]

path2 = Path(verts2, codes2)
patch2 = patches.PathPatch(path2, edgecolor='red', lw=2, alpha=0.5)
ax1.add_patch(patch2)
ax1.plot(verts2[:, 0], verts2[:, 1], color='red', alpha=0.5)

ax1.set_xlim(0., 4.)
ax1.set_ylim(0., 4.)

plt.show()
