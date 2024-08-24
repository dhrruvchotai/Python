try:
    a = int(input("Enter number a : "))
    b =  int(input("Enter number b : "))
    print(f"a/b = {a/b}")

except Exception as e: 
    print(e)

else:
    print("Else executed.") #If try block runs successfully then else is executed.