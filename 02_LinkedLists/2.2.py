from LinkedList import LinkedList

def returnKthFromEnd(linkedList, k):
    current = linkedList.head
    storedList = [0]*(k+1)
    while current:
        storedList.append(current)
        storedList.pop(0)
        current = current.get_next()
    return storedList.pop(0)

#setup list to test with
testLinkedList = LinkedList()
for i in range(15):
    testLinkedList.insert(i)

#print original list for comparison purposes
testLinkedList.printList()

print "///////////"

print returnKthFromEnd(testLinkedList,6).get_data()
