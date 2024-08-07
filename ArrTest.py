nums = [1,2,3,4,5]

for num in nums:
    print(num)

for i in range (0,len(nums)):  #for i in range (0,len(nums),increment factor x): i = i+x;  
    # This both are same.
    print(nums[i],end="\n") 
    print(nums[i])  

    #For not printing in new line
    print(nums[i],end=" ") #This prints 1 2 3 4 5 ....

while i < len(nums) :
    print(nums[i],end=" ")
    i+=1


