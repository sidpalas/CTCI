# write a function that checks if someone has won at tic tac toe

# representing board as list of lists with None, "X", and "O":
# [[,,],[,,],[,,]]

def checkTicTacToe(board):
    # check rows
    for i in range(0,3):
        lineResult = checkLine(board[i])
        if bool(lineResult):
            return lineResult
    # check columns
    for i in range(0,3):
        colResult = checkLine([board[0][i], board[1][i], board[2][i]])
        if bool(colResult):
            return colResult
    # check diagonal 1
    diag1Result = checkLine([board[0][0],board[1][1],board[2][2]])
    if bool(diag1Result):
        return diag1Result
    #check diagonal 2
    diag2Result = checkLine([board[0][2],board[1][1],board[2][0]])
    if bool(diag2Result):
        return diag2Result

    #no winning lines found
    return False

def checkLine(line):
    if None in line:
        return False
    lineSet = set(line)
    if len(lineSet)==1: #all values are equal
        return line[0]
    return False

testBoard1 = [[None, None, None], [None, None, None], [None, None, None]]
testBoard2 = [['X','X','X'], [None, None, None], [None, None, None]]
testBoard3 = [[None, 'O', None], [None, 'O', None], [None, 'O', None]]
testBoard4 = [[None, None, 'O'], [None, 'O', None], ['O', None, None]]
testBoard5 = [[None, None, None], ['X', 'O', 'X'], [None, None, None]]

print(checkTicTacToe(testBoard1)) #False
print(checkTicTacToe(testBoard2)) #X
print(checkTicTacToe(testBoard3)) #O
print(checkTicTacToe(testBoard4)) #O
print(checkTicTacToe(testBoard5)) #False
