def areCharsUnique(string):
    #would be improved by checking if string is longer than total number
    #of unique characters (i.e. 128 for ascii)
    unique = True
    chars = dict()
    for character in string:
        if character in chars:
            unique = False
            return unique
        else:
            chars[character] = True
    return unique

print (areCharsUnique('blah'))
print (areCharsUnique('hello'))
print (areCharsUnique("!@#%783"))
