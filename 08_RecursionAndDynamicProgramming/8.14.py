def countEval(stringIn, desiredResult, cache = dict()):
    if len(stringIn) == 0:
        return 0
    if len(stringIn) == 1:
        return eval(stringIn) == desiredResult

    if str(desiredResult) + stringIn in cache:
        print('Woo! Using cached result!')
        return cache[str(desiredResult) + stringIn]

    count = 0
    for i in range(0, len(stringIn)-2, 2):
        operator = stringIn[(i+1)]
        left = stringIn[0:(i+1)]
        right = stringIn[(i+2):]

        leftTrue = countEval(left, True, cache)
        leftFalse = countEval(left, False, cache)
        rightTrue = countEval(right, True, cache)
        rightFalse = countEval(right, False, cache)

        totalCombinations = (leftTrue + leftFalse) * (rightTrue + rightFalse)
        totalTrue = 0

        if operator == "&":
            totalTrue = leftTrue * rightTrue
        elif operator == "|":
            totalTrue = leftTrue * rightTrue + leftTrue * rightFalse + leftFalse * rightTrue
        elif operator == "^":
            totalTrue = leftTrue * rightFalse + leftFalse * rightTrue

        if desiredResult:
            subCount = totalTrue
        else:
            subCount = totalCombinations - totalTrue

        count += subCount

    cache[str(desiredResult) + stringIn] = count
    return count

print('1^0|0|1')
val = countEval('1^0|0|1', False)
print(val)


print('0&0&0&1^1|0')
val = countEval('0&0&0&1^1|0', True)
print(val)
