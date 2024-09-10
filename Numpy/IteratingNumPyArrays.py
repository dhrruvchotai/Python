import numpy as np

#simple way using loops to iterate through the array
#for 1-D array
np1 = np.array([1,2,3,4,5,6,7,8,9,10])

print("np1 using loop : ")
for x in np1:
    print(x,end=" ")

print('\n')

#for 2-array
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print("np2 using loop : ")
for x in np2: #here x is a whole first array
    for y in x: #and we are iterating each inner array through y.
        print(y,end=" ")

print("\n")

#for 3-D array
np3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]]])

# elmt 1 = [1,2,3],[4,5,6]
# elmt2 = [7,8,9]
# elmt3 - [10,11,12]

print("np3 using loop : ")
for x in np3:
    for y in x:
        for z in y:
            print(z,end=" ")

print("\n")

#numpy way to iterate through the loop.
#using np.nditer() used for any n-dimension array. 

print(f"np3 using nditer = ")
for x in np.nditer(np3):
    print(x,end=" ")

#.....Till l6!!