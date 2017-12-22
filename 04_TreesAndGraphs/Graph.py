class Graph(object):
    def __init__(self):
        self.nodes = []

class Node(object):
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
