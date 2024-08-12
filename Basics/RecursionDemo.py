#Factorial 
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)

for i in range (1,6):
    print(f"factorial of {i} is : {factorial(i)}")

#Sum of first n
def sum(num):
    if num == 1:
        return 1
    return sum(num - 1) + num

print(sum(5))

#Pattern using recursion
def pattern(num):
    if(num == 0):
       return
    print("*"*num)
    pattern(num-1)

pattern(3)