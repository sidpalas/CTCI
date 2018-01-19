from Tree import BinaryNode
from Tree import minTree
import sys

def checkBST(root, minBound, maxBound):
    #print("%s <= %s < %s ?" % (minBound, root.getData(), maxBound))
    if root == None:
        return True
    if not (root.getData() >= minBound and root.getData() < maxBound):
        return False
    else:
        return (checkBST(root.getLeft(), minBound, root.getData()) and checkBST(root.getRight(), root.getData(), maxBound))

def isValidBST(root):
    if root.getData() == None:
        return True

    minBound = -sys.maxint-1
    maxBound = sys.maxint
    return (checkBST(root.getLeft(), minBound, root.getData()) and checkBST(root.getRight(), root.getData(), maxBound))

testTree1 = BinaryNode(8,BinaryNode(4,BinaryNode(2),BinaryNode(6)),BinaryNode(10,None,BinaryNode(20)))
print isValidBST(testTree1)
print "test1 complete"

testTree2 = BinaryNode(8,BinaryNode(4,BinaryNode(2),BinaryNode(12)),BinaryNode(10,None,BinaryNode(20)))
print isValidBST(testTree2)
print "test2 complete"
