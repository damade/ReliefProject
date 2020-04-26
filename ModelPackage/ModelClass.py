class ReliefModel():
    def __init__(self,name, age, location, householdSize, employmentStatus):
        self.name = name
        self.age = age
        self.location = location
        self.householdSize = householdSize
        self.employmentStatus = employmentStatus
        self.criteriaDetail = []

    def gradeAge(self):
        personalAge = self.age
        if (50 <= personalAge <= 100):
            self.criteriaDetail += ["Lower Class"]
        elif (34 <= personalAge <= 49):
            self.criteriaDetail += ["Middle Class"]
        elif (18 <= personalAge <= 33):
            self.criteriaDetail += ["Higher Class"]
        else:
            self.criteriaDetail += ["Not Eligible"]

    def gradeEmploymentStatus(self):
        personalES = self.employmentStatus
        if (personalES == "unemployed"):
            self.criteriaDetail += ["Lower Class"]
        elif (personalES == "self-employed"):
            self.criteriaDetail += ["Middle Class"]
        elif (personalES == "student"):
            self.criteriaDetail += ["Higher Class"]
        else:
            self.criteriaDetail += ["Not Eligible"]

    def gradeHouseHoldSize(self):
        personalHS = self.householdSize
        if (personalHS >= 8):
            self.criteriaDetail += ["Lower Class"]
        elif (3 < personalHS <= 7):
            self.criteriaDetail += ["Middle Class"]
        elif (0 < personalHS <= 3):
            self.criteriaDetail += ["Higher Class"]
        else:
            self.criteriaDetail += ["Not Eligible"]

    def gradeLocation(self):
        personalLocation = self.location
        if (personalLocation == "rural"):
            self.criteriaDetail += ["Lower Class"]
        elif (personalLocation == "metropolitan"):
            self.criteriaDetail += ["Middle Class"]
        elif (personalLocation == "urban"):
            self.criteriaDetail += ["Higher Class"]
        else:
            self.criteriaDetail += ["Not Eligible"]

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
        if "Not Eligible" in theList:
            print(f"{self.name}, you are not Eligible")
        else:
            count = {}
            for i in theList:
                count.setdefault(i, 0)
                count[i] = count[i] + 1
            sorted(count.values())
            newArr = []
            for v in sorted(count.items()):
                newArr += [v]
            theLead = newArr[len(newArr) - 1][0]
            amountDict = {"Higher Class": 5000, "Middle Class": 8000, "Lower Class": 10000}
            print(f"{self.name}, you are qualified for the #{amountDict[theLead]:,}")
