from LinkedList import LinkedList

def partitionLL(linkedList, p):
    current = linkedList.head
    lowLL = LinkedList()
    lowEnd = None
    highLL = LinkedList()
    while current:
        currentData = current.get_data()
        if currentData < p:
            lowLL.insert(currentData)
            if lowEnd == None:
                lowEnd = lowLL.head #this ends up being the end of the low list
        else:
            highLL.insert(currentData)
        current = current.get_next()
    #combine the two lists
    if lowEnd != None:
        lowEnd.set_next(highLL.head)
    if lowEnd == None:
        lowLL = highLL
    return lowLL

#setup list to test with
testLinkedList = LinkedList()
for i in [6,2,10,1, 5,8,5,3]:
    testLinkedList.insert(i)

#print original list for comparison purposes
testLinkedList.printList()

print "///////////"

partitionedLinkedList = partitionLL(testLinkedList, 5)

partitionedLinkedList.printList()
