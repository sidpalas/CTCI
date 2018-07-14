def sumSwap(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    gap = (sum1-sum2)/2
    if gap == 0:
        return ()

    matchDict = dict()
    for val in list1:
        matchDict[val-gap] = True

    for val in list2:
        if val in matchDict:
            return (val+gap, val)

print(sumSwap([4,1,2,1,1,2],[3,6,3,3]))
