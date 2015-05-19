#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apgl.graph.GeneralVertexList import GeneralVertexList
from apgl.graph.SparseGraph import SparseGraph

numVertices = 10
graph = SparseGraph(GeneralVertexList(numVertices))

graph[0, 1] = 1
graph[0, 2] = 1

P = graph.floydWarshall()
print(graph.geodesicDistance(P=P))
print(graph.harmonicGeodesicDistance(P=P))
