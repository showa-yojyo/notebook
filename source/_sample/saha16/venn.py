#!/usr/bin/env python
"""venn.py: 

Usage:
  venn.py
"""
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet

def main():
    if True:
        s1 = FiniteSet(*range(1, 20, 2))
        s2 = FiniteSet(2, 3, 5, 7, 11, 13, 17, 19)
    else:
        s1 = {i for i in range(1, 20, 2)}
        s2 = {2, 3, 5, 7, 11, 13, 17, 19}
    venn2(subsets=[s1, s2])
    plt.show()

if __name__ == '__main__':
    main()
