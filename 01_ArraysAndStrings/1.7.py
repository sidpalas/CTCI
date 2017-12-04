def rotateClockwise(image):
    #should add checks to see if image is non-zero sized and square
    N = len(image[0])
    outputImage = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            outputImage[j][N-(i+1)] = image[i][j]
    return outputImage

#to do the rotation in place, you would work inwards from the outer later, also
#you would need to temporarily store off the starting layer as it gets replaced

a = rotateClockwise([[1,2,3],[4,5,6],[7,8,9]])
b = rotateClockwise(a)
c = rotateClockwise(b)
d = rotateClockwise(c)

print a
print b
print c
print d
