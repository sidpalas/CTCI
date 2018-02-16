#from bitarray import bitarray
from operator import mul,add

global max32
max32 = 2**32-1

def insertNum(N,M,i,j):
    onesItoJ = int('1'*(j - i + 1),2)
    #question ambiguous about whether i to j will always be length of M
    #if the range from i to j is longer you could use the len(M) to determine
    #the mask size.  You would also need to determine how far to shift in
    #the next step as well.
    shiftedOnesItoJ = onesItoJ << i
    mask = shiftedOnesItoJ ^ max32
    shiftedM = M << i
    return (N & mask) | shiftedM

testN = int('10000000000',2)
testM = int('10011',2)
print(bin(insertNum(testN,testM,2,6)))
