def matrixZeroer(matrix):
    M = len(matrix)
    N = len(matrix[0])
    zeroMap = [[1]*N for i in range(M)]
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                for k in range(M):
                    zeroMap[k][j] = 0
                for l in range(N):
                    zeroMap[i][l] = 0
    for i in range(M):
        for j in range(N):
            matrix[i][j] = matrix[i][j] * zeroMap[i][j]
    return matrix

print matrixZeroer([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print matrixZeroer([[1,2,3],[4,0,6],[7,8,9],[10,11,0]])
