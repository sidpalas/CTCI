def calcResult(equationList):
    halfway = handleMultandDivide(equationList)
    print(halfway)
    return handleAddandSubtract(halfway)

def handleMultandDivide(equationList):
    i = len(equationList)-1
    reverseEquation = equationList[::-1]
    while i >= 0:
        current = reverseEquation[i]
        if str(current) in '*/':
            if current == '*':
                temp = reverseEquation[i+1]*reverseEquation[i-1]
            else:
                temp = reverseEquation[i+1]/reverseEquation[i-1]
            del reverseEquation[(i-1):(i+2)]
            reverseEquation.insert(i-1, temp)
            i -= 1
        else:
            i -= 1
    return reverseEquation[::-1]

def handleAddandSubtract(equationList):
    total = equationList[0]
    for i in range(1,len(equationList)-1,2):
        if equationList[i] == '+':
            total += equationList[i+1]
        else:
            total -= equationList[i+1]
    return total

testEquation = [2,'+',4,'*', 5, '/',6,'*',3,'+',15,'/',2]

print(calcResult(testEquation))
