#!/usr/bin/env python
"""maximal_matching.py: demonstrate maximal_matching.
"""
import networkx as nx

def main():
    """The main function."""

    for edge_list in generate_edges():
        print(nx.maximal_matching(nx.Graph(edge_list)))

def generate_edges():
    """Generate edge lists to demonstrate maximal matching.

    Yields:
      Tuple of integer pairs.
    """

    # Fig. (a)
    yield (
        (0, 1), (0, 2),
        (1, 2),
        (3, 1),
        (4, 1),
        (5, 1))

    # Fig. (b)
    yield (
        (0, 1), (0, 2),
        (1, 2),
        (3, 1), (3, 4), (3, 5),
        (4, 2))

    # Fig. (c)
    yield (
        (0, 1), (0, 2),
        (1, 2),
        (3, 1), (3, 4),
        (4, 2))

if __name__ == '__main__':
    main()
