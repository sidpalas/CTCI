def printKMoves(k):
    board = dict()
    position = [0,0]
    topLeft = [0,0]
    bottomRight = [0,0]
    heading = 'right'
    for i in range(k):
        # print(position, heading, topLeft, bottomRight)
        [position, heading, board] = moveAnt(position, heading, board)
        #move bounds
        if position[0] < topLeft[0]:
            topLeft[0] = position[0]
        if position[0] > bottomRight[0]:
            bottomRight[0] = position[0]
        if position[1] < topLeft[1]:
            topLeft[1] = position[1]
        if position[1] > bottomRight[1]:
            bottomRight[1] = position[1]

    for i in range(topLeft[0],bottomRight[0]+1):
        row = []
        for j in range(topLeft[1],bottomRight[1]+1):
            if (i,j) in board:
                row.append(board[(i,j)])
            else:
                row.append('w')
        print(row)

def moveAnt(position, heading, board):
    if tuple(position) in board:
        currentColor = board[tuple(position)]
    else:
        currentColor = 'w' #if it hasn't been visited it is white
    if currentColor == 'w':
        heading = turnClock(heading)
    else:
        heading = turnCounterClock(heading)

    flippedColor = 'b' if currentColor == 'w' else 'w'

    board[tuple(position)] = flippedColor

    if heading == 'right':
        position[1] += 1
    elif heading == 'down':
        position[0] += 1
    elif heading == 'left':
        position[1] -= 1
    else: #heading == 'up'
        position[0] -= 1

    return position, heading, board


def turnClock(heading):
    currentIdx = headings.index(heading)
    nextIdx = (currentIdx + 1)%4
    return headings[nextIdx]

def turnCounterClock(heading):
    currentIdx = headings.index(heading)
    nextIdx = (currentIdx - 1)%4
    return headings[nextIdx]

headings = ('right', 'down', 'left', 'up')

for i in range(100a):
    printKMoves(i)
    print('\n######\n')
