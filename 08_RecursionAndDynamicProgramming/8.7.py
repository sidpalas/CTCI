def permuteNoDups(stringIn):
    if len(stringIn) == 1:
        return [[stringIn]]
    else:
        permutes = []
        prevPermutes = permuteNoDups(stringIn[0:-1])
        for permutation in prevPermutes:
            for i in range(0,len(permutation + 1)):
                permutes.append(permutation.insert(stringIn[-1],i))
        return permutes

print(permuteNoDups('a'))
