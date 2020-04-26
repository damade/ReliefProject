from ModelPackage.ModelClass import ReliefModel


try:
    '''firstName = input("What is your name: ")
    age = int(input("What is your name: "))
    location = input("Choose your area type: ")
    householdSize = int(input("What is your household size: "))
    employmentStatus = input("What is your employment status: ")
    individual = ReliefModel(age, location, householdSize, employmentStatus)'''
    individual = ReliefModel("dammy", 18, "metropolitan",2,"self-employed")
    #individual.printGradeResult()
    individual.chooseClass()
except ValueError:
    print("Please enter valid details")
