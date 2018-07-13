colorMap = {'R':0, 'G':1, 'B':2, 'Y':3}

def checkHits(board, guess):
    #preprocess board
    colorCounts = [0,0,0,0]
    for color in board:
        colorIdx = colorMap[color]
        colorCounts[colorIdx] += 1

    #find hits -- this could have been combined with the preprocess step
    hitCount = 0
    for i, color in enumerate(guess):
        if board[i] == guess[i]:
            hitCount += 1
            colorIdx = colorMap[color]
            colorCounts[colorIdx] -= 1 #dont allow hits to match with other psuedo hits

    #find pseudo-hits
    psuedoHitCount = 0
    for color in guess:
        colorIdx = colorMap[color]
        if colorCounts[colorIdx]>0:
            psuedoHitCount += 1
            colorCounts[colorIdx] -= 1

    return (hitCount, psuedoHitCount)


print(checkHits(['R', 'G', 'B', 'Y'],['G', 'G', 'R', 'R']))

print(checkHits(['R', 'G', 'B', 'Y'],['R', 'G', 'B', 'Y']))

print(checkHits(['R', 'G', 'B', 'Y'],['R', 'G', 'B', 'Y'][::-1]))
