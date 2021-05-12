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

class Edge:
    def __init__(self, id, beginNode, endNode):
        self.id = id
        self.amplification = 1
        self.beginNode = beginNode
        self.endNode = endNode

