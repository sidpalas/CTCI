def tripleStep(n):
    if n < 0:
        raise ValueError("You can't have zero or negative steps!")
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else: #n>3
        #Each combination of ways to get to step n-3 can be updated with a 3 step hop
        #Each combination of ways to get to step n-2 can be updated with a 2 step hop            #Each combination of ways to get to step n-1 can be updated with a 1 step hop
        return tripleStep(n-1) + tripleStep(n-2) + tripleStep(n-3)
    #to reduce runtime and memory needs we could use memoization to store the past 3 values
    #and look them up directly rather than compute recursively each time...

for i in range(1,6):
    print("For staircase of length", i, "there are", tripleStep(i), "possible ways!")

#bad input
tripleStep(0)
