def idxFromYear(year):
    return year-1900

def yearFromIdx(idx):
    return idx + 1900

def mostLivingPeople(people):
    startYear = 1900
    endYear = 2000

    numYears = endYear - startYear + 2 #extra year accounts for death in final year

    birthTracker=[0]*numYears
    deathTracker=[0]*numYears

    for person in people:
        birthIdx = idxFromYear(person[0])
        deathIdx = idxFromYear(person[1])
        birthTracker[birthIdx] += 1
        deathTracker[deathIdx+1] += 1 #deaths don't reduce population until following year

    peopleAlive = [0]*numYears
    prevPeopleAlive = 0
    maxPeople = 0
    maxIdx = 0
    for i in range(numYears-1):
        currentPeople = prevPeopleAlive + birthTracker[i] - deathTracker[i]
        #there is actually no need to store this... but it makes it easier to debug
        peopleAlive[i] += currentPeople
        prevPeopleAlive = currentPeople
        if currentPeople > maxPeople:
            maxPeople = currentPeople
            maxIdx = i

    print(peopleAlive)
    return yearFromIdx(maxIdx)


import pytest

def test_1():
    people = [[1900,1910], [1905, 1929], [1915, 1915], [1900, 1940], [1912,1970]]
    assert mostLivingPeople(people) == 1915

pytest.main()
