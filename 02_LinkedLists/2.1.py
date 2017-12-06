from LinkedList import LinkedList

def removeDups(linkedList):
    current = linkedList.head
    buffer = dict()
    buffer[current.get_data()] = True
    while current.get_next():
        if current.get_next().get_data() in buffer:
            current.set_next(current.get_next().get_next())
        else:
            current = current.get_next()
            buffer[current.get_data()] = True
    return

#setup list to test with
testLinkedList = LinkedList()
for i in range(15):
    testLinkedList.insert(i % 3)

#print original list for comparison purposes
testLinkedList.printList()

print "///////////"

removeDups(testLinkedList)

#print modified list
testLinkedList.printList()
