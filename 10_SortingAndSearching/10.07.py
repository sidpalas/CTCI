def findMissingInt(bigArrayIn):
    #initialize bit vector:
    bitVector = 0
    for val in bigArrayIn:
        #by not breaking this up into small values, this gets super inefficient for large numbers
        #a real BitVector implementation would use an array of smaller numbers (8, 16, or 32 bytes each)
        bitVector = bitVector | 1 << val
        print(bin(bitVector))
    i = 1
    gapFound = 0
    while not gapFound:
        if ~ bitVector & 1:
            gapFound = 1
            return i - 1
        else:
            bitVector = bitVector >> 1 #should account for going past max digit...
            i += 1
    return -1


testArray = list(range(0,56)) + list(range(57,99))

print(findMissingInt(testArray))

#to do with less memory (where full bit vector doesnt fit in memory)
#you would need to make multiple pases
#first n pass(es) you dial in the range
#final pass (once you can fit bit vector in memory) you get the missing int
