def parenGen(numParenPairs, idx = 0, numOpenParens = 0, numUnmatchedOpenParens = 0,prevSequence = ''):
    if idx == numParenPairs*2-1:
        print(prevSequence + '0')
    else:
        if numParenPairs == numOpenParens:
            parenGen(numParenPairs, idx + 1, numOpenParens, numUnmatchedOpenParens - 1, prevSequence + '0')
        elif numUnmatchedOpenParens == 0:
            parenGen(numParenPairs, idx + 1, numOpenParens + 1, numUnmatchedOpenParens + 1, prevSequence + '1')
        else:
            parenGen(numParenPairs, idx + 1, numOpenParens, numUnmatchedOpenParens - 1, prevSequence + '0')
            parenGen(numParenPairs, idx + 1, numOpenParens + 1, numUnmatchedOpenParens + 1, prevSequence + '1')
    return None

for i in range(1, 5):
    print(i, "Parentheses Pairs:")
    parenGen(i)
