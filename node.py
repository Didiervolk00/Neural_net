import numpy as np

# Author:       Ricardo Mokveld || Didier Volk  || Diederik van Linden
# Studentnr:    0971051         || 0973139      || 0970665

class Node:
    def __init__(self, outgoingEdge, incommingEdge, value):
        self.list_outgoingEdges = []   
        self.list_incommingEdges = [] 
        self.value = value 
    
    #Creates a list of outgoing edges
    def addOutgoingEdge(self, outgoingEdge):
        self.list_outgoingEdges.append(outgoingEdge)
    
    #Creates a list of incomming edges
    def addIncommingEdge(self, incommingEdge):
        self.list_incommingEdges.append(incommingEdge)

    #Function to insert data in the first layer
    def addValue(self, value):
        self.value = value

    #Extract value trough edges so the amplification is applied
    def getValue(self):
        total = 0 
        for i in range(len(self.list_incommingEdges)):
            total += self.list_incommingEdges[i].getValue()
            
        return self.Sigmoid(total)
    
    #Sigmoid is applied in every node
    def Sigmoid(self, x): 
        return 1/(1 + np.exp(-x))   

      