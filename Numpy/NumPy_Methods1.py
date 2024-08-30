import numpy as np
#Note that numpy array can only have one data type at a time soo

#np.array
    # create 1-D array
arr1 =  np.array([0,1,2,3,4,5])
print(f"Arr1 is : {arr1}") #all integers

arr2 = np.array([0,12,23,"hello"])
print(f"Arr2 is : {arr2}") #all elements in string will be printed because 1 hello is in string

arr3 = np.array([(1.5, 2, 3), (4, 5, 6)])
print(f"Arr3 is : {arr3}") #all will be in floating point because one element is in float soo.

    # create 2-D array 
arr1 = np.array([(1,2,3,4),(11,12,13,14)])
print(f"2D - Arr1 is : {arr1}") #all integers

print("\n")

#np.shape
print(f"Shape of arr1 is : {arr1.shape}") #prints the shape of arr1 (if 1d then only gives len otherwise print (row,col))
print(f"Shape of arr2 is : {arr2.shape}") #prints len of arr2 because it is 1-D.
print(f"Shape of arr3 is : {arr3.shape}") #2d array means o/p:- (2,3) rows cols

print("\n")

#np.arange(only for 1d for 2d you have to use reshape with this!!)
arr4 = np.arange(10) #elements from 0 to 9 
print(f"Arr4 is : {arr4}") 
arr4 = np.arange(0,13,3) #start stop range (basically creates an array)
print(f"Arr4 is : {arr4}")

print("\n")

#np.zeros
arr5 = np.zeros(5) #creates an array with 5 (floating point) 0 in it.
print(f"Arr5 is : {arr5}")

    #In multi-dim array
arr6 = np.zeros((2,4)) #creates array of 2 rows an 4 cols with all 0's
print(f"Arr6 is : {arr6}")

print("\n")

#np.full
    #1-D array
arr7 = np.full(2,14)
print(f"Arr7 is : {arr7}")
    #2-D array
arr7 = np.full((2,4),14)
print(f"Arr7 is : {arr7}")

print("\n")

#Convert list to numpy array
list1 = [1,23,45,5]
arr8 = np.array(list1)
print(f"Arr8 is : {arr8}")