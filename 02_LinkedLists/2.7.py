from LinkedList import LinkedList

def doesIntersect(LL1, LL2):
    current = LL1.head
    hashTable = dict()
    while current:
        hashTable[current] = True
        current = current.get_next()
    current2 = LL2.head
    while current2:
        if current2 in hashTable:
            return current2
        current2 = current2.get_next()
    return False

#I missed the fact that once an intersection occurs, the lists will be
#necessarily equal until the end.  Therefore one could simply walk to the
#end of the lists and check equality.
#
#to then find the intersection point, you could have built up two stacks along the way
#and checked the top elements until they no longer are equal.
#
#if you knew the length you could chop off elements of the longer list until they
#are equal...

#setup lists to test with
testLinkedList1 = LinkedList()
for i in [6,1,7]:
    testLinkedList1.insert(i)
testLinkedList1.printList()
print "///////////"

testLinkedList2 = LinkedList()
for i in [2,1,5]:
    testLinkedList2.insert(i)
testLinkedList2.printList()
print "///////////"

testLinkedListIntersect = LinkedList()
testLinkedListIntersect.insert(3)
#this will actually make the lists intersect in multiple places... but should
#trigger the function to return true
currentTest = testLinkedListIntersect.head
currentTest.set_next(testLinkedList1.head)
testLinkedListIntersect.printList()

print doesIntersect(testLinkedList1, testLinkedList2)
print doesIntersect(testLinkedList1, testLinkedListIntersect)
