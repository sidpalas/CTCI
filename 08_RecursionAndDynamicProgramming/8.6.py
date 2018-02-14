class TowersOfHanoi(object):
    def __init__(self, numDisks):
        self.tower0 = list(range(numDisks,0,-1))
        self.tower1 = []
        self.tower2 = []
        self.towers = [self.tower0, self.tower1, self.tower2]
        print(self)

    def __str__(self):
        return(str(self.towers))

    def moveDisk(self, fromTower, toTower):
        if not self.towers[toTower]:
            self.towers[toTower].append(self.towers[fromTower].pop())
        elif self.towers[fromTower][-1] < self.towers[toTower][-1]:
            self.towers[toTower].append(self.towers[fromTower].pop())
        else:
            print("Illegal Move")
        print(self)

    def isComplete(self):
        if len(self.towers[2]) == numDisks:
            return True
        else:
            return False

def solveTowersOfHanoi(towerHeight, initialPole, goalPole, otherPole):
    if towerHeight == 1:
        return [[initialPole, goalPole]]
    else:
        freeLargeDisk = solveTowersOfHanoi(towerHeight-1, initialPole, otherPole, goalPole) #need to move all but the largest disk out of the way
        freeLargeDisk.append([initialPole, goalPole]) #move the large disk where it needs to go!
        solveRemainingPuzzle = solveTowersOfHanoi(towerHeight - 1, otherPole, goalPole, initialPole) #now start over, for the shorter stack with the stack in a different starting location
        return freeLargeDisk + solveRemainingPuzzle

print("solving tower of 1")
print(solveTowersOfHanoi(1,0,2,1))

print("solving tower of 2")
print(solveTowersOfHanoi(2,0,2,1))

print("solving tower of 3")
print(solveTowersOfHanoi(3,0,2,1))

print("solving tower of 5")
fiveSolution = solveTowersOfHanoi(5,0,2,1)

testTowers = TowersOfHanoi(5)
for move in fiveSolution:
    testTowers.moveDisk(move[0],move[1])
