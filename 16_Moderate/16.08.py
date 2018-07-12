# English Int

def englishInt(n):
    mapping = dict()
    mapping[1] = 'one'
    mapping[2] = 'two'
    mapping[3] = 'three'
    mapping[4] = 'four'
    mapping[5] = 'five'
    mapping[6] = 'six'
    # ...
    mapping[8] = 'eight'
    mapping[9] = 'nine'
    # ...
    mapping[13] = 'thirteen'
    #
    mapping[20] = 'twenty'
    mapping[30] = 'thirty'
    mapping[40] = 'fourty'
    mapping[50] = 'fifty'
    #...
    mapping[70] = 'seventy'
    mapping[90] = 'ninety'

    multiplesOf1000 = ['', ' thousand', ' million', ' billion', ' trillion']

    englishInt = ''

    if n == 0:
        return mapping[n]
    if n < 0:
        englishInt.append('negative')

    intString = str(n)

    # pad with zeros to make divisible by 3
    while len(intString) % 3 != 0:
        intString = "0" + intString

    powerOf1000 = 0

    for i in range(len(intString), 0, -3):
        group = intString[(i-3):(i)]
        englishGroup = ''
        digits = [int(group[0]), int(group[1]), int(group[2])]
        if digits[0] > 0: #hundreds digit
            englishGroup += ' ' + mapping[int(group[0])] + ' hundred'

        if digits[1] == 1:
            englishGroup += ' ' + mapping[int(group[1:3])]
        elif digits[1] > 1:
            englishGroup += ' ' +mapping[int(group[1] + "0")]
            if digits[2] > 0:
                englishGroup += ' ' + mapping[int(group[2])]
        else: #digits[2] == 0
            englishGroup += ' ' + mapping[int(group[2])]

        englishInt = englishGroup + multiplesOf1000[powerOf1000] + englishInt
        powerOf1000 += 1

    return englishInt

print(englishInt(32413243124))
print(englishInt(298571239))
print(englishInt(2456))
