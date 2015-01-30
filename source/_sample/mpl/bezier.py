# -*- coding: utf-8 -*-
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
verts1 = [(0., 0.), (2., 4.), (4., 0.)]
codes1 = [Path.MOVETO, Path.CURVE3, Path.CURVE3]

path1 = Path(verts1, codes1)
patch1 = patches.PathPatch(path1, edgecolor='blue', lw=2, alpha=0.5)
ax1.add_patch(patch1)
ax1.plot([v[0] for v in verts1], [v[1] for v in verts1], color='blue', alpha=0.5)

# Define a cubic Bezier curve as path2.
verts2 = [(0., 0.), (0.5, 3.5), (1., 4.), (4., 0.)]
codes2 = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4,]

path2 = Path(verts2, codes2)
patch2 = patches.PathPatch(path2, edgecolor='red', lw=2, alpha=0.5)
ax1.add_patch(patch2)
ax1.plot([v[0] for v in verts2], [v[1] for v in verts2], color='red', alpha=0.5)

ax1.set_xlim(0., 4.)
ax1.set_ylim(0., 4.)

plt.show()
