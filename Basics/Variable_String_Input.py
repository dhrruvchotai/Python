# Simple print
print("hello")

# Define a variable
a = 10

# prints type of variable
print(type(a)) 

#boolean 
b = True

#None type variable
c = None
print(type(b))
print(type(c))

# input function
temp = int(input("enter a value :")) # parsing into int , byDefault input function gives value in string
print(temp)

#String functions

name = "DHRUV"

 #length of a string
print(len(name))

#substring in a string
print(name[0:3]) #Using +ve index.
print(name[-5:-2]) #You can also use negative indices like this
print(name[:4]) # same as print name[0:4]
print(name[0:]) #same as print [0:5]

# slice function 
ans3 = name[0:5:2] # startIndx :endIndx :how many values to skip here i = i+2; means indx 0 2 4 prints
print(ans3)


#fstring 

print(f"Hello {name}")  
print("Hello "+name+" ") #both are same.


#chaining of function

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>'''

print((letter.replace("<|Name|>","DHRUV")).replace("<|Date|>","-- 10 July"))


#Find double space in a string
str = "Hello my name is  DHRUV"
print(str.find("  "))