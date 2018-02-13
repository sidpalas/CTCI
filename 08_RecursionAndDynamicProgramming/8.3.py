def findMagicIndex(arrayIn, offset):
    arrayLen = len(arrayIn)
    midIdx = (arrayLen-1)//2
    if arrayLen:
        if arrayIn[midIdx] == midIdx + offset:
            return midIdx + offset
        else:
            #if the input array were still ordered but not distinct, we would also need to
            #check the values of arrayIn far enough away such that duplicate values
            #could allow the index to "catch up"
            #i.e. [-2,-1,4,4,5,5]... 4 is "too high" but because of duplicates, 5 can still be
            #a magic index
            if arrayIn[midIdx] > (midIdx + offset):
                return findMagicIndex(arrayIn[0:(midIdx)], offset)
            else: #arrayIn[midIdx] < (midIdx + offset):
                return findMagicIndex(arrayIn[(midIdx+1):], offset + midIdx + 1)
    else:
        return -1 #magic index not found


testArray = [0]
print(findMagicIndex(testArray, 0)) # should return 0

testArray = [1]
print(findMagicIndex(testArray, 0)) # should return -1

testArray = [-10,-3,-1,3,7]
print(findMagicIndex(testArray, 0)) # should return 3

testArray = [-10,-3,-1,2,4]
print(findMagicIndex(testArray, 0)) # should return 4

testArray = [-2,1,3,5,7,9]
print(findMagicIndex(testArray, 0)) # should return 1

testArray = [-2,-1,0,3,7,9]
print(findMagicIndex(testArray, 0)) # should return 3

testArray = [-2,-1,0,2,3,5]
print(findMagicIndex(testArray, 0)) # should return 5

testArray = [-2,-1,0,2,3,9]
print(findMagicIndex(testArray, 0)) # should return -1
