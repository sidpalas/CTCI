from Stack import Stack

def sortStack(s1):
    s2 = Stack()
    while s1.top:
        temp = s1.pop() #store off top value in temp var to allow for using s1 to store the rest of the values
        while temp < s2.peek():
            s1.push(s2.pop())
        s2.push(temp)
    #now all the elements are in s2 with largest at the top
    while s2.top:
        s1.push(s2.pop())
    return s1

testStack = Stack()
for i in [1,7,2,6,3,5,4]:
    testStack.push(i)
print "unsorted:"
testStack.printStack()
print "==============="
print "sorted:"
sortStack(testStack).printStack()
