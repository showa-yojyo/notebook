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
    G.add_edge('s', 'o', capacity=3)
    G.add_edge('s', 'p', capacity=3)
    G.add_edge('o', 'p', capacity=2)
    G.add_edge('o', 'q', capacity=3)
    G.add_edge('q', 'r', capacity=4)
    G.add_edge('q', 't', capacity=2)
    G.add_edge('p', 'r', capacity=2)
    G.add_edge('r', 't', capacity=3)

    flow_value, flows = nx.maximum_flow(G, 's', 't')
    print('maximum flow: {}'.format(flow_value))

    caps = nx.get_edge_attributes(G, 'capacity')
    for u in nx.topological_sort(G):
        for v, flow in sorted(flows[u].items()):
            print('({}, {}): {}/{}'.format(u, v, flow, caps[(u, v)]))

if __name__ == '__main__':
    main()
