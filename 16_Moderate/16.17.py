def contiguousSum(listIn):
    bestSum = max(listIn)
    #we dont actually need to merge the list for the same algorithm to work
    # listIn = mergeLikeSigns(listIn)
    runningSum = 0
    for val in listIn:
        if (runningSum + val) > 0:
            runningSum += val
            if runningSum > bestSum:
                bestSum = runningSum
        else:
            runningSum = 0
    return bestSum

def mergeLikeSigns(listIn):
    print(listIn)
    merges = 0
    newList = []
    sign = getSign(listIn[0])
    runningTotal = 0
    for val in listIn:
        thisSign = getSign(val)
        # print(val, sign, thisSign)
        if sign == thisSign or thisSign == 0:
            merges += 1
            runningTotal += val
        else:
            newList.append(runningTotal)
            runningTotal = val
            sign = thisSign
    if runningTotal >= 0:
        newList.append(runningTotal)
    if merges > 1:
        return mergeLikeSigns(newList)
    else:
        return newList


def getSign(val):
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else: #val == 0
        return 0


testList = [-5,2, 5, 3, 0, -3, 0, -5, 8, 2, -1, -4, -6, 12, 1, -1, 2]
testList2 = [2,-8,3,-2,4,-10]

print(contiguousSum(testList))
print(contiguousSum(testList2))
