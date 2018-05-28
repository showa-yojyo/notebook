#!/usr/bin/env python
"""hessian.py: Compute Hessian of function
:math:`(2 + \cos y)(a\cos x + b\sin x) + c\sin y.`

Usage:
  hessian.py
"""
from sympy import (symbols, hessian, cos, sin, latex)
from sympy.abc import (a, b, c)

def main():
    x, y = symbols('x y', real=True)
    f = (2 + cos(y)) * (a * cos(x) + b * sin(x)) + c * sin(y)
    H = hessian(f, (x, y))
    print(latex(H, fold_func_brackets=True,
                mat_str='pmatrix', mat_delim=''))

if __name__ == '__main__':
    main()
