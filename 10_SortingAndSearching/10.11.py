import sys

def sortValleysAndPeaks(arrayIn):
    for i in range(1,len(arrayIn),2):
        biggestIdx = maxIndex(arrayIn, i - 1, i, i + 1)
        if not i == biggestIdx:
            tempI = arrayIn[i]
            arrayIn[i] = arrayIn[biggestIdx]
            arrayIn[biggestIdx] = tempI
    return

def maxIndex(arrayIn, a, b, c):
    minVal = float('-inf')
    length = len(arrayIn)
    if a >= 0 and a < length:
        aValue = arrayIn[a]
    else:
        aValue = minVal

    if b >= 0 and b < length:
        bValue = arrayIn[b]
    else:
        bValue = minVal

    if c >= 0 and c < length:
        cValue = arrayIn[c]
    else:
        cValue = minVal

    maxVal = max(aValue, max(bValue, cValue))
    if aValue == maxVal:
        return a
    elif bValue == maxVal:
        return b
    else:
        return c

testArray = [9, 1, 0, 4, 8, 7]

print(testArray)

sortValleysAndPeaks(testArray)

print(testArray)
