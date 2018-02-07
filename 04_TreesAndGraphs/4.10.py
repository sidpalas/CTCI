from Tree import BinaryNode
from Tree import minTree

#could have used a pre-order traversal with a null object in the list for empty spots.
#the

def checkTreeMatch(root1,root2):
    if bool(root1) ^ bool(root2):
        return False #one of the trees ended and the other didn't! (i.e. the final node was left off of one)
    elif not (root1 and root2):
        return True #you have reached the end of both trees without failing
    if (root1 and root2):
        if (root1.getData() != root2.getData()):
            return False #a value doesn't match!
        else:
            return checkTreeMatch(root1.getLeft(), root2.getLeft()) and checkTreeMatch(root1.getRight(), root2.getRight())

print "Testing helper function checkTreeMatch():"

testRoot1 = minTree(range(1,8))
testRoot2 = minTree(range(1,8))
testRoot3 = minTree(range(1,7))

print checkTreeMatch(testRoot1, testRoot2)
print checkTreeMatch(testRoot1, testRoot3)

def isSubtree(root1, root2):
    if not root1:
        return False
    else:
        if checkTreeMatch(root1,root2):
            return True
    if (root1.getLeft() and root1.getRight()):
        return isSubtree(root1.getLeft(),root2) or isSubtree(root1.getRight(),root2)
    elif root1.getLeft():
        return isSubtree(root1.getLeft(),root2)
    else: #root1.getRight():
        return isSubtree(root1.getRight(),root2)

print 'Test main function isSubtree():'

testRoot4 = minTree(range(5,8))

print isSubtree(testRoot1, testRoot2) #1 and 2 are same tree (True)
print isSubtree(testRoot1, testRoot4) #4 is a subtree of 1 (True)
print isSubtree(testRoot3, testRoot4) #4 is NOT a subtree of 3 (3 doesnt have the 7 node)
