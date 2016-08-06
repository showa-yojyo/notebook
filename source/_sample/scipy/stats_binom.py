#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""stats_binom.py: Demonstrate how ``scipy.stats.binom`` works.
"""
from scipy.stats import binom

# pylint: disable=invalid-name

N = 6
p = 0.25
rv = binom(N, p)

# Compute moments.
mean, var, skew, kurt = rv.stats(moments='mvsk')

# mean == N * p
print("mean: {:.3f}".format(float(mean)))

# median == np.floor(N * p) or np.ceil(N * p) ?
print("median: {:.3f}".format(rv.median()))

# var == N * p * (1 - p)
print("var: {:.3f}".format(float(var)))

# skew == (1 - 2 * p)/np.sqrt(N * p * (1 - p))
print("skew: {:.3f}".format(float(skew)))

# kurt == (1 - 6 * p * (1 - p))/(N * p * (1 - p))
print("kurt: {:.3f}".format(float(kurt)))

# std == np.sqrt(var)
print("std: {:.3f}".format(rv.std()))

print("How many times you win:")
for i in range(N + 1):
    print("{}/{}: {:.8f}".format(i, N, float(rv.pmf(i))))
