def pairsWithSum(listIn, sum):
    outputList = []
    complementDict = dict()
    for val in listIn:
        if val in complementDict:
            outputList.append((val, sum-val))
        complementDict[sum-val] = True
    return outputList

testList = [1,2,3,4,5,6,7,-2]

print(pairsWithSum(testList, 5))

print(pairsWithSum(testList, 13))

print(pairsWithSum(testList, 14))
