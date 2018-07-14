#implement T9 texting

def returnValidWords(number, wordList):
    wordDict = processWords(wordList)
    return wordDict[str(number)]

def processWords(wordList):
    wordDict = dict()
    for word in wordList:
        numList = []
        for letter in word:
            numList.append(getNumber(letter))
        numString = ''.join(numList)
        if numString in wordDict:

            wordDict[numString].append(word)
        else:
            wordDict[numString] = [word]
    return wordDict

def getNumber(letter):
    if letter in 'abc':
        return '2'
    elif letter in 'def':
        return '3'
    elif letter in 'ghi':
        return '4'
    elif letter in 'jkl':
        return '5'
    elif letter in 'mno':
        return '6'
    elif letter in 'pqrs':
        return '7'
    elif letter in 'tuv':
        return '8'
    elif letter in 'wxyz':
        return '9'
    else:
        return False



testWordList = ['tree', 'used', 'blah', 'what']

print(returnValidWords(8733, testWordList))
