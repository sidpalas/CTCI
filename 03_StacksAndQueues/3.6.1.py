from collections import deque

class Animal(object):
    def __init__(self, animalType, timestamp):
        self.animalType = animalType
        self.timestamp = timestamp

class AnimalShelterQueue(object):
    def __init__(self):
        self.cats = deque()
        self.dogs = deque()

    def enqueue(self, animal):
        if animal.animalType == "C":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueAny(self):
        if self.cats[-1].timestamp < self.dogs[-1].timestamp:
            return self.cats.popleft()
        else:
            return self.dogs.popleft()

    def dequeueCat(self):
        return self.cats.popleft()

    def dequeueDog(self):
        return self.dogs.popleft()

testAnimalShelter = AnimalShelterQueue()
count = 0
for i in ["C","C","D","C","C","D","D"]:
    testAnimalShelter.enqueue(Animal(i,count))
    count += 1

animalOut = testAnimalShelter.dequeueDog()
print animalOut.animalType, animalOut.timestamp
animalOut = testAnimalShelter.dequeueDog()
print animalOut.animalType, animalOut.timestamp
animalOut = testAnimalShelter.dequeueAny()
print animalOut.animalType, animalOut.timestamp
animalOut = testAnimalShelter.dequeueCat()
print animalOut.animalType, animalOut.timestamp
animalOut = testAnimalShelter.dequeueDog()
print animalOut.animalType, animalOut.timestamp
