def slowRecurseMult(a,b):
    if b == 1:
        return a
    else:
        return a + slowRecurseMult(a,b-1)

print(slowRecurseMult(6,7), '=?=', 6*7)
print('%%%%%%')

def fasterRecurseMult(larger, smaller, cache):
    #because we call with recurseMultInit, a will always be less than b
    if smaller == 0:
        return 0
    elif smaller == 1:
        return larger
    elif str(larger)+'_'+str(smaller) in cache:
        return cache[str(larger)+'_'+str(smaller)]
    s = smaller >> 1 # divide by 2
    side1 = fasterRecurseMult(larger, s, cache)
    side2 = side1
    if (smaller % 2) == 1: #if smaller is odd, it wont divide evently by two
        side2 = fasterRecurseMult(larger, smaller - s, cache)
    cache[str(larger)+'_'+str(smaller)] = side1 + side2
    return side1 + side2

def recurseMultInit(a,b):
    if a >= b:
        return fasterRecurseMult(a,b,dict())
    else:
        return fasterRecurseMult(b,a,dict())

print(recurseMultInit(150,7), '=?=', 150*7)
print('%%%%%%')

print(recurseMultInit(150,7231), '=?=', 150*7231)
print('%%%%%%')

print(recurseMultInit(1251,11323), '=?=', 1251*11323)
print('%%%%%%')
