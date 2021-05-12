import node

# Author:       Ricardo Mokveld || Didier Volk  || Diederik van Linden
# Studentnr:    0971051         || 0973139      || 0970665

class Edge:
    def __init__(self, id, beginNode, endNode, cargo):
        self.id = id
        self.amplification = 1
        self.beginNode = beginNode
        self.endNode = endNode
        self.cargo = cargo

    def getValue(self):
        return self.beginNode.matrixInput * self.amplification

    def setAmplification(self, amplification):
        self.amplification = amplification
