# Author:       Ricardo Mokveld || Didier Volk  || Diederik van Linden
# Studentnr:    0971051         || 0973139      || 0970665
# Class:        Tinlab Machine Learning
# Assignment:   Assignment 2 :: symbol recognizer

# Prioritized requirements:
# - Create a neural net application, that can distuinguish (sloppy handwritten) circles and crosses from each other.
# - Atleast 2 layers of nodes
# - The usage of Machine learning libraries is prohibited

# Main design choices:
# -
# -

# Test specification:
# -
# -

import numpy as np
import node
import edge

Node = node.Node # deze twee zijn nieuw
Edge = edge.Edge

nodeInput = [Node() for i in range(9)]
nodeOutput = [Node() for i in range(2)]
edges = [Edge(i, i, i) for i in range(18)]

edgeId = 0

for nodeIn in nodeInput:
    for nodeOut in nodeOutput:
        edge = Edge(edgeId, nodeIn, nodeOut)
        nodeIn.addOutgoingEdge(edge)
        nodeOut.addIncommingEdge(edge)
        edgeId+=1
        edges.append(edge)

# print(nodeInput[5])
# print(edges[2])
# print(nodeInput[5].outgoingEdge.id)
# print(nodeInput[6].outgoingEdge.id)
# print(nodeOutput[1].incommingEdge.id)
