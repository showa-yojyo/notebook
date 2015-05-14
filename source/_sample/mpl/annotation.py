#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

ax = plt.gca()
ann = ax.annotate(
    'An annotate',
    xy=(1.0, 3.0),
    xycoords='data',
    xytext=(2.0, 2.5),
    textcoords='data',
    arrowprops=dict(arrowstyle='->'))

line = ax.plot((1, 2, 3, 4))

ax.xaxis.grid(True)
ax.xaxis.set_label('TEST')
for label in ax.xaxis.get_ticklabels(minor=False):
    label.set_color('red')
    label.set_rotation(-45.)
    label.set_fontsize(16)

plt.show()
