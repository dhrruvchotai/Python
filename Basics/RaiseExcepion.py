#1
a = -10

if(a < 0):
    raise Exception("The number cannot be less than 0.")
else:
    print("Number is okey!!")

#2
a = 10
b = 0

if(b == 0):
    raise ZeroDivisionError("Number a can't be divided by zero.")
else:
    print(a/b)