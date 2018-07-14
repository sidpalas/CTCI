def countPonds(landscape):
    ponds = []
    numRows = len(landscape)
    numCols = len(landscape[0])
    for i in range(numRows):
        for j in range(numCols):
            if landscape[i][j] == 0:
                landscape[i][j] = None
                ponds.append(spiralSearch(1,[[i,j]],landscape))
            else:
                landscape[i][j] = None
    return ponds

def spiralSearch(currentSum, searchQueue, landscape):
    numRows = len(landscape)
    numCols = len(landscape[0])
    while len(searchQueue) > 0:
        currentPosition = searchQueue.pop(0) #collections.deque would be faster (w/ popleft)
        for rowOffset in [-1,0,1]:
            for colOffset in [-1,0,1]:
                searchRow = currentPosition[0]+rowOffset
                searchCol = currentPosition[1] + colOffset
                if 0 <= searchRow < numRows and 0 <= searchCol < numCols:
                    if landscape[searchRow][searchCol] == 0:
                        searchQueue.append([searchRow, searchCol])
                        landscape[searchRow][searchCol] = None
                        currentSum += 1
    return currentSum


testLandscape = [[0,1,1,0,1],
                 [1,1,0,1,1],
                 [0,1,0,1,0],
                 [0,1,0,1,0],
                 [1,0,1,1,0]]

print(countPonds(testLandscape))
