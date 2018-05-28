#!/usr/bin/env python
"""torus.py: (Demonstration)

Usage:
  torus.py
"""

from sympy import (symbols, cos, sin, simplify, Matrix, latex, Derivative, sqrt)
from sympy.abc import t, xi, eta
from sympy.printing import print_latex

def main():
    x_1, x_2 = symbols('x_1 x_2', real=True)

    # Phi(x_1, x_2) = a torus.
    Phi = Matrix([(2 + cos(x_2)) * cos(x_1),
                  (2 + cos(x_2)) * sin(x_1),
                  sin(x_2),])
    DPhi = Phi.jacobian([x_1, x_2])
    print_latex(DPhi, fold_func_brackets=True,
        mat_str='pmatrix', mat_delim=None)

    tDPhi = DPhi.transpose()
    print_latex(tDPhi, fold_func_brackets=True,
        mat_str='pmatrix', mat_delim=None)

    tDPhiDPhi = simplify(tDPhi * DPhi) # simplify \sin^2 + \cos^2.
    print_latex(tDPhiDPhi, fold_func_brackets=True,
        mat_str='pmatrix', mat_delim=None)
    dcdt = Matrix([Derivative(xi, t, 1), Derivative(eta, t, 1)])

    print_latex(sqrt((dcdt.transpose() @ tDPhiDPhi).dot(dcdt)),
       fold_func_brackets=True)

if __name__ == '__main__':
    main()
