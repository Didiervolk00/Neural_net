import numpy as np

# Author:       Ricardo Mokveld || Didier Volk  || Diederik van Linden
# Studentnr:    0971051         || 0973139      || 0970665

class Node:
    def __init__(self, outgoingEdge, incommingEdge, matrixInput, value):
        self.list_outgoingEdges = []   
        self.list_incommingEdges = [] 
        self.value = value 
            
    def addOutgoingEdge(self, outgoingEdge):
        self.list_outgoingEdges.append(outgoingEdge)
        
    def addIncommingEdge(self, incommingEdge):
        self.list_incommingEdges.append(incommingEdge)

    def addMatrixInput(self, matrixInput):
        self.value = matrixInput

    def getValue(self):
        total = 0 
        for i in range(len(self.list_incommingEdges)):
            total += self.list_incommingEdges[i].getValue()
            
        return self.Sigmoid(total)
            
    def Sigmoid(self, x): 
        return 1/(1 + np.exp(-x))   

      