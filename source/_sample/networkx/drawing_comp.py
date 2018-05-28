#!/usr/bin/env python
"""drawing_comp.py: demonstrate NetworkX (circular_layout).
"""
import colorsys

import networkx as nx
import matplotlib.pyplot as plt
from numpy import (array, cos, sin, float32, pi)

num_nodes = 17
G = nx.complete_graph(num_nodes)

if False:
    pos = nx.circular_layout(G)
else:
    pos = {}
    for i in range(num_nodes):
        theta = 2 * pi * i / num_nodes
        pos[i] = array([cos(theta), sin(theta)], dtype=float32)

# Node colors.
ncolors = [colorsys.hsv_to_rgb(h / num_nodes, 1.0, 1.0)
           for h in range(num_nodes)]

nx.draw_networkx(G, pos, node_color=ncolors)
plt.axes().set_aspect('equal', 'datalim')
plt.show()
