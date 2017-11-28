#!/usr/bin/env python
"""s1.py: Construct :math:`S^1` as a smooth manifold.
"""

from itertools import product
from sympy import (symbols, sqrt)
from sympy.diffgeom import (Manifold, Patch, CoordSystem)

def main():
    # A unit circle in \RR^2:
    S1 = Manifold('S**1', 1)

    # Coordinate charts :math:`(U_i^\pm, \phi_i^\pm)` for S1:
    # 0, 1 -> x0, x1
    # p, m -> +, -
    phip0 = CoordSystem('phip0', Patch('Up0', S1), ['x1'])
    phim0 = CoordSystem('phim0', Patch('Um0', S1), ['x1'])
    phip1 = CoordSystem('phip1', Patch('Up1', S1), ['x0'])
    phim1 = CoordSystem('phim1', Patch('Um1', S1), ['x0'])

    intersections = (
        (phip0, phip1), (phip0, phim1),
        (phim0, phip1), (phim0, phim1),)

    # Transition maps:
    x0, x1 = symbols('x:2', real=True)
    phip0.connect_to(phip1, [x1], [sqrt(1 - x1**2)], inverse=False)
    phip0.connect_to(phim1, [x1], [sqrt(1 - x1**2)], inverse=False)
    phim0.connect_to(phip1, [x1], [-sqrt(1 - x1**2)], inverse=False)
    phim0.connect_to(phim1, [x1], [-sqrt(1 - x1**2)], inverse=False)
    phip1.connect_to(phip0, [x0], [sqrt(1 - x0**2)], inverse=False)
    phip1.connect_to(phim0, [x0], [sqrt(1 - x0**2)], inverse=False)
    phim1.connect_to(phip0, [x0], [-sqrt(1 - x0**2)], inverse=False)
    phim1.connect_to(phim0, [x0], [-sqrt(1 - x0**2)], inverse=False)

    # Jacobian matrices:
    for map0, map1 in intersections:
        print('Jacobian {} -> {}: {}'.format(
            map0.name, map1.name, map0.jacobian(map1, ['x1'])))
        print('Jacobian {} -> {}: {}'.format(
            map1.name, map0.name, map1.jacobian(map0, ['x0'])))

    # Transition maps:
    data = (
        (phip0, 1/2, phip1),
        (phip0, -1/2, phim1),
        (phim0, 1/2, phip1),
        (phim0, -1/2, phim1),
        (phip1, 1/2, phip0),
        (phip1, -1/2, phim0),
        (phim1, 1/2, phip0),
        (phim1, -1/2, phim0),)
    for cfrom, t, cto in data:
        print('{}({:7.4f}) = {}({:7.4f})'.format(
            cfrom.name, t, 
            cto.name, cto.point_to_coords(cfrom.point([t]))[0]))

if __name__ == '__main__':
    main()
