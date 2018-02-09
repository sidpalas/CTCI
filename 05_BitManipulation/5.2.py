def bin2Str(val):
    remainder = val
    count = 0
    string = ''
    while count < 32:
        count += 1
        digitVal = 1/(2 ** count)
        if remainder >= digitVal:
            remainder -= digitVal
            string += '1'
            if remainder == 0:
                return string
        else:
            string += '0'
    return "Error"

print(bin2Str(0.5))

print(bin2Str(0.72))

print(bin2Str(0.75))

print(bin2Str(0.8525390625)) #1/2 + 1/4 + 1/16 + 1/32 + 1/128 + 1/(2**10)
