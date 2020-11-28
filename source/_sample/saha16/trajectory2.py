#!/usr/bin/env python
"""trajectory2.py: Python からはじめる数学入門 pp. 166-167

Usage:
  trajectory2.py
"""
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import sys

G = 9.8

def get_intervals(u, theta):
    # Time of flight
    t_flight = 2 * u * np.sin(theta) / G

    # Find the intervals
    return np.linspace(0, t_flight, int(t_flight / 0.05))

def create_animation(u, theta):
    intervals = get_intervals(u, theta)

    xmin = 0
    xmax = u * np.cos(theta) * intervals[-1]

    ymin = 0
    t_max = u * np.sin(theta) / G
    ymax = u * np.sin(theta) * t_max - 0.5 * G * t_max**2

    fig = plt.gcf()
    ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
    ax.set_aspect('equal')
    circle = plt.Circle((xmin, xmax), 1.0)
    ax.add_patch(circle)

    amin = animation.FuncAnimation(
        fig, update_position,
        fargs=(circle, intervals, u, theta),
        frames=len(intervals),
        interval=1,
        repeat=False)

    plt.title('Projectile Motion')
    plt.xlabel('horizontal [m]')
    plt.ylabel('vertical [m]')

    plt.show()

def update_position(i, circle, intervals, u, theta):
    t = intervals[i]
    x = u * np.cos(theta) * t
    y = u * np.sin(theta) * t - 0.5 * G * t**2
    circle.center = x, y
    return circle

def main():
    try:
        u = float(input('Enter the initial velocity [m/s]: '))
        theta = float(input('Enter the angle of projection [degrees]: '))
        create_animation(u, np.radians(theta))
    except ValueError as exc:
        print('You entered an invalid input', exc)

if __name__ == '__main__':
    main()
