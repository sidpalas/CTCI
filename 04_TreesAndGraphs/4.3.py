from collections import deque
from LinkedList import LinkedList
from Tree import BinaryNode
from Tree import minTree

def listOfDepths(binaryTreeRoot):
    queue = deque()
    listOfLists = []
    currentList = LinkedList()
    listOfLists.append(currentList)
    currentList.append(binaryTreeRoot.name)
    queue.append(-1)
    left = binaryTreeRoot.getLeft()
    if left:
        queue.append(left)
    right = binaryTreeRoot.getRight()
    if right:
        queue.append(right)
    #assumes binary tree wont contain negatives (could use a different divider otherwise)
    while len(queue)>0:
        currentNode = queue.popleft()
        if currentNode == -1:
            if len(queue)>0:
                currentList = LinkedList()
                listOfLists.append(currentList)
                queue.append(-1)
        else:
            left = currentNode.getLeft()
            if left:
                queue.append(left)
            right = currentNode.getRight()
            if right:
                queue.append(right)
            currentList.append(currentNode.name)
    return listOfLists

testList = range(22)
testTree = minTree(testList)

for list in listOfDepths(testTree):
    print list.head.get_data()
