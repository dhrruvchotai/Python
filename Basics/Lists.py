#Mutable data type.
items = [3,8,2,9,1,"Hello"]

print(items[0:3]) #just like slice in a string

# items.sort()
# print("After Sort : ",items)  #if there is a string with nums in a list it can't be sorted!!

my_list = [3, 1, 2]
my_list.sort() # Output: [1, 2, 3]
my_list.sort(reverse=True) # Output: [3, 2, 1] For Sorting in rev order


items.reverse()
print("After Reverse : ",items)

items.insert(5,"DHRUV")
print("After Insert : ",items)

ans = items.pop(-2) #By default it removes the elmt from the last.
print("After Pop : ",items)
print("Popped elmt is : ",ans)

items.remove("Hello") #In case of string it is case sensitive.
print("After Removing : ",items)

#To extend the list 
items.extend([10,12]) 
print("After extendig : ",items)

#Taking input in a list
names = []

for i in range(0,5):
    name = input("Enter a Name : ")
    names.append(name)

print(names)

