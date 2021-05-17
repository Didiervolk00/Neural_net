import numpy as np
import edge
import json

from node import Node
from edge import Edge

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


nodeInput = [Node(i, i, i, 1) for i in range(9)]
nodeOutput = [Node(i, i, i, 1) for i in range(2)]
edges = []

edgeId = 0
prevAmp = 0
bestAmp = 0
desiredError = 0.001
avgError = np.Infinity

testSet = open('trainingset.json',)
data = json.load(testSet)

trainingsSet = data['trainingsSet']
testSet = data['testSet']
figures = data['figures']

for nodeIn in nodeInput:
    for nodeOut in nodeOutput:
        edge = Edge(edgeId, nodeIn, nodeOut)
        nodeIn.addOutgoingEdge(edge)
        nodeOut.addIncommingEdge(edge)
        edgeId+=1
        edges.append(edge)

#Calculate the total mean error for the trainingsset
def calculateMean():
    totalMean = 0
    for i in range(len(trainingsSet)):

        currentFigure = trainingsSet[f'{i}']['input']
        expectedResult = figures[f"{trainingsSet[f'{i}']['figure']}"]

        for j in range(len(nodeInput)):
            nodeInput[j].addMatrixInput(currentFigure[j])

        a = nodeOutput[0].getValue()
        b = nodeOutput[1].getValue()
        vector = [a, b]

        normalized_v = vector / np.linalg.norm(vector)
        mean = np.mean((normalized_v - expectedResult) ** 2)
        
        totalMean += mean
    
    return totalMean / len(trainingsSet)

#Learn the program what a cross and circle is.
while avgError > desiredError:
    currentBestError = np.Infinity
    for edge in edges:
        for value in [-0.1, 0.1]:
            edge.changeAmplification(value)
            newError = calculateMean()
            edge.changeAmplification(-value)

            if newError < currentBestError:
                currentBestError = newError
                bestEdge = edge
                bestAmp = value

    bestEdge.changeAmplification(bestAmp)
    avgError = currentBestError
    print(avgError)

# Run the test set trough the nodes and edges with various amplifications
for i in range(len(testSet)):
    currentFigure = testSet[f'{i}']['input']
    expectedResult = figures[f"{testSet[f'{i}']['figure']}"]


    for j in range(len(nodeInput)):
        nodeInput[j].addMatrixInput(currentFigure[j])

    a = nodeOutput[0].getValue()
    b = nodeOutput[1].getValue()
    vector = [a, b]
    normalized_v = vector / np.linalg.norm(vector)

    print(f'{i}: Expected result: {expectedResult}. Actual result: {normalized_v}')





