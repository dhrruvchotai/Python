class Class1:
    def __init__(self):
        print("Hello from method1")

class Class2():
    a = 10
    def __init__(self):
        print("Hello from method2")

class Class3(Class1,Class2): 
    def __init__(self):
        super().__init__()#This will call constructor of parent(In this case Class1 because of multiple inheritance.)
        print("Hello from method3")
        print(f"and value of a from Class2 is {super().a}") #If ypu want to access any var of parent same way uh can access methods
        
 
obj = Class3()

