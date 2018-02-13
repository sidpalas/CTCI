from random import random

class Grid(object):
    def __init__(self, N, M, blockedThreshold):
        self.N = N
        self.M = M
        self.grid = []
        for i in range(0,N):
            row = []
            for j in  range(0,M):
                row.append(int(random() > blockedThreshold))
            self.grid.append(row)
        self.grid[0][0] = 1 #make sure first block is open
        self.grid[N-1][M-1] = 1 #make sure final block is open

    def isFinished(self, r, c):
        if r == self.N-1 and c == self.M-1:
            return True
        else:
            return False

def findPath(grid, currentR, currentC, blockedPaths):
    if (currentR > grid.N - 1) or (currentC > grid.M - 1):
        return '' #you went past the edge of the grid
    elif (grid.grid[currentR][currentC] == False) or (blockedPaths[currentR][currentC] == True):
        return '' #you hit a block

    if grid.isFinished(currentR, currentC):
        return 'X'

    #try down:
    path = findPath(grid, currentR + 1, currentC, blockedPaths)
    if path:
        # print('Down Branch:', 'D' + path)
        return 'D' + path

    #try right:
    path = findPath(grid, currentR, currentC + 1, blockedPaths)
    if path:
        # print('Right Branch:', 'R' + path)
        return 'R' + path

    #without this memoization, it gets bogged down with M = N = 50
    blockedPaths[currentR][currentC] = True

    return ''

testN = 60
testM = 80
testThresh = 0.2
testGrid = Grid(testN ,testM , testThresh)
zeroGrid = []
for i in range(0,testN):
    row = []
    for j in range(0,testM):
        row.append(False)
    zeroGrid.append(row)

print(testGrid.grid)

print(findPath(testGrid, 0, 0, zeroGrid))
