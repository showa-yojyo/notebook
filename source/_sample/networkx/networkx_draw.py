#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""neteworkx_draw.py: nx.draw_networkx demonstration"""

import networkx as nx
import matplotlib.pyplot as plt

# Make a graph.
G = nx.Graph()

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

# Position nodes using Fruchterman-Reingold force-directed algorithm.
pos = nx.spring_layout(G, k=5.)

# Draw labels for nodes and edges.
nx.draw_networkx_labels(G, pos)

# Draw only weight attribute as edge label.
edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Finish drawing.
nx.draw(G, pos)

# Display with Matplotlib.
plt.axis('off')
plt.show()
