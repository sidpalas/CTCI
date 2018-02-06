class Graph(object):
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

class Node(object):
    def __init__(self, name, children = [], parents = []):
        self.name = name
        self.children = children
        self.parents = parents

    def addChild(self, child):
        self.children.append(child)

    def addParent(self, parent):
        self.parents.append(parent)
