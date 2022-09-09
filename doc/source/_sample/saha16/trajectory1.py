#!/usr/bin/env python
"""trajectory1.py: Python からはじめる数学入門 pp. 53-56 改造版

Usage:
  trajectory1.py
"""
from matplotlib import pyplot as plt
import numpy as np
import sys

def draw_trajectory(u, theta):
    """Draw the trajectory of a projectile motion"""
    theta = np.radians(theta)
    g = 9.8

    # Time of flight
    t_flight = 2 * u * np.sin(theta) / g

    # Find the intervals
    intervals = np.linspace(0, t_flight, int(t_flight / 0.001))

    x_data = u * np.cos(theta) * intervals
    y_data = [u * np.sin(theta) * t - 0.5 * g * t**2 for t in intervals]
    plt.plot(x_data, y_data)

def main():

    plt.xlabel('horizontal [m]')
    plt.ylabel('vertical [m]')

    if len(sys.argv) > 1 and sys.argv[1] == '-i':
        try:
            u = float(input('Enter the initial velocity [m/s]: '))
            theta = float(input('Enter the angle of projection [degrees]: '))
            draw_trajectory(u, theta)
            plt.title('Projectile motion of a ball')
            plt.show()

        except ValueError as exc:
            print('You entered an invalid input', exc)

        return

    u_list = [20, 40, 60]
    theta = 45
    for u in u_list:
        draw_trajectory(u, theta)

    # Add a legend and show the graph
    plt.legend([str(i) for i in u_list])
    plt.title('Projectile motion at different initial verlocities')
    plt.show()

if __name__ == '__main__':
    main()
