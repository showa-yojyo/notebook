#!/usr/bin/env python
"""drawing_tree.py: draw a tree graph with pydot_layout.
"""
import colorsys

import networkx as nx
import matplotlib.pyplot as plt

# A tree graph is given.
branching = 2
height = 5
G = nx.balanced_tree(branching, height)

#pos = nx.spring_layout(G) # default; bad
#pos = nx.shell_layout(G) # bad
#pos = nx.spectral_layout(G) # poor
pos = nx.nx_pydot.pydot_layout(G, prog='dot') # good

# Node colors.
ncolors = []
height += 1
for i in range(height):
    ncolors.extend(
        [colorsys.hsv_to_rgb(i / height, 1.0, 1.0)] * branching ** i)

nx.draw_networkx(G, pos, node_color=ncolors)

#plt.axes().set_aspect('equal', 'datalim')
plt.axis('off')
plt.show()
