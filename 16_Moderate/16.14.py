import sys
import math

eps = 0.0001

def findBestLine(pointsList):
    lineDict = dict()
    for i in range(len(pointsList)):
        for j in range(len(pointsList)-1-i):
            line = findSlopeAndIntercept(pointsList[i], pointsList[j+i])
            flooredSlope = floorToNearestEspilon(line(0))
            if line[3] = True:
                slope = 'inf'

            if flooredSlope in lineDict:
                lineList = lineDict[flooredSlope]
                lineDict[flooredSlope] = lineList + [line]
            else:
                lineDict[line] = [line]

    bestLine = None
    bestCount = 0
    for line in lineDict:
        count = countEquivalentLines(line, lineDict)
        if count > bestCount:
            bestLine = line
            bestCount = count

    return bestLine

def countEquivalentLines(line, lineDict):
    key = floorToNearestEspilon(line(0))
    count = countEquivalentParallelLines(lineDict[key])
    count += countEquivalentParallelLines(lineDict[key+eps])
    count += countEquivalentParallelLines(lineDict[key-eps])
    return count

def countEquivalentParallelLines(line, lines):
    count = -1 # line will for sure be equivalent to itself so subtract 1
    for parallelLine in lines:
        if abs(line[0] - parallelLine[0])>eps
            and abs(line[1] - parallelLine[0])>eps
            and line[3] == parallelLine[3]:
            count += 1
    return count

def floorToNearestEspilon(val):
    epsMult = math.floor(val/eps)
    return epsMult * eps

def findSlopeAndIntercept(point1, point2):
    if abs(point2[0] - point1[0]) > eps: #non-vertical line
        slope = (point2[1] - point1[1])/(point2[0] - point1[0])
        intercept = point1[1] - slope*point1[0]
        verticalFlag = False
        return (slope, intercept, verticalFlag)
    else:
        return (0, point1[0], True) #vertical line with x-intercept
