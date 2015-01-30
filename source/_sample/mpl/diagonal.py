# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
fig = plt.figure()

ax1 = fig.add_subplot(211)
ax2 = fig.add_axes([0.1, 0.1, 0.7, 0.3])

l1 = mpl.lines.Line2D([0, 1], [0, 1], transform=fig.transFigure, figure=fig)
fig.lines.extend([l1])
fig.canvas.draw()
plt.show()
