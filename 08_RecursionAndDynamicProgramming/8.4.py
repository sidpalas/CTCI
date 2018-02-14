from copy import deepcopy

def powerSet(setIn):
    if not setIn:
        return [[]]
    else:
        sets = powerSet(setIn[0:-1])
        prevSets = deepcopy(sets)
        for thisSet in prevSets:
            thisSet.append(setIn[-1])
        sets.extend(prevSets)
        return sets

print(powerSet([]))

print(powerSet(['a']))

print(powerSet(['a','b']))

print(powerSet(['a','b','c']))

print(powerSet(['a','b','c','d']))
