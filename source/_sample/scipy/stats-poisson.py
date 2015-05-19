#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Demonstrate how ``scipy.stats.poisson`` works.
"""
from scipy.stats import poisson
import numpy as np

mu = 1 / 256
rv = poisson(mu)

# Compute moments.
mean, var, skew, kurt = rv.stats(moments='mvsk')

# mean == mu
print("mean: {:.8f}".format(float(mean)))

# median
print("median: {:.8f}".format(rv.median()))

# var == mu
print("var: {:.8f}".format(float(var)))

# skew == 1/sqrt(mu)
print("skew: {:.8f}".format(float(skew)))

# kurt == 1/mu
print("kurt: {:.8f}".format(float(kurt)))

# std == np.sqrt(var)
print("std: {:.8f}".format(rv.std()))
