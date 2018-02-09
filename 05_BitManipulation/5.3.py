def bitFlip(num):
    if num == 0:
        return 1
    elif False: #add conditional for case where all bits are 1
        pass
    else:
        prevGroup = 0
        curGroup = 0
        prevBit = 0
        best = 0
        for bit in num:
            if bit == '1':
                curGroup += 1
                prevBit = 1
            else:
                if prevBit:
                    prevGroup = curGroup
                    prevBit = 0
                else:
                    prevGroup = curGroup
                    #prevBit = 0 #not necessary
                curGroup = 0
            best = max(best, prevGroup + curGroup)
    return best + 1 #+1 to get credit for the flipped bit as well

print(bitFlip('1101011101011111001111111100'))

print(bitFlip('11011101111'))
