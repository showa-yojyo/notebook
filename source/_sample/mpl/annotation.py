#!/usr/bin/env python
"""annotation.py: Demonstrate how to show an annotation.
"""
import matplotlib.pyplot as plt

cur_axes = plt.gca()
ann = cur_axes.annotate(
    'An annotate',
    xy=(1.0, 3.0),
    xycoords='data',
    xytext=(2.0, 2.5),
    textcoords='data',
    arrowprops=dict(arrowstyle='->'))

line = cur_axes.plot((1, 2, 3, 4))

cur_axes.xaxis.grid(True)
cur_axes.xaxis.set_label('TEST')
for label in cur_axes.xaxis.get_ticklabels(minor=False):
    label.set_color('red')
    label.set_rotation(-45.)
    label.set_fontsize(16)

plt.show()
