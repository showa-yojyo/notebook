#!/usr/bin/env python
"""tex.py: Demonstrate how to use TeX notation in Matplotlib.

You can obtain the original script file from:
From http://matplotlib.org/mpl_examples/statistics/histogram_demo_features.py
"""
from numpy.random import randn
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# pylint: disable=invalid-name

NPDF_TEX = r'''
$\frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{(x - \mu)^{2}}{2 \sigma ^{2}}}$
'''

# example data
MU = 100 # mean of distribution
SIGMA = 15 # standard deviation of distribution
x = MU + SIGMA * randn(10000)

NUM_BINS = 50
# the histogram of the data
n, bins, patches = plt.hist(
    x, NUM_BINS, normed=1, facecolor='deeppink', label='random')

# add a 'best fit' line
y = mlab.normpdf(bins, MU, SIGMA)
plt.plot(bins, y, 'r--', label=NPDF_TEX)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu={}$, $\sigma={}$'.format(MU, SIGMA))
plt.legend(loc='upper left', shadow=True)

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
