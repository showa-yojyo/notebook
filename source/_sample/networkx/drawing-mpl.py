#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""drawing-mpl.py: Demonstrate nx.draw_networkx.
"""
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text

def main():
    """Display a graph with Matplotlib."""

    G = nx.DiGraph()
    G.add_edge('賢者の石', '金塊', weight=1)
    G.add_edge('賢者の石', 'オリハルコン', weight=1),
    G.add_edge('賢者の石', 'せかいじゅのしずく', weight=1)
    G.reverse(False)

    pos = nx.shell_layout(G)

    # Draw edge labels.
    edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Draw the graph.
    nx.draw(G, pos, nodelist=[], node_color='w')

    # Draw node labels.
    text_items = nx.draw_networkx_labels(G, pos)

    # Change the font for node labels.
    fp = FontProperties(fname=r'C:\WINDOWS\Fonts\meiryo.ttc')
    for t in text_items.values():
        t.set_fontproperties(fp)

    # Display with Matplotlib.
    plt.show()

if __name__ == '__main__':
    main()
