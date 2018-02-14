def permuteWithDups(stringIn):
    if len(stringIn) == 1:
        return [stringIn]
    else:
        permutes = []
        cache = dict()
        prevPermutes = permuteWithDups(stringIn[0:-1])
        for permutation in prevPermutes:
            for i in range(0,len(permutation) + 1):
                temp = permutation[0:i] + stringIn[-1] + permutation[i:]
                if temp not in cache: #check if already exists
                    cache[temp] = True
                    permutes.append(temp)
        return permutes

print(permuteWithDups('a'))

print(permuteWithDups('ab'))

print(permuteWithDups('abc'))

print(permuteWithDups('aba'))

print(permuteWithDups('abab'))
