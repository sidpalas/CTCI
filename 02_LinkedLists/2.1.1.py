from LinkedList import LinkedList

def removeDupsNoBuffer(linkedList):
    primary = linkedList.head
    while primary:
        runner = primary
        while runner.get_next():
            if runner.get_next().get_data() == primary.get_data():
                runner.set_next(runner.get_next().get_next())
            else:
                runner = runner.get_next()
        primary = primary.get_next()
    return

#setup list to test with
testLinkedList = LinkedList()
for i in range(15):
    testLinkedList.insert(i % 5)

#print original list for comparison purposes
testLinkedList.printList()

print "///////////"

removeDupsNoBuffer(testLinkedList)

#print modified list
testLinkedList.printList()
