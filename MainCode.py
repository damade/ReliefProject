from ModelPackage.ModelClass import ReliefModel
from ModelPackage.ModelClassAmount import ReliefModelAmount


try:
    name = input("What is your name: ")
    age = int(input("What is your name: "))
    location = input("Choose your area type: ")
    householdSize = int(input("What is your household size: "))
    employmentStatus = input("What is your employment status: ")
    individual = ReliefModel(name, age, location, householdSize, employmentStatus)
    person = ReliefModelAmount(name, age, location, householdSize, employmentStatus)
    #individual.printGradeResult()
    individual.chooseClass()
    person.chooseClass()
except ValueError:
    print("Please enter valid details")
