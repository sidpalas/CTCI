class Square:
    def __init__(self, bottomLeft, topRight):
        self.bottomLeft = bottomLeft
        self.topRight = topRight

    def getCenter(self):
        x = (self.bottomLeft[0] + self.topRight[0])/2
        y = (self.bottomLeft[1] + self.topRight[1])/2
        return (x,y)

def lineFromPoints(point1, point2):
    if point2[0] != point1[0]: #vertical line
        slope = (point2[1] - point1[1])/(point2[0] - point1[0])
        intercept = point1[1] - slope*point1[0]
        return "y = " + str(slope) + "x + " + str(intercept)
    else:
        return "x = " + str(point1[0]) #vertical line

def bisectSquares(square1, square2):
    center1 = square1.getCenter()
    center2 = square2.getCenter()

    return lineFromPoints(center1, center2)

testSquare1 = Square([-1,-1],[1,1])
testSquare2 = testSquare1
testSquare3 = Square([1,-1],[3,1])
testSquare4 = Square([1,1],[2,2])
testSquare5 = Square([3,-3],[5,-1])

print(bisectSquares(testSquare1, testSquare2)) #any line passing thorugh origin
print(bisectSquares(testSquare1, testSquare3)) #y = 0
print(bisectSquares(testSquare1, testSquare4)) #y = x
print(bisectSquares(testSquare3, testSquare5)) #y = -x + 2
