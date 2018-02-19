def groupAnagrams(arrayIn):
    anagramDict = dict()
    for currentString in arrayIn:
        sortedString = ''.join(sorted(currentString))
        if sortedString in anagramDict:
            temp = anagramDict[sortedString]
            temp.append(currentString)
            anagramDict[sortedString] = temp
        else:
            anagramDict[sortedString] = [currentString]

    arrayOut = []
    for currentKey in anagramDict:
        arrayOut.extend(anagramDict[currentKey])

    return arrayOut

testArray = ['aba','abc','abb','aad','aab','cba']

print(groupAnagrams(testArray))
