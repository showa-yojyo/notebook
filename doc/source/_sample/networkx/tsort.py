#!/usr/bin/env python
"""tsort.py: demonstrate NetworkX (topological_sort)
"""
import networkx as nx

def main():
    """The main function.

    Returns:
      None
    """

    G = setup_graph()
    print_sort(G)

def setup_graph():
    """Create a DAG to demonstrate topological_sort.

    Returns:
      (DiGraph): A DAG.
    """
    G = nx.DiGraph()

    # http://en.wikipedia.org/wiki/File:Directed_acyclic_graph.png
    G.add_edges_from((
        (7, 11),
        (5, 11),
        (11, 2),
        (11, 9),
        (3, 8),
        (8, 9),
        (3, 10),
        (7, 8),
        (11, 10)))

    #assert nx.is_directed_acyclic_graph(G)
    return G

def print_sort(G):
    """Execute topological_sort and print the result.

    Args:
      G (Graph): A DAG.

    Returns:
      None
    """
    print(list(nx.topological_sort(G)))

if __name__ == '__main__':
    main()
