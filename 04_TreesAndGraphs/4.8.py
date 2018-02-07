from Tree import BinaryNode
from Tree import minTree

def checkMatch(node, SN1, SN2, found):
    if node == SN1:
        found[0] = True
    if node == SN2:
        found[1] = True
    return found

def checkLeftTreeForNodes(node, root, SN1, SN2, found):
    if not node:
        return found
    else:
        found = checkMatch(node, SN1, SN2, found)
        if node == root:
            return checkLeftTreeForNodes(node.getLeft(), root, SN1, SN2, found)
        else: #(node != root) #allows branching right after the first step
            return checkLeftTreeForNodes(node.getLeft(), root, SN1, SN2, found) and checkLeftTreeForNodes(node.getRight(), root, SN1, SN2, found)

def findFirstCommonAncestor(root,SN1,SN2):
    leftTreeFound = checkLeftTreeForNodes(root,root,SN1,SN2,[False,False])
    if leftTreeFound[0] ^ leftTreeFound[1]: #^ performs xor function. the not causes this to be true when one was found
        return root
    if leftTreeFound[0] and leftTreeFound[1]: #both were found, stick with the left side
        return findFirstCommonAncestor(root.getLeft(),SN1,SN2)
    else: #neither were found, move to the right side
        return findFirstCommonAncestor(root.getRight(),SN1,SN2)


testRoot = minTree(range(1,16))
#        8
#   4        12
# 2   6   10     14
#1 3 5 7 9  11 13  15

testNode1 = testRoot.getLeft().getLeft() #2
testNode2 = testRoot.getLeft().getRight().getRight() #7
testNode3 = testRoot.getRight().getRight().getLeft() #13
testNode4 = testRoot.getRight().getRight().getRight() #15

print findFirstCommonAncestor(testRoot, testNode1, testNode2).getData() #should be the 4 node
print findFirstCommonAncestor(testRoot, testNode1, testNode3).getData() #should be the 8 node
print findFirstCommonAncestor(testRoot, testNode3, testNode4).getData() #should be the 14 node
