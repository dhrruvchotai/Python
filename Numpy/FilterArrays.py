import numpy as np
 
np1 = np.array([1,2,4,5,9])
np2 = np.array([1,2,3,4,5,6,7,8,9,10])

#filter an array using boolean index lists.
x = [True,False,True,True,False] 

print(np1[x]) #prints the element of np1 where x is True.


#if you want to find anything based on condition just loop throught it (Simple Method)

multipleOfThree = []

for item in np2:
    if(item % 3 == 0):
        multipleOfThree.append(True)
    else:
        multipleOfThree.append(False)

print(np2[multipleOfThree])

#same thing as upper using numpy shortcut
filterd = np2 % 4 == 0
print(np2[filterd])

#.....Till l9 over!!