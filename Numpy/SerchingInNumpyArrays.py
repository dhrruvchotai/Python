import numpy as np

#Search the number using np.where
np1 = np.array([1,2,3,8,4,5,4,10,14])

index =  np.where(np1 == 4) #return the tuple of indexs where the num matches.
print(index)

#Return indexs of even elemets
np2 = np.array([1,2,3,4,5,6,7,8,9,10])
evenIndexs = np.where(np2 % 2 == 0)
print(evenIndexs)

#Same for odd index
oddIndexs = np.where(np2 % 2 == 1)
print(oddIndexs)


#.....Till l8!!