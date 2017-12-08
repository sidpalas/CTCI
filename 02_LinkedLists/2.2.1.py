from LinkedList import LinkedList

def returnKthFromEnd(linkedList, k):
    lag = linkedList.head
    lead = lag
    for i in range(k):
        lead = lead.get_next()
    while lead.get_next():
        lead = lead.get_next()
        lag = lag.get_next()
    return lag

#setup list to test with
testLinkedList = LinkedList()
for i in range(15):
    testLinkedList.insert(i)

#print original list for comparison purposes
testLinkedList.printList()

print "///////////"

print returnKthFromEnd(testLinkedList,3).get_data()
