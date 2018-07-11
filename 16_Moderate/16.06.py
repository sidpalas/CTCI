# given two arrays of integers, return the pair (one from each) with the smallest difference

def smallestDiff(list1, list2):
    #sort lists first
    list1.sort() #O(n*log(n))
    list2.sort() #O(m*log(m))

    minDiff = abs(list1[0] - list2[0])
    idx = [0,0]
    pointer1 = 0
    pointer2 = 0

    print(list1, list2)

    while pointer1 < len(list1) or pointer2 < len(list2):
        print(pointer1, pointer2)
        val1 = list1[pointer1]
        val2 = list2[pointer2]
        currentDiff = abs(val1 - val2)
        if currentDiff < minDiff:
            minDiff = currentDiff
            idx = [pointer1, pointer2]
        if val1 <= val2 and pointer1 < len(list1)-1:
            pointer1 += 1
        elif val2 <= val1 and pointer2 < len(list2)-1:
            pointer2 += 1
        else:
            return minDiff

#####

test1 = [1,3,15,11,2]
test2 = [23,127,235,19,8]

print(smallestDiff(test1, test2)) #should be 3
