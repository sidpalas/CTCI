def isOneAway(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    len1 = len(str1)
    len2 = len(str2)
    oneAway = True
    i = 0
    j = 0
    edits = 0
    if abs(len1 - len2) > 1:
        oneAway = False
        return oneAway
    elif (len1 - len2) == 1: #look for potential deletion
        while j < len2: #use the shorter string here to prevent out of range index errors
            if str1[i] == str2[j]:
                i+=1
                j+=1
            else:
                edits+=1
                i+=1
                #j doesnt increment
                if edits > 1:
                    oneAway = False
                    return oneAway
    elif (len1 - len2) == -1: #look for a potential insertion
        while i < len1: #use the shorter string here to prevent out of range index errors
            if str1[i] == str2[j]:
                i+=1
                j+=1
            else:
                edits+=1
                #i doesn't increment
                j+=1
                if edits > 1:
                    oneAway = False
                    return oneAway
    else: #look for a character swap
        while i < len1:
            if str1[i] == str2[j]:
                i+=1
                j+=1
            else:
                edits+=1
                i+=1
                j+=1
                if edits > 1:
                    oneAway = False
                    return oneAway
    return oneAway

print isOneAway("pale","ple")
print isOneAway("pales","pale")
print isOneAway("pale","bale")
print isOneAway("pale","bake")
