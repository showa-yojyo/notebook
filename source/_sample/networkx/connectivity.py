#!/usr/bin/env python
"""connectivity.py: demonstrate NetworkX edge_connectivity, etc.
"""
import networkx as nx

def main():
    """The main function.

    Returns:
        None.
    """

    for i, G in enumerate(generate_graphs()):
        print(f"G{i} is "
              f"{nx.node_connectivity(G)}-connected and "
              f"{nx.edge_connectivity(G)}-edge connected.")

def generate_graphs():
    """Generate graphs to demonstrate connectivities.

    Graphs are borrowed from:
    http://www.personal.kent.edu/~rmuhamma/GraphTheory/MyGraphTheory/connectivity.htm

    Yields:
      Graph instances.
    """

    # G0
    yield nx.MultiGraph((
        (0, 2), (2, 0),
        (1, 2),
        (3, 1)))
    # G1
    yield nx.Graph((
        (0, 1), (1, 2), (2, 0),
        (2, 3),
        (3, 4), (4, 6), (6, 3)))
    # G2
    yield nx.Graph((
        (0, 1), (1, 2), (2, 0),
        (2, 3), (3, 4), (4, 2)))
    # G3
    G = nx.cycle_graph(4)
    G.add_edge(3, 3)
    yield G

if __name__ == '__main__':
    main()
