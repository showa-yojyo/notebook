#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import colorsys

plt.axes().set_aspect('equal', 'datalim')

num_nodes = 17
G = nx.complete_graph(num_nodes)
pos = nx.circular_layout(G)
ncolors = [colorsys.hsv_to_rgb(h / num_nodes, 1.0, 1.0)
           for h in range(num_nodes)]
nx.draw_networkx(G, pos, node_color=ncolors)
