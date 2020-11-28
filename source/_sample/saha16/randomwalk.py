#!/usr/bin/env python
"""randomwalk.py: Python からはじめる数学入門

Usage:
  randomwalk.py [iterations]
"""
from itertools import tee
import matplotlib.pyplot as plt
import random
import sys

def transformation1(p):
    return p[0] + 1, p[1] - 1

def transformation2(p):
    return p[0] + 1, p[1] + 1

def transform(p):
    return random.choice((transformation1, transformation2))(p)

def build_trajectory(p, n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    return x, y

def main():
    # initial point
    p = (1, 1)
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input('Enter the number of iterations: '))
    x, y = build_trajectory(p, n)

    plt.plot(x, y)
    plt.title(f'{n} iterations')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

if __name__ == '__main__':
    main()
