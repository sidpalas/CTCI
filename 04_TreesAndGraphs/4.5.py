from Tree import BinaryNode
from Tree import minTree
import sys

def checkBST(root, minBound, maxBound):
    print("%s <= %s < %s ?" % (minBound, root.getData(), maxBound))
    if root.getData() == None:
        return
    if root.getData() >= minBound and root.getData() < maxBound:
        if root.getLeft():
            checkBST(root.getLeft(), minBound, root.getData())
        if root.getRight():
            checkBST(root.getRight(), root.getData(), maxBound)
    else:
        print "NOT A BST!!!"

testTree1 = BinaryNode(8,BinaryNode(4,BinaryNode(2),BinaryNode(6)),BinaryNode(10,None,BinaryNode(20)))
checkBST(testTree1, -sys.maxint-1, sys.maxint)
print "test1 complete"

testTree2 = BinaryNode(8,BinaryNode(4,BinaryNode(2),BinaryNode(12)),BinaryNode(10,None,BinaryNode(20)))
checkBST(testTree2, -sys.maxint-1, sys.maxint)
print "test2 complete"
