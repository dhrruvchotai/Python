class Demo:

    # def m1(self):
    #     print(f"Name is {self.name}")
    
    @property
    def name1(self):
       return f"{self.fname} {self.lname}"
    
    @name1.setter
    def name1(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

obj = Demo()
obj.name1 = "Dhruv Chotai" #Call the name setter 

print(obj.name1)
print(obj.fname)
print(obj.lname)