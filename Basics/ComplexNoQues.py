class Complex:
    
    def __init__(self,r,i):
        self.r = r
        self.i = i
    
    def __add__(c1,c2):
        return Complex(c1.r+c2.r,c1.i+c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
com1 = Complex(1,2)
com2 = Complex(2,1)

com3 = com1 + com2

print(f"Addtion of 2 complex nums are : {com3}")  #This gives output by default in string so you have to use __str__()

#Note that __str__ is called by default when you print any object of that class.
