import numpy as np

#create an 1-d array and get shape
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(f"np1 is : {np1}")
print(f"shape of np1 is : {np1.shape}")
print(f"number of dimensions is : {np1.ndim}")

print('\n')

#create an 2-d array and get shape (rows,cols)
np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(f"np2 is : {np2}")
print(f"shape of np2 is : {np2.shape}") 
print(f"number of dimensions is : {np2.ndim}")


print('\n')

#reshape np1 to 2-d array
np3 = np1.reshape(2,6) #try here 2,4 will not work because array is of total 12 elements.
#here you should enter 12 elements no matter how you enter like 2,6 or 6,2 or 3,4 or 4,3 or 1,12 or 12,1
print(f"np3 is : {np3}")
print(f"shape of np3 is : {np3.shape}")
print(f"number of dimensions is : {np3.ndim}")


print('\n')

#reshape np1 to 3d array
np4 = np1.reshape(1,4,3) #means there is 1 array inside that there are other 4 arrays and each have 3 elements.
#other (1,12,1) (12,1,1) (2,3,2) (3,2,2) (2,2,3) (4,3,1) (3,4,1) (1,4,3) #check for 1,1,12 specially.
print(f"np4 is : {np4}")
print(f"shape of np4 is : {np4.shape}")
print(f"number of dimensions is : {np4.ndim}")

print('\n')

#flatten np4 or any other array to 1-d array
np5 = np4.reshape(-1)
print(f"np5 is : {np5}")
print(f"shape of np5 is : {np5.shape}")
print(f"dimension of np5 is : {np5.ndim}")

print('\n')

#flatten np3 from 2-d to 1-d array
np6 = np4.reshape(-1)
print(f"np6 is : {np6}")
print(f"shape of np6 is : {np6.shape}")
print(f"dimension of np5 is : {np6.ndim}")


#.....Till l5!!