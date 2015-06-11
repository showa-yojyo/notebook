#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Demonstrate Ceva's theorem with SymPy."""
from sympy import Point, Line, simplify, symbols

def demonstrate_ceva(O, A, B, C):
    """Demonstrate Ceva's theorem."""

    c, a, b = Line(A, B), Line(B, C), Line(C, A)
    OA, OB, OC = (Line(O, p) for p in (A, B, C))
    P, Q, R = (i.intersection(j)[0] for i, j in zip((OA, OB, OC), (a, b, c)))

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
    O = Point(0, 0)
    A = Point(21, 344)
    B = Point(-143, -22)
    C = Point(59, 300)
else:
    O, A, B, C = [Point(i, j) for i, j in zip(symbols('x0:4'), symbols('y0:4'))]

demonstrate_ceva(O, A, B, C)
