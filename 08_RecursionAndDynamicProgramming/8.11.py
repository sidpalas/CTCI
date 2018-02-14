def findCoinVariants(cents, startingCoin = 25, seq = ''):
    if cents == 0:
        print(seq)
        return
    else:
        if startingCoin >= 25 and cents - 25 >= 0:
            findCoinVariants(cents - 25, 25, seq + 'q')
        if startingCoin >= 10 and cents - 10 >= 0:
            findCoinVariants(cents - 10, 10, seq + 'd')
        if startingCoin >= 5 and cents - 5 >= 0:
            findCoinVariants(cents - 5, 5, seq + 'n')
        if startingCoin >= 1 and cents - 1 >= 0:
            findCoinVariants(cents - 1, 1, seq + 'p')

for i in range(0,21):
    print('For coins totaling:', i)
    findCoinVariants(i)
