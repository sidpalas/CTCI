class Employee(object):
    def __init__(self, available = True, ability = 0):
        self.available = True
        self.ability = ability
        self.level = None

    def getAvailability(self):
        return self.available

    def setAvailability(self,available):
        self.available = available

    def getAbility(self):
        return self.ability

    def setAbility(self,ability):
        self.ability = ability

    def getLevel(self):
        return self.employeeLevel

    def takeCall(self,call):
        if self.getAvailability():
            if self.getAbility() >= call.getDifficulty():
                self.setAvailability(False)
                return "Call taken"
            else:
                return "Call too difficult"
        else:
            return "Employee unavailable"

class Director(Employee):
    def __init__(self, available = True, ability = 10):
        Employee.__init__(self, available, ability)
        self.employeeLevel = 2

class Manager(Employee):
    def __init__(self, available = True, ability = 7):
        Employee.__init__(self, available, ability)
        self.employeeLevel = 1

class Respondent(Employee):
    def __init__(self, available = True, ability = 4):
        Employee.__init__(self, available, ability)
        self.employeeLevel = 0

class Call(object):
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def getDifficulty(self):
        return self.difficulty
    #could add a duration attribute to know when to reset an employees
    #availability back to true after taking a call

class CallCenter(object):
    def __init__(self, directors, managers, respondents):
        self.directors = directors
        self.managers = managers
        self.respondents = respondents

    def escalateCall(self, call, currentLevel):
        if currentLevel < 3:
            return self.receiveCall(call, 0, currentLevel + 1)
        else:
            print('Director unavailable or call is too difficult even for the director!')
            return False

    def receiveCall(self, call, idx = 0, level = 0):
        if level == 0:
            group = self.respondents
        elif level == 1:
            group = self.managers
        else: #level == 2
            group = self.directors
        employee = group[idx]
        #could store the availability of the groups such that we only iterate over
        #those which are available each time a call is taken
        response = employee.takeCall(call)
        print(response)
        if response == "Call taken":
            print("Call Taken!!!!")
            return True
        elif response == "Employee unavailable":
            if employee == group[-1]:
                print ('Reached final employee in group, escalating')
                return self.escalateCall(call, level)
            else: #Try next employee at this level
                return self.receiveCall(call, idx + 1, level)
        else: #"Call too difficult"
                return self.escalateCall(call, level)

directors = []
for i in range(0,1):
    directors.append(Director())
managers = []
for i in range(0,2):
    managers.append(Manager())
respondents = []
for i in range(0,3):
    respondents.append(Respondent())

testCallCenter = CallCenter(directors, managers, respondents)

for i in range(0,2):
    print('Call: ', i, ' Difficulty: 0')
    print(testCallCenter.receiveCall(Call(0)))

for i in range(0,2):
    print('Call: ', i, ' Difficulty: 9')
    print(testCallCenter.receiveCall(Call(9)))
