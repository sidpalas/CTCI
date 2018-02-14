def permuteNoDups(stringIn):
    if len(stringIn) == 1:
        return [stringIn]
    else:
        permutes = []
        prevPermutes = permuteNoDups(stringIn[0:-1])
        for permutation in prevPermutes:
            for i in range(0,len(permutation) + 1):
                temp = permutation[0:i] + stringIn[-1] + permutation[i:]
                permutes.append(temp)
        return permutes

print(permuteNoDups('a'))

print(permuteNoDups('ab'))

print(permuteNoDups('abc'))

print(permuteNoDups('abcd'))
