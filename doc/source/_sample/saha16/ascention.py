#!/usr/bin/env python
"""ascention.py: Python からはじめる数学入門 pp. 209-210, 213-214.

Usage:
  ascention.py
"""
from sympy import sympify, Symbol, diff, solve

class GradientAscentError(Exception): pass

def grad_ascent(x0, f1x, x):
    """Gradient ascent to find the maximum value of a single
    variable function
    """

    if not solve(f1x):
        raise GradientAscentError(
            f'Cannot continue, solution for {f1x} = 0 does not exist')

    eps = 1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old + step_size * f1x.subs({x: x_old}).evalf()
    while abs(x_old - x_new) > eps:
        x_old = x_new
        x_new = x_old + step_size * f1x.subs({x: x_old}).evalf()

    return x_new

def main():
    f = input('Enter a function in one variable: ')
    v = input('Enter the variable: ')
    init = float(input('Enter the initial value of the variable: '))
    f = sympify(f)

    v = Symbol(v)
    d = diff(f, v)
    try:
        vmax = grad_ascent(init, d, v)
        print(f'{v.name}: {vmax}')
        print(f'Maximum value: {f.subs({v: vmax})}')
    except GradientAscentError as exc:
        print(exc)

if __name__ == '__main__':
    main()
