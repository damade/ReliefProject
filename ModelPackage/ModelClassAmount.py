class ReliefModel():
    def __init__(self, name, age, location, householdSize, employmentStatus):
        self.name = name
        self.age = age
        self.location = location
        self.householdSize = householdSize
        self.employmentStatus = employmentStatus
        self.criteriaDetail = []

    def gradeAge(self):
        personalAge = self.age
        if (55 < personalAge < 90):
            self.criteriaDetail += ["Lower Class"]
        elif (18 < personalAge < 45):
            self.criteriaDetail += ["Middle Class"]
        elif (0 < personalAge <= 18):
            self.criteriaDetail += ["Higher Class"]
        else:
            self.criteriaDetail += ["Not Eligible"]

    def gradeEmploymentStatus(self):
        personalES = self.employmentStatus
        if (personalES == "unemployed"):
            self.criteriaDetail += [10000]
        elif (personalES == "self-employed" or personalES == "low-income"):
            self.criteriaDetail += [8000]
        elif (personalES == "student" or personalES == "employed"):
            self.criteriaDetail += [5000]
        else:
            self.criteriaDetail += [0]

    def gradeHouseHoldSize(self):
        personalHS = self.householdSize
        if (personalHS > 8):
            self.criteriaDetail += [10000]
        elif (3 < personalHS <= 7):
            self.criteriaDetail += [8000]
        elif (0 < personalHS <= 3):
            self.criteriaDetail += [5000]
        else:
            self.criteriaDetail += [0]

    def gradeLocation(self):
        personalLocation = self.location
        if (personalLocation == "rural"):
            self.criteriaDetail += [10000]
        elif (personalLocation == "metropolitan"):
            self.criteriaDetail += [8000]
        elif (personalLocation == "urban"):
            self.criteriaDetail += [5000]
        else:
            self.criteriaDetail += [0]

    def gradeTheParameters(self):
        self.gradeAge()
        self.gradeLocation()
        self.gradeHouseHoldSize()
        self.gradeEmploymentStatus()

    def printGradeResult(self):
        self.gradeTheParameters()
        print(self.criteriaDetail)

    def chooseClass(self):
        self.gradeTheParameters()
        theList = self.criteriaDetail
        count = 0
        for i in theList:
            count += i
            avg = count / 4
        print(f"{self.name}, you are qualified for the #{avg}")
