class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self,num):
        return self.n + num.n
    def __mul__(self,num):
        return self.n * num.n
    def __sub__(num1,num2): #param name doesn't matter self or num1 or any.
        return num1.n - num2.n
    def __truediv__(num1,num2):
        return num1.n / num2.n
    def __floordiv__(self,num2):
        return self.n // num2.n
    
num1 = Number(1)
num2 = Number(2)


print(f"Sum is :  {num1+num2}")
print(f"Substraction is :  {num1-num2}")
print(f"Multiplication is : {num1 * num2}")
print(f"True division is : {num1/num2}")
print(f"Floor division is : {num1//num2}")