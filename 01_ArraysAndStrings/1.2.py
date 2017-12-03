def isPermutation(str1, str2):
    #would be improved if we checked that the lengths were equal first...
    #could also increment with str1 and decrement with str2, stopping if a
    #negative value is ever reached
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
