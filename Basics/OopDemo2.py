class Employee:
    company = "SAMSUNG"

    def __init__(self,name,id):
        self.name = name
        self.id = id

    def getDetails(self):
        print(f"Company : {self.company}, Name : {self.name},  Id : {self.id}")
    
    @staticmethod #Make any method static using @staticmethod keyword!!
    def greet():
        print("Hello Employees")

emp1 = Employee("DHRUV",19)
emp2 = Employee("PARTH",21)

emp1.getDetails()
Employee.getDetails(emp1)#This is same as upper line.
emp2.getDetails()

Employee.greet() #Sometimes we want to call method without creating an object so we can do it like this by using class name.


