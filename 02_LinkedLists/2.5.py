from LinkedList import LinkedList

def sumLinkedList(LL1, LL2):
    sumLL = LinkedList()
    current1 = LL1.head
    current2 = LL2.head
    remainder = 0
    while current1 and current2:
        digitSum = current1.get_data() + current2.get_data() + remainder
        [sumLL, remainder] = applyDigitSum(sumLL, digitSum)
        current1 = current1.get_next()
        current2 = current2.get_next()
    while current1:
        digitSum = current1.get_data() + remainder
        [sumLL, remainder] = applyDigitSum(sumLL, digitSum)
        current1 = current1.get_next()
    while current2:
        digitSum = current2.get_data() + remainder
        [sumLL, remainder] = applyDigitSum(sumLL, digitSum)
        current2 = current2.get_next()
    if remainder != 0:
        sumLL.insert(remainder)
    return sumLL

#solution could have been shortened by solving recursively

#if order of input linked lists was reversed (i.e. 1's digit last), you would have to
#keep track of the previous node to apply the remainders after the fact.

def applyDigitSum(LL, digitSum):
    if digitSum < 10:
        #insert method as implemented puts node on front of list, this is
        #opposite of what the problem asks for, but could be easily swapped
        LL.insert(digitSum)
        remainder = 0
    else:
        LL.insert(digitSum - 10)
        remainder = 1
    return LL, remainder



#setup list to test with
testLinkedList1 = LinkedList()
for i in [6,1,7]:
    testLinkedList1.insert(i)
testLinkedList1.printList()
print "///////////"

testLinkedList2 = LinkedList()
for i in [2,9,5]:
    testLinkedList2.insert(i)
testLinkedList2.printList()
print "///////////"

sumLinkedList(testLinkedList1,testLinkedList2).printList()
