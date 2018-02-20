class Listy():
    def __init__(self, listIn):
        self.list = listIn
        self.len = len(listIn)

    def elementAt(self, i):
        if i < self.len:
            return self.list[i]
        else:
            return -1

# testListy = Listy([1,2,3,4])
#
# print(testListy.elementAt(1))
# print(testListy.elementAt(6))

def listyBinarySearch(listy, searchVal):
    lowBound = 0
    idx = 0
    while listy.elementAt(idx) < searchVal and listy.elementAt(idx) > 0:
        lowBound = idx
        if idx == 0:
            idx = 1
        else:
            idx = idx << 1 #double

    if listy.elementAt(idx) == searchVal:
        return idx

    highBound = idx
    mid = (lowBound + highBound) // 2

    while lowBound < highBound:
        midVal = listy.elementAt(mid)
        if midVal == searchVal:
            return mid
        elif midVal > searchVal or midVal == -1:
            #go left
            highBound = mid - 1
        else: # midVal < searchVal and not midVal == -1
            #go right
            lowBound = mid + 1
        mid = (lowBound + highBound) // 2

    if listy.elementAt(mid) == searchVal:
        return mid
    else:
        return -1 #searchVal not found

testListy = Listy(list(range(1,53)))

print(listyBinarySearch(testListy, 1)) # 0

print(listyBinarySearch(testListy, 20)) # 19

print(listyBinarySearch(testListy, 50)) # 49

print(listyBinarySearch(testListy, 53)) # -1
