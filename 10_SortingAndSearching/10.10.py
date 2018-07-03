class streamTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.tally = 1

def track(root, intIn):
    if root.val == intIn:
        root.tally += 1
    elif root.val > intIn:
        root.tally += 1
        if root.left:
            track(root.left, intIn)
        else:
            root.left = streamTreeNode(intIn)
    else: # root.val < intIn
        if root.right:
            track(root.right, intIn)
        else:
            root.right = streamTreeNode(intIn)

def getRankOfNumber(root, intIn):
    atLeaf = False
    cumulativeTally = 0
    while not atLeaf:
        if root.val == intIn:
            return root.tally + cumulativeTally
        elif root.val > intIn and root.left:
            root = root.left
        elif root.val < intIn and root.right:
            cumulativeTally += root.tally
            root = root.right
        else:
            if root.val < intIn:
                cumulativeTally += root.tally
            atLeaf = True
    return cumulativeTally

testRoot = streamTreeNode(5)

for val in [1,4,4,5,9,7,13,3]:
    track(testRoot,val)

for i in range(0,15):
    print(i, "-->", getRankOfNumber(testRoot, i))
