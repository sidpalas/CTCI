from Tree import BinaryNode
from Tree import minTree

def checkBalanced(rootNode):
    depths = []
    global depths
    findImbalances(rootNode, 0)

def findImbalances(rootNode, depth):
    if rootNode.getLeft():
        findImbalances(rootNode.getLeft(), depth + 1)
    if rootNode.getRight():
        findImbalances(rootNode.getRight(), depth + 1)
    if not (rootNode.getLeft() or rootNode.getRight()): #indicates end of branch
        if len(depths) == 0:
            depths.append(depth)
        elif len(depths) == 1 and depths[0] != depth:
            if abs(depths[0] - depth) > 1:
                print "Unbalanced"
            depths.append(depth)
        elif not (depth in depths):
            print "Unbalanced"

#should adjust such that function returns true or false rather than simply
#printing "Unbalanced" when an imbalance is found.


testList1 = range(22)
testTree1 = minTree(testList1)
checkBalanced(testTree1)
print "test1 complete"

testTree2 = BinaryNode(1,BinaryNode(2,BinaryNode(3,BinaryNode(4))),BinaryNode(5))
checkBalanced(testTree2)
print "test2 complete"
