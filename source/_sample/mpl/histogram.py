#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""histogram.py: Demonstrate how to show a histogram.
"""

import matplotlib.pyplot as plt
from numpy.random import randn

cur_axes = plt.gca()
_, bins, rects = cur_axes.hist(randn(1000), 50, facecolor='yellow')

for tick in cur_axes.xaxis.get_minor_ticks():
    tick.tick1On = True

for tick in cur_axes.yaxis.get_major_ticks():
    tick.gridOn = True
    tick.tick1On = False
    tick.tick2On = True
    tick.label1On = False
    tick.label2On = True

plt.show()
