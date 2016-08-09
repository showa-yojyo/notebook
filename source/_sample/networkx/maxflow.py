#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""maxflow.py: demonstrate NetworkX (maximum_flow).
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

    flow_value, flows = nx.maximum_flow(G, 's', 't')
    print('maximum flow: {}'.format(flow_value))

    caps = nx.get_edge_attributes(G, 'capacity')
    for u in nx.topological_sort(G):
        for v, flow in sorted(flows[u].items()):
            print('({}, {}): {}/{}'.format(u, v, flow, caps[(u, v)]))

if __name__ == '__main__':
    main()
