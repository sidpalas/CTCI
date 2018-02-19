def mergeArrays(A, B):
    idx = len(A) + len(B) - 1
    aIdx = len(A) - 1
    bIdx = len(B) - 1
    A.extend(B) #make space in A for B

    while aIdx >= 0 and bIdx >= 0:
        if A[aIdx] >= B[bIdx]:
            A[idx] = A[aIdx]
            aIdx -= 1
        else: # B value greater
            A[idx] = B[bIdx]
            bIdx -= 1
        idx -= 1

    while bIdx >=0:
        A[idx] = B[bIdx]
        bIdx -= 1
        idx -= 1

    return A

testA = [1,3,5,7,9]
testB = [4,5,10]

print(mergeArrays(testA, testB))
