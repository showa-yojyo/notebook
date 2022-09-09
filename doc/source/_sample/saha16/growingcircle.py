#!/usr/bin/env python
"""growingcircle.py: Python ではじめる数学入門 pp. 163-164

Usage:
  growingcircle.py
"""

from matplotlib import pyplot as plt
from matplotlib import animation

def create_circle():
    return plt.Circle((0, 0), radius=0.05)

def update_radius(i, circle):
    circle.radius = i * 0.5
    return circle

def create_animation():
    # Get the current Figure
    fig = plt.gcf()

    ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
    ax.set_aspect('equal')

    circle = create_circle()
    ax.add_patch(circle)

    # fargs: update_radius() にわたす全引数
    # frames: update_radius() を呼び出す回数
    # interval: ミリ秒単位のフレーム間隔
    anim = animation.FuncAnimation(
        fig, update_radius, fargs=(circle,), frames=30, interval=50)
    plt.title('Simple Circle Animation')
    plt.show()

def main():
    create_animation()

if __name__ == '__main__':
    main()
