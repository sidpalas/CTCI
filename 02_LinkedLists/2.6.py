from LinkedList import LinkedList

def isPalindrome(linkedList):
    current = linkedList.head
    length = 0
    reverseLL = LinkedList()
    while current:
        length += 1
        reverseLL.insert(current.get_data())
        current = current.get_next()
    current = linkedList.head
    currentCompare = reverseLL.head
    for i in range(length/2 + 1):
        if current.get_data() != currentCompare.get_data():
            return False
        current = current.get_next()
        currentCompare = currentCompare.get_next()
    return True

# If we sent a "fast runner" traversing twice as fast as "current" we could have
# Started the comparison once it reached the end this would have shortend runtime
# but both solutions would be O(N)

#setup list to test with
testLinkedList = LinkedList()
for i in [6,2,3,4,6]:
    testLinkedList.insert(i)

#print original list for comparison purposes
testLinkedList.printList()

print "///////////"

print isPalindrome(testLinkedList)
