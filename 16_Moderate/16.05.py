# Write an algo to calculate the # of trailing zeros in n factorial

# Brute force would be to calculate n! and then check... we could do this iteratively or recursively (with memoization!)

# A the trick is to look for powers of 5 because each time a power of 5 is encountered the number of zeros increases
def powersOf5(n):
    power = 0
    while True:
        if n % 5 == 0:
            n /= 5
            power += 1
        else:
            return power

def factorialZerosPattern(n):
    trailingZerosCount = 0
    for multiplier in range(1,n+1):
        trailingZerosCount += powersOf5(multiplier)
    return trailingZerosCount

####

for testN in range(1,105):
    print(testN, factorialZerosPattern(testN))
