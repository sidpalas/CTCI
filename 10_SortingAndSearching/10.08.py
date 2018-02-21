def printDuplicateVals(arrayIn):
    #initialize bit vector:
    bitVector = 0
    for val in arrayIn:
        #by not breaking this up into small values, this gets super inefficient for large numbers
        #a real BitVector implementations will use an array of smaller 8, 16, or 32 bit ints
        if bitVector >> val & 1:
            print(val)
        else:
            bitVector = bitVector | 1 << val
    return

testArray = list(range(0,50)) + list(range(30,41))

printDuplicateVals(testArray)
