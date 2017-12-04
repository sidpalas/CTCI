def strCompressor(inputStr):
    currentRepeat = 1
    maxRepeat = 1
    prevChar = inputStr[0]
    outputStr = prevChar
    for char in inputStr[1:]:
        if char == prevChar:
            currentRepeat += 1
            maxRepeat = max(maxRepeat, currentRepeat)
        else:
            #I assumed you wouldnt want to add a 1 after a single nonrepeated character
            #the following if statement (and the one after the for loop) could be removed to change this
            #the check at the bottom would be to compare len(outputStr) to len(inputStr) or you could keep
            #track of how many characters each substitution was saving/harming throughout
            if currentRepeat > 1:
                outputStr += str(currentRepeat)
            outputStr += char
            prevChar = char
            currentRepeat = 1
    if currentRepeat > 1: #handle the final character sequence
        outputStr += str(currentRepeat)

    if maxRepeat > 2:
        return outputStr
    else:
        return inputStr

print strCompressor('aabcccccccccccccccccaaa')
print strCompressor('aabbcc')
print strCompressor('aaacvb')
