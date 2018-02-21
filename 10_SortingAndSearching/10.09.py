def findDiagonalPair(gridIn, searchVal):
    numRows = len(gridIn)
    numCols = len(gridIn[0])
    rowOffset = 0
    colOffset = 0
    if numRows > numCols:
        rowOffset = numRows - numCols
    elif numRows < numCols:
        colOffset = numCols - numRows

    low = 0
    high = min(numRows - 1, numCols - 1)
    mid = (low + high) // 2

    while low < high:
        compareVal = gridIn[mid + rowOffset][mid + colOffset]
        if compareVal == searchVal:
            return mid + rowOffset, mid + colOffset
        elif compareVal > searchVal:
            high = mid - 1
        else: #compareVal < searchVal:
            low = mid + 1
        mid = (low + high) // 2

    return mid + rowOffset, mid + colOffset

def binarySearch(arrayIn, searchVal):
    if not arrayIn:
        return -1
    low = 0
    high = len(arrayIn) - 1
    mid = (low + high) // 2
    while low < high:
        if arrayIn[mid] == searchVal:
            return mid
        elif arrayIn[mid] > searchVal:
            high = mid - 1
        else:
            low = mid + 1
        mid = (low + high) // 2

    if arrayIn[mid] == searchVal:
        return mid
    else:
        return -1

def searchGrid(gridIn, searchVal):
    (diagRow, diagCol) = findDiagonalPair(gridIn, searchVal)
    compareVal = gridIn[diagRow][diagCol]

    if compareVal < searchVal: #ensure you are starting above searchVal
        if diagRow == len(gridIn) - 1 or diagCol == len(gridIn[0]) - 1:
            return -1, -1 #already as high as you can go
        diagRow += 1
        diagCol += 1
        compareVal = gridIn[diagRow][diagCol]

    if compareVal == searchVal:
        return diagRow, diagCol
    elif compareVal > searchVal:
        #search this column
        colSearch = binarySearch(gridIn[diagRow][0:diagCol], searchVal)
        if colSearch >= 0:
            return diagRow, colSearch
        #search this row
        rowSearch = binarySearch([row[diagCol] for row in gridIn[0:diagRow]], searchVal)
        # print([row[diagCol] for row in gridIn[0:diagRow]], rowSearch)
        if rowSearch >= 0:
            return rowSearch, diagCol

    return -1, -1 #searchVal not found...


testGrid = [list(range(1,7)),\
            list(range(2,8)),\
            list(range(3,9)),\
            list(range(4,10))]

testGrid[1][5] = 8
testGrid[2][5] = 9
testGrid[3][5] = 10

#by not drawing a good test grid initially I fooled myself into thinking element
#[1][5] can't be greater than [2][4]... this is not true. Instead should have
#recursively searched the top right and bottom right subgrids recursively 

for row in testGrid:
    print(row)

for i in range(0,11):
    print(searchGrid(testGrid, i))
