class LRUCache:
    def __init__(self,size):
        self.primaryStore = dict()
        self.editOrder = [None]*size

    def insert(self,key,value):
        removalKey = self.editOrder.pop(0)
        if removalKey != None:
            del self.primaryStore[removalKey]
        self.editOrder.append(key)
        self.primaryStore[key] = value

    def retrieve(self,key):
        if key in self.primaryStore:
            self.editOrder.remove(key)
            self.editOrder.append(key)
            return self.primaryStore[key]
        else:
            return False

testCache = LRUCache(3)

for i in range(15):
    testCache.insert(i, str(i))

testCache.retrieve(12)
testCache.insert(15, '15')

print(testCache.primaryStore)
