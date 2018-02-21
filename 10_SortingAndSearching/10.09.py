def gridBinarySearch(gridIn, searchVal, combinedRowOffset = 0, combinedColOffset = 0):
    if not gridIn:
        return None
    if not gridIn[0]:
        return None
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
        mid = max(((low + high) // 2),0)

    compareVal = gridIn[mid + rowOffset][mid + colOffset]
    if compareVal == searchVal:
        return mid + rowOffset + combinedRowOffset, mid + colOffset + combinedColOffset
    if compareVal < searchVal:
        if (mid + rowOffset) == len(gridIn) - 1 or (mid + colOffset) == len(gridIn[0]) - 1:
            return None #already as high as you can go
        rowOffset += 1
        colOffset += 1

    compareVal = gridIn[mid + rowOffset][mid + colOffset]

    topRightGrid = [row[(mid+ colOffset):] for row in gridIn[:(mid + rowOffset)]]
    bottomLeftGrid = [row[:(mid+ colOffset)] for row in gridIn[(mid + rowOffset):]]

    return gridBinarySearch(topRightGrid, searchVal, combinedRowOffset, combinedColOffset + (mid + colOffset)) \
            or gridBinarySearch(bottomLeftGrid, searchVal,  combinedRowOffset + (mid + rowOffset), combinedColOffset)

testGrid = [list(range(1,7)),\
            list(range(2,8)),\
            list(range(3,9)),\
            list(range(4,10))]

testGrid[0][0] = 0

testGrid[1][5] = 8
testGrid[2][5] = 9
testGrid[3][5] = 10



#by not drawing a good test grid initially I fooled myself into thinking element
#[1][5] can't be greater than [2][4]... this is not true. Instead should have
#recursively searched the top right and bottom right subgrids recursively

#fixed...

for row in testGrid:
    print(row)

for i in range(0,12):
    print(i, gridBinarySearch(testGrid, i))
