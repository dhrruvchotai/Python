#Declared an List
nums = [1,2,3,4,5]

#for loop type 1
for num in nums:
    print(num)

print(" ")

#for loop type 2
for i in range (0,len(nums)):  #for i in range (0,len(nums),increment factor x) -> i = i+x;  
    # This both are same.
    print(nums[i],end="\n") 
    print(nums[i])  

    #For not printing in new line
    print(nums[i],end=" ") #This prints 1 2 3 4 5 ....

print(" ")


#while loop
while i < len(nums) :
    print(nums[i],end=" ")
    i+=1

print(" ")

#Print the string 
name = "Dhruv"
for i in name:
    print(i,end="")

print(" ")

#Print the dictionary
dict = {
    "name" : "Dhruv",
    "id" : 10,
    "marks":[3030,9003]
}

for i in dict:
    print(dict.get(i))

print(" ")

#For loop with else
for i in range(1,6):
    print(i,end=" ")
else:
    print("Loop is over now!!") #This is printed when the loop is Over!!