#!/usr/bin/env python
"""cutset.py: demonstrate NetworkX minimum_(edge|node)_cut.
"""
import networkx as nx

def main():
    """The main function.

    Returns:
        None.
    """

    # Set up a graph.
    # This graph is borrowed from the following article:
    # http://www.personal.kent.edu/~rmuhamma/GraphTheory/MyGraphTheory/connectivity.htm
    G = nx.Graph()
    G.add_path((0, 1, 3, 5, 7))
    G.add_path((0, 2, 4, 6, 5))
    G.add_edge(1, 4)
    G.add_edge(3, 4)
    print("G:", G.edges())

    st_pairs = ((0, 7), (0, 6), (1, 7),)
    for f in (nx.minimum_edge_cut, nx.minimum_node_cut):
        print("{func}: ".format(func=f.__name__))
        for s, t in st_pairs:
            print("(s, t) = ({s}, {t}): cutset = {cutset}".format(
                s=s, t=t, cutset=f(G, s=s, t=t)))

if __name__ == '__main__':
    main()
