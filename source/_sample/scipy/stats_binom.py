#!/usr/bin/env python
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
print(f"mean: {float(mean):.3f}")

# median == np.floor(N * p) or np.ceil(N * p) ?
print(f"median: {rv.median():.3f}")

# var == N * p * (1 - p)
print(f"var: {float(var):.3f}")

# skew == (1 - 2 * p)/np.sqrt(N * p * (1 - p))
print(f"skew: {float(skew):.3f}")

# kurt == (1 - 6 * p * (1 - p))/(N * p * (1 - p))
print(f"kurt: {float(kurt):.3f}")

# std == np.sqrt(var)
print(f"std: {rv.std():.3f}")

print("How many times you win:")
for i in range(N + 1):
    print(f"{i}/{N}: {float(rv.pmf(i)):.8f}")
