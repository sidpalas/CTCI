from Tree import BinaryNode
from Tree import minTree

def returnNextValue(node):
    if node.getRight() == None and node.isLeft():
        return node.getParent()
    elif node.getRight() == None and node.isRight():
        tempNode = node.getParent()
        while tempNode.isRight():
            tempNode = tempNode.getParent()
        if tempNode.getParent()
            return tempNode.getParent()
        else:
            return None
    else:
        tempNode.getRight()
        while tempNode.getLeft():
            tempNode = tempNode.getLeft()
        return tempNode
