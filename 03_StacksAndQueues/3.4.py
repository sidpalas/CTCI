from Stack import Stack

class MyQueue(object):
    def __init__(self):
        self.forward = Stack()
        self.reverse = Stack()
        self.toggle = 'F'

    def push(self, data):
        if self.toggle == 'F':
            self.forward.push(data)
        else:
            self.toggle = 'F'
            #move all the data to the forward stack and push on top of it
            while self.reverse.top:
                self.forward.push(self.reverse.pop())
            self.forward.push(data)

    def pop(self):
        if self.toggle == 'R':
            return self.reverse.pop()
        else:
            self.toggle = 'R'
            while self.forward.top:
                self.reverse.push(self.forward.pop())
            return self.reverse.pop()

    def __str__(self):
        print 'Forward'
        testQueue.forward.printStack()
        print 'Reverse:'
        testQueue.reverse.printStack()

testQueue = MyQueue()

for i in range(6):
    testQueue.push(i)

testQueue.forward.printStack()
print '============='
print testQueue.pop()
print "forward stack:"
testQueue.forward.printStack()
print '-------------'
print "reverse stack:"
testQueue.reverse.printStack()
print testQueue.pop()
print '============='
testQueue.push(99)
print "forward stack:"
testQueue.forward.printStack()
print '-------------'
print "reverse stack:"
testQueue.reverse.printStack()
print '-------------'
testQueue.forward.printStack()
