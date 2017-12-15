from Stack import Stack

class MyQueue(object):
    def __init__(self):
        self.forward = Stack()
        self.reverse = Stack()

    def push(self, data):
        self.forward.push(data)

    def pop(self):
        #if there is data in the reverse stack, use it
        if self.reverse.top:
            return self.reverse.pop()
        #if not, move all the data from the forward stack over
        else:
            print "Shifting elements to reverse stack..."
            while self.forward.top:
                self.reverse.push(self.forward.pop())
            return self.reverse.pop()


testQueue = MyQueue()

for i in range(3):
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
print testQueue.pop()
print testQueue.pop()
