#!/usr/bin/env python
"""mincut.py: demonstrate NetworkX (minimum_cut).
"""
import networkx as nx

def main():
    """The main function.

    Returns:
        None.
    """

    # This graph is borrowed from:
    # http://en.wikipedia.org/wiki/Maximum_flow_problem
    G = nx.DiGraph()
    G.add_edges_from((('s', 'o', dict(capacity=3)),
                      ('s', 'p', dict(capacity=3)),
                      ('o', 'p', dict(capacity=2)),
                      ('o', 'q', dict(capacity=3)),
                      ('q', 'r', dict(capacity=4)),
                      ('q', 't', dict(capacity=2)),
                      ('p', 'r', dict(capacity=2)),
                      ('r', 't', dict(capacity=3)),))

    # partition here is a tuple with the two sets of nodes that
    # define the minimum cut (S, T).
    cut_value, partition = nx.minimum_cut(G, 's', 't')
    S, T = partition

    print(f'cut value: {cut_value}')
    print(f'(S, T): ({S}, {T})')

    # Compute the cut set of edges that induce the minimum cut
    # as follows:
    cutset = set()
    for u, nbrs in ((n, G[n]) for n in S):
        cutset.update((u, v) for v in nbrs if v in T)
    print(f'cut set: {cutset}')

if __name__ == '__main__':
    main()
