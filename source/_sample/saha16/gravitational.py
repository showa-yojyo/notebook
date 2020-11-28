#!/usr/bin/env python
"""
Python からはじめる数学入門 (pp. 49-50) 改造版
"""
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
FONT_PROP = FontProperties(fname=r'C:\WINDOWS\Fonts\HGRME.TTC')

def draw_graph(xdata, ydata):
    plt.plot(xdata, ydata, marker='o')
    plt.xlabel('距離 [m]', fontproperties=FONT_PROP)
    plt.ylabel('引力 [N]', fontproperties=FONT_PROP)
    plt.title('引力と距離', fontproperties=FONT_PROP)
    plt.show()

def generate_F_r():
    G = 6.674 * 10**-11
    m1 = 0.5
    m2 = 1.5
    r = range(100, 1000 + 1, 50)

    # Calculate force
    F = [G * (m1 * m2) / (dist ** 2) for dist in r]
    draw_graph(r, F)

if __name__ == '__main__':
    generate_F_r()
