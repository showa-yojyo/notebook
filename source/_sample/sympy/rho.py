#!/usr/bin/env python
"""rho.py: Study the following :math:`C^\infty` function:

.. math::

   \rho(x) =
   \begin{cases}
   0 & \quad\text{if } x \le 0,\\
   \exp\left(-\dfrac{1}{x}\right) & \quad\text{if } 0 < x.
   \end{cases}
"""

from sympy import (symbols, Function, simplify,
                   latex, exp, Limit, diff, Derivative, Eq)
from sympy.printing import print_latex

def main():
    x = symbols('x', real=True)
    rho = Function('\\rho')(x)
    expr = exp(-1/x)

    # \rho^{(i)} and their limits for some orders
    print('$$')
    print(r'\begin{align*}')
    for i in range(4):
        if i == 0:
            df = diff(expr, x)
        else:
            df = diff(df, x)
        df = simplify(df)

        lhs = Derivative(rho, x, i + 1)
        print_latex(Eq(lhs, df))
        print(',& \quad ')

        print_latex(Eq(
            Limit(lhs, x, 0, '+'),
            Limit(df, x, 0, '+').doit()))
        print(r'\\')

    print(r'\end{align*}')
    print('$$')

if __name__ == '__main__':
    main()
