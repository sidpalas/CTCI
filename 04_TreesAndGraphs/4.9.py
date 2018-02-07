from Tree import BinaryNode
from Tree import minTree

def printAllPossibleArrays(allowable, prevSequence):
    if len(allowable)==0:
        print prevSequence
        return
    else:
        for node in allowable:
            tempAllowable = allowable[:]
            if node.getLeft():
                tempAllowable.append(node.getLeft())
            if node.getRight():
                tempAllowable.append(node.getRight())
            tempAllowable.remove(node)

            tempPrevSequence = prevSequence[:]
            tempPrevSequence.append(node.getData())
            printAllPossibleArrays(tempAllowable, tempPrevSequence)

testRoot = minTree(range(1,4))
printAllPossibleArrays([testRoot], [])

print '%%%%%%%%'

testRoot2 = minTree(range(1,8))
printAllPossibleArrays([testRoot2], [])
