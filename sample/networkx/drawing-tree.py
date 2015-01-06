#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""drawing-tree.py: draw a tree graph with pydot_layout.
"""
import networkx as nx
import matplotlib.pyplot as plt
import pydot
import colorsys
from math import log, floor

# A tree graph is given.
height = 5
G = nx.balanced_tree(2, height)

#pos = nx.spring_layout(G) # default; bad
#pos = nx.shell_layout(G) # bad
#pos = nx.spectral_layout(G) # poor
pos = nx.pydot_layout(G, prog='dot') # good

# Node colors.
num_nodes = len(G)
ncolors = [colorsys.hsv_to_rgb(
              floor(log(h + 1, 2)) / (height + 1), 1.0, 1.0)
              for h in range(num_nodes)]

nx.draw_networkx(G, pos, node_color=ncolors)

#plt.axes().set_aspect('equal', 'datalim')
plt.axis('off')
plt.show()
