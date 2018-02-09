def countSetBits(num):
    count = 0
    n = num
    while n:
        count += n & 1 #adds one if 0th bit is 1
        n >>= 1 #shifts number
    return count

def conversion(num1, num2):
    return (countSetBits(num1 ^ num2))

print(conversion(29, 15)) #2

print(conversion(16, 3)) #3
