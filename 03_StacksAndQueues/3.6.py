from collections import deque
import random

class AnimalShelterQueue(object):
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.q2CatsOrDogs = None

    def enqueue(self, data):
        self.q1.append(data)

    def dequeueAny(self):
        if len(self.q2)>0:
            if len(self.q2)==1:
                self.q2CatsOrDogs = None
            return self.q2.popleft()
        else:
            return self.q1.popleft()

    def dequeueSpecific(self,animalType):
        if self.q2CatsOrDogs == animalType:
            if len(self.q2)==1:
                self.q2CatsOrDogs = None
            return self.q2.popleft()
        else:
            while (self.q1[0].find(animalType) == -1) and len(self.q1)>1:
                self.q2.append(self.q1.popleft())
                if animalType == "C":
                    self.q2CatsOrDogs = "D"
                if animalType == "D":
                    self.q2CatsOrDogs = "C"
            if len(self.q1)>0:
                return self.q1.popleft()
        #would also want to have error handling to deal with when there are no
        #more of the desired animal available

testAnimalShelter = AnimalShelterQueue()
for i in ["C1","C2","D1","C3","C4","D2","D3"]:
    testAnimalShelter.enqueue(i)

print testAnimalShelter.q2, " | ", testAnimalShelter.q1
print testAnimalShelter.dequeueSpecific("D")
print testAnimalShelter.q2, " | ", testAnimalShelter.q1
print testAnimalShelter.dequeueSpecific("D")
print testAnimalShelter.q2, " | ", testAnimalShelter.q1
print testAnimalShelter.dequeueAny()
print testAnimalShelter.q2, " | ", testAnimalShelter.q1
print testAnimalShelter.dequeueSpecific("C")
print testAnimalShelter.q2, " | ", testAnimalShelter.q1
print testAnimalShelter.dequeueSpecific("D")
