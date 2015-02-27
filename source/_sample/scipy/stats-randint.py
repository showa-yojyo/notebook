# -*- coding: utf-8 -*-
"""Demonstrate how ``scipy.stats.randint`` works.
"""
from scipy.stats import randint
import numpy as np

# Define a dice model.
low = 1
high = 7
dice = randint(low, high)

# Compute moments.
mean, var, skew, kurt = dice.stats(moments='mvsk')

print("mean: {:.3f}".format(float(mean)))
print("median: {:.3f}".format(dice.median()))
print("var: {:.3f}".format(float(var)))
print("skew: {:.3f}".format(float(skew)))
print("kurt: {:.3f}".format(float(kurt)))
print("std: {:.3f}".format(dice.std())) # Or np.sqrt(var).
