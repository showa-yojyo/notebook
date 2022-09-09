#!/usr/bin/env python
"""sierpinski.py: Python からはじめる数学入門 pp. 175-177 改造版

Usage:
  sierpinski.py [number of points]
"""

import random
import sys
import matplotlib.pyplot as plt

def transformation1(p):
    x, y = p
    x1 = 0.5 * x
    y1 = 0.5 * y
    return x1, y1

def transformation2(p):
    x, y = p
    x1 = 0.5 * x + 0.5
    y1 = 0.5 * y + 0.5
    return x1, y1

def transformation3(p):
    x, y = p
    x1 = 0.5 * x + 1
    y1 = 0.5 * y
    return x1, y1

TRANSFORMATIONS = (
    transformation1,
    transformation2,
    transformation3,)

def transform(p):
    x, y = random.choice(TRANSFORMATIONS)(p)
    return x, y

def calc_points(n):
    xdata = [0] * n
    ydata = [0] * n

    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transform((x1, y1))
        xdata[i] = x1
        ydata[i] = y1

    return xdata, ydata

def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input('Enter the number of points in the gasket: '))

    xdata, ydata = calc_points(n)

    plt.plot(xdata, ydata, 'o')
    plt.title(f'Sierpinski with {n} points')
    plt.show()

if __name__ == '__main__':
    main()
