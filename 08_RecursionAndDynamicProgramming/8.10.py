def getAdjacentIdx(idr, idc):
    return [[idr, idc-1],[idr+1, idc],[idr, idc+1],[idr-1,idc]]

#I implemented this like a breadth first search (non-recursive)
#It could have been implemented with depth first search recursively...
def generateIndices(arrayIn, startPoint, newColor, cache = dict()):
    row = startPoint[0]
    column = startPoint[1]
    originalColor = arrayIn[row][column]
    queue = [startPoint]
    cache[str(startPoint)] = True
    while queue:
        currentPoint = queue.pop() #should use collections.deque rather than use list as queue
        currentRow = currentPoint[0]
        currentColumn = currentPoint[1]
        adjacents = getAdjacentIdx(currentRow,currentColumn)
        for point in adjacents:
            tempRow = point[0]
            tempColumn = point[1]
            if tempRow >= 0 and tempRow < len(arrayIn) and tempColumn >= 0 and tempColumn < len(arrayIn[0]): #point is in the array
                if not str(point) in cache:
                    if originalColor == arrayIn[tempRow][tempColumn]:
                        queue.insert(0, point)
                        cache[str(point)] = True
    return cache

def paintFill(arrayIn, startPoint, newColor):
    indices = generateIndices(arrayIn, startPoint, newColor)
    for key in indices:
        temp = list(key)
        arrayIn[int(temp[1])][int(temp[4])] = newColor #this will break for arrays larger than 9... would have be smarter with what I use as the hashtable key...
    return arrayIn

testArray = [[0,0,1,0,0], \
             [0,0,0,0,0], \
             [0,1,1,0,0], \
             [0,0,1,0,0], \
             [0,0,2,0,0]]
for row in testArray:
    print(row)

newArray = paintFill(testArray, [0,2], 1)
for row in newArray:
    print(row)
