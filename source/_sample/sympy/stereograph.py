#!/usr/bin/env python
"""stereograph.py: Compute length of a geodesic in the unit sphere.
"""

from sympy import (symbols, Function, Matrix, factor, simplify, latex, sqrt)
from sympy.abc import (t, xi, eta)
from sympy.printing import print_latex

def main():
    u, v, R = symbols('u v R', real=True)
    xi, eta = symbols(r'\xi \eta', cls=Function)

    numer = 4*R**2
    denom = u**2 + v**2 + numer

    # inverse of a stereographic projection from the south pole
    # onto the XY plane:
    pinv = Matrix([numer * u / denom,
                   numer * v / denom,
                   -(2 * R * (u**2 + v**2)) / denom]) # OK
    if False:
        # textbook style
        Dpinv = simplify(pinv.jacobian([u, v]))
        print_latex(Dpinv, mat_str='pmatrix', mat_delim=None) # OK?

        tDpinvDpinv = factor(Dpinv.transpose() @ Dpinv)
        print_latex(tDpinvDpinv, mat_str='pmatrix', mat_delim=None) # OK

        tDpinvDpinv = tDpinvDpinv.subs([(u, xi(t)), (v, eta(t))])
        dcdt = Matrix([xi(t).diff(), eta(t).diff()])
        print_latex(simplify(
            sqrt((dcdt.transpose() @ tDpinvDpinv).dot(dcdt))))
    else:
        # directly 
        dpinvc = pinv.subs([(u, xi(t)), (v, eta(t))]).diff(t, 1)
        print_latex(sqrt(factor(dpinvc.dot(dpinvc))))

if __name__ == '__main__':
    main()
