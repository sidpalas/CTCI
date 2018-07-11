class Line:
    def __init__(self, startX,startY,endX, endY):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.minX = min(self.startX, self.endX)
        self.maxX = max(self.startX, self.endX)
        self.minY = min(self.startY, self.endY)
        self.maxY = max(self.startY, self.endY)

    def calcSlope(self):
        if (self.maxX - self.minX) != 0:
            slope = (self.endY - self.startY)/(self.endX - self.startX)
        else:
            raise ValueError
        return slope

    def calcYIntercept(self):
        slope = self.calcSlope()
        intercept = self.startY - slope * self.startX
        return intercept


def computeIntersection(line1, line2):

    slope1 = line1.calcSlope()
    intercept1 = line1.calcYIntercept()
    slope2 = line2.calcSlope()
    intercept2 = line2.calcYIntercept()

    if slope1 == slope2:
        if intercept1 == intercept2: #co-linear
            if isBetween(line1.minX, line2.minX, line1.maxX):
                xIntersection = line2.minX
                yIntersection = slope2 * line2.minX + intercept2
            elif isBetween(line1.minX, line2.maxX, line1.maxX):
                xIntersection = line2.maxX
                yIntersection = slope2 * line2.maxX + intercept2
            elif isBetween(line2.minX, line1.minX, line2.maxX):
                xIntersection = line1.minX
                yIntersection = slope1 * line1.minX + intercept1
            elif isBetween(line2.minX, line1.maxX, line2.maxX):
                xIntersection = line1.maxX
                yIntersection = slope1 * line1.maxX + intercept1
            else: #no endpoint falls within other lines range (no overlap)
                return "colinear but no overlap"
            return (xIntersection, yIntersection)

        else: #Lines are parallel and will never intersect
            return "parallel with no intersection"
    else: #slopes not equal so lines will eventually intersect
        xIntersection = (intercept2 - intercept1)/(slope1 - slope2)
        yIntersection = slope1 * xIntersection + intercept1

        if isBetween(line1.minX, xIntersection, line1.maxX) \
            and isBetween(line2.minX, xIntersection, line2.maxX):
            return (xIntersection, yIntersection)
        else: #intersection occurs outside of at least one line
            return "intersection not on lines"

def isBetween(start, val, end):
    return min(start,end) <= val <= max(start,end)

testLine1 = Line(-1, -1, 1,  1)
testLine2 = Line(-1,  1, 1, -1)
testLine3 = Line(-1,  1, 1,  1)
testLine4 = Line(-1, -1+.2, 1,  1+.2)
testLine5 = Line(2, 2, 3, 3)
testLine6 = Line(-1,  1, -.5, .5)
testLine7 = Line(1, -1, -1, 1)
testLine8 = Line(-2, -2, 2,  2)

print(computeIntersection(testLine1, testLine2)) #should be (0,0)
print(computeIntersection(testLine1, testLine3)) #should be (1,1)
print(computeIntersection(testLine1, testLine4)) #should be False (parallel and offset)
print(computeIntersection(testLine1, testLine5)) #should be False (colinear but not overlapping)
print(computeIntersection(testLine1, testLine6)) #should be False (would intersect, but not in correct range)
print(computeIntersection(testLine1, testLine7)) #should be (0,0) (same as first case, but specified backwards)
print(computeIntersection(testLine1, testLine8)) #should be anything in line1
