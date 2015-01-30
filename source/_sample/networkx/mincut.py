#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    G.add_edge('s', 'o', capacity=3)
    G.add_edge('s', 'p', capacity=3)
    G.add_edge('o', 'p', capacity=2)
    G.add_edge('o', 'q', capacity=3)
    G.add_edge('q', 'r', capacity=4)
    G.add_edge('q', 't', capacity=2)
    G.add_edge('p', 'r', capacity=2)
    G.add_edge('r', 't', capacity=3)

    # partition here is a tuple with the two sets of nodes that
    # define the minimum cut (S, T).
    cut_value, partition = nx.minimum_cut(G, 's', 't')
    S, T = partition

    print('cut value: {}'.format(cut_value))
    print('(S, T): ({}, {})'.format(S, T))

    # Compute the cut set of edges that induce the minimum cut
    # as follows:
    cutset = set()
    for u, nbrs in ((n, G[n]) for n in S):
        cutset.update((u, v) for v in nbrs if v in T)
    print('cut set: {}'.format(cutset))

if __name__ == '__main__':
    main()
