#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from apgl.graph.VertexList import VertexList
from apgl.graph.SparseGraph import SparseGraph
numVertices = 5
numFeatures = 2
graph = SparseGraph(VertexList(numVertices, numFeatures))

# Add some edges to the graph.
# Vertices are indexed starting from 0.
graph[0, 1] = 0.1
graph[1, 2] = 1.0

# Set the label of the 0th vertex to [2, 3].
graph.setVertex(0, np.array([2, 3]))

# Display edge weights.
print(graph[1, 2]) # 1.0
print(graph[1, 3]) # 0.0 (default)

# Add some edges to the graph.
edges = np.array([[0, 1], [1, 2]], np.int)
edgeValues = np.array([0.1, 1.0])
graph.addEdges(edges, edgeValues)

# Display the edge weight between v1 and v2.
print(graph[1, 2])
