#simple function
print("Func 1 : \n")
def printSomething():
    print("Hello")
printSomething() #function call
print("\n")


#parametrized function
print("Func 2 : \n")
def sqaure(num):
    return num * num

for i in range (1,6):
    print(sqaure(i),end=" ")

print("\n")

#function with default param
print("Func 3 : \n")
def squareDeault(num,fact = 3): #by default it will take fact = 3 if you not pass
    #if uh passed fact = anynumber then it will consider that given num.
    return num * fact

for i in range(1,11):
    print(squareDeault(i,4),end=" ")