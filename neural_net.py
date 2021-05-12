import numpy as np
import node
import edge
import json

# Author:       Ricardo Mokveld || Didier Tolk  || Diederik van Linden
# Studentnr:    0971051         || 0973139      || 0970665
# Class:        Tinlab Machine Learning
# Assignment:   Assignment 2 :: symbol recognizer

# Prioritized requirements:
# - Create a neural net application, that can distuinguish (sloppy handwritten) circles and crosses from each other.
# - Atleast 2 layers of nodes
# - The usage of Machine learning libraries is prohibited

# Main design choices:
    # - We made two modules, edge.py and node.py. We use modules to break down the program into small manageable and organized files.
    # - Using modules provide reusability of the code.

    # Class Edge
    # - The class Edge is designed that the edges are placed in a list and the beginNode and the endNode are linked to the edge.

    # Class Node 
    # - We designed the class node in a way that the neural net is easy scaleable if you want to add multiple layers.
    # - The class Node is designed in a way that every node has an incomming edge and an outgoing edge. 

# Test specification:
# -
# -

Node = node.Node
Edge = edge.Edge

nodeInput = [Node(i, i) for i in range(9)]
nodeOutput = [Node(i, i) for i in range(2)]
edges = [Edge(0, 0, 0)]

edgeId = 0

for nodeIn in nodeInput:
    for nodeOut in nodeOutput:
        edge = Edge(edgeId, nodeIn, nodeOut)
        nodeIn.addOutgoingEdge(edge)
        nodeOut.addIncommingEdge(edge)
        edgeId+=1
        edges.append(edge)

t = open('trainingset.json',)

data = json.load(t)

# for i in data['trainingsSet']:
#     print(data['trainingsSet'][f'{i}']['input'])

test = [data['trainingsSet'][f'{1}']['input']]

print(test)
# print("\n======== Input Nodes ========\n")
# for i in range(len(nodeInput)):
#     print(i, nodeInput[i])
# print("\n======== Output Nodes ========\n")
# for i in range(len(nodeOutput)):
#     print(i, nodeOutput[i])
# for i in range(2):
#     print(i, nodeInput[5].list_outgoingEdges[i])
# print("\n======== Edges ===============\n")
# for i in range(len(edges)):
#     print(i, edges[i])
