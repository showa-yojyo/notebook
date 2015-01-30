# -*- coding: utf-8 -*-
# g.findAllDistances demonstration

from apgl.graph.SparseGraph import SparseGraph
#from apgl.graph.PySparseGraph import PySparseGraph
from apgl.graph.GeneralVertexList import GeneralVertexList

# Make a graph.
numVertices = 6
vlist = GeneralVertexList(numVertices)
graph = SparseGraph(vlist, undirected=True)

# Define edges.

graph[0, 1] = 10.0
graph[0, 2] = 14.0
graph[0, 3] = 12.0
graph[1, 2] = 8.0
graph[1, 4] = 19.0
graph[2, 3] = 7.0
graph[2, 5] = 22.0
graph[3, 5] = 21.0
graph[4, 5] = 11.0

# Compute the shortest paths by means of Dijkstra's algorithm.
dists = graph.findAllDistances(True)

# Obtain the distance of the shortest path.
print(dists)
