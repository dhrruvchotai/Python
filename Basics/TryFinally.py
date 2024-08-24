def main():
    try:
        a = int(input("Enter number a : "))
        b =  int(input("Enter number b : "))
        print(f"a/b = {a/b}")
        return #return hai but but finally will be executed.!!!

    except Exception as e: 
        print(e)
        return #return hai but but finally will be executed.!!!
    
    finally:
        print("Finally executed.")

#Remember in simple code if you write print or any code without finally it will be executed.
#it is used mainly in this type of cases when function uses return or anything else.


try:
    a = int(input("Enter number a : "))
    b =  int(input("Enter number b : "))
    print(f"a/b = {a/b}")

except Exception as e: 
    print(e)

print("This print always executed you don't need finally for this.!!")