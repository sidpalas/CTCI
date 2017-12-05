#this one has a "Trick"... a string is a rotation of another string if and only if
#it is a substring of the comparison string concatenated with itself.
def isRotation(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        s2s2 = "".join([s2,s2])
    return isSubstring(s1, s2s2)

def isSubstring(s1, s2):
    return s1 in s2

print isRotation("waterbottle","erbottlewat")
print isRotation("waterbottle","erbottlewta")
