#Immutable data type

a = () 
print(type(a)) #For this it gives type = tuple but but..

b = (1)
print(type(b)) #For this it gives type = int because it considers only elmt 1 which is int

#To avoid this
c = (1,) #Now this is a type = tuple
print(type(c))

#methods of Tuple

mytuple = (1,2,3,2,4,2)

print(mytuple.count(2))

print(mytuple.index(2)) #Gives index of first occurance 

#Joins to tuples
my_tuple1 = (1, 2)
my_tuple2 = (3, 4)
print(my_tuple1 + my_tuple2) # Output: (1, 2, 3, 4)

#For printing tuple multiple times
print(mytuple * 3)

# checks if any elmt is there in a tuple returns True or False
print(3 in mytuple)
print(5 in mytuple)

