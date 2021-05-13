import numpy as np
import node
import edge
import json
import random

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
    # - Check if the nodes are connected correctly with the right edge in between
    # - Is it possible to insert the data from the trainingset into the node
    # - Check if sigmoid function is applied on the last nodes
    # - Check if the values are the same or different (because of amplification) on the edges as on the begin nodes


Node = node.Node
Edge = edge.Edge

nodeInput = [Node(i, i, i, 0) for i in range(9)]
nodeOutput = [Node(i, i, i, 0) for i in range(2)]
edges = []

edgeId = 0
cargo = 0

for nodeIn in nodeInput:
    for nodeOut in nodeOutput:
        edge = Edge(edgeId, nodeIn, nodeOut, cargo)
        nodeIn.addOutgoingEdge(edge)
        nodeOut.addIncommingEdge(edge)
        edgeId+=1
        edges.append(edge)

testSet = open('trainingset.json',)

data = json.load(testSet)

matrix = data['trainingsSet'][f'{0}']['input']

# for i in range(len(edges)):
#   edges[i].setAmplification()

#??? ik weet niet of dit een goede oplossing is voor de amplification is, misschien beter om er gestructureerd door heen te loopen.
# krijg de nieuwe amplifications niet in de edges, mean verandert niet....
# for i in range(18):
#     edges[i].setAmplification(i)
#     print(edges[i].amplification)

for i in range(len(nodeInput)):
    nodeInput[i].addMatrixInput(matrix[i])
    print(nodeInput[i].matrixInput)

print('=========================')

# for i in range(len(edges)):
#     print(edges[i].getValue())

# for i in range(len(nodeOutput)):
#     print(nodeOutput[i].Sigmoid())

def calcMean():
    a = nodeOutput[0].Sigmoid()
    b = nodeOutput[1].Sigmoid()
    vector = [a,b]

    normalized_v = vector / np.linalg.norm(vector)
    # print(normalized_v)

    circle = data['figures']['O']
    cross = data['figures']['X']

    p = np.mean((normalized_v - circle)**2)
    
    return p

print(calcMean())