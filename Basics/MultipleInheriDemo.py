class Class1:
    def method1(self):
        print("Hello from method1")

class Class2:
    def method2(self):
        print("Hello from method2")

class Class3(Class1,Class2): 
    def method3(self):
        print("Hello from method3")

obj = Class3()

obj.method1()
obj.method2()
obj.method3()