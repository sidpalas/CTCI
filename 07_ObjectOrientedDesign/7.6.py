class PuzzlePiece(object):
    def __init__(self):
        self.edges = [None]*4

    def setEdge(self, edgeType, edgeID):
        self.edges[edgeType] = edgeID

    def getEdge(self, edgeType):
        return self.edges[edgeType]

class Jigsaw(object):
    def __init__(self, N = 2):
        self.N = N
        self.pieces = []
        self.present = []
        for i in range(0,N):
            row = []
            presentRow = []
            for j in range(0,N):
                row.append(PuzzlePiece())
                presentRow.append(False)
            self.pieces.append(row)
            self.present.append(presentRow)
        self.cutPieces()

    def cutPieces(self):
        edgeID = 0
        for i in range(0,self.N):
            for j in range(0,self.N):
                adjacents = self.getAdjacentIdx(i,j)
                for k in range(0,4):
                    coord = adjacents[k]
                    if coord[0] >= 0 and coord[0] < self.N and coord[1] >= 0 and coord[1] < self.N:
                        self.pieces[i][j].setEdge(k,edgeID)
                        self.pieces[coord[0]][coord[1]].setEdge(((k + 2) % 4), edgeID)
                        edgeID += 1 #change ID

    def addPiece(self, piece, idx, idy, orientation):
        #code to insert piece into present object or return false if trying to insert at wrong location

        #check if puzzle is complete
        self.isComplete

    def isComplete(self):
        return min(min(self.present))

    def getAdjacentIdx(self, idx, idy):
        return [[idx, idy-1],[idx+1, idy],[idx, idy+1],[idx-1,idy]]

class PuzzleCluster(object):
    def __init__(self):
        pass

    def __add__(self,otherCluster):
        #code to merge clusters
        pass

testPuzzle = Jigsaw(6)

#checking that adjacent edgeIDs match

print("[1,0], bottom: ", testPuzzle.pieces[1][0].getEdge(2))
print("[1,1], top: ", testPuzzle.pieces[1][1].getEdge(0))

print("[3,3], right : ", testPuzzle.pieces[3][3].getEdge(1))
print("[4,3], left: ", testPuzzle.pieces[4][3].getEdge(3))

#To solve puzzle we could sort into groups based on how many edges are not None (i.e. corners, edges, inner)
#Starting with a corner we could then fill in the rest by searching the appropriate groups.
#Solving in this way would eliminate the need for clusters but be less efficient for large puzzles.
