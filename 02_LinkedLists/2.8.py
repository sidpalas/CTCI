from LinkedList import LinkedList

def isLoop(linkedList):
    current = linkedList.head
    hashTable = dict()
    while current:
        if current in hashTable:
            return current
        hashTable[current] = True
        current = current.get_next()
    return False

#setup lists to test with
testLinkedList = LinkedList()
for i in [6,1,7]:
    testLinkedList.append(i)
midTail = testLinkedList.tail
testLinkedList.append(45)
#causes LL loop back to the 7
testLinkedList.tail.set_next(midTail)

print "///////////"

print isLoop(testLinkedList).get_data()
