# building a diving board with two lengths of
# planks "L" (longer) and "S" (shorter)

# write a method to return all possible lenths

def allPossibleSizes(S, L, k):
    lowerBound = S*k
    upperBound = L*k

    #starting with [S,S,S,...,S]

    #and swapping out each board one at a time
    #the length grows by L-S each time

    if S != L:
        return range(lowerBound, upperBound+(L-S), L-S)
    else:
        return S*k

print(*allPossibleSizes(1,2,5))
print(*allPossibleSizes(11,15,3))
print(allPossibleSizes(2,2,5))
