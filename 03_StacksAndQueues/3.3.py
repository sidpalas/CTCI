#assumes class Stack() implementation with the standard
#push(), pop(), and peek() methods as well as a pointer to the
#top node of each referenced by stack.top
from Stack import Stack


class setOfStacks(object):
    def __init__(self, n=5):
        self.currentStack = Stack()
        self.stackOfStacks = [] #does this take extra storage or does the list only contain pointers to the stacks?
        self.maxHeight = n
        self.currentHeight = 0

    def push(self, data):
        if self.currentHeight < (self.maxHeight):
            self.currentStack.push(data)
            self.currentHeight += 1
        else:
            print "== moving up a stack =="
            self.stackOfStacks.append(self.currentStack)
            self.currentStack = Stack()
            self.currentStack.push(data)
            self.currentHeight = 1

    def pop(self):
        if self.currentHeight > 0:
            self.currentHeight -= 1
            return self.currentStack.pop()
        elif len(self.stackOfStacks) > 0:
            self.currentStack = self.stackOfStacks.pop()
            self.currentHeight = self.maxHeight - 1
            print "== moving down a stack =="
            return self.currentStack.pop() #returns the node, not the stack
        else:
            return "emptyStackException"

testSetOfStacks = setOfStacks(5)
for i in range(50):
    testSetOfStacks.push(i)
    print "+" + str(i)

#print out the top values of each stack in set
for stack in testSetOfStacks.stackOfStacks:
    print stack.printStack()

print '################'

for i in range(30):
    print "-" + str(testSetOfStacks.pop())

for i in range(20):
    testSetOfStacks.push(i)
    print "+" + str(i)

for i in range(41):
    print "-" + str(testSetOfStacks.pop())
