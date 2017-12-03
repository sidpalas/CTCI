def isPalindromePermute(inputStr):
    if len(inputStr) == 0:
        return False
    #Could also put a check to make sure string isnt just a bunch of blank spaces...
    #should have also thought about even and odd length strings
    #i think my solution handles both, but would have been good to call out
    #also could have broken into multiple functions
    charCount = [0]*128
    for char in inputStr.lower():
        if char == " ":
            pass
        else:
            charCount[ord(char)]+=1

    palPermute = True
    oddCounts = 0
    for count in charCount:
        if count % 2 == 1:
            oddCounts += 1
            if oddCounts > 1:
                palPermute = False
                return palPermute
        else:
            pass
    return palPermute


print isPalindromePermute('')
print isPalindromePermute('12315 ')
print isPalindromePermute('Tact Coa')
