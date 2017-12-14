class minStack(object):
    #could have made this more space efficient by only keeping a stack of the
    #mins (one per value) then when using pop() I could check if there remain
    #any more values that match the current min or not.  This solution still
    #satisfies O(1) runtime, but wastes some space.
    def __init__(self):
        self.stack = []
        self.minSubStack = []

    def push(self,data):
        self.stack.append(data)
        if len(self.minSubStack)==0:
            self.minSubStack.append(data)
        elif data < self.minSubStack[-1]:
            self.minSubStack.append(data)
        else:
            self.minSubStack.append(self.minSubStack[-1])

    def pop(self):
        if len(self.stack) == 0:
            return "emptyStackException"
        else:
            self.minSubStack.pop()
            return self.stack.pop()

    def minimum(self):
        return self.minSubStack[-1]

if __name__ == '__main__':
    testStack = minStack()
    for val in [5,4,3,2,1,3,4,5]:
        testStack.push(val)

    print testStack.stack
    print testStack.minSubStack

    print testStack.pop()
    print testStack.pop()
    print testStack.minimum()
    print testStack.pop()
    print testStack.pop()
    print testStack.pop()
    print testStack.pop()
