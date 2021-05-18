# Author:       Ricardo Mokveld || Didier Volk  || Diederik van Linden
# Studentnr:    0971051         || 0973139      || 0970665

class Edge:
    def __init__(self, id, beginNode, endNode):
        self.id = id
        self.amplification = 1
        self.beginNode = beginNode
        self.endNode = endNode

    #Gets x value from node and amplifies this
    def getValue(self):
        return self.beginNode.value * self.amplification

    #Change the amplification to vary trough different values
    def changeAmplification(self, change):
        self.amplification += change