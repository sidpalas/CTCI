#assumes other methods have been implemented
#and that node has method getSize() which returns size of tree under testNode
#this value would be updated in the insert() and delete() methods

from random import randint

def returnRandomNode(root):
    if root.getLeft():
        sizeLeft = root.getLeft().getSize()
    else:
        sizeLeft = 0
    if root.getRight():
        sizeRight = root.getRight().getSize()
    else:
        sizeRight = 0
    rand = randint(0,root.getSize()-1)
    if rand == 0:
        return root
    elif rand > 0 <= sizeLeft:
        return returnRandomNode(root.getLeft())
    else: #rand > sizeLeft
        return returnRandomNode(root.getRight())
