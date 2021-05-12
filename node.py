import numpy as np
import edge

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
        self.matrixInput = matrixInput




    def getValue(self):
        for i in range(len(self.list_incommingEdges)):
            self.value += self.list_incommingEdges[i].getValue()
            
        return self.value
            
    def sigmoid(self): 
        x = self.getValue()
        return 1/(1 + np.exp(-x))   
   
            