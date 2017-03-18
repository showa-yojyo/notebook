#!/usr/bin/env python
"""stats_bernoulli.py: Demonstrate how ``scipy.stats.bernoulli`` works.
"""
from scipy.stats import bernoulli

# pylint: disable=invalid-name

# Let p be the probability of the coin landing heads.
p = 0.5
rv = bernoulli(p)

# Compute moments.
mean, var, skew, kurt = rv.stats(moments='mvsk')

# mean == p.
print("mean: {:.3f}".format(float(mean)))

# median == 0.5 (if p == 0.5)
print("median: {:.3f}".format(rv.median()))

# var == p * (1 - p)
print("var: {:.3f}".format(float(var)))

# skew == (1 - 2 * p)/np.sqrt(p * (1 - p))
print("skew: {:.3f}".format(float(skew)))

# kurt == -2 (if p == 0.5)
print("kurt: {:.3f}".format(float(kurt)))

# std == np.sqrt(var)
print("std: {:.3f}".format(rv.std()))
