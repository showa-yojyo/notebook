#!/usr/bin/env python
"""mandelbrot.py: Python からはじめる数学入門 p. 186 改造

Usage:
  mandelbrot.py [max_iterations]
"""
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def initialize_image(x_p, y_p):
    return [[0] * x_p for i in range(y_p)]

def main():
    N = 400
    x_p = y_p = N
    image = initialize_image(x_p, y_p)

    max_iteration = 1000

    # これは遅いだろうな
    for j, imag in enumerate(np.linspace(-1.0, 1.0, N)):
        for i, real in enumerate(np.linspace(-2.5, 1.0, N)):
            # 1.
            z1 = complex(0, 0)
            c = complex(real, imag)
            # 2.
            iteration = 0
            while iteration < max_iteration:
                # 3.
                z1 = z1 ** 2 + c
                #print(z1)
                # 4.
                iteration += 1
                # 5.
                if z1.real**2 + z1.imag**2 < 4:
                    continue
                # 6.
                image[j][i] = iteration
                break

    plt.imshow(image, origin='lower', extent=(-2.5, 1.0, -1.0, 1.0),
               cmap=cm.Greys_r, interpolation='nearest')
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()
