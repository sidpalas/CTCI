class BinaryNode(object):
    def __init__(self, name, left = None, right = None):
        self.name = name
        self.left = left
        self.right = right

    def setLeft(self, left):
        self.left = left


    def setRight(self, right):
        self.right = right

    def getLeft(self):
        if self.left:
            return self.left
        else:
            return None

    def getRight(self):
        if self.right:
            return self.right
        else:
            return None

def minTree(array):
    if len(array) == 0:
        return
    elif len(array) == 1:
        return BinaryNode(array[0])
    else:
        idxMiddle = len(array)/2
        middleBinaryNode = BinaryNode(array[idxMiddle])
        leftArray = array[0:(idxMiddle)]
        rightArray = array[(idxMiddle+1):]
        middleBinaryNode.setLeft(minTree(leftArray))
        middleBinaryNode.setRight(minTree(rightArray))
    return middleBinaryNode
