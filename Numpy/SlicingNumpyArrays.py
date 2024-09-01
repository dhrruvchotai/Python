import numpy as np 

arr1 = np.array([0,1,2,3,4,5,6,7,8,9])
#Slice an array regular py 1-D

#return 2 3 4 5
print(arr1[1:5]) #This is like basic python.

#return from some index to till end of indexes.!!
print(arr1[3:]) #prints from index 3 till end!!!

#Negative slices
print(arr1[-3:]) #7 8 9
print(arr1[-3:-1])# o/p: 7 8

#slicing with steps
print(arr1[1:5:2]) #start end and increment 
print(arr1[::2]) #all even indexes.
print(arr1[1::2]) #all odd!!


#In 2-D array.
arr2 = np.array([[0,1,2,3],[4,5,6,7],[9,10,11,12]])

print(arr2[1][3]) #or print(arr2[1,3]) 

print(arr2[0:2,1:3]) #from rows:rows and cols:cols

#.....Till l2!!

