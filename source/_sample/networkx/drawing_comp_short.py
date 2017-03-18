#!/usr/bin/env python
"""drawing_comp_short.py: Draw a complete graph.
"""
import colorsys

import networkx as nx
import matplotlib.pyplot as plt

plt.axes().set_aspect('equal', 'datalim')

num_nodes = 17
G = nx.complete_graph(num_nodes)
pos = nx.circular_layout(G)
ncolors = [colorsys.hsv_to_rgb(h / num_nodes, 1.0, 1.0)
           for h in range(num_nodes)]
nx.draw_networkx(G, pos, node_color=ncolors)
plt.show()
