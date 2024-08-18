class Engineer:

    sal = 1000000

    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"The name is {self.name} and salary is {self.sal}")

class Worker(Engineer):
    
    sal = 2000

    # def __init__(self, name,sal):
    #   # super().__init__(name)You can call parent constructor like this.
        # self.sal = sal

            #or 

    #     self.sal = sal
    #     self.name = name

     
#This is inheritance 
worker1 = Worker("worker1")  #If you dont write constructor for worker then it is inherited from parent.
eng1 = Engineer("harry")

#as woker is inherited from engineer class it can use show method also.
worker1.show()
eng1.show()