def numSwap(numA, numB):
    print("numSwap")
    print("input numA: ", numA)
    print("input numB: ", numB)
    temp = numA
    numA = numB
    numB = temp
    print("output numA: ", numA)
    print("output numB: ", numB)
    return

def numSwapInPlace(numA, numB):
    print("numSwapInPlace")
    print("input numA: ", numA)
    print("input numB: ", numB)
    numA = numA + numB    #numA = numA + numB, numB = numB
    numB = -(numB - numA) #numA = numA + numB, numB = -numA
    numA = numA - numB    #numA = numB         numB = numA
    print("output numA: ", numA)
    print("output numB: ", numB)
    return

# Solution only works for integers... could have used bit manipulation to make a more general solution.

######
numA = 45
numB = 23

numSwap(numA,numB)

numSwapInPlace(numA,numB)
