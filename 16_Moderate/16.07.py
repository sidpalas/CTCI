# write max method without using comparitors

# use the fact that a-b will be positive ony when a>b

def specialMax(a,b):
    diff = a-b
    k = greaterThanZero(diff)
    return k*a + (not k)*b

def greaterThanZero(a):
    try:
        return bool((1 + int(a / (a**2)**0.5))/2)
    except:
        return True

####

print(specialMax(5, 8))
print(specialMax(-1,-5))
