#!/usr/bin/env python
import scipy.sparse as sps
from apgl.graph.GeneralVertexList import GeneralVertexList
from apgl.graph.SparseGraph import SparseGraph

numVertices = 10
vList = GeneralVertexList(numVertices)

Wght = sps.lil_matrix((numVertices, numVertices))
graph = SparseGraph(vList, W=Wght, undirected=False)

# Add some edges to the graph.
# Vertices are indexed starting from 0.
graph[0, 1] = 1
graph[0, 2] = 1

# Set the label of the 0th vertex to [2, 3].
graph.setVertex(0, "abc")
graph.setVertex(1, 123)

print(graph.inDegreeDistribution())
