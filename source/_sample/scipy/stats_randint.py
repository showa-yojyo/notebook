#!/usr/bin/env python
"""stats_randint.py: Demonstrate how ``scipy.stats.randint`` works.
"""
from scipy.stats import randint

# pylint: disable=invalid-name

# Define a dice model.
low = 1
high = 7
dice = randint(low, high)

# Compute moments.
mean, var, skew, kurt = dice.stats(moments='mvsk')

print(f"mean: {float(mean):.3f}")
print(f"median: {dice.median():.3f}")
print(f"var: {float(var):.3f}")
print(f"skew: {float(skew):.3f}")
print(f"kurt: {float(kurt):.3f}")
print(f"std: {dice.std():.3f}") # Or np.sqrt(var).
