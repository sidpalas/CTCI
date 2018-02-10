#Apocalypse

#All families will continue having children until they have a girl (and then stop)
#What gender ratio will this produce?

#Options:
#g = 1/2
#bg = (1/2)^2
#bbg = (1/2)^3
#bbbg = (1/2)^4
#bbbbg = (1/2)^5

#girls sum from n = 1 to inf. of 1/(2^n)
#boys sum from n = 2 to inf. of (n-1)/(2^n)

from random import random

def familySim(numFamilies):
    numBoys = 0
    numGirls = 0
    for i in range(0,numFamilies):
        if i % 100000 == 0:
            print(i)
        hadGirl = 0
        while not hadGirl:
            if random() > 0.5:
                numGirls += 1
                hadGirl = 1
            else:
                numBoys += 1
    print('numGirls/numBoys: ', numGirls/numBoys)
    return

familySim(9999999)

#the ratio is 1:1
