from LinkedList import LinkedList

def removeNode(node):
    currentNode = node
    nextNode = node.get_next()
    current.data = nextNode.get_data()
    current.set_next(nextNode.get_next())
    return

#setup list to test with
testLinkedList = LinkedList()
for i in range(7,-1,-1):
    testLinkedList.insert(i % 30)

#print original list for comparison purposes
testLinkedList.printList()

print "///////////"

current = testLinkedList.head
for i in range(5):
    current=current.get_next()

removeNode(current)

#print modified list
testLinkedList.printList()
