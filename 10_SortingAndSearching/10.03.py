def findRotationIdx(arrayIn, offset = 0, minVal = 99999, minValIdx = None):
    arrayLength = len(arrayIn)

    midIdx = (arrayLength - 1) // 2
    leftIdx = 0
    rightIdx = arrayLength - 1

    midVal = arrayIn[midIdx]
    leftVal = arrayIn[leftIdx]
    rightVal = arrayIn[rightIdx]

    if leftVal <= midVal and rightVal >= midVal:
        if leftVal < minVal:
            return offset
        else:
            return offset + arrayLength
    if midVal < minVal:
        minVal = midVal
        minValIdx = midIdx
    if leftVal > midVal:
        return findRotationIdx(arrayIn[0:midIdx], offset, minVal, minValIdx)
    else: # rightVal < midVal
        return findRotationIdx(arrayIn[(midIdx + 1):], offset + midIdx + 1, minVal, minValIdx)

def getRotatedIdx(originalIdx, n, rotation):
    return (originalIdx + rotation) % n

def getOriginalIdx(rotatedIdx, n, rotation):
    return (rotatedIdx - rotation) % n

def rotatedBinarySearch(arrayIn, searchVal):
    #implement as iterative rather than recursive to avoid creating odd slices and recalculating rotations
    arrayLength = len(arrayIn)
    lowIdx = 0
    highIdx = arrayLength - 1

    rotation = findRotationIdx(arrayIn)

    while lowIdx <= highIdx:
        midIdx = (lowIdx + highIdx) // 2
        rotatedMidIdx = getRotatedIdx(midIdx, arrayLength, rotation)
        midVal = arrayIn[rotatedMidIdx]
        if midVal < searchVal:
            lowIdx = midIdx + 1
        elif midVal > searchVal:
            highIdx = midIdx - 1
        else:
            return getRotatedIdx(midIdx, arrayLength, rotation)

    return -1 #value not found


testArray = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
print(rotatedBinarySearch(testArray, 5)) # 8

print('%%%%%%')

testArray = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]
print(rotatedBinarySearch(testArray, 5)) # 3
