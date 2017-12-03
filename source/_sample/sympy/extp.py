#!/usr/bin/env python
""" extp.py: Print p-forms and exterior products.
"""

from sympy import (symbols, Symbol)
from sympy.printing import (latex, print_latex)
from sympy.printing.latex import LatexPrinter
from sympy.diffgeom import Differential
from sympy.diffgeom.rn import R3_r

def _print_BaseScalarField(self, field):
    string = field._coord_sys._names[field._index]
    return '{}'.format(self._print(Symbol(string)))

def _print_Differential(self, diff):
    field = diff._form_field
    if hasattr(field, '_coord_sys'):
        string = field._coord_sys._names[field._index]
        return r'\dd {}'.format(self._print(Symbol(string)))
    else:
        return r'\dd({})'.format(self._print(field))

for m in (_print_BaseScalarField, _print_Differential):
    setattr(LatexPrinter, m.__name__, m)

def main():
    a, b, c = symbols('a b c', real=True)
    x, y, z = R3_r.coord_functions()
    dx, dy, dz = R3_r.base_oneforms()
    ex, ey, ez = R3_r.base_vectors()

    fx = a* x * y * z
    fy = b * x ** 2 * z
    fz = -3 * x**2 * y
    omega = fx * dx + fy * dy + fz * dz
    print_latex(omega)

    domega = Differential(omega)
    print_latex(domega)

    print_latex(domega(ey, ez)) # for WedgeProduct(dy, dz)
    print_latex(domega(ez, ex)) # for WedgeProduct(dz, dx)
    print_latex(domega(ex, ey)) # for WedgeProduct(dx, dy)

if __name__ == '__main__':
    main()
