#would need to do logical right shift to handle negative numbers as well...
def pairwiseSwap(num):
    #Assumes max of 32 bit values
    maskOdd = int('01'*16,2)
    maskEven = int('10'*16,2)
    return ((num & maskOdd) << 1) | ((num & maskEven) >> 1)

print(bin(pairwiseSwap(int('1110110101',2)))) #1101111010
