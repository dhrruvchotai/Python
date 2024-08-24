try:
    a = int(input("Enter number a : "))
    b =  int(input("Enter number b : "))
    print(f"a/b = {a/b}")


except ValueError as ve: #Datatype error.
    print(ve)
    print("Enter an Integer Number.")

except ZeroDivisionError as zde: #Exception when num divided by zero.
    print("Number a can't be divided by zero.")
    print(zde)

except Exception as e: #By default exception
    print(e)

#There are many more you can explore.


