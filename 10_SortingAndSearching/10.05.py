def findNextNonEmptyIdx(arrayIn, idx, lowBound, highBound):
    idxL = idx
    idxR = idx
    while not (arrayIn[idxL] or arrayIn[idxR]):
        idxL -= 1
        idxR += 1

    if arrayIn[idxL]:
        return idxL
    elif arrayIn[idxR]:
        return idxR
    else:
        return -1

def sparseBinarySearch(arrayIn, searchStr):
    if searchStr == "":
        pass #should address what happens when someone searches for an empty string...
    low = 0
    high = len(arrayIn) - 1
    mid = (low + high) // 2
    while low < high:
        if not arrayIn[mid]:
            mid = findNextNonEmptyIdx(arrayIn, mid, low, high)
            if mid == -1:
                return -1

        if arrayIn[mid] == searchStr:
            return mid
        elif arrayIn[mid] > searchStr: #go left
            high = mid - 1
        else: # arrayIn[mid] < searchStr
            low = mid + 1
        mid = (low + high) // 2

    if arrayIn[mid] == searchStr:
        return mid
    else:
        return -1

testArray = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", ""]

print(sparseBinarySearch(testArray, "ball"))

print(sparseBinarySearch(testArray, "at"))

print(sparseBinarySearch(testArray, "car"))

print(sparseBinarySearch(testArray, "dad"))
