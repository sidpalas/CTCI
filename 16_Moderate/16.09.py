#write methods for all multiply, subtract, divide using only add

def negate(a):
    neg = 0;
    if a<0:
        newSign = 1
    else:
        newSign = -1
    while a != 0:
        neg += newSign
        a += newSign

    return neg

def sub(a,b):
    return a + negate(b) # this is sort of cheating, but I dont know of a way to flip sign bit of an int in python b/c the int size is variable (not fixed)

def mult(a,b):
    product = 0
    for i in range(abs(b)):
        if b > 0:
            product += a
        else:
            product = sub(product,a)
    return product

def div(a,b):
    # we can start with 1 and work our way up doubling along the way
    if bool(a<0) ^ bool(b<0): #exactly 1 of the values is < zero
        return sub(negate(1), div(abs(a), abs(b)))

    if a < b:
        return 0
    lower = 1
    upper = 1
    while mult(upper,b) < a:
        lower = upper
        upper = mult(upper,2)

    while mult(lower,b) < a:
        #could continue to split the range in half here rather than increment by 1,
        #it would require very careful bookkeeping of the relevant ranges to avoid
        #off by one errors
        lower += 1

    return lower-1

####

print(mult(5,6)) #30
print(mult(-4, 2)) #-8
print(mult(3, -5)) #-15
print(mult(-6,-7)) #42

####

print(sub(4,10)) #-6

####

print(div(13248,5)) #2649
print(div(-3, 2)) #-2
print(div(2523, -23)) # -110
