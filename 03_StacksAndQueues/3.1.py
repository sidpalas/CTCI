class TripleStack(object):
    #this implementation assumes a fixed size... if we wanted dynamic sizing
    #we would need to shift the elements and resize when the capacity is reached
    #also, exception handling for dealing with full or empty stacks would be useful
    def __init__(self, size = 100):
        self.array=[None]*size
        self.indices = [0,1,2]

    def push(self, data, n):
        self.array[self.indices[n]] = data
        self.indices[n] += 3

    def pop(self, n):
        self.indices[n] -= 3
        value = self.array[self.indices[n]]
        self.array[self.indices[n]] = None
        return value

if __name__ == '__main__':
    testStacks = TripleStack(9)
    testStacks.push(45,1)
    print testStacks.array
    testStacks.push(23,1)
    print testStacks.array
    testStacks.push(999,1)
    print testStacks.array
    print testStacks.pop(1)
    print testStacks.array
    testStacks.push(243,2)
    print testStacks.array
