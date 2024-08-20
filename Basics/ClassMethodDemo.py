class Demo:
    a = 10
    def method1(self):
        print(f"The value of class variable a from method1 : {self.a}")
    
    @classmethod
    def method2(self):
        print(f"The value of class variable a from method2 : {self.a}")

obj = Demo()
obj.method1() #Here it will print a = 10 which is ok.

obj.a = 20
obj.method1()#but here it will print a = 20 but we want value of class attribute which is a= 10 so
#Make the method class method

obj.a = 30
obj.method2() #after changing the value of a it will give the value of class val which is 10(Class Method).
