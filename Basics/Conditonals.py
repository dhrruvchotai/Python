num = (int)(input("Enter any number : "))

if(num > 0):
    print("Num is positive.")
elif(num == 0):
    print("Num is zero.")
else:
    print("Num is negative.")

num1 = (int)(input("Enter number 1 : "))
num2 = (int)(input("Enter number 2 : "))
num3 = (int)(input("Enter number 3 : "))

if(num1 > num2 and num1 > num3):
    print("Num 1 : ",num1,"is greater.")
elif(num2 > num1 and num2 > num3):
    print("Num 2 : ",num2,"is greater.")
else:
    print("Num 3 : ",num3,"is greater.")