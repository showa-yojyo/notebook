#!/usr/bin/env python
"""geodesic.py: Compute geodesic equations for :math:`z = h(x1, x2).`
"""

from sympy import (symbols, Eq, Function, Matrix,
                   simplify, latex, hessian)
from sympy.printing import print_latex

def geodesic(h, x1, x2):
    """Compute geodesic equations for z = h(x1, x2)."""

    coords = [x1, x2]
    Dh = Matrix([h]).jacobian(coords)
    Hh = hessian(h, coords)
    assert Hh.is_symmetric()
    v = [x.diff() for x in coords]

    numer2 = Hh[0, 0] * v[0]**2 + 2 * Hh[0, 1] * v[0] * v[1] + Hh[1, 1] * v[1]**2
    denom = 1 + Dh[0, 0]**2 + Dh[0, 1]**2

    print(r'$$\begin{align*}')
    for i, x in enumerate(coords):
        numer1 = -Dh[0, i]
        geq = Eq(x.diff(), simplify(numer1 * numer2 / denom))
        print_sympyobj(geq)
        print(r'\\')
    print(r'\end{align*}$$')

def main():
    t = symbols('t', real=True)
    x1 = Function('x1')(t)
    x2 = Function('x2')(t)

    geodesic(x1 * x2, x1, x2) # hyperbolic paraboloid
    geodesic(-x1**2 - x2**2, x1, x2) # ellipric paraboloid

if __name__ == '__main__':
    main()
