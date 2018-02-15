from copy import deepcopy

def findQueenPlacements(N, rowIdx, allowable, seq = ''):
    if rowIdx == N:
        print(seq)
        return
    for i in range(0,N):
        tempAllow = deepcopy(allowable)
        if allowable[rowIdx][i]:
            for j in range(rowIdx,N):
                tempAllow[j][i] = False #block column
                if i - (j - rowIdx) >= 0:
                    tempAllow[j][i - (j - rowIdx)] = False #block left diagonal
                if i + (j - rowIdx) < N:
                    tempAllow[j][i + (j - rowIdx)] = False #block right diagonal

            findQueenPlacements(N, rowIdx + 1, tempAllow, seq + str(i))

N = 8
testAllowable = []
for i in range(0,N):
    row = []
    for j in range(0,N):
        row.append(True)
    testAllowable.append(row)

findQueenPlacements(N, 0, testAllowable)

sampleSolution = '04752613'

zeros = [0,0,0,0,0,0,0,0]
for char in sampleSolution:
    boardRow = zeros.copy()
    boardRow[int(char)] = 1
    print(boardRow)
