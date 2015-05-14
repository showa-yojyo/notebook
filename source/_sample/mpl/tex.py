#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tex.py: Demonstrate how to use TeX notation in Matplotlib.

You can obtain the original script file from:
From http://matplotlib.org/mpl_examples/statistics/histogram_demo_features.py
"""
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

NPDF_TEX = r'$\frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{(x - \mu)^{2}}{2 \sigma ^{2}}}$'

# example data
mu = 100 # mean of distribution
sigma = 15 # standard deviation of distribution
x = mu + sigma * np.random.randn(10000)

num_bins = 50
# the histogram of the data
n, bins, patches = plt.hist(
    x, num_bins, normed=1, facecolor='deeppink', label='random')

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--', label=NPDF_TEX)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu={}$, $\sigma={}$'.format(mu, sigma))
plt.legend(loc='upper left', shadow=True)

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
