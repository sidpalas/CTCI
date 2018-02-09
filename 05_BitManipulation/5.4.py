def nextNumbers(num, upOrDown):
    binString = bin(num)
    revBinString = binString[::-1]
    revBinString = revBinString[:-2]
    revBinString += '0' #add a trailing zero
    if upOrDown == 'up':
        print('going up!')
        count = 0
        onesCount = 0
        for bit in revBinString:
            if onesCount:
                if bit == '0':
                    mask = -1 << count + 1
                    primaryBit = 1 << count
                    if onesCount > 1:
                        minBits = ~(-1 << (onesCount -1))
                    else:
                        minBits = 0
                    return (num & mask) | primaryBit | minBits
            if bit == '1':
                onesCount += 1
            count += 1


    elif upOrDown == 'down':
        print('going down!')
        count = 0
        seenZero = 0
        onesCount = 0
        for bit in revBinString:
            if seenZero:
                if bit == '1':
                    mask = -1 << count + 1
                    #primary bit not needed (mask clears it)
                    minBits = ~(-1 << (onesCount + 1)) << (count - onesCount - 1) #can count - onesCount - 1 be negative?
                    return (num & mask) | minBits
            if bit == '0':
                seenZero = 1
            if bit == '1':
                onesCount += 1
            count += 1

    else:
        return "Error: please specify up or down"

print(nextNumbers(int('1000',2),'up')) #8 --> 16
print(nextNumbers(int('1000',2),'down')) #8 --> 4

print(nextNumbers(int('1001',2),'up')) #9 --> 10
print(nextNumbers(int('1001',2),'down')) #9 --> 6

print(nextNumbers(int('1111000',2),'up')) #120 --> 135
print(nextNumbers(int('1111000',2),'down')) #120 --> 116
