#!/usr/bin/env python
"""henon.py: Python からはじめる数学入門 pp. 175-177 改造版

Usage:
  henon.py [number of points]
"""

import random
import sys
import matplotlib.pyplot as plt

def transform(p):
    x, y = p
    x1 = y + 1 - 1.4 * x**2
    y1 = 0.3 * x
    return x1, y1

def calc_points(n):
    xdata = [0] * n
    ydata = [0] * n

    x1, y1 = 1, 1
    for i in range(n):
        x1, y1 = transform((x1, y1))
        xdata[i] = x1
        ydata[i] = y1

    return xdata, ydata

def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input('Enter the number of points in the Henon map: '))

    xdata, ydata = calc_points(n)

    plt.plot(xdata, ydata, 'o')
    plt.title(f'Henon map with {n} points')
    plt.show()

if __name__ == '__main__':
    main()
