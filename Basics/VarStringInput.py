print("hello")

a = 10#Define a variable
print(type(a))#prints type of variable 

b = True
print(type(b))

#input function
temp = int(input("enter a value :"))#parsing into int , byDefault input function gives value in string
print(temp)

#String functions

print(len(name)) #length of a string

name = "dhruv"
ans = name[0:3] #substring in a string
print(ans)

ans1 = name[0:6:2] #slice function startIndx :endIndx :how many values to slip here i = i+2; means indx 0 2 4 prints
print(ans1)
