import random

def rand5():
    return random.randint(0,4)

def rand7():
    while True:
        #need to generate evenly distributed values in range larger than 7
        val = 5 * rand5() + rand5()
        if val < 21:
            return val % 7

freqList = [0]*7
for i in range(50000):
    val = rand7()
    freqList[val] += 1

print(freqList)
