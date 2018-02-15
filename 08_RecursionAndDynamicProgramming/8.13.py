from random import random

class Box(object):
    id = 0
    def __init__(self,w,h,d):
        self.id = Box.id
        Box.id += 1
        self.w = w
        self.h = h
        self.d = d

    def __str__(self):
        return "id:" + str(self.id) + ", h:" + str(self.h) + ", w:" + str(self.w) + ", d:" + str(self.d)

def sortBoxes( boxes ):
    wSort = sorted(boxes, key = lambda box: box.w)
    hSort = sorted(boxes, key = lambda box: box.h)
    dSort = sorted(boxes, key = lambda box: box.d)
    return (wSort, hSort, dSort)

#default values for prev dimensions assumes boxes will all be < 1 in all dimensions
def stackBoxes( hSortedBoxes, prevW = 1, prevH = 1, prevD = 1, seq = '', typeStr = '' ):
    # print(typeStr)
    if not hSortedBoxes:
        print("valid stack:", seq)
        return 0
    elif len(hSortedBoxes) == 1:
        #must check final box agains previous box size... was incorrectly stacking the final box
        #because of this base case sometimes
        if hSortedBoxes[0].w < prevW and hSortedBoxes[0].h < prevH and hSortedBoxes[0].d < prevD:
            print("valid stack:", seq + str(hSortedBoxes[0].id))
            return hSortedBoxes[0].h
        else:
            print("valid stack:", seq)
            return 0
    else:
        currentID = hSortedBoxes[-1].id
        currentH = hSortedBoxes[-1].h
        currentW = hSortedBoxes[-1].w
        currentD = hSortedBoxes[-1].d
        tempSort = []
        for box in hSortedBoxes[1:]:
            if box.w < currentW and box.d < currentD:
                tempSort.append(box)
        #if no smaller box found, tempSort will be empty and the next call of stackBoxes will return zero
        heightWith = currentH + stackBoxes(tempSort, currentW, currentH, currentD, seq + str(currentID), 'with')
        heightWithout = stackBoxes(hSortedBoxes[0:-1], prevW, prevH, prevD, seq, 'without')
        return max(heightWith, heightWithout)

testBoxes = []
for i in range(0,4):
    testBoxes.append(Box(random(),random(),random()))

# testBoxes = [Box(0.8944137442257065, 0.3221709438795636, 0.9953864718991), \
#              Box(0.10202759189996946, 0.6193987845159934, 0.44857036868345423), \
#              Box(0.47890388707144593, 0.734354088583807, 0.8589498270470706), \
#              Box(0.7688224403363461, 0.16707765711354017, 0.9478028649549562)]

wSort, hSort, dSort = sortBoxes( testBoxes )

for box in hSort:
    print(box)

print(stackBoxes(hSort))
