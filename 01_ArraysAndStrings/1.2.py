def isPermutation(str1, str2):
    charCount1 = [0]*256
    charCount2 = [0]*256
    for char in str1:
        charCount1[ord(char)] += 1
    for char in str2:
        charCount2[ord(char)] += 1
    return charCount1 == charCount2

print(isPermutation('asdf', 'fdsa'))
print(isPermutation('asdf', 'fsdfsddsa'))
print(isPermutation('asdf', '1234'))
