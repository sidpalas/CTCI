#Explain what (n & (n-1) == 0) does

#It returns true when either:
#a) n = 0, or
#b) n has exactly one bit set to true (i.e. n is a power of 2)

for i in range(-20,65):
    print('n: ', i, ' Output: ', (i & (i-1) == 0))
