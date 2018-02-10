def drawLine(byteList, width, x1, x2, y):
    #could add error checking to ensure width is large enough to contain x1 and x2...
    bytesPerRow = width // 8
    bytesBeforeY = bytesPerRow * (y-1)
    bytesBeforeX1 = x1//8 + bytesBeforeY
    bitsBeforeX1 = x1 - 8 * (x1 // 8)
    bytesX1ToX2 = x2//8 - x1//8
    if bytesX1ToX2 == 0:
        bitWidth = x2-x1+1
        trailingZeros = 8 - bitsBeforeX1 - bitWidth
        byteList[bytesBeforeX1] = ((~(-1 << (8-bitsBeforeX1)) & (-1 << trailingZeros)) & 255)
    elif bytesX1ToX2 > 0:
        #add first and last bytes
        #first byte
        trailingZeros = 0
        byteList[bytesBeforeX1] = ((~(-1 << (8-bitsBeforeX1)) & (-1 << trailingZeros)) & 255)

        #last byte
        bitsRemain = (x2 - 8 * (x2 // 8)) #remainder
        byteList[bytesBeforeX1 + bytesX1ToX2] = (-1 << (7 - bitsRemain)) & 255

    if bytesX1ToX2 > 1:
        #add filler bytes @ 255
        for i in range(1,bytesX1ToX2):
            byteList[i+bytesBeforeX1] = 255

    return byteList

def printScreen(line):
    for i in range(0,64//8):
        print(line[i*8+0],line[i*8+1],line[i*8+2],line[i*8+3],line[i*8+4],line[i*8+5],line[i*8+6],line[i*8+7])

testLine1 = drawLine([0]*64, 64, 17, 21, 4)
printScreen(testLine1)

print('')

testLine2 = drawLine([0]*64, 64, 25, 62, 4)
printScreen(testLine2)
