#!/usr/bin/env python
from apgl.graph.DictGraph import DictGraph
from apgl.graph.SparseGraph import SparseGraph
from apgl.graph.GeneralVertexList import GeneralVertexList

graph = DictGraph()
graph.addEdge("a", "b")
graph.addEdge("a", "c")
graph.addEdge("a", "d")

edgeIndices = graph.getAllEdgeIndices()

graph2 = SparseGraph(GeneralVertexList(graph.getNumVertices()))
graph2.addEdges(edgeIndices)
