#!/usr/bin/env python
"""circle_power.py: Demonstrate power-of-a-point theorem with SymPy.
"""
from sympy import (Point, Line, Circle)

def demonstrate_circle_power(circle):
    """Demonstrate power-of-a-point theorem."""

    A, B, C, D = (circle.random_point() for i in range(4))
    P = Line.intersection(Line(A, B), Line(C, D))
    assert len(P) == 1
    P = P[0]

    PAPB = P.distance(A) * P.distance(B)
    PCPD = P.distance(C) * P.distance(D)

    print("PA * PB =", PAPB.evalf())
    print("PC * PD =", PCPD.evalf())

if __name__ == '__main__':
    center = Point(0, 0)
    radius = 1
    demonstrate_circle_power(Circle(center, radius))
