# Author:       Ricardo Mokveld || Didier Volk  || Diederik van Linden
# Studentnr:    0971051         || 0973139      || 0970665

class Edge:
    def __init__(self, id, beginNode, endNode):
        self.id = id
        self.amplification = 1
        self.beginNode = beginNode
        self.endNode = endNode

    def getValue(self):
        return self.beginNode.value * self.amplification

    def setAmplification(self, amplification):
        self.amplification = amplification

    def changeAmplification(self, change):
        self.amplification += change