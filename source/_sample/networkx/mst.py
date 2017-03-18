#!/usr/bin/env python
"""mst.py: demonstrate NetworkX (minimum_spanning_tree)

This code solves the problem #2, presented by:
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A&lang=jp
"""
import networkx as nx

# CSV of source-node destination-node weight.
GRAPH_TEXT = """\
0 1 1
0 2 3
1 2 1
1 3 7
2 4 1
1 4 3
3 4 1
3 5 1
4 5 6
"""

def main():
    """The main function.

    Returns:
      None
    """

    G = setup_graph()
    print_spanning(G)

def setup_graph():
    """Create a graph to demonstrate MST.

    Returns:
      (Graph): A simple undirected graph.
    """
    G = nx.Graph()

    for i in GRAPH_TEXT.splitlines():
        source, destination, cost = (int(j) for j in i.split())
        G.add_edge(source, destination, weight=cost)

    return G

def print_spanning(G):
    """Compute MST and print the result.

    Args:
      G (Graph): A simple undirected graph.

    Returns:
      None
    """

    print('size of G: {}'.format(G.size(weight='weight')))
    T = nx.minimum_spanning_tree(G)

    print('size of MST: {}'.format(T.size(weight='weight')))
    print('spanning edges:')
    for i in sorted(T.edges(data=True)):
        print(i)

if __name__ == '__main__':
    main()
