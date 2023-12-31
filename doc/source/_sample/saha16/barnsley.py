#!/usr/bin/env python
"""barnsley.py: Python からはじめる数学入門 pp. 175-177 改造版

Draw Barnsley's Fern

Usage:
  barnsley.py [number of points]
"""

import random
import sys
import matplotlib.pyplot as plt

PROBABILITY = (0.85, 0.07, 0.07, 0.01)

def transformation1(p):
    x, y = p
    x1 = 0.85 * x + 0.04 * y
    y1 = -0.04 * x + 0.85 * y + 1.6
    return x1, y1

def transformation2(p):
    x, y = p
    x1 = 0.2 * x - 0.26 * y
    y1 = 0.23 * x + 0.22 * y + 1.6
    return x1, y1

def transformation3(p):
    x, y = p
    x1 = -0.15 * x + 0.28 * y
    y1 = 0.26 * x + 0.24 * y + 0.44
    return x1, y1

def transformation4(p):
    x, y = p
    x1 = 0
    y1 = 0.16 * y
    return x1, y1

TRANSFORMATIONS = (
    transformation1,
    transformation2,
    transformation3,
    transformation4,)

def transform(p):
    x, y = random.choices(TRANSFORMATIONS, weights=PROBABILITY)[0](p)
    return x, y

def draw_fern(n):
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
        n = int(input('Enter the number of points in the fern: '))

    xdata, ydata = draw_fern(n)

    plt.plot(xdata, ydata, 'o')
    plt.title(f'Fern with {n} points')
    plt.show()

if __name__ == '__main__':
    main()
