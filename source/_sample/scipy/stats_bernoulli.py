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
print(f"mean: {float(mean):.3f}")

# median == 0.5 (if p == 0.5)
print(f"median: {rv.median():.3f}")

# var == p * (1 - p)
print(f"var: {float(var):.3f}")

# skew == (1 - 2 * p)/np.sqrt(p * (1 - p))
print(f"skew: {float(skew):.3f}")

# kurt == -2 (if p == 0.5)
print(f"kurt: {float(kurt):.3f}")

# std == np.sqrt(var)
print(f"std: {rv.std():.3f}")
