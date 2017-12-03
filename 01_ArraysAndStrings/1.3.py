def urlify(str, trueLen):
    #if we wanted to sort in place we would need to take two passes
    #1st pass counting the spaces, 2nd pass adding the %20s working back from
    #the end of the string to avoid having to repeatedly shift characters
    urlstr = ""
    for char in str[0:trueLen]:
        if char == " ":
            urlstr += "%20"
        else:
            urlstr += char
    return urlstr

print urlify("Mr John Smith    ", 13)
