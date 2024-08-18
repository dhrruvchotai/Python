class Employee:
    language = "Python"
    salary = "11000000"
    
    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod #To make any method static write this.
    def greet():
        print("Hello Employees.")


emp1 = Employee()
print(f"language : {emp1.language}, salary : {emp1.salary}")
emp1.name = "abc"
print(f"name : {emp1.name}, language : {emp1.language}, salary : {emp1.salary}")

emp2 = Employee()
emp2.language = "Java" #Java is obj attribute so it overwrites Python..
print(emp2.language,emp2.salary)

#Note that here name is an object attribute and sal and language are class attributes.

Employee.getInfo(emp1) #or you can write emp1.getInfo()
Employee.getInfo(emp2)

Employee.greet()

