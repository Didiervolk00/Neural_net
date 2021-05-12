import numpy as np
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

class Node:
    def __init__(self, outgoingEdge, incommingEdge):
        self.list_outgoingEdges = []   
        self.list_incommingEdges = []  
            
    def addOutgoingEdge(self, outgoingEdge):
        self.list_outgoingEdges.append(outgoingEdge)
        
    def addIncommingEdge(self, incommingEdge):
        self.list_incommingEdges.append(incommingEdge)

    def sigmoid(x): 
        return 1/(1 + np.exp(-x))      