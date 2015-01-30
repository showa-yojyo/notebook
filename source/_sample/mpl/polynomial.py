# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(111)

f = np.poly1d([1, -4, 3, 0]) # x = 0, 1, 3 を根に持つ 3 次多項式。
xs = np.arange(-2, 4, 0.1) # x in [-2, 4] を 0.1 刻みでプロット。
ys = [f(x) for x in xs] # xs と対になる ys
ax1.plot(xs, ys)

# x = [-1, 3] から 1 間隔に接線を引く。
slope = f.deriv()
for a in range(-1, 3, 1):
    b = f(a)
    ys1 = [slope(a) * (x - a) + b for x in xs]
    ax1.plot(xs, ys1)

plt.show()
