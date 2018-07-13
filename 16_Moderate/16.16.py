# I am assuming we only care about sorting in ascending order

def subSortIdx(listIn):
    largestSeenFwd = [None]*len(listIn)

    largestSeenFwd[0] = listIn[0]
    for i, val in enumerate(listIn[1:]):
        i+=1
        if val > largestSeenFwd[i-1]:
            largestSeenFwd[i] = val
        else:
            largestSeenFwd[i] = largestSeenFwd[i-1]

    smallestSeenBackwards = [None]*len(listIn)
    smallestSeenBackwards[-1] = listIn[-1]
    i = len(listIn)-2
    while i >= 0:
        val = listIn[i]
        if val < smallestSeenBackwards[i+1]:
            smallestSeenBackwards[i] = val
        else:
            smallestSeenBackwards[i] = smallestSeenBackwards[i+1]
        i -= 1

    if largestSeenFwd == smallestSeenBackwards:
        return "Already sorted"

    #could generalize the following two loops into a method
    sortStart = -1
    i = 0
    while sortStart < 0:
        if largestSeenFwd[i] != smallestSeenBackwards[i]:
            sortStart = i
        i += 1

    sortEnd = -1
    i = len(listIn)-1
    while sortEnd < 0:
        if largestSeenFwd[i] != smallestSeenBackwards[i]:
            sortEnd = i
        i -= 1

    return (sortStart, sortEnd)

testList = [1,2,4,7,10,11,7,12,6,7,16,18,19]

print(subSortIdx(testList))
