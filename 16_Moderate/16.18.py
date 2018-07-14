#port of book solution... I got stuck and frustrated trying to solve on my own

def doesMatch(pattern, value):
    if len(pattern) == 0:
        return len(value) == 0

    mainChar = pattern[0]
    altChar = 'b' if mainChar == 'a' else 'a'
    size = len(value)

    countOfMain = countOf(pattern, mainChar)
    countOfAlt = len(pattern) - countOfMain
    firstAlt = pattern.find(altChar)
    maxMainSize = size/countOfMain

    for mainSize in range(maxMainSize+1):
        remainingLength = size - mainSize * countOfMain
        if countOfAlt == 0 or remainingLength % countOfAlt == 0:
            altIndex = firstAlt * mainSize
            altSize = 0 if countOfAlt == 0 else remainingLength/countOfAlt
            if matches(pattern, value, mainSize, altSize, altIndex):
                return True

    return False

def matches(pattern, value, mainSize, altSize, firstAlt):
    stringIndex = mainSize
    for i in range(1,len(pattern)):
        size = mainSize if pattern[i] == pattern[0] else altSize
        offset = 0 if pattern[i] == pattern[0] else firstAlt
        if not isEqual(value, offset, stringIndex, size):
            return False
        stringIndex += size
    return True

def isEqual(s1, offset1, offset2, size):
    for i in range(size):
        if s1[offset1 + i] != s1[offset2 + i]:
            return False
    return True

def countOf(pattern, c):
    count = 0
    for char in pattern:
        if char == c:
            count += 1
    return count

testPattern1 = 'aabab'
testValue1 = 'catcatgocatgo'

print(doesMatch(testPattern1,testValue1))
