a = 89

def abc():
    global a
    a = 14 #here i made a global and assigned value 14
    print(f"Value of a inside function : {a}") # so this will affect value of a globally so it will print 14 here.

abc()
print(f"Value of a outside function : {a}") #because i have called abc() now a is global and it's val is 14. 