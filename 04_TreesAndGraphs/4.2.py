from Tree import BinaryNode
from math import floor

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

testList = range(8)

tree = minTree(testList)
print tree.name
print tree.left.name
print tree.right.name
print tree.left.left.name
print tree.left.right.name
print tree.right.left.name
print tree.right.right.name
print tree.left.left.left.name
print tree.left.left.right
