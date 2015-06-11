#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Demonstrate Menelaus' theorem with SymPy."""
from sympy import Point, Line, simplify, symbols

def demonstrate_menelaus(l, A, B, C):
    """Demonstrate Menelaus' theorem."""

    c, a, b = Line(A, B), Line(B, C), Line(C, A)
    P, Q, R = (l.intersection(i)[0] for i in (a, b, c))

    print("P=", P.evalf())
    print("Q=", Q.evalf())
    print("R=", R.evalf())

    numer = A.distance(R) * B.distance(P) * C.distance(Q)
    denom = R.distance(B) * P.distance(C) * Q.distance(A)

    print("numer=", numer.evalf())
    print("denom=", denom.evalf())

    # Or show simplify(numer/denom).
    print((numer/denom).evalf())

if True:
    l = Line(Point(0, 0), Point(1, 1))
    A = Point(21, 344)
    B = Point(-143, -22)
    C = Point(59, 300)
else:
    l = Line(*[Point(i, j) for i, j in zip(symbols('X1:3'), symbols('Y1:3'))])
    A, B, C = [Point(i, j) for i, j in zip(symbols('x1:4'), symbols('y1:4'))]

demonstrate_menelaus(l, A, B, C)
