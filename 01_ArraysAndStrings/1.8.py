def matrixZeroer(matrix):
    M = len(matrix)
    N = len(matrix[0])
    #didnt need to be storing the full matrix... instead just the row and columns
    #need to be zeroed... this saves storage space (doesnt speed up algorithm though)
    rowNulls = [False]*M
    colNulls = [False]*N
    #we could even get rid of this extra storage by using the first row and column as 
    #a these storage vectors as described in solution.  Seems overly complex unless
    #storage is really an issue.
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                rowNulls[i] = True
                colNulls[j] = True
    #dont need to loop through entire matrix... only need to touch the rows/columns specified
    #depending on how many zeros are expected this approach could be faster or slower
    for i in range(M):
        for j in range(N):
            if rowNulls[i] or colNulls[j]:
                matrix[i][j] = 0
    return matrix

print matrixZeroer([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print matrixZeroer([[1,2,3],[4,0,6],[7,8,9],[10,11,0]])
