from Tree import BinaryNode
from Tree import minTree

#should have broken up into multiple functions... kind of hard to follow

def findPathsWithSums(root, sumOfInterest, prevSum, searchDict, depth):
    print searchDict
    if root:
        newSum = prevSum + root.getData()
        if newSum in searchDict:
            possibleIndices = searchDict[newSum]
            for val in possibleIndices:
                if val <= depth-1:
                    print '%%%%%%%%'
                    print "Starting Depth:", val
                    print "Ending Depth:", depth - 1
                    print "Leaf Value:", root.getData()
                    print '%%%%%%%%'
        newSumOfInterest = sumOfInterest + newSum
        if newSumOfInterest in searchDict:
            temp = searchDict[newSumOfInterest] #when I tried to append directly this didnt work...
            temp.append(depth)
            searchDict[newSumOfInterest] = temp
        else:
            searchDict[newSumOfInterest] = [depth]
        if root.getLeft():
            findPathsWithSums(root.getLeft(), sumOfInterest, newSum, searchDict, depth + 1)
        if root.getRight():
            findPathsWithSums(root.getRight(), sumOfInterest, newSum, searchDict, depth + 1)

testRoot = minTree(range(1,16))
testDict = dict()
testDict[34] = [0]
#findPathsWithSums(testRoot, 34, 0, testDict, 1)

print 'first test complete'

testRoot2 = BinaryNode(1)

L1 = BinaryNode(2)
testRoot2.setLeft(L1)

L2 = BinaryNode(3)
L1.setLeft(L2)

L3 = BinaryNode(4)
L2.setLeft(L3)

L4 = BinaryNode(-5)
L3.setLeft(L4)

L5 = BinaryNode(-2)
L4.setLeft(L5)

L6 = BinaryNode(4)
L5.setLeft(L6)

L7 = BinaryNode(1)
L5.setRight(L7)

testDict2 = dict()
testDict2[2] = [0]
findPathsWithSums(testRoot2, 2, 0, testDict2, 1)

print 'second test complete'

testDict3 = dict()
testDict3[3] = [0]
findPathsWithSums(testRoot2, 3, 0, testDict3, 1)
