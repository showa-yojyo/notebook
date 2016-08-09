#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""dijkstra.py: all_pairs_dijkstra_path demonstration
"""

import networkx as nx
from networkx.algorithms.shortest_paths.weighted import all_pairs_dijkstra_path_length

# Make a graph.
G = nx.DiGraph()

# Define edges with weights.
G.add_weighted_edges_from(
    ((0, 1, 10.0),
     (0, 2, 14.0),
     (0, 3, 12.0),
     (1, 2, 8.0),
     (1, 4, 19.0),
     (2, 3, 7.0),
     (2, 5, 22.0),
     (3, 5, 21.0),
     (4, 5, 11.0),))

# Compute the shortest path lengths between all nodes in graph G.
all_pairs = all_pairs_dijkstra_path_length(G)
for source, mapping in all_pairs.items():
    for target in mapping.keys():
        if source != target:
            dist = mapping[target]
            print("({}, {}): {:4.1f}".format(source, target, dist))
