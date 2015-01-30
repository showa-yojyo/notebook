# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

ax = plt.gca()
n, bins, rects = ax.hist(np.random.randn(1000), 50, facecolor='yellow')

for tick in ax.xaxis.get_minor_ticks():
    tick.tick1On = True

for tick in ax.yaxis.get_major_ticks():
    tick.gridOn = True
    tick.tick1On = False
    tick.tick2On = True
    tick.label1On = False
    tick.label2On = True

plt.show()
