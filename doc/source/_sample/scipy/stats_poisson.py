#!/usr/bin/env python
"""stats_poisson.py: Demonstrate how ``scipy.stats.poisson`` works.
"""
from scipy.stats import poisson

# pylint: disable=invalid-name

mu = 1 / 256
rv = poisson(mu)

# Compute moments.
mean, var, skew, kurt = rv.stats(moments='mvsk')

# mean == mu
print(f"mean: {float(mean):.8f}")

# median
print(f"median: {rv.median():.8f}")

# var == mu
print(f"var: {float(var):.8f}")

# skew == 1/sqrt(mu)
print(f"skew: {float(skew):.8f}")

# kurt == 1/mu
print(f"kurt: {float(kurt):.8f}")

# std == np.sqrt(var)
print(f"std: {rv.std():.8f}")
